"""Weekly collection run: fetch every board, derive signal, write the dataset.

Outputs three things, each with a different lifetime:
  data/snapshots/<week>.json.gz  full derived postings for that week (archive)
  data/latest.json               the most recent week, uncompressed (dashboard)
  data/trends.csv                one row per week per metric (permanent record)

Raw description text is never written to disk. It is used to extract skills and
then discarded, which keeps a weekly-committed dataset to a few hundred KB.
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


def iso_week(d=None):
    d = d or date.today()
    y, w, _ = d.isocalendar()
    return f"{y}-W{w:02d}"


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


def summarize(jobs, week, failures):
    """Aggregate one week into the metrics that get tracked over time."""
    total = len(jobs)
    skill_counts = Counter(s for j in jobs for s in j["skills"])
    salaried = [j for j in jobs if j["salary"]]
    mids = sorted((j["salary"][0] + j["salary"][1]) / 2 for j in salaried)
    return {
        "week": week,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "total_jobs": total,
        "companies": len(set(j["company"] for j in jobs)),
        "failed_boards": len(failures),
        "remote_share": round(sum(j["remote"] for j in jobs) / total, 4) if total else 0,
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
    """Append this week's skill shares to the long-lived time series."""
    rows = []
    for skill, count in summary["skills"].items():
        rows.append({
            "week": summary["week"],
            "skill": skill,
            "category": taxonomy.SKILL_CAT.get(skill, ""),
            "count": count,
            "share": summary["skill_share"].get(skill, 0),
            "total_jobs": summary["total_jobs"],
        })
    fields = ["week", "skill", "category", "count", "share", "total_jobs"]
    existing = []
    if TRENDS.exists():
        with TRENDS.open() as f:
            existing = [r for r in csv.DictReader(f) if r["week"] != summary["week"]]
    with TRENDS.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(existing)
        w.writerows(rows)
    return len(rows)


def main():
    started = time.time()
    companies = json.loads((ROOT / "config" / "companies.json").read_text())
    week = iso_week()
    print(f"Collecting {len(companies)} boards for {week}...", file=sys.stderr)

    jobs, failures = collect_all(companies)
    if not jobs:
        print("No jobs collected - aborting without writing.", file=sys.stderr)
        return 1

    jobs.sort(key=lambda j: (j["company"].lower(), j["title"].lower()))
    summary = summarize(jobs, week, failures)

    SNAPSHOTS.mkdir(parents=True, exist_ok=True)
    payload = {"summary": summary, "jobs": jobs}

    # Full archive: gzipped, ~600KB/week. This is the record of what was open.
    with gzip.open(SNAPSHOTS / f"{week}.json.gz", "wt", encoding="utf-8") as f:
        json.dump(payload, f, separators=(",", ":"))
    # Uncompressed working copy for the same run - gitignored, since committing
    # 6MB every week would bloat history far faster than the archive does.
    (DATA / "latest.json").write_text(json.dumps(payload, separators=(",", ":")))
    (DATA / "summary.json").write_text(json.dumps(summary, indent=2))
    n = append_trends(summary)

    print(
        f"\n{summary['total_jobs']} jobs / {summary['companies']} companies "
        f"/ {n} skill rows / {len(failures)} failed boards "
        f"in {time.time() - started:.0f}s",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
