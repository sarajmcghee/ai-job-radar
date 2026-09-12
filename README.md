# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-09-12** — tracking **2,995 open remote roles** across **94 companies** (852 of them engineering roles). 1,682 postings disclose pay. **58 appeared today.**

<sub>Remote-only: 14,142 postings were collected across all locations and 21.2% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 852 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 409 | 48.0% |
| 2 | Observability | Practices | 288 | 33.8% |
| 3 | Distributed Systems | Practices | 276 | 32.4% |
| 4 | Machine Learning | ML Fundamentals | 262 | 30.8% |
| 5 | Go | Languages | 259 | 30.4% |
| 6 | AI Agents | LLM & GenAI | 250 | 29.3% |
| 7 | LLMs | LLM & GenAI | 244 | 28.6% |
| 8 | AWS | Infra & Cloud | 232 | 27.2% |
| 9 | Kubernetes | Infra & Cloud | 227 | 26.6% |
| 10 | TypeScript | Languages | 178 | 20.9% |
| 11 | SQL | Languages | 157 | 18.4% |
| 12 | Statistics | ML Fundamentals | 152 | 17.8% |
| 13 | Data Pipelines | Data Engineering | 146 | 17.1% |
| 14 | GCP | Infra & Cloud | 140 | 16.4% |
| 15 | CI/CD | Practices | 132 | 15.5% |
| 16 | Terraform | Infra & Cloud | 126 | 14.8% |
| 17 | Java | Languages | 115 | 13.5% |
| 18 | React | Frameworks & Libraries | 103 | 12.1% |
| 19 | Azure | Infra & Cloud | 89 | 10.4% |
| 20 | Airflow | Data Engineering | 81 | 9.5% |
| 21 | Rust | Languages | 73 | 8.6% |
| 22 | Snowflake / BigQuery | Data Engineering | 72 | 8.5% |
| 23 | Kafka | Data Engineering | 71 | 8.3% |
| 24 | Evals | LLM & GenAI | 71 | 8.3% |
| 25 | Spark | Data Engineering | 67 | 7.9% |
| 26 | Docker | Infra & Cloud | 60 | 7.0% |
| 27 | Linux | Infra & Cloud | 54 | 6.3% |
| 28 | Security | Practices | 52 | 6.1% |
| 29 | PyTorch | Frameworks & Libraries | 48 | 5.6% |
| 30 | RAG | LLM & GenAI | 47 | 5.5% |
| 31 | dbt | Data Engineering | 47 | 5.5% |
| 32 | Deep Learning | ML Fundamentals | 41 | 4.8% |
| 33 | A/B Testing | Practices | 40 | 4.7% |
| 34 | Recommender Systems | ML Fundamentals | 40 | 4.7% |
| 35 | Databricks | Data Engineering | 39 | 4.6% |
| 36 | MLOps | Practices | 39 | 4.6% |
| 37 | MCP | LLM & GenAI | 38 | 4.5% |
| 38 | Prompt Engineering | LLM & GenAI | 38 | 4.5% |
| 39 | AI Safety | LLM & GenAI | 36 | 4.2% |
| 40 | Fine-tuning | LLM & GenAI | 35 | 4.1% |

</details>

## Movers

Change in share of postings since 2026-09-05, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| AWS | +0.63 | | Statistics | -0.57 |
| Data Pipelines | +0.19 | | AI Safety | -0.43 |
| GCP | +0.14 | | Snowflake / BigQuery | -0.38 |
| Rust | +0.13 | | SQL | -0.38 |
| LangChain | +0.11 | | Java | -0.37 |
| Computer Vision | +0.10 | | dbt | -0.35 |
| NLP | +0.10 | | MCP | -0.26 |
| Databricks | +0.07 | | React | -0.24 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,186 | 39.6% |
| swe | 493 | 16.5% |
| other | 452 | 15.1% |
| ops | 272 | 9.1% |
| product | 233 | 7.8% |
| infra | 149 | 5.0% |
| ml-ai | 85 | 2.8% |
| data | 79 | 2.6% |
| research | 46 | 1.5% |

## Disclosed pay, remote engineering roles

554 of 852 engineering postings (65%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $195,450 |
| Median | $228,085 |
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


<sub>Generated 2026-09-12T11:59:17+00:00 · 2 board(s) unreachable this run</sub>
