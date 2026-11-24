# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-11-24** — tracking **2,889 open remote roles** across **87 companies** (793 of them engineering roles). 1,721 postings disclose pay. **59 appeared today.**

<sub>Remote-only: 14,719 postings were collected across all locations and 19.6% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 793 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 358 | 45.1% |
| 2 | Observability | Practices | 273 | 34.4% |
| 3 | AI Agents | LLM & GenAI | 239 | 30.1% |
| 4 | LLMs | LLM & GenAI | 238 | 30.0% |
| 5 | Distributed Systems | Practices | 230 | 29.0% |
| 6 | Go | Languages | 226 | 28.5% |
| 7 | Machine Learning | ML Fundamentals | 222 | 28.0% |
| 8 | Kubernetes | Infra & Cloud | 216 | 27.2% |
| 9 | AWS | Infra & Cloud | 201 | 25.3% |
| 10 | TypeScript | Languages | 190 | 24.0% |
| 11 | Statistics | ML Fundamentals | 148 | 18.7% |
| 12 | CI/CD | Practices | 133 | 16.8% |
| 13 | SQL | Languages | 127 | 16.0% |
| 14 | GCP | Infra & Cloud | 126 | 15.9% |
| 15 | React | Frameworks & Libraries | 118 | 14.9% |
| 16 | Terraform | Infra & Cloud | 117 | 14.8% |
| 17 | Data Pipelines | Data Engineering | 103 | 13.0% |
| 18 | Java | Languages | 94 | 11.9% |
| 19 | Azure | Infra & Cloud | 67 | 8.4% |
| 20 | Security | Practices | 65 | 8.2% |
| 21 | Evals | LLM & GenAI | 63 | 7.9% |
| 22 | Snowflake / BigQuery | Data Engineering | 63 | 7.9% |
| 23 | Airflow | Data Engineering | 62 | 7.8% |
| 24 | Rust | Languages | 60 | 7.6% |
| 25 | Spark | Data Engineering | 56 | 7.1% |
| 26 | Kafka | Data Engineering | 55 | 6.9% |
| 27 | MCP | LLM & GenAI | 52 | 6.6% |
| 28 | Docker | Infra & Cloud | 44 | 5.5% |
| 29 | Linux | Infra & Cloud | 43 | 5.4% |
| 30 | AI Safety | LLM & GenAI | 41 | 5.2% |
| 31 | PyTorch | Frameworks & Libraries | 40 | 5.0% |
| 32 | Recommender Systems | ML Fundamentals | 37 | 4.7% |
| 33 | Databricks | Data Engineering | 33 | 4.2% |
| 34 | MLOps | Practices | 32 | 4.0% |
| 35 | Deep Learning | ML Fundamentals | 32 | 4.0% |
| 36 | GPU Clusters | Infra & Cloud | 32 | 4.0% |
| 37 | Multimodal | LLM & GenAI | 30 | 3.8% |
| 38 | RAG | LLM & GenAI | 30 | 3.8% |
| 39 | Prompt Engineering | LLM & GenAI | 29 | 3.7% |
| 40 | A/B Testing | Practices | 28 | 3.5% |

</details>

## Movers

Change in share of postings since 2026-11-17, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Terraform | +0.43 | | Data Pipelines | -0.80 |
| Security | +0.27 | | Databricks | -0.58 |
| TypeScript | +0.26 | | Snowflake / BigQuery | -0.53 |
| Observability | +0.22 | | Machine Learning | -0.42 |
| Azure | +0.21 | | dbt | -0.32 |
| AWS | +0.16 | | Python | -0.22 |
| Embeddings | +0.15 | | MLOps | -0.19 |
| Evals | +0.14 | | SQL | -0.17 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,190 | 41.2% |
| swe | 427 | 14.8% |
| other | 422 | 14.6% |
| ops | 271 | 9.4% |
| product | 213 | 7.4% |
| infra | 173 | 6.0% |
| ml-ai | 79 | 2.7% |
| data | 66 | 2.3% |
| research | 48 | 1.7% |

## Disclosed pay, remote engineering roles

538 of 793 engineering postings (68%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $197,050 |
| Median | $228,950 |
| 75th | $260,450 |
| 90th | $308,520 |

<details><summary>Highest disclosed engineering bands by company</summary>

| Company | Top posted midpoint |
|---|---:|
| Anthropic | $675,000 |
| OpenAI | $455,500 |
| Pinterest | $371,087 |
| Reddit | $351,000 |
| Harvey | $340,000 |
| Agility Robotics | $329,500 |
| Snorkel AI | $325,000 |
| Coinbase | $320,142 |
| Discord | $310,000 |
| Plaid | $308,520 |

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


<sub>Generated 2026-11-24T19:20:43+00:00 · 5 board(s) unreachable this run</sub>
