# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-10-28** — tracking **2,888 open remote roles** across **90 companies** (821 of them engineering roles). 1,676 postings disclose pay. **47 appeared today.**

<sub>Remote-only: 14,430 postings were collected across all locations and 20.0% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 821 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 369 | 44.9% |
| 2 | Observability | Practices | 265 | 32.3% |
| 3 | Machine Learning | ML Fundamentals | 244 | 29.7% |
| 4 | Distributed Systems | Practices | 242 | 29.5% |
| 5 | Go | Languages | 242 | 29.5% |
| 6 | LLMs | LLM & GenAI | 238 | 29.0% |
| 7 | AI Agents | LLM & GenAI | 223 | 27.2% |
| 8 | Kubernetes | Infra & Cloud | 217 | 26.4% |
| 9 | AWS | Infra & Cloud | 206 | 25.1% |
| 10 | TypeScript | Languages | 177 | 21.6% |
| 11 | Statistics | ML Fundamentals | 154 | 18.8% |
| 12 | SQL | Languages | 148 | 18.0% |
| 13 | Data Pipelines | Data Engineering | 126 | 15.3% |
| 14 | Terraform | Infra & Cloud | 121 | 14.7% |
| 15 | CI/CD | Practices | 119 | 14.5% |
| 16 | GCP | Infra & Cloud | 119 | 14.5% |
| 17 | React | Frameworks & Libraries | 113 | 13.8% |
| 18 | Java | Languages | 92 | 11.2% |
| 19 | Snowflake / BigQuery | Data Engineering | 77 | 9.4% |
| 20 | Azure | Infra & Cloud | 69 | 8.4% |
| 21 | Airflow | Data Engineering | 65 | 7.9% |
| 22 | Kafka | Data Engineering | 65 | 7.9% |
| 23 | Rust | Languages | 62 | 7.6% |
| 24 | Spark | Data Engineering | 61 | 7.4% |
| 25 | Security | Practices | 56 | 6.8% |
| 26 | Evals | LLM & GenAI | 56 | 6.8% |
| 27 | PyTorch | Frameworks & Libraries | 53 | 6.5% |
| 28 | Docker | Infra & Cloud | 46 | 5.6% |
| 29 | dbt | Data Engineering | 46 | 5.6% |
| 30 | AI Safety | LLM & GenAI | 45 | 5.5% |
| 31 | Linux | Infra & Cloud | 43 | 5.2% |
| 32 | Recommender Systems | ML Fundamentals | 43 | 5.2% |
| 33 | MCP | LLM & GenAI | 41 | 5.0% |
| 34 | Databricks | Data Engineering | 41 | 5.0% |
| 35 | Deep Learning | ML Fundamentals | 40 | 4.9% |
| 36 | Multimodal | LLM & GenAI | 39 | 4.8% |
| 37 | MLOps | Practices | 37 | 4.5% |
| 38 | RAG | LLM & GenAI | 32 | 3.9% |
| 39 | TensorFlow | Frameworks & Libraries | 32 | 3.9% |
| 40 | Fine-tuning | LLM & GenAI | 31 | 3.8% |

</details>

## Movers

Change in share of postings since 2026-10-21, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Snowflake / BigQuery | +0.27 | | Observability | -0.92 |
| AI Agents | +0.14 | | Distributed Systems | -0.90 |
| Security | +0.12 | | Machine Learning | -0.59 |
| Evals | +0.11 | | GCP | -0.59 |
| Docker | +0.05 | | Databricks | -0.49 |
| NLP | +0.03 | | Python | -0.48 |
| Transformers | +0.02 | | Statistics | -0.44 |
| Kafka | +0.01 | | Data Pipelines | -0.44 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,121 | 38.8% |
| other | 465 | 16.1% |
| swe | 439 | 15.2% |
| ops | 259 | 9.0% |
| product | 222 | 7.7% |
| infra | 163 | 5.6% |
| ml-ai | 94 | 3.3% |
| data | 72 | 2.5% |
| research | 53 | 1.8% |

## Disclosed pay, remote engineering roles

550 of 821 engineering postings (67%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $195,000 |
| Median | $226,200 |
| 75th | $260,000 |
| 90th | $292,500 |

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


<sub>Generated 2026-10-28T14:51:57+00:00 · 4 board(s) unreachable this run</sub>
