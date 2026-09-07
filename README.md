# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-09-07** — tracking **3,059 open remote roles** across **95 companies** (883 of them engineering roles). 1,712 postings disclose pay. **4 appeared today.**

<sub>Remote-only: 14,138 postings were collected across all locations and 21.6% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 883 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 428 | 48.5% |
| 2 | Observability | Practices | 298 | 33.7% |
| 3 | Distributed Systems | Practices | 284 | 32.2% |
| 4 | Machine Learning | ML Fundamentals | 272 | 30.8% |
| 5 | Go | Languages | 270 | 30.6% |
| 6 | AI Agents | LLM & GenAI | 262 | 29.7% |
| 7 | LLMs | LLM & GenAI | 251 | 28.4% |
| 8 | AWS | Infra & Cloud | 240 | 27.2% |
| 9 | Kubernetes | Infra & Cloud | 235 | 26.6% |
| 10 | TypeScript | Languages | 186 | 21.1% |
| 11 | Statistics | ML Fundamentals | 174 | 19.7% |
| 12 | SQL | Languages | 157 | 17.8% |
| 13 | GCP | Infra & Cloud | 149 | 16.9% |
| 14 | Data Pipelines | Data Engineering | 145 | 16.4% |
| 15 | CI/CD | Practices | 140 | 15.9% |
| 16 | Terraform | Infra & Cloud | 133 | 15.1% |
| 17 | Java | Languages | 132 | 14.9% |
| 18 | React | Frameworks & Libraries | 110 | 12.5% |
| 19 | Azure | Infra & Cloud | 104 | 11.8% |
| 20 | Snowflake / BigQuery | Data Engineering | 84 | 9.5% |
| 21 | Airflow | Data Engineering | 81 | 9.2% |
| 22 | Kafka | Data Engineering | 74 | 8.4% |
| 23 | Rust | Languages | 74 | 8.4% |
| 24 | Spark | Data Engineering | 72 | 8.2% |
| 25 | Evals | LLM & GenAI | 71 | 8.0% |
| 26 | Docker | Infra & Cloud | 62 | 7.0% |
| 27 | Linux | Infra & Cloud | 55 | 6.2% |
| 28 | Security | Practices | 51 | 5.8% |
| 29 | PyTorch | Frameworks & Libraries | 51 | 5.8% |
| 30 | Databricks | Data Engineering | 48 | 5.4% |
| 31 | RAG | LLM & GenAI | 47 | 5.3% |
| 32 | dbt | Data Engineering | 45 | 5.1% |
| 33 | A/B Testing | Practices | 44 | 5.0% |
| 34 | Prompt Engineering | LLM & GenAI | 44 | 5.0% |
| 35 | MCP | LLM & GenAI | 43 | 4.9% |
| 36 | Deep Learning | ML Fundamentals | 42 | 4.8% |
| 37 | Recommender Systems | ML Fundamentals | 42 | 4.8% |
| 38 | MLOps | Practices | 41 | 4.6% |
| 39 | Fine-tuning | LLM & GenAI | 36 | 4.1% |
| 40 | AI Safety | LLM & GenAI | 35 | 4.0% |

</details>

## Movers

Change in share of postings since 2026-08-31, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Statistics | +0.40 | | Azure | -2.49 |
| CI/CD | +0.17 | | GCP | -2.37 |
| Databricks | +0.12 | | Distributed Systems | -1.98 |
| Ray | +0.07 | | AWS | -1.51 |
| MCP | +0.07 | | Kubernetes | -1.41 |
| A/B Testing | +0.07 | | Kafka | -1.16 |
| GPU Clusters | +0.07 | | Spark | -0.88 |
| NLP | +0.07 | | TypeScript | -0.81 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,191 | 38.9% |
| swe | 513 | 16.8% |
| other | 470 | 15.4% |
| ops | 284 | 9.3% |
| product | 231 | 7.6% |
| infra | 153 | 5.0% |
| ml-ai | 94 | 3.1% |
| data | 79 | 2.6% |
| research | 44 | 1.4% |

## Disclosed pay, remote engineering roles

568 of 883 engineering postings (64%) publish a salary range. Figures are the midpoint of the posted band.

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


<sub>Generated 2026-09-07T13:58:30+00:00 · 2 board(s) unreachable this run</sub>
