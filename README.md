# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-09-14** — tracking **2,972 open remote roles** across **94 companies** (849 of them engineering roles). 1,671 postings disclose pay. **8 appeared today.**

<sub>Remote-only: 14,116 postings were collected across all locations and 21.1% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 849 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 407 | 47.9% |
| 2 | Observability | Practices | 288 | 33.9% |
| 3 | Distributed Systems | Practices | 275 | 32.4% |
| 4 | Machine Learning | ML Fundamentals | 261 | 30.7% |
| 5 | Go | Languages | 260 | 30.6% |
| 6 | AI Agents | LLM & GenAI | 246 | 29.0% |
| 7 | LLMs | LLM & GenAI | 243 | 28.6% |
| 8 | AWS | Infra & Cloud | 232 | 27.3% |
| 9 | Kubernetes | Infra & Cloud | 226 | 26.6% |
| 10 | TypeScript | Languages | 177 | 20.8% |
| 11 | SQL | Languages | 154 | 18.1% |
| 12 | Statistics | ML Fundamentals | 150 | 17.7% |
| 13 | Data Pipelines | Data Engineering | 143 | 16.8% |
| 14 | GCP | Infra & Cloud | 140 | 16.5% |
| 15 | CI/CD | Practices | 133 | 15.7% |
| 16 | Terraform | Infra & Cloud | 127 | 15.0% |
| 17 | Java | Languages | 115 | 13.5% |
| 18 | React | Frameworks & Libraries | 102 | 12.0% |
| 19 | Azure | Infra & Cloud | 90 | 10.6% |
| 20 | Airflow | Data Engineering | 82 | 9.7% |
| 21 | Rust | Languages | 72 | 8.5% |
| 22 | Snowflake / BigQuery | Data Engineering | 72 | 8.5% |
| 23 | Kafka | Data Engineering | 71 | 8.4% |
| 24 | Evals | LLM & GenAI | 70 | 8.2% |
| 25 | Spark | Data Engineering | 67 | 7.9% |
| 26 | Docker | Infra & Cloud | 59 | 6.9% |
| 27 | Linux | Infra & Cloud | 55 | 6.5% |
| 28 | Security | Practices | 52 | 6.1% |
| 29 | PyTorch | Frameworks & Libraries | 48 | 5.7% |
| 30 | RAG | LLM & GenAI | 46 | 5.4% |
| 31 | dbt | Data Engineering | 45 | 5.3% |
| 32 | Deep Learning | ML Fundamentals | 41 | 4.8% |
| 33 | A/B Testing | Practices | 40 | 4.7% |
| 34 | Recommender Systems | ML Fundamentals | 40 | 4.7% |
| 35 | MLOps | Practices | 39 | 4.6% |
| 36 | Databricks | Data Engineering | 38 | 4.5% |
| 37 | MCP | LLM & GenAI | 37 | 4.4% |
| 38 | AI Safety | LLM & GenAI | 37 | 4.4% |
| 39 | Fine-tuning | LLM & GenAI | 35 | 4.1% |
| 40 | Prompt Engineering | LLM & GenAI | 35 | 4.1% |

</details>

## Movers

Change in share of postings since 2026-09-07, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| AWS | +0.79 | | Statistics | -0.61 |
| GCP | +0.24 | | SQL | -0.39 |
| Azure | +0.21 | | dbt | -0.37 |
| Data Pipelines | +0.18 | | Java | -0.34 |
| Airflow | +0.17 | | AI Safety | -0.32 |
| LangChain | +0.13 | | Snowflake / BigQuery | -0.31 |
| Kubernetes | +0.11 | | MCP | -0.25 |
| RAG | +0.11 | | AI Agents | -0.20 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,172 | 39.4% |
| swe | 491 | 16.5% |
| other | 451 | 15.2% |
| ops | 268 | 9.0% |
| product | 232 | 7.8% |
| infra | 150 | 5.0% |
| ml-ai | 85 | 2.9% |
| data | 77 | 2.6% |
| research | 46 | 1.5% |

## Disclosed pay, remote engineering roles

552 of 849 engineering postings (65%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $196,185 |
| Median | $228,500 |
| 75th | $260,000 |
| 90th | $290,000 |

<details><summary>Highest disclosed engineering bands by company</summary>

| Company | Top posted midpoint |
|---|---:|
| Anthropic | $675,000 |
| OpenAI | $455,500 |
| Pinterest | $371,087 |
| Reddit | $351,000 |
| Vanta | $349,500 |
| Databricks | $343,425 |
| Agility Robotics | $329,500 |
| Mercury | $325,900 |
| Snorkel AI | $316,000 |
| Hightouch | $310,000 |

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


<sub>Generated 2026-09-14T14:44:11+00:00 · 2 board(s) unreachable this run</sub>
