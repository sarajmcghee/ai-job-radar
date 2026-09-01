# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-09-01** — tracking **3,190 open remote roles** across **94 companies** (947 of them engineering roles). 1,769 postings disclose pay. **36 appeared today.**

<sub>Remote-only: 14,210 postings were collected across all locations and 22.4% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 947 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 458 | 48.4% |
| 2 | Distributed Systems | Practices | 333 | 35.2% |
| 3 | Observability | Practices | 322 | 34.0% |
| 4 | Go | Languages | 291 | 30.7% |
| 5 | Machine Learning | ML Fundamentals | 287 | 30.3% |
| 6 | Kubernetes | Infra & Cloud | 273 | 28.8% |
| 7 | AWS | Infra & Cloud | 272 | 28.7% |
| 8 | AI Agents | LLM & GenAI | 266 | 28.1% |
| 9 | LLMs | LLM & GenAI | 265 | 28.0% |
| 10 | TypeScript | Languages | 211 | 22.3% |
| 11 | GCP | Infra & Cloud | 197 | 20.8% |
| 12 | SQL | Languages | 190 | 20.1% |
| 13 | Statistics | ML Fundamentals | 176 | 18.6% |
| 14 | Azure | Infra & Cloud | 154 | 16.3% |
| 15 | Data Pipelines | Data Engineering | 153 | 16.2% |
| 16 | Terraform | Infra & Cloud | 148 | 15.6% |
| 17 | Java | Languages | 142 | 15.0% |
| 18 | CI/CD | Practices | 135 | 14.3% |
| 19 | React | Frameworks & Libraries | 115 | 12.1% |
| 20 | Kafka | Data Engineering | 96 | 10.1% |
| 21 | Airflow | Data Engineering | 91 | 9.6% |
| 22 | Spark | Data Engineering | 89 | 9.4% |
| 23 | Snowflake / BigQuery | Data Engineering | 86 | 9.1% |
| 24 | Docker | Infra & Cloud | 79 | 8.3% |
| 25 | Evals | LLM & GenAI | 77 | 8.1% |
| 26 | Rust | Languages | 75 | 7.9% |
| 27 | Linux | Infra & Cloud | 66 | 7.0% |
| 28 | Security | Practices | 60 | 6.3% |
| 29 | PyTorch | Frameworks & Libraries | 56 | 5.9% |
| 30 | dbt | Data Engineering | 53 | 5.6% |
| 31 | RAG | LLM & GenAI | 52 | 5.5% |
| 32 | Databricks | Data Engineering | 50 | 5.3% |
| 33 | MLOps | Practices | 48 | 5.1% |
| 34 | MCP | LLM & GenAI | 46 | 4.9% |
| 35 | Prompt Engineering | LLM & GenAI | 46 | 4.9% |
| 36 | Recommender Systems | ML Fundamentals | 44 | 4.6% |
| 37 | A/B Testing | Practices | 43 | 4.5% |
| 38 | Deep Learning | ML Fundamentals | 43 | 4.5% |
| 39 | AI Safety | LLM & GenAI | 41 | 4.3% |
| 40 | Embeddings | LLM & GenAI | 41 | 4.3% |

</details>

## Movers

Change in share of postings since 2026-08-27, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| SQL | +0.33 | | Distributed Systems | -1.23 |
| Machine Learning | +0.23 | | Airflow | -1.02 |
| Evals | +0.18 | | Go | -0.79 |
| Databricks | +0.16 | | TypeScript | -0.73 |
| Snowflake / BigQuery | +0.14 | | GCP | -0.66 |
| Embeddings | +0.14 | | Java | -0.65 |
| LLMs | +0.14 | | Observability | -0.62 |
| MCP | +0.12 | | Azure | -0.55 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,213 | 38.0% |
| swe | 549 | 17.2% |
| other | 508 | 15.9% |
| ops | 279 | 8.7% |
| product | 243 | 7.6% |
| infra | 178 | 5.6% |
| ml-ai | 99 | 3.1% |
| data | 78 | 2.4% |
| research | 43 | 1.3% |

## Disclosed pay, remote engineering roles

591 of 947 engineering postings (62%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $187,450 |
| Median | $227,735 |
| 75th | $260,450 |
| 90th | $283,000 |

<details><summary>Highest disclosed engineering bands by company</summary>

| Company | Top posted midpoint |
|---|---:|
| Anthropic | $675,000 |
| OpenAI | $418,500 |
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


<sub>Generated 2026-09-01T13:04:33+00:00 · 1 board(s) unreachable this run</sub>
