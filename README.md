# AI Job Radar

> Weekly snapshot of what AI and tech companies are actually hiring for, built from public job-board APIs. Updated every Monday by GitHub Actions.

**Week 2026-W35** — tracking **14,257 open roles** across **122 companies** (4,504 of them engineering roles). 36.6% remote-friendly. 7,730 postings disclose pay.

---

## Most-requested skills in engineering roles

Share of the 4,504 engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 2,001 | 44.4% |
| 2 | Distributed Systems | Practices | 1,530 | 34.0% |
| 3 | Machine Learning | ML Fundamentals | 1,472 | 32.7% |
| 4 | LLMs | LLM & GenAI | 1,254 | 27.8% |
| 5 | Observability | Practices | 1,241 | 27.6% |
| 6 | Kubernetes | Infra & Cloud | 1,037 | 23.0% |
| 7 | AI Agents | LLM & GenAI | 1,027 | 22.8% |
| 8 | AWS | Infra & Cloud | 1,023 | 22.7% |
| 9 | Go | Languages | 942 | 20.9% |
| 10 | TypeScript | Languages | 874 | 19.4% |
| 11 | GCP | Infra & Cloud | 766 | 17.0% |
| 12 | Data Pipelines | Data Engineering | 685 | 15.2% |
| 13 | CI/CD | Practices | 679 | 15.1% |
| 14 | SQL | Languages | 647 | 14.4% |
| 15 | Azure | Infra & Cloud | 640 | 14.2% |
| 16 | Java | Languages | 628 | 13.9% |
| 17 | Statistics | ML Fundamentals | 603 | 13.4% |
| 18 | React | Frameworks & Libraries | 520 | 11.5% |
| 19 | Terraform | Infra & Cloud | 489 | 10.9% |
| 20 | Evals | LLM & GenAI | 442 | 9.8% |
| 21 | Rust | Languages | 419 | 9.3% |
| 22 | Linux | Infra & Cloud | 356 | 7.9% |
| 23 | Databricks | Data Engineering | 351 | 7.8% |
| 24 | Docker | Infra & Cloud | 343 | 7.6% |
| 25 | Snowflake / BigQuery | Data Engineering | 330 | 7.3% |
| 26 | Spark | Data Engineering | 301 | 6.7% |
| 27 | Airflow | Data Engineering | 279 | 6.2% |
| 28 | Kafka | Data Engineering | 273 | 6.1% |
| 29 | Security | Practices | 265 | 5.9% |
| 30 | PyTorch | Frameworks & Libraries | 262 | 5.8% |
| 31 | GPU Clusters | Infra & Cloud | 233 | 5.2% |
| 32 | Reinforcement Learning | ML Fundamentals | 229 | 5.1% |
| 33 | RAG | LLM & GenAI | 223 | 5.0% |
| 34 | AI Safety | LLM & GenAI | 219 | 4.9% |
| 35 | Deep Learning | ML Fundamentals | 216 | 4.8% |
| 36 | Fine-tuning | LLM & GenAI | 212 | 4.7% |
| 37 | MLOps | Practices | 212 | 4.7% |
| 38 | MCP | LLM & GenAI | 193 | 4.3% |
| 39 | Vector Databases | LLM & GenAI | 175 | 3.9% |
| 40 | dbt | Data Engineering | 174 | 3.9% |

</details>

## Week-over-week movers

_Trend lines appear once a second week has been collected. Each Monday's run appends to `data/trends.csv`._

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 4,582 | 32.1% |
| swe | 2,610 | 18.3% |
| other | 2,302 | 16.1% |
| ops | 1,614 | 11.3% |
| product | 1,255 | 8.8% |
| infra | 910 | 6.4% |
| ml-ai | 450 | 3.2% |
| research | 277 | 1.9% |
| data | 257 | 1.8% |

## Disclosed pay, engineering roles

2,745 of 4,504 engineering postings (61%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $205,000 |
| Median | $240,000 |
| 75th | $287,625 |
| 90th | $347,500 |

<details><summary>Highest disclosed engineering bands by company</summary>

| Company | Top posted midpoint |
|---|---:|
| Anthropic | $675,000 |
| OpenAI | $470,500 |
| Pinterest | $453,179 |
| Lambda | $412,500 |
| Waymo | $390,000 |
| xAI | $390,000 |
| Snowflake | $370,500 |
| Duolingo | $370,000 |
| Datadog | $360,000 |
| Decagon | $355,000 |

</details>

## Who is hiring most

![Top companies](docs/charts/companies.svg)

---

## How this works

Every Monday at 08:00 UTC a GitHub Actions workflow queries the public job-board APIs of the companies in [`config/companies.json`](config/companies.json) — Greenhouse, Lever and Ashby all expose unauthenticated JSON endpoints. Each posting's description is scanned for the ~66 technologies defined in [`config/skills.json`](config/skills.json), then the description text is discarded and only the derived record is stored.

| Path | What it holds |
|---|---|
| `data/trends.csv` | One row per skill per week — the long-run time series |
| `data/snapshots/<week>.json.gz` | Every derived posting for that week |
| `data/summary.json` | Aggregates for the latest week |
| `config/companies.json` | Tracked companies and their ATS slugs |
| `config/profile.json` | Your skills — drives the weekly match issue |

### Adding a company

Job boards are keyed by an ATS slug that has to be discovered. Append `Name,slug-guess` lines to a text file and run the prober, which tries all three platforms and keeps whatever answers:

```bash
python src/probe_slugs.py candidates.txt > config/companies.json
```

### Caveats

- Skills are matched by keyword, so a description that merely mentions a technology counts the same as one that requires it.
- Company boilerplate repeated across most of a company's postings is stripped before matching; without that, an "About us" blurb would register as a skill on every role.
- Coverage is limited to companies using Greenhouse, Lever or Ashby. Firms on Workday and Taleo are absent, which skews toward startups and scale-ups.
- Counts include every posted location for a role, so widely-posted roles are represented more than once.


<sub>Generated 2026-08-27T19:48:34+00:00 · 0 board(s) unreachable this run</sub>
