# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-10-30** — tracking **2,879 open remote roles** across **90 companies** (819 of them engineering roles). 1,667 postings disclose pay. **58 appeared today.**

<sub>Remote-only: 14,482 postings were collected across all locations and 19.9% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 819 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 360 | 44.0% |
| 2 | Observability | Practices | 264 | 32.2% |
| 3 | Machine Learning | ML Fundamentals | 244 | 29.8% |
| 4 | Go | Languages | 240 | 29.3% |
| 5 | Distributed Systems | Practices | 239 | 29.2% |
| 6 | LLMs | LLM & GenAI | 233 | 28.4% |
| 7 | AI Agents | LLM & GenAI | 223 | 27.2% |
| 8 | Kubernetes | Infra & Cloud | 213 | 26.0% |
| 9 | AWS | Infra & Cloud | 198 | 24.2% |
| 10 | TypeScript | Languages | 175 | 21.4% |
| 11 | Statistics | ML Fundamentals | 158 | 19.3% |
| 12 | SQL | Languages | 145 | 17.7% |
| 13 | Data Pipelines | Data Engineering | 123 | 15.0% |
| 14 | GCP | Infra & Cloud | 117 | 14.3% |
| 15 | CI/CD | Practices | 116 | 14.2% |
| 16 | Terraform | Infra & Cloud | 116 | 14.2% |
| 17 | React | Frameworks & Libraries | 113 | 13.8% |
| 18 | Java | Languages | 96 | 11.7% |
| 19 | Snowflake / BigQuery | Data Engineering | 77 | 9.4% |
| 20 | Airflow | Data Engineering | 66 | 8.1% |
| 21 | Azure | Infra & Cloud | 65 | 7.9% |
| 22 | Rust | Languages | 65 | 7.9% |
| 23 | Kafka | Data Engineering | 64 | 7.8% |
| 24 | Spark | Data Engineering | 61 | 7.4% |
| 25 | Evals | LLM & GenAI | 55 | 6.7% |
| 26 | Security | Practices | 54 | 6.6% |
| 27 | PyTorch | Frameworks & Libraries | 49 | 6.0% |
| 28 | Docker | Infra & Cloud | 46 | 5.6% |
| 29 | AI Safety | LLM & GenAI | 44 | 5.4% |
| 30 | Databricks | Data Engineering | 43 | 5.3% |
| 31 | Linux | Infra & Cloud | 43 | 5.3% |
| 32 | dbt | Data Engineering | 42 | 5.1% |
| 33 | MCP | LLM & GenAI | 41 | 5.0% |
| 34 | Recommender Systems | ML Fundamentals | 41 | 5.0% |
| 35 | Deep Learning | ML Fundamentals | 37 | 4.5% |
| 36 | MLOps | Practices | 35 | 4.3% |
| 37 | Multimodal | LLM & GenAI | 35 | 4.3% |
| 38 | RAG | LLM & GenAI | 31 | 3.8% |
| 39 | TensorFlow | Frameworks & Libraries | 31 | 3.8% |
| 40 | Fine-tuning | LLM & GenAI | 30 | 3.7% |

</details>

## Movers

Change in share of postings since 2026-10-23, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Snowflake / BigQuery | +0.31 | | Observability | -1.04 |
| SQL | +0.11 | | Kubernetes | -0.76 |
| LangChain | +0.10 | | LLMs | -0.67 |
| Airflow | +0.06 | | AWS | -0.67 |
| Evals | +0.05 | | GCP | -0.61 |
| Linux | +0.01 | | Distributed Systems | -0.61 |
| Vector Databases | +0.00 | | Python | -0.53 |
| Ray | +0.00 | | Data Pipelines | -0.49 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,132 | 39.3% |
| other | 446 | 15.5% |
| swe | 443 | 15.4% |
| ops | 258 | 9.0% |
| product | 224 | 7.8% |
| infra | 158 | 5.5% |
| ml-ai | 96 | 3.3% |
| data | 72 | 2.5% |
| research | 50 | 1.7% |

## Disclosed pay, remote engineering roles

549 of 819 engineering postings (67%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $196,000 |
| Median | $227,735 |
| 75th | $260,450 |
| 90th | $299,500 |

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


<sub>Generated 2026-10-30T14:50:09+00:00 · 4 board(s) unreachable this run</sub>
