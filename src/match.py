"""Score today's newly-appeared postings against config/profile.json.

Writes a Markdown digest that the daily workflow posts as a GitHub Issue, and
exits with a marker the workflow reads so it can skip posting on quiet days.
This is the personal half of the repo: it surfaces and ranks roles for a human
to read. It never contacts an employer or submits anything.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

# A skill you already have is worth more than one you are working toward.
W_HAVE, W_LEARNING = 3.0, 1.5
W_FAMILY, W_SENIORITY, W_LOCATION, W_TITLE, W_SALARY = 6.0, 3.0, 2.0, 4.0, 2.0


def load_profile():
    return json.loads((ROOT / "config" / "profile.json").read_text())


def load_latest():
    return json.loads((DATA / "latest.json").read_text())


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


def new_jobs(payload):
    """Postings whose id was first observed on this run.

    collect.py sets this from data/seen.csv, so it stays accurate on a daily
    cadence without keeping a full snapshot for every single day.
    """
    fresh = [j for j in payload["jobs"] if j.get("new")]
    # First ever run: everything is "new", which would be a useless digest, so
    # fall back to scoring the whole board once.
    return fresh, len(fresh) == len(payload["jobs"])


def render(matches, day, n_new, first_run):
    if not matches:
        return (f"## No new matches — {day}\n\n"
                f"{n_new:,} new postings appeared today; none cleared the profile "
                f"in `config/profile.json`.\n")

    L = [f"## {len(matches)} new roles worth a look — {day}\n"]
    if first_run:
        L.append("_First run, so this scores every posting currently open. "
                 "From tomorrow it will only show roles that newly appeared._\n")
    else:
        L.append(f"_Scored against {n_new:,} postings that appeared today._\n")

    for i, (job, sc, reasons) in enumerate(matches, 1):
        loc = "Remote" if job["remote"] else (job["location"] or "\u2014")
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
    payload = load_latest()
    day = payload["summary"]["date"]
    candidates, first_run = new_jobs(payload)

    scored = []
    for job in candidates:
        sc, reasons = score(job, profile)
        if sc > 0:
            scored.append((job, sc, reasons))
    scored.sort(key=lambda t: -t[1])
    scored = scored[: profile.get("max_results", 25)]

    (DATA / "matches.md").write_text(render(scored, day, len(candidates), first_run))
    # The workflow reads this to decide whether opening an issue is worthwhile.
    (DATA / "match_count.txt").write_text(str(len(scored)))
    print(f"{len(scored)} matches from {len(candidates)} new postings")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
