# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-10-06** — tracking **2,788 open remote roles** across **89 companies** (832 of them engineering roles). 1,611 postings disclose pay. **57 appeared today.**

<sub>Remote-only: 14,196 postings were collected across all locations and 19.6% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 832 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 371 | 44.6% |
| 2 | Observability | Practices | 298 | 35.8% |
| 3 | Distributed Systems | Practices | 280 | 33.7% |
| 4 | Go | Languages | 250 | 30.0% |
| 5 | Machine Learning | ML Fundamentals | 244 | 29.3% |
| 6 | LLMs | LLM & GenAI | 234 | 28.1% |
| 7 | AI Agents | LLM & GenAI | 221 | 26.6% |
| 8 | AWS | Infra & Cloud | 218 | 26.2% |
| 9 | Kubernetes | Infra & Cloud | 197 | 23.7% |
| 10 | TypeScript | Languages | 170 | 20.4% |
| 11 | Statistics | ML Fundamentals | 162 | 19.5% |
| 12 | SQL | Languages | 146 | 17.5% |
| 13 | GCP | Infra & Cloud | 136 | 16.3% |
| 14 | Data Pipelines | Data Engineering | 136 | 16.3% |
| 15 | CI/CD | Practices | 132 | 15.9% |
| 16 | React | Frameworks & Libraries | 127 | 15.3% |
| 17 | Terraform | Infra & Cloud | 119 | 14.3% |
| 18 | Java | Languages | 111 | 13.3% |
| 19 | Azure | Infra & Cloud | 86 | 10.3% |
| 20 | Snowflake / BigQuery | Data Engineering | 77 | 9.3% |
| 21 | Airflow | Data Engineering | 76 | 9.1% |
| 22 | Kafka | Data Engineering | 74 | 8.9% |
| 23 | Rust | Languages | 66 | 7.9% |
| 24 | Spark | Data Engineering | 63 | 7.6% |
| 25 | Docker | Infra & Cloud | 51 | 6.1% |
| 26 | Linux | Infra & Cloud | 50 | 6.0% |
| 27 | Security | Practices | 48 | 5.8% |
| 28 | AI Safety | LLM & GenAI | 47 | 5.6% |
| 29 | dbt | Data Engineering | 47 | 5.6% |
| 30 | PyTorch | Frameworks & Libraries | 46 | 5.5% |
| 31 | Evals | LLM & GenAI | 44 | 5.3% |
| 32 | MCP | LLM & GenAI | 42 | 5.0% |
| 33 | MLOps | Practices | 40 | 4.8% |
| 34 | Recommender Systems | ML Fundamentals | 40 | 4.8% |
| 35 | Deep Learning | ML Fundamentals | 39 | 4.7% |
| 36 | Databricks | Data Engineering | 38 | 4.6% |
| 37 | RAG | LLM & GenAI | 36 | 4.3% |
| 38 | Multimodal | LLM & GenAI | 32 | 3.8% |
| 39 | A/B Testing | Practices | 31 | 3.7% |
| 40 | Prompt Engineering | LLM & GenAI | 30 | 3.6% |

</details>

## Movers

Change in share of postings since 2026-09-29, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| React | +0.96 | | AI Agents | -1.15 |
| Observability | +0.92 | | Python | -0.59 |
| CI/CD | +0.51 | | LLMs | -0.48 |
| Terraform | +0.50 | | Evals | -0.46 |
| Distributed Systems | +0.45 | | Data Pipelines | -0.44 |
| Snowflake / BigQuery | +0.22 | | Machine Learning | -0.35 |
| Airflow | +0.22 | | Security | -0.24 |
| TypeScript | +0.21 | | Embeddings | -0.21 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,032 | 37.0% |
| swe | 471 | 16.9% |
| other | 442 | 15.9% |
| ops | 267 | 9.6% |
| product | 215 | 7.7% |
| infra | 146 | 5.2% |
| data | 87 | 3.1% |
| ml-ai | 78 | 2.8% |
| research | 50 | 1.8% |

## Disclosed pay, remote engineering roles

549 of 832 engineering postings (66%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $195,450 |
| Median | $226,200 |
| 75th | $259,000 |
| 90th | $285,825 |

<details><summary>Highest disclosed engineering bands by company</summary>

| Company | Top posted midpoint |
|---|---:|
| Anthropic | $675,000 |
| OpenAI | $455,500 |
| Pinterest | $371,087 |
| Reddit | $351,000 |
| Databricks | $343,425 |
| Agility Robotics | $329,500 |
| Snorkel AI | $316,000 |
| Discord | $306,000 |
| GitLab | $301,800 |
| Pika | $292,500 |

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


<sub>Generated 2026-10-06T14:45:07+00:00 · 4 board(s) unreachable this run</sub>
