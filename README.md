# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-11-10** — tracking **2,912 open remote roles** across **87 companies** (818 of them engineering roles). 1,731 postings disclose pay. **112 appeared today.**

<sub>Remote-only: 14,632 postings were collected across all locations and 19.9% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 818 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 361 | 44.1% |
| 2 | Observability | Practices | 277 | 33.9% |
| 3 | Distributed Systems | Practices | 245 | 30.0% |
| 4 | LLMs | LLM & GenAI | 241 | 29.5% |
| 5 | AI Agents | LLM & GenAI | 236 | 28.9% |
| 6 | Machine Learning | ML Fundamentals | 236 | 28.9% |
| 7 | Go | Languages | 233 | 28.5% |
| 8 | Kubernetes | Infra & Cloud | 212 | 25.9% |
| 9 | AWS | Infra & Cloud | 188 | 23.0% |
| 10 | TypeScript | Languages | 183 | 22.4% |
| 11 | Statistics | ML Fundamentals | 150 | 18.3% |
| 12 | SQL | Languages | 144 | 17.6% |
| 13 | CI/CD | Practices | 125 | 15.3% |
| 14 | Data Pipelines | Data Engineering | 124 | 15.2% |
| 15 | React | Frameworks & Libraries | 119 | 14.5% |
| 16 | GCP | Infra & Cloud | 115 | 14.1% |
| 17 | Terraform | Infra & Cloud | 110 | 13.4% |
| 18 | Java | Languages | 98 | 12.0% |
| 19 | Snowflake / BigQuery | Data Engineering | 72 | 8.8% |
| 20 | Airflow | Data Engineering | 68 | 8.3% |
| 21 | Rust | Languages | 65 | 7.9% |
| 22 | Kafka | Data Engineering | 64 | 7.8% |
| 23 | Evals | LLM & GenAI | 61 | 7.5% |
| 24 | Azure | Infra & Cloud | 60 | 7.3% |
| 25 | Spark | Data Engineering | 58 | 7.1% |
| 26 | Security | Practices | 52 | 6.4% |
| 27 | MCP | LLM & GenAI | 47 | 5.7% |
| 28 | Linux | Infra & Cloud | 46 | 5.6% |
| 29 | Docker | Infra & Cloud | 45 | 5.5% |
| 30 | Databricks | Data Engineering | 42 | 5.1% |
| 31 | PyTorch | Frameworks & Libraries | 42 | 5.1% |
| 32 | dbt | Data Engineering | 41 | 5.0% |
| 33 | MLOps | Practices | 40 | 4.9% |
| 34 | Recommender Systems | ML Fundamentals | 37 | 4.5% |
| 35 | AI Safety | LLM & GenAI | 35 | 4.3% |
| 36 | Deep Learning | ML Fundamentals | 33 | 4.0% |
| 37 | Multimodal | LLM & GenAI | 32 | 3.9% |
| 38 | RAG | LLM & GenAI | 32 | 3.9% |
| 39 | Prompt Engineering | LLM & GenAI | 30 | 3.7% |
| 40 | A/B Testing | Practices | 28 | 3.4% |

</details>

## Movers

Change in share of postings since 2026-11-03, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Observability | +0.62 | | Machine Learning | -0.53 |
| Linux | +0.36 | | SQL | -0.27 |
| Distributed Systems | +0.32 | | Snowflake / BigQuery | -0.24 |
| CI/CD | +0.27 | | Python | -0.22 |
| Go | +0.25 | | AWS | -0.19 |
| Prompt Engineering | +0.24 | | Computer Vision | -0.18 |
| TypeScript | +0.22 | | PyTorch | -0.18 |
| Evals | +0.19 | | Spark | -0.16 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,171 | 40.2% |
| swe | 447 | 15.4% |
| other | 416 | 14.3% |
| ops | 274 | 9.4% |
| product | 233 | 8.0% |
| infra | 160 | 5.5% |
| ml-ai | 90 | 3.1% |
| data | 70 | 2.4% |
| research | 51 | 1.8% |

## Disclosed pay, remote engineering roles

549 of 818 engineering postings (67%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $196,285 |
| Median | $228,500 |
| 75th | $260,450 |
| 90th | $292,500 |

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


<sub>Generated 2026-11-10T16:03:51+00:00 · 5 board(s) unreachable this run</sub>
