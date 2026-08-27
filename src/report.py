"""Render the weekly README, charts and dashboard payload from collected data.

Everything here is derived from data/latest.json plus the accumulated
data/trends.csv, so the report can be regenerated without re-fetching boards.
"""
import csv
import json
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import charts  # noqa: E402
import taxonomy  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DOCS = ROOT / "docs"
ASSETS = DOCS / "charts"

# Families whose postings describe engineering work. Skill counts over *all*
# postings are diluted by sales and ops roles, so headline numbers use these.
TECH_FAMILIES = {"research", "ml-ai", "data", "infra", "swe"}
MIN_MOVER_BASE = 25


def movers_baseline(days):
    """Label for the day the movers table compares against."""
    if len(days) < 2:
        return None
    cur = days[-1]
    prior = [d for d in days if d < cur]
    older = [d for d in prior if (date.fromisoformat(cur) - date.fromisoformat(d)).days >= 7]
    return older[-1] if older else prior[0]  # ignore skills too rare for a share change to mean anything


def load_trends():
    """trends.csv -> {skill: {date: share}} plus the ordered list of dates."""
    if not TRENDS_PATH.exists():
        return {}, []
    by_skill = defaultdict(dict)
    days = []
    with TRENDS_PATH.open() as f:
        for row in csv.DictReader(f):
            day = row.get("date") or row.get("week", "")
            if "-W" in day:  # legacy weekly rows, dropped on the next write
                continue
            by_skill[row["skill"]][day] = float(row["share"])
            if day not in days:
                days.append(day)
    return by_skill, sorted(days)


TRENDS_PATH = DATA / "trends.csv"


def movers(by_skill, days, counts, limit=8, lookback=7):
    """Largest share changes over `lookback` days, in percentage points.

    Compared against roughly a week ago rather than yesterday: day-to-day churn
    on job boards is mostly posting noise, not a shift in demand.
    """
    if len(days) < 2:
        return [], []
    cur = days[-1]
    prior = [d for d in days if d < cur]
    # nearest day at least `lookback` back, else the oldest we have
    older = [d for d in prior if (date.fromisoformat(cur) - date.fromisoformat(d)).days >= lookback]
    prev = older[-1] if older else prior[0]
    deltas = []
    for skill, series in by_skill.items():
        if cur not in series or prev not in series:
            continue
        if counts.get(skill, 0) < MIN_MOVER_BASE:
            continue
        deltas.append((skill, (series[cur] - series[prev]) * 100))
    deltas.sort(key=lambda t: -t[1])
    return deltas[:limit], [d for d in deltas[::-1] if d[1] < 0][:limit]


def pct(x):
    return f"{x * 100:.1f}%"


def build_readme(summary, jobs, by_skill, days):
    tech = [j for j in jobs if j["family"] in TECH_FAMILIES]
    tech_skills = Counter(s for j in tech for s in j["skills"])
    n_tech = len(tech) or 1

    up, down = movers(by_skill, days, Counter(s for j in jobs for s in j["skills"]))
    baseline = movers_baseline(days)
    sal = [j for j in jobs if j["salary"]]
    tech_sal = [j for j in tech if j["salary"]]

    L = []
    remote_only = summary.get("remote_only")
    scope = "remote " if remote_only else ""
    L.append("# AI Job Radar\n")
    L.append(
        f"> Daily snapshot of what AI and tech companies are hiring for in "
        f"{'remote roles' if remote_only else 'all roles'}, built from public "
        "job-board APIs. Updated every morning by GitHub Actions.\n"
    )
    L.append(
        f"**{summary['date']}** — tracking **{summary['total_jobs']:,} open "
        f"{scope}roles** across **{summary['companies']} companies** "
        f"({len(tech):,} of them engineering roles). "
        f"{summary['salary_disclosed']:,} postings disclose pay. "
        f"**{summary.get('new_today', 0):,} appeared today.**\n"
    )
    if remote_only:
        L.append(
            f"<sub>Remote-only: {summary['total_collected']:,} postings were "
            f"collected across all locations and "
            f"{pct(summary['remote_share'])} of them were remote. "
            f"Set `remote_only` to false in `config/settings.json` to track "
            f"every location.</sub>\n"
        )
    L.append("---\n")

    L.append(f"## Most-requested skills in {scope}engineering roles\n")
    L.append(f"Share of the {len(tech):,} {scope}engineering postings that mention each skill.\n")
    L.append("![Top skills](docs/charts/top-skills.svg)\n")

    L.append("<details><summary>Full skill table</summary>\n")
    L.append("| # | Skill | Category | Postings | Share |")
    L.append("|---:|---|---|---:|---:|")
    for i, (skill, c) in enumerate(tech_skills.most_common(40), 1):
        cat = taxonomy.CATEGORIES.get(taxonomy.SKILL_CAT.get(skill, ""), "-")
        L.append(f"| {i} | {skill} | {cat} | {c:,} | {c / n_tech * 100:.1f}% |")
    L.append("\n</details>\n")

    if up:
        L.append("## Movers\n")
        L.append(f"Change in share of postings since {baseline}, in percentage points.\n")
        L.append("| Rising | Δ pp | | Falling | Δ pp |")
        L.append("|---|---:|---|---|---:|")
        for i in range(max(len(up), len(down))):
            a = f"{up[i][0]} | +{up[i][1]:.2f}" if i < len(up) else " | "
            b = f"{down[i][0]} | {down[i][1]:.2f}" if i < len(down) else " | "
            L.append(f"| {a} | | {b} |")
        L.append("")
        L.append("![Skill trends](docs/charts/trends.svg)\n")
    else:
        L.append("## Movers\n")
        L.append(
            "_Trend lines appear once a second day has been collected. "
            "Each morning's run appends to `data/trends.csv`._\n"
        )

    L.append("## Where the roles are\n")
    L.append("![Role families](docs/charts/families.svg)\n")
    L.append("| Role family | Postings | Share |")
    L.append("|---|---:|---:|")
    for fam, c in summary["by_family"].items():
        L.append(f"| {fam} | {c:,} | {c / summary['total_jobs'] * 100:.1f}% |")
    L.append("")

    if tech_sal:
        mids = sorted((j["salary"][0] + j["salary"][1]) / 2 for j in tech_sal)
        p = lambda q: int(mids[int(len(mids) * q)])  # noqa: E731
        L.append(f"## Disclosed pay, {scope}engineering roles\n")
        L.append(
            f"{len(tech_sal):,} of {len(tech):,} engineering postings "
            f"({len(tech_sal) / n_tech * 100:.0f}%) publish a salary range. "
            "Figures are the midpoint of the posted band.\n"
        )
        L.append("| Percentile | Midpoint |")
        L.append("|---|---:|")
        for label, q in (("25th", 0.25), ("Median", 0.5), ("75th", 0.75), ("90th", 0.9)):
            L.append(f"| {label} | ${p(q):,} |")
        L.append("")
        top_pay = sorted(
            ((j["company"], (j["salary"][0] + j["salary"][1]) / 2) for j in tech_sal),
            key=lambda t: -t[1],
        )
        seen, rows = set(), []
        for comp, mid in top_pay:
            if comp not in seen:
                seen.add(comp)
                rows.append((comp, mid))
            if len(rows) == 10:
                break
        L.append("<details><summary>Highest disclosed engineering bands by company</summary>\n")
        L.append("| Company | Top posted midpoint |")
        L.append("|---|---:|")
        for comp, mid in rows:
            L.append(f"| {comp} | ${int(mid):,} |")
        L.append("\n</details>\n")

    L.append("## Who is hiring most\n")
    L.append("![Top companies](docs/charts/companies.svg)\n")

    L.append("---\n")
    L.append("## How this works\n")
    L.append(
        "Every day at 08:00 UTC a GitHub Actions workflow queries the public "
        "job-board APIs of the companies in [`config/companies.json`]"
        "(config/companies.json) — Greenhouse, Lever and Ashby all expose "
        "unauthenticated JSON endpoints. Each posting's description is scanned "
        "for the ~66 technologies defined in [`config/skills.json`]"
        "(config/skills.json), then the description text is discarded and only "
        "the derived record is stored.\n"
    )
    L.append("| Path | What it holds |")
    L.append("|---|---|")
    L.append("| `data/trends.csv` | One row per skill per day — the long-run time series |")
    L.append("| `data/seen.csv` | Every posting id and the date it first appeared |")
    L.append("| `data/snapshots/<week>.json.gz` | Full postings, archived weekly |")
    L.append("| `data/summary.json` | Aggregates for the latest run |")
    L.append("| `config/companies.json` | Tracked companies and their ATS slugs |")
    L.append("| `config/profile.json` | Your skills — drives the daily match issue |")
    L.append("| `config/settings.json` | `remote_only` and other pipeline switches |")
    L.append("")
    L.append("### Adding a company\n")
    L.append(
        "Job boards are keyed by an ATS slug that has to be discovered. Append "
        "`Name,slug-guess` lines to a text file and run the prober, which tries "
        "all three platforms and keeps whatever answers:\n"
    )
    L.append("```bash")
    L.append("python src/probe_slugs.py candidates.txt > config/companies.json")
    L.append("```\n")
    L.append("### Caveats\n")
    L.append(
        "- Skills are matched by keyword, so a description that merely mentions a "
        "technology counts the same as one that requires it.\n"
        "- Company boilerplate repeated across most of a company's postings is "
        "stripped before matching; without that, an \"About us\" blurb would "
        "register as a skill on every role.\n"
        "- Coverage is limited to companies using Greenhouse, Lever or Ashby. "
        "Firms on Workday and Taleo are absent, which skews toward startups and "
        "scale-ups.\n"
        "- Counts include every posted location for a role, so widely-posted "
        "roles are represented more than once.\n"
        "- Remote status comes from each board's own field where one exists and "
        "from the posted location otherwise. Ashby's `isRemote` is ignored "
        "because boards set it true on hybrid onsite roles; its `workplaceType` "
        "is used instead.\n"
    )
    L.append(f"\n<sub>Generated {summary['generated_at']} · "
             f"{summary['failed_boards']} board(s) unreachable this run</sub>\n")
    return "\n".join(L)


def write_charts(summary, jobs, by_skill, days):
    ASSETS.mkdir(parents=True, exist_ok=True)
    tech = [j for j in jobs if j["family"] in TECH_FAMILIES]
    n_tech = len(tech) or 1
    tech_skills = Counter(s for j in tech for s in j["skills"])

    top = tech_skills.most_common(18)
    colors = {k: charts.CAT_COLOR.get(taxonomy.SKILL_CAT.get(k, ""), "#58a6ff") for k, _ in top}
    (ASSETS / "top-skills.svg").write_text(charts.bar_chart(
        [(k, v / n_tech) for k, v in top],
        f"Skills in {len(tech):,} {'remote ' if summary.get('remote_only') else ''}"
        f"engineering postings ({summary['date']})",
        value_fmt="{:.1%}", colors=colors,
    ))

    (ASSETS / "families.svg").write_text(charts.bar_chart(
        list(summary["by_family"].items())[:9],
        f"Open {'remote ' if summary.get('remote_only') else ''}roles by function "
        f"({summary['total_jobs']:,} postings)",
        label_w=110,
    ))

    (ASSETS / "companies.svg").write_text(charts.bar_chart(
        list(summary["by_company"].items())[:18],
        f"Companies with the most open {'remote ' if summary.get('remote_only') else ''}roles",
        label_w=170,
    ))

    if len(days) >= 2:
        headline = [k for k, _ in tech_skills.most_common(6)]
        series = {s: [by_skill.get(s, {}).get(d) for d in days] for s in headline}
        svg = charts.line_chart(series, [d[5:] for d in days], "Skill share over time")
        if svg:
            (ASSETS / "trends.svg").write_text(svg)


def write_dashboard(summary, jobs):
    """Slim payload for docs/index.html - kept small enough to commit weekly."""
    tech = [j for j in jobs if j["family"] in TECH_FAMILIES]
    recent = sorted(tech, key=lambda j: j["posted_at"], reverse=True)[:400]
    slim = [
        {
            "t": j["title"], "c": j["company"], "l": j["location"],
            "r": j["remote"], "u": j["url"], "d": j["posted_at"],
            "f": j["family"], "s": j["skills"][:8],
            "p": j["salary"],
        }
        for j in recent
    ]
    DOCS.mkdir(parents=True, exist_ok=True)
    (DOCS / "data.json").write_text(json.dumps(
        {"summary": summary, "recent": slim}, separators=(",", ":")))


def main():
    payload = json.loads((DATA / "latest.json").read_text())
    summary, jobs = payload["summary"], payload["jobs"]
    by_skill, days = load_trends()

    write_charts(summary, jobs, by_skill, days)
    write_dashboard(summary, jobs)
    (ROOT / "README.md").write_text(build_readme(summary, jobs, by_skill, days))
    print(f"report written for {summary['date']} ({len(days)} day(s) of history)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
