"""Daily collection run: fetch every board, derive signal, write the dataset.

Outputs, each with a different lifetime and update cadence:
  data/trends.csv                one row per skill per DAY (permanent series)
  data/seen.csv                  id -> first date observed, append-only
  data/snapshots/<week>.json.gz  full derived postings, archived WEEKLY
  data/latest.json               today's run, uncompressed (gitignored)

The archive stays weekly on purpose. Postings persist for weeks, so consecutive
daily snapshots are near-duplicates, and gzip blobs do not delta-compress in
git: archiving 620KB every day would add ~226MB per year to history that
deleting the files later cannot reclaim. The daily signal lives in trends.csv
and seen.csv, which are text and compress well.

Raw description text is never written to disk. It is used to extract skills and
then discarded.
"""
import csv
import gzip
import json
import sys
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import boilerplate  # noqa: E402
import sources  # noqa: E402
import taxonomy  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SNAPSHOTS = DATA / "snapshots"
TRENDS = DATA / "trends.csv"
SEEN = DATA / "seen.csv"
SETTINGS = ROOT / "config" / "settings.json"


# Which weekday gets the full archive snapshot (0 = Monday).
ARCHIVE_WEEKDAY = 0


def today_key(d=None):
    """Runs are keyed by calendar date so each day is its own trend point."""
    return (d or date.today()).isoformat()


def iso_week(d=None):
    d = d or date.today()
    y, w, _ = d.isocalendar()
    return f"{y}-W{w:02d}"


def load_seen():
    """id -> first date observed. Append-only, so git stores it efficiently."""
    seen = {}
    if SEEN.exists():
        with SEEN.open() as f:
            for row in csv.DictReader(f):
                seen[row["id"]] = row["first_seen"]
    return seen


def update_seen(jobs, day):
    """Record ids never seen before; return the set that is new today."""
    seen = load_seen()
    fresh = {j["id"] for j in jobs if j["id"] not in seen}
    if fresh:
        write_header = not SEEN.exists()
        with SEEN.open("a", newline="") as f:
            w = csv.writer(f)
            if write_header:
                w.writerow(["id", "first_seen"])
            for jid in sorted(fresh):
                w.writerow([jid, day])
    return fresh


def collect_all(companies, workers=12):
    """Fetch every company in parallel. A board that fails is skipped, not fatal:
    one company being down should never lose the whole week's snapshot."""
    jobs, failures = [], []
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(sources.collect_company, c): c for c in companies}
        for fut in as_completed(futures):
            company = futures[fut]
            try:
                batch = fut.result()
            except Exception as e:  # noqa: BLE001
                failures.append((company["name"], type(e).__name__))
                print(f"  FAIL {company['name']}: {type(e).__name__}", file=sys.stderr)
                continue
            boilerplate.clean_company(batch)
            jobs.extend(taxonomy.enrich(j) for j in batch)
            print(f"  ok   {company['name']:<26} {len(batch):>4}", file=sys.stderr)
    return jobs, failures


def summarize(jobs, day, failures, n_new, collected, remote_count, remote_only):
    """Aggregate one day into the metrics that get tracked over time.

    `jobs` is the post-filter set. `collected`/`remote_count` describe every
    posting fetched, so the market-wide remote share stays trackable even when
    the dataset itself is limited to remote roles.
    """
    total = len(jobs)
    skill_counts = Counter(s for j in jobs for s in j["skills"])
    salaried = [j for j in jobs if j["salary"]]
    mids = sorted((j["salary"][0] + j["salary"][1]) / 2 for j in salaried)
    return {
        "date": day,
        "week": iso_week(),
        "new_today": n_new,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "total_jobs": total,
        "total_collected": collected,
        "remote_only": remote_only,
        "companies": len(set(j["company"] for j in jobs)),
        "failed_boards": len(failures),
        # Share of the whole market that is remote, not of the filtered set.
        "remote_share": round(remote_count / collected, 4) if collected else 0,
        "salary_disclosed": len(salaried),
        "median_salary_midpoint": int(mids[len(mids) // 2]) if mids else None,
        "by_family": dict(Counter(j["family"] for j in jobs).most_common()),
        "by_seniority": dict(Counter(j["seniority"] for j in jobs).most_common()),
        "by_company": dict(Counter(j["company"] for j in jobs).most_common()),
        "skills": dict(skill_counts.most_common()),
        # Share is the honest cross-week metric: it stays comparable even when
        # the number of tracked companies changes.
        "skill_share": {k: round(v / total, 4) for k, v in skill_counts.most_common()} if total else {},
    }


def append_trends(summary):
    """Append today's skill shares to the long-lived time series.

    Rows for the same date are replaced, so re-running a day is idempotent.
    Legacy ISO-week rows (from when this ran weekly) are dropped on sight.
    """
    rows = []
    for skill, count in summary["skills"].items():
        rows.append({
            "date": summary["date"],
            "skill": skill,
            "category": taxonomy.SKILL_CAT.get(skill, ""),
            "count": count,
            "share": summary["skill_share"].get(skill, 0),
            "total_jobs": summary["total_jobs"],
        })
    fields = ["date", "skill", "category", "count", "share", "total_jobs"]
    existing = []
    if TRENDS.exists():
        with TRENDS.open() as f:
            existing = [
                r for r in csv.DictReader(f)
                # keep other days, drop today's rerun and any pre-daily rows
                if r.get("date", "") != summary["date"] and "-W" not in (r.get("date") or r.get("week") or "-W")
            ]
    with TRENDS.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(existing)
        w.writerows(rows)
    return len(rows)


def main():
    started = time.time()
    companies = json.loads((ROOT / "config" / "companies.json").read_text())
    day = today_key()
    print(f"Collecting {len(companies)} boards for {day}...", file=sys.stderr)

    jobs, failures = collect_all(companies)
    if not jobs:
        print("No jobs collected - aborting without writing.", file=sys.stderr)
        return 1

    jobs.sort(key=lambda j: (j["company"].lower(), j["title"].lower()))

    settings = json.loads(SETTINGS.read_text()) if SETTINGS.exists() else {}
    remote_only = settings.get("remote_only", False)
    collected, remote_count = len(jobs), sum(j["remote"] for j in jobs)
    if remote_only:
        jobs = [j for j in jobs if j["remote"]]
        print(f"  remote_only: kept {len(jobs)} of {collected}", file=sys.stderr)
        if not jobs:
            print("No remote jobs matched - aborting without writing.", file=sys.stderr)
            return 1

    DATA.mkdir(parents=True, exist_ok=True)
    fresh = update_seen(jobs, day)
    for j in jobs:
        j["new"] = j["id"] in fresh

    summary = summarize(jobs, day, failures, len(fresh),
                        collected, remote_count, remote_only)
    payload = {"summary": summary, "jobs": jobs}

    # Working copy for report.py and match.py; gitignored, ~6MB.
    (DATA / "latest.json").write_text(json.dumps(payload, separators=(",", ":")))
    (DATA / "summary.json").write_text(json.dumps(summary, indent=2))

    # Full archive once a week - see the module docstring for why not daily.
    SNAPSHOTS.mkdir(parents=True, exist_ok=True)
    archive = SNAPSHOTS / f"{iso_week()}.json.gz"
    if date.today().weekday() == ARCHIVE_WEEKDAY or not archive.exists():
        with gzip.open(archive, "wt", encoding="utf-8") as f:
            json.dump(payload, f, separators=(",", ":"))
        print(f"  archived {archive.name}", file=sys.stderr)

    n = append_trends(summary)

    print(
        f"\n{summary['total_jobs']} jobs (of {collected} collected) "
        f"/ {summary['companies']} companies "
        f"/ {len(fresh)} new today / {n} skill rows / {len(failures)} failed boards "
        f"in {time.time() - started:.0f}s",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
