# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-11-27** — tracking **2,865 open remote roles** across **88 companies** (797 of them engineering roles). 1,718 postings disclose pay. **13 appeared today.**

<sub>Remote-only: 14,751 postings were collected across all locations and 19.4% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 797 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 354 | 44.4% |
| 2 | Observability | Practices | 273 | 34.3% |
| 3 | AI Agents | LLM & GenAI | 247 | 31.0% |
| 4 | LLMs | LLM & GenAI | 242 | 30.4% |
| 5 | Distributed Systems | Practices | 233 | 29.2% |
| 6 | Go | Languages | 228 | 28.6% |
| 7 | Machine Learning | ML Fundamentals | 225 | 28.2% |
| 8 | Kubernetes | Infra & Cloud | 218 | 27.4% |
| 9 | AWS | Infra & Cloud | 208 | 26.1% |
| 10 | TypeScript | Languages | 186 | 23.3% |
| 11 | Statistics | ML Fundamentals | 152 | 19.1% |
| 12 | CI/CD | Practices | 136 | 17.1% |
| 13 | GCP | Infra & Cloud | 130 | 16.3% |
| 14 | React | Frameworks & Libraries | 120 | 15.1% |
| 15 | SQL | Languages | 120 | 15.1% |
| 16 | Terraform | Infra & Cloud | 118 | 14.8% |
| 17 | Data Pipelines | Data Engineering | 102 | 12.8% |
| 18 | Java | Languages | 94 | 11.8% |
| 19 | Azure | Infra & Cloud | 72 | 9.0% |
| 20 | Evals | LLM & GenAI | 67 | 8.4% |
| 21 | Snowflake / BigQuery | Data Engineering | 67 | 8.4% |
| 22 | Security | Practices | 66 | 8.3% |
| 23 | Airflow | Data Engineering | 62 | 7.8% |
| 24 | Rust | Languages | 60 | 7.5% |
| 25 | Spark | Data Engineering | 57 | 7.2% |
| 26 | Kafka | Data Engineering | 55 | 6.9% |
| 27 | MCP | LLM & GenAI | 52 | 6.5% |
| 28 | Docker | Infra & Cloud | 45 | 5.6% |
| 29 | Linux | Infra & Cloud | 45 | 5.6% |
| 30 | AI Safety | LLM & GenAI | 41 | 5.1% |
| 31 | PyTorch | Frameworks & Libraries | 38 | 4.8% |
| 32 | Recommender Systems | ML Fundamentals | 38 | 4.8% |
| 33 | Databricks | Data Engineering | 33 | 4.1% |
| 34 | MLOps | Practices | 32 | 4.0% |
| 35 | Deep Learning | ML Fundamentals | 32 | 4.0% |
| 36 | RAG | LLM & GenAI | 31 | 3.9% |
| 37 | GPU Clusters | Infra & Cloud | 31 | 3.9% |
| 38 | dbt | Data Engineering | 31 | 3.9% |
| 39 | Prompt Engineering | LLM & GenAI | 29 | 3.6% |
| 40 | Multimodal | LLM & GenAI | 29 | 3.6% |

</details>

## Movers

Change in share of postings since 2026-11-20, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| CI/CD | +0.42 | | SQL | -0.63 |
| Terraform | +0.35 | | Data Pipelines | -0.57 |
| Go | +0.32 | | Snowflake / BigQuery | -0.40 |
| TypeScript | +0.32 | | Machine Learning | -0.40 |
| AI Agents | +0.31 | | Kafka | -0.22 |
| Linux | +0.24 | | PyTorch | -0.20 |
| React | +0.22 | | Databricks | -0.17 |
| Evals | +0.21 | | RAG | -0.16 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,165 | 40.7% |
| swe | 433 | 15.1% |
| other | 428 | 14.9% |
| ops | 261 | 9.1% |
| product | 214 | 7.5% |
| infra | 175 | 6.1% |
| ml-ai | 78 | 2.7% |
| data | 64 | 2.2% |
| research | 47 | 1.6% |

## Disclosed pay, remote engineering roles

545 of 797 engineering postings (68%) publish a salary range. Figures are the midpoint of the posted band.

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
| Cohere | $362,500 |
| Reddit | $351,000 |
| Harvey | $340,000 |
| Agility Robotics | $329,500 |
| Snorkel AI | $325,000 |
| Coinbase | $320,142 |
| Instacart | $312,500 |

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


<sub>Generated 2026-11-27T17:51:27+00:00 · 5 board(s) unreachable this run</sub>
