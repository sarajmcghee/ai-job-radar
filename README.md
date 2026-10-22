# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-10-22** — tracking **2,868 open remote roles** across **90 companies** (846 of them engineering roles). 1,670 postings disclose pay. **81 appeared today.**

<sub>Remote-only: 14,413 postings were collected across all locations and 19.9% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 846 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 368 | 43.5% |
| 2 | Observability | Practices | 293 | 34.6% |
| 3 | Distributed Systems | Practices | 259 | 30.6% |
| 4 | LLMs | LLM & GenAI | 253 | 29.9% |
| 5 | Machine Learning | ML Fundamentals | 253 | 29.9% |
| 6 | Go | Languages | 246 | 29.1% |
| 7 | AI Agents | LLM & GenAI | 233 | 27.5% |
| 8 | Kubernetes | Infra & Cloud | 223 | 26.4% |
| 9 | AWS | Infra & Cloud | 221 | 26.1% |
| 10 | TypeScript | Languages | 178 | 21.0% |
| 11 | Statistics | ML Fundamentals | 165 | 19.5% |
| 12 | SQL | Languages | 146 | 17.3% |
| 13 | Data Pipelines | Data Engineering | 132 | 15.6% |
| 14 | GCP | Infra & Cloud | 132 | 15.6% |
| 15 | Terraform | Infra & Cloud | 130 | 15.4% |
| 16 | CI/CD | Practices | 118 | 13.9% |
| 17 | React | Frameworks & Libraries | 118 | 13.9% |
| 18 | Java | Languages | 95 | 11.2% |
| 19 | Snowflake / BigQuery | Data Engineering | 81 | 9.6% |
| 20 | Azure | Infra & Cloud | 78 | 9.2% |
| 21 | Airflow | Data Engineering | 67 | 7.9% |
| 22 | Kafka | Data Engineering | 66 | 7.8% |
| 23 | Rust | Languages | 66 | 7.8% |
| 24 | Spark | Data Engineering | 60 | 7.1% |
| 25 | Evals | LLM & GenAI | 56 | 6.6% |
| 26 | Security | Practices | 53 | 6.3% |
| 27 | PyTorch | Frameworks & Libraries | 52 | 6.1% |
| 28 | dbt | Data Engineering | 51 | 6.0% |
| 29 | Docker | Infra & Cloud | 48 | 5.7% |
| 30 | AI Safety | LLM & GenAI | 46 | 5.4% |
| 31 | Databricks | Data Engineering | 44 | 5.2% |
| 32 | Linux | Infra & Cloud | 44 | 5.2% |
| 33 | Recommender Systems | ML Fundamentals | 44 | 5.2% |
| 34 | MCP | LLM & GenAI | 42 | 5.0% |
| 35 | Deep Learning | ML Fundamentals | 40 | 4.7% |
| 36 | Multimodal | LLM & GenAI | 39 | 4.6% |
| 37 | MLOps | Practices | 38 | 4.5% |
| 38 | Fine-tuning | LLM & GenAI | 37 | 4.4% |
| 39 | Prompt Engineering | LLM & GenAI | 33 | 3.9% |
| 40 | RAG | LLM & GenAI | 33 | 3.9% |

</details>

## Movers

Change in share of postings since 2026-10-15, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Observability | +0.97 | | SQL | -0.86 |
| Azure | +0.84 | | Python | -0.85 |
| GCP | +0.71 | | Machine Learning | -0.76 |
| AWS | +0.64 | | React | -0.43 |
| AI Agents | +0.48 | | Statistics | -0.42 |
| Terraform | +0.43 | | Airflow | -0.31 |
| Kubernetes | +0.41 | | Data Pipelines | -0.26 |
| Security | +0.33 | | dbt | -0.23 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,108 | 38.6% |
| swe | 461 | 16.1% |
| other | 419 | 14.6% |
| ops | 266 | 9.3% |
| product | 229 | 8.0% |
| infra | 159 | 5.5% |
| ml-ai | 96 | 3.3% |
| data | 79 | 2.8% |
| research | 51 | 1.8% |

## Disclosed pay, remote engineering roles

564 of 846 engineering postings (67%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $196,285 |
| Median | $226,200 |
| 75th | $260,050 |
| 90th | $289,530 |

<details><summary>Highest disclosed engineering bands by company</summary>

| Company | Top posted midpoint |
|---|---:|
| Anthropic | $675,000 |
| OpenAI | $455,500 |
| Pinterest | $371,087 |
| Reddit | $351,000 |
| Agility Robotics | $329,500 |
| Coinbase | $320,142 |
| Snorkel AI | $316,000 |
| GitLab | $314,000 |
| Discord | $306,000 |
| Pika | $300,000 |

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


<sub>Generated 2026-10-22T13:27:01+00:00 · 4 board(s) unreachable this run</sub>
