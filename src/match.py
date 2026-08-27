"""Score this week's newly-appeared postings against config/profile.json.

Writes a Markdown digest that the weekly workflow posts as a GitHub Issue.
This is the personal half of the repo: it surfaces and ranks roles for a human
to read. It never contacts an employer or submits anything.
"""
import gzip
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SNAPSHOTS = DATA / "snapshots"

# A skill you already have is worth more than one you are working toward.
W_HAVE, W_LEARNING = 3.0, 1.5
W_FAMILY, W_SENIORITY, W_LOCATION, W_TITLE, W_SALARY = 6.0, 3.0, 2.0, 4.0, 2.0


def load_profile():
    return json.loads((ROOT / "config" / "profile.json").read_text())


def snapshot_weeks():
    return sorted(p.stem.replace(".json", "") for p in SNAPSHOTS.glob("*.json.gz"))


def load_snapshot(week):
    with gzip.open(SNAPSHOTS / f"{week}.json.gz", "rt", encoding="utf-8") as f:
        return json.load(f)


def score(job, profile):
    """Additive score plus the reasons behind it, so the digest can explain itself."""
    have = set(profile["have_skills"])
    learning = set(profile["learning_skills"])
    skills = set(job["skills"])
    reasons = []
    total = 0.0

    hit_have = sorted(skills & have)
    hit_learn = sorted(skills & learning)
    total += W_HAVE * len(hit_have) + W_LEARNING * len(hit_learn)
    if hit_have:
        reasons.append("matches " + ", ".join(hit_have))
    if hit_learn:
        reasons.append("stretches into " + ", ".join(hit_learn))

    if job["family"] in profile["target_families"]:
        total += W_FAMILY
    if job["seniority"] in profile["target_seniority"]:
        total += W_SENIORITY
    else:
        total -= W_SENIORITY  # wrong level is a real mismatch, not a neutral

    loc = (job["location"] or "").lower()
    if job["remote"] and profile.get("remote_ok"):
        total += W_LOCATION
        reasons.append("remote")
    elif any(l.lower() in loc for l in profile.get("locations", [])):
        total += W_LOCATION

    title = job["title"].lower()
    if any(t.lower() in title for t in profile.get("title_boost", [])):
        total += W_TITLE
    if any(re.search(re.escape(t.lower()), title) for t in profile.get("title_exclude", [])):
        return 0.0, ["excluded by title"]

    if job["salary"]:
        floor = profile.get("min_salary")
        if floor and job["salary"][1] < floor:
            return 0.0, ["below salary floor"]
        total += W_SALARY
        reasons.append(f"${job['salary'][0]:,}-${job['salary'][1]:,}")

    return total, reasons


def new_jobs(current, previous):
    """Postings present this week that were absent last week."""
    if previous is None:
        return current["jobs"]
    seen = {j["id"] for j in previous["jobs"]}
    return [j for j in current["jobs"] if j["id"] not in seen]


def render(matches, week, n_new, first_run):
    if not matches:
        return (f"## No new matches this week ({week})\n\n"
                f"{n_new:,} new postings were collected; none cleared the profile "
                f"in `config/profile.json`. Loosen `target_families` or "
                f"`title_exclude` if this keeps happening.\n")

    L = [f"## {len(matches)} roles worth a look — {week}\n"]
    if first_run:
        L.append("_First run, so this scores every posting currently open. "
                 "From next week it will only show newly-appeared roles._\n")
    else:
        L.append(f"_Scored against {n_new:,} postings that are new since last week._\n")

    for i, (job, sc, reasons) in enumerate(matches, 1):
        loc = "Remote" if job["remote"] else (job["location"] or "—")
        pay = f" · ${job['salary'][0]:,}–${job['salary'][1]:,}" if job["salary"] else ""
        L.append(f"**{i}. [{job['title']}]({job['url']})** — {job['company']}  ")
        L.append(f"<sub>{loc}{pay} · {job['family']} / {job['seniority']} · score {sc:.0f}</sub>  ")
        why = [r for r in reasons if r not in ("remote",)]
        if why:
            L.append(f"<sub>{'; '.join(why)}</sub>")
        L.append("")

    L.append("---")
    L.append("<sub>Ranked by overlap with `config/profile.json`. "
             "Edit that file to change what surfaces here.</sub>")
    return "\n".join(L)


def main():
    profile = load_profile()
    weeks = snapshot_weeks()
    if not weeks:
        print("No snapshots found.", file=sys.stderr)
        return 1

    current = load_snapshot(weeks[-1])
    previous = load_snapshot(weeks[-2]) if len(weeks) > 1 else None
    candidates = new_jobs(current, previous)

    scored = []
    for job in candidates:
        sc, reasons = score(job, profile)
        if sc > 0:
            scored.append((job, sc, reasons))
    scored.sort(key=lambda t: -t[1])
    scored = scored[: profile.get("max_results", 25)]

    body = render(scored, weeks[-1], len(candidates), previous is None)
    out = DATA / "matches.md"
    out.write_text(body)
    print(f"{len(scored)} matches from {len(candidates)} new postings -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
