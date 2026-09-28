# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-09-28** — tracking **2,878 open remote roles** across **93 companies** (831 of them engineering roles). 1,642 postings disclose pay. **16 appeared today.**

<sub>Remote-only: 14,242 postings were collected across all locations and 20.2% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 831 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 382 | 46.0% |
| 2 | Observability | Practices | 299 | 36.0% |
| 3 | Distributed Systems | Practices | 277 | 33.3% |
| 4 | Go | Languages | 258 | 31.0% |
| 5 | Machine Learning | ML Fundamentals | 258 | 31.0% |
| 6 | LLMs | LLM & GenAI | 245 | 29.5% |
| 7 | AWS | Infra & Cloud | 238 | 28.6% |
| 8 | AI Agents | LLM & GenAI | 235 | 28.3% |
| 9 | Kubernetes | Infra & Cloud | 216 | 26.0% |
| 10 | TypeScript | Languages | 166 | 20.0% |
| 11 | Statistics | ML Fundamentals | 154 | 18.5% |
| 12 | GCP | Infra & Cloud | 152 | 18.3% |
| 13 | SQL | Languages | 147 | 17.7% |
| 14 | Data Pipelines | Data Engineering | 143 | 17.2% |
| 15 | CI/CD | Practices | 121 | 14.6% |
| 16 | Terraform | Infra & Cloud | 115 | 13.8% |
| 17 | Java | Languages | 108 | 13.0% |
| 18 | React | Frameworks & Libraries | 105 | 12.6% |
| 19 | Azure | Infra & Cloud | 101 | 12.2% |
| 20 | Kafka | Data Engineering | 78 | 9.4% |
| 21 | Snowflake / BigQuery | Data Engineering | 77 | 9.3% |
| 22 | Rust | Languages | 75 | 9.0% |
| 23 | Airflow | Data Engineering | 70 | 8.4% |
| 24 | Spark | Data Engineering | 66 | 7.9% |
| 25 | Docker | Infra & Cloud | 60 | 7.2% |
| 26 | Evals | LLM & GenAI | 56 | 6.7% |
| 27 | Security | Practices | 52 | 6.3% |
| 28 | Linux | Infra & Cloud | 50 | 6.0% |
| 29 | MCP | LLM & GenAI | 47 | 5.7% |
| 30 | PyTorch | Frameworks & Libraries | 47 | 5.7% |
| 31 | AI Safety | LLM & GenAI | 44 | 5.3% |
| 32 | Databricks | Data Engineering | 43 | 5.2% |
| 33 | Deep Learning | ML Fundamentals | 41 | 4.9% |
| 34 | dbt | Data Engineering | 41 | 4.9% |
| 35 | MLOps | Practices | 40 | 4.8% |
| 36 | RAG | LLM & GenAI | 39 | 4.7% |
| 37 | Recommender Systems | ML Fundamentals | 38 | 4.6% |
| 38 | Prompt Engineering | LLM & GenAI | 35 | 4.2% |
| 39 | Fine-tuning | LLM & GenAI | 33 | 4.0% |
| 40 | A/B Testing | Practices | 32 | 3.9% |

</details>

## Movers

Change in share of postings since 2026-09-21, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| AWS | +1.31 | | Snowflake / BigQuery | -0.45 |
| GCP | +0.95 | | A/B Testing | -0.41 |
| Azure | +0.90 | | dbt | -0.40 |
| Distributed Systems | +0.71 | | Statistics | -0.38 |
| Kubernetes | +0.54 | | CI/CD | -0.27 |
| Docker | +0.45 | | SQL | -0.26 |
| Machine Learning | +0.45 | | Data Pipelines | -0.25 |
| Go | +0.40 | | Airflow | -0.22 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,115 | 38.7% |
| swe | 477 | 16.6% |
| other | 450 | 15.6% |
| ops | 259 | 9.0% |
| product | 223 | 7.7% |
| infra | 155 | 5.4% |
| ml-ai | 80 | 2.8% |
| data | 72 | 2.5% |
| research | 47 | 1.6% |

## Disclosed pay, remote engineering roles

536 of 831 engineering postings (65%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $195,000 |
| Median | $227,735 |
| 75th | $260,000 |
| 90th | $290,000 |

<details><summary>Highest disclosed engineering bands by company</summary>

| Company | Top posted midpoint |
|---|---:|
| Anthropic | $675,000 |
| OpenAI | $455,500 |
| Pinterest | $371,087 |
| Reddit | $351,000 |
| Databricks | $343,425 |
| Agility Robotics | $329,500 |
| Snorkel AI | $316,000 |
| Hightouch | $310,000 |
| Discord | $306,000 |
| GitLab | $301,800 |

</details>

## Who is hiring most

![Top companies](docs/charts/companies.svg)

---

## How this works

Every day at 08:00 UTC a GitHub Actions workflow queries the public job-board APIs of the companies in [`config/companies.json`](config/companies.json) — Greenhouse, Lever and Ashby all expose unauthenticated JSON endpoints. Each posting's description is scanned for the ~66 technologies defined in [`config/skills.json`](config/skills.json), then the description text is discarded and only the derived record is stored.

| Path | What it holds |
|---|---|
| `data/trends.csv` | One row per skill per day — the long-run time series |
| `data/seen.csv` | Every posting id and the date it first appeared |
| `data/snapshots/<week>.json.gz` | Full postings, archived weekly |
| `data/summary.json` | Aggregates for the latest run |
| `config/companies.json` | Tracked companies and their ATS slugs |
| `config/profile.json` | Your skills — drives the daily match issue |
| `config/settings.json` | `remote_only` and other pipeline switches |

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
- Remote status comes from each board's own field where one exists and from the posted location otherwise. Ashby's `isRemote` is ignored because boards set it true on hybrid onsite roles; its `workplaceType` is used instead.


<sub>Generated 2026-09-28T16:27:04+00:00 · 2 board(s) unreachable this run</sub>
