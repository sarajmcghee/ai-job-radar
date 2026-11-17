# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-11-17** — tracking **2,913 open remote roles** across **87 companies** (811 of them engineering roles). 1,730 postings disclose pay. **49 appeared today.**

<sub>Remote-only: 14,627 postings were collected across all locations and 19.9% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 811 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 352 | 43.4% |
| 2 | Observability | Practices | 271 | 33.4% |
| 3 | LLMs | LLM & GenAI | 248 | 30.6% |
| 4 | AI Agents | LLM & GenAI | 241 | 29.7% |
| 5 | Distributed Systems | Practices | 237 | 29.2% |
| 6 | Go | Languages | 237 | 29.2% |
| 7 | Machine Learning | ML Fundamentals | 228 | 28.1% |
| 8 | Kubernetes | Infra & Cloud | 215 | 26.5% |
| 9 | AWS | Infra & Cloud | 195 | 24.0% |
| 10 | TypeScript | Languages | 186 | 22.9% |
| 11 | Statistics | ML Fundamentals | 145 | 17.9% |
| 12 | SQL | Languages | 137 | 16.9% |
| 13 | CI/CD | Practices | 134 | 16.5% |
| 14 | GCP | Infra & Cloud | 122 | 15.0% |
| 15 | React | Frameworks & Libraries | 121 | 14.9% |
| 16 | Data Pipelines | Data Engineering | 118 | 14.5% |
| 17 | Terraform | Infra & Cloud | 112 | 13.8% |
| 18 | Java | Languages | 94 | 11.6% |
| 19 | Snowflake / BigQuery | Data Engineering | 75 | 9.2% |
| 20 | Airflow | Data Engineering | 66 | 8.1% |
| 21 | Evals | LLM & GenAI | 63 | 7.8% |
| 22 | Azure | Infra & Cloud | 61 | 7.5% |
| 23 | Security | Practices | 60 | 7.4% |
| 24 | Rust | Languages | 59 | 7.3% |
| 25 | Kafka | Data Engineering | 58 | 7.2% |
| 26 | MCP | LLM & GenAI | 56 | 6.9% |
| 27 | Spark | Data Engineering | 55 | 6.8% |
| 28 | Docker | Infra & Cloud | 48 | 5.9% |
| 29 | Databricks | Data Engineering | 47 | 5.8% |
| 30 | Linux | Infra & Cloud | 45 | 5.5% |
| 31 | PyTorch | Frameworks & Libraries | 40 | 4.9% |
| 32 | dbt | Data Engineering | 39 | 4.8% |
| 33 | AI Safety | LLM & GenAI | 36 | 4.4% |
| 34 | MLOps | Practices | 36 | 4.4% |
| 35 | Recommender Systems | ML Fundamentals | 36 | 4.4% |
| 36 | Prompt Engineering | LLM & GenAI | 32 | 3.9% |
| 37 | Deep Learning | ML Fundamentals | 31 | 3.8% |
| 38 | Multimodal | LLM & GenAI | 30 | 3.7% |
| 39 | RAG | LLM & GenAI | 30 | 3.7% |
| 40 | GPU Clusters | Infra & Cloud | 30 | 3.7% |

</details>

## Movers

Change in share of postings since 2026-11-10, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| CI/CD | +0.51 | | Data Pipelines | -0.25 |
| GCP | +0.44 | | Fine-tuning | -0.24 |
| AWS | +0.44 | | Rust | -0.24 |
| AI Agents | +0.41 | | Python | -0.21 |
| Azure | +0.34 | | MLOps | -0.21 |
| MCP | +0.31 | | Kafka | -0.18 |
| Databricks | +0.28 | | Distributed Systems | -0.17 |
| dbt | +0.28 | | Transformers | -0.17 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,180 | 40.5% |
| swe | 444 | 15.2% |
| other | 421 | 14.5% |
| ops | 276 | 9.5% |
| product | 225 | 7.7% |
| infra | 164 | 5.6% |
| ml-ai | 86 | 3.0% |
| data | 67 | 2.3% |
| research | 50 | 1.7% |

## Disclosed pay, remote engineering roles

552 of 811 engineering postings (68%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $196,000 |
| Median | $226,200 |
| 75th | $260,450 |
| 90th | $289,530 |

<details><summary>Highest disclosed engineering bands by company</summary>

| Company | Top posted midpoint |
|---|---:|
| Anthropic | $675,000 |
| OpenAI | $455,500 |
| Pinterest | $371,087 |
| Reddit | $351,000 |
| Harvey | $340,000 |
| Agility Robotics | $329,500 |
| Coinbase | $320,142 |
| Snorkel AI | $316,000 |
| Discord | $306,000 |
| Cohere | $300,000 |

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


<sub>Generated 2026-11-17T17:21:58+00:00 · 5 board(s) unreachable this run</sub>
