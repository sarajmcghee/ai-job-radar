# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-11-16** — tracking **2,918 open remote roles** across **86 companies** (811 of them engineering roles). 1,741 postings disclose pay. **26 appeared today.**

<sub>Remote-only: 14,645 postings were collected across all locations and 19.9% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 811 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 350 | 43.2% |
| 2 | Observability | Practices | 271 | 33.4% |
| 3 | LLMs | LLM & GenAI | 248 | 30.6% |
| 4 | AI Agents | LLM & GenAI | 240 | 29.6% |
| 5 | Distributed Systems | Practices | 239 | 29.5% |
| 6 | Go | Languages | 237 | 29.2% |
| 7 | Machine Learning | ML Fundamentals | 230 | 28.4% |
| 8 | Kubernetes | Infra & Cloud | 213 | 26.3% |
| 9 | AWS | Infra & Cloud | 195 | 24.0% |
| 10 | TypeScript | Languages | 186 | 22.9% |
| 11 | Statistics | ML Fundamentals | 148 | 18.2% |
| 12 | CI/CD | Practices | 134 | 16.5% |
| 13 | SQL | Languages | 134 | 16.5% |
| 14 | GCP | Infra & Cloud | 125 | 15.4% |
| 15 | React | Frameworks & Libraries | 120 | 14.8% |
| 16 | Data Pipelines | Data Engineering | 114 | 14.1% |
| 17 | Terraform | Infra & Cloud | 113 | 13.9% |
| 18 | Java | Languages | 91 | 11.2% |
| 19 | Snowflake / BigQuery | Data Engineering | 75 | 9.2% |
| 20 | Azure | Infra & Cloud | 64 | 7.9% |
| 21 | Airflow | Data Engineering | 64 | 7.9% |
| 22 | Evals | LLM & GenAI | 64 | 7.9% |
| 23 | Security | Practices | 60 | 7.4% |
| 24 | Kafka | Data Engineering | 60 | 7.4% |
| 25 | Rust | Languages | 60 | 7.4% |
| 26 | MCP | LLM & GenAI | 55 | 6.8% |
| 27 | Spark | Data Engineering | 54 | 6.7% |
| 28 | Databricks | Data Engineering | 48 | 5.9% |
| 29 | Docker | Infra & Cloud | 48 | 5.9% |
| 30 | Linux | Infra & Cloud | 45 | 5.5% |
| 31 | dbt | Data Engineering | 40 | 4.9% |
| 32 | PyTorch | Frameworks & Libraries | 39 | 4.8% |
| 33 | AI Safety | LLM & GenAI | 37 | 4.6% |
| 34 | MLOps | Practices | 35 | 4.3% |
| 35 | Recommender Systems | ML Fundamentals | 35 | 4.3% |
| 36 | Prompt Engineering | LLM & GenAI | 34 | 4.2% |
| 37 | Deep Learning | ML Fundamentals | 31 | 3.8% |
| 38 | RAG | LLM & GenAI | 31 | 3.8% |
| 39 | A/B Testing | Practices | 29 | 3.6% |
| 40 | Multimodal | LLM & GenAI | 29 | 3.6% |

</details>

## Movers

Change in share of postings since 2026-11-08, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| CI/CD | +0.58 | | Python | -0.61 |
| dbt | +0.57 | | Data Pipelines | -0.35 |
| GCP | +0.50 | | SQL | -0.34 |
| AWS | +0.44 | | Java | -0.26 |
| Azure | +0.37 | | MLOps | -0.25 |
| Distributed Systems | +0.32 | | PyTorch | -0.22 |
| Evals | +0.26 | | Transformers | -0.21 |
| Kubernetes | +0.25 | | Airflow | -0.15 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,184 | 40.6% |
| swe | 443 | 15.2% |
| other | 423 | 14.5% |
| ops | 280 | 9.6% |
| product | 220 | 7.5% |
| infra | 165 | 5.7% |
| ml-ai | 88 | 3.0% |
| data | 66 | 2.3% |
| research | 49 | 1.7% |

## Disclosed pay, remote engineering roles

554 of 811 engineering postings (68%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $196,000 |
| Median | $227,000 |
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


<sub>Generated 2026-11-16T17:54:18+00:00 · 5 board(s) unreachable this run</sub>
