# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-08-28** — tracking **3,243 open remote roles** across **95 companies** (963 of them engineering roles). 1,788 postings disclose pay. **67 appeared today.**

<sub>Remote-only: 14,268 postings were collected across all locations and 22.7% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 963 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 464 | 48.2% |
| 2 | Distributed Systems | Practices | 361 | 37.5% |
| 3 | Observability | Practices | 335 | 34.8% |
| 4 | Go | Languages | 300 | 31.2% |
| 5 | Machine Learning | ML Fundamentals | 288 | 29.9% |
| 6 | Kubernetes | Infra & Cloud | 288 | 29.9% |
| 7 | AWS | Infra & Cloud | 286 | 29.7% |
| 8 | AI Agents | LLM & GenAI | 275 | 28.6% |
| 9 | LLMs | LLM & GenAI | 267 | 27.7% |
| 10 | TypeScript | Languages | 219 | 22.7% |
| 11 | GCP | Infra & Cloud | 214 | 22.2% |
| 12 | SQL | Languages | 188 | 19.5% |
| 13 | Statistics | ML Fundamentals | 176 | 18.3% |
| 14 | Azure | Infra & Cloud | 167 | 17.3% |
| 15 | Java | Languages | 158 | 16.4% |
| 16 | Data Pipelines | Data Engineering | 154 | 16.0% |
| 17 | Terraform | Infra & Cloud | 151 | 15.7% |
| 18 | CI/CD | Practices | 143 | 14.8% |
| 19 | React | Frameworks & Libraries | 116 | 12.0% |
| 20 | Airflow | Data Engineering | 115 | 11.9% |
| 21 | Kafka | Data Engineering | 96 | 10.0% |
| 22 | Spark | Data Engineering | 89 | 9.2% |
| 23 | Snowflake / BigQuery | Data Engineering | 84 | 8.7% |
| 24 | Docker | Infra & Cloud | 83 | 8.6% |
| 25 | Rust | Languages | 77 | 8.0% |
| 26 | Evals | LLM & GenAI | 77 | 8.0% |
| 27 | Linux | Infra & Cloud | 65 | 6.7% |
| 28 | Security | Practices | 61 | 6.3% |
| 29 | PyTorch | Frameworks & Libraries | 56 | 5.8% |
| 30 | RAG | LLM & GenAI | 53 | 5.5% |
| 31 | Databricks | Data Engineering | 50 | 5.2% |
| 32 | dbt | Data Engineering | 50 | 5.2% |
| 33 | MLOps | Practices | 49 | 5.1% |
| 34 | MCP | LLM & GenAI | 46 | 4.8% |
| 35 | Prompt Engineering | LLM & GenAI | 46 | 4.8% |
| 36 | A/B Testing | Practices | 44 | 4.6% |
| 37 | Recommender Systems | ML Fundamentals | 44 | 4.6% |
| 38 | Deep Learning | ML Fundamentals | 43 | 4.5% |
| 39 | AI Safety | LLM & GenAI | 40 | 4.2% |
| 40 | Embeddings | LLM & GenAI | 39 | 4.0% |

</details>

## Movers

Change in share of postings since 2026-08-27, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| AI Agents | +0.20 | | Go | -0.32 |
| Machine Learning | +0.20 | | Statistics | -0.29 |
| Evals | +0.20 | | Observability | -0.26 |
| Python | +0.16 | | TypeScript | -0.26 |
| Airflow | +0.12 | | Recommender Systems | -0.20 |
| SQL | +0.12 | | Docker | -0.13 |
| Snowflake / BigQuery | +0.09 | | React | -0.10 |
| Java | +0.09 | | CI/CD | -0.09 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,228 | 37.9% |
| swe | 565 | 17.4% |
| other | 526 | 16.2% |
| ops | 277 | 8.5% |
| product | 249 | 7.7% |
| infra | 182 | 5.6% |
| ml-ai | 98 | 3.0% |
| data | 75 | 2.3% |
| research | 43 | 1.3% |

## Disclosed pay, remote engineering roles

591 of 963 engineering postings (61%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $187,450 |
| Median | $226,200 |
| 75th | $259,000 |
| 90th | $280,000 |

<details><summary>Highest disclosed engineering bands by company</summary>

| Company | Top posted midpoint |
|---|---:|
| Anthropic | $675,000 |
| OpenAI | $418,500 |
| Pinterest | $371,087 |
| Reddit | $351,000 |
| Databricks | $343,425 |
| Agility Robotics | $329,500 |
| Mercury | $325,900 |
| Snorkel AI | $316,000 |
| Hightouch | $310,000 |
| Lambda | $299,000 |

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


<sub>Generated 2026-08-28T19:54:04+00:00 · 0 board(s) unreachable this run</sub>
