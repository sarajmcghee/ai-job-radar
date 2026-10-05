# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-10-05** — tracking **2,806 open remote roles** across **91 companies** (819 of them engineering roles). 1,614 postings disclose pay. **25 appeared today.**

<sub>Remote-only: 14,218 postings were collected across all locations and 19.7% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 819 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 377 | 46.0% |
| 2 | Observability | Practices | 293 | 35.8% |
| 3 | Distributed Systems | Practices | 275 | 33.6% |
| 4 | Go | Languages | 257 | 31.4% |
| 5 | Machine Learning | ML Fundamentals | 245 | 29.9% |
| 6 | LLMs | LLM & GenAI | 233 | 28.4% |
| 7 | AI Agents | LLM & GenAI | 223 | 27.2% |
| 8 | AWS | Infra & Cloud | 222 | 27.1% |
| 9 | Kubernetes | Infra & Cloud | 197 | 24.1% |
| 10 | TypeScript | Languages | 163 | 19.9% |
| 11 | Statistics | ML Fundamentals | 154 | 18.8% |
| 12 | SQL | Languages | 145 | 17.7% |
| 13 | Data Pipelines | Data Engineering | 141 | 17.2% |
| 14 | GCP | Infra & Cloud | 140 | 17.1% |
| 15 | CI/CD | Practices | 132 | 16.1% |
| 16 | React | Frameworks & Libraries | 118 | 14.4% |
| 17 | Java | Languages | 116 | 14.2% |
| 18 | Terraform | Infra & Cloud | 112 | 13.7% |
| 19 | Azure | Infra & Cloud | 86 | 10.5% |
| 20 | Snowflake / BigQuery | Data Engineering | 79 | 9.6% |
| 21 | Airflow | Data Engineering | 78 | 9.5% |
| 22 | Kafka | Data Engineering | 77 | 9.4% |
| 23 | Rust | Languages | 65 | 7.9% |
| 24 | Spark | Data Engineering | 62 | 7.6% |
| 25 | Security | Practices | 51 | 6.2% |
| 26 | Docker | Infra & Cloud | 51 | 6.2% |
| 27 | Linux | Infra & Cloud | 47 | 5.7% |
| 28 | AI Safety | LLM & GenAI | 46 | 5.6% |
| 29 | PyTorch | Frameworks & Libraries | 46 | 5.6% |
| 30 | dbt | Data Engineering | 46 | 5.6% |
| 31 | Evals | LLM & GenAI | 45 | 5.5% |
| 32 | MCP | LLM & GenAI | 42 | 5.1% |
| 33 | MLOps | Practices | 41 | 5.0% |
| 34 | Recommender Systems | ML Fundamentals | 40 | 4.9% |
| 35 | RAG | LLM & GenAI | 39 | 4.8% |
| 36 | Databricks | Data Engineering | 38 | 4.6% |
| 37 | Deep Learning | ML Fundamentals | 38 | 4.6% |
| 38 | TensorFlow | Frameworks & Libraries | 33 | 4.0% |
| 39 | Prompt Engineering | LLM & GenAI | 32 | 3.9% |
| 40 | A/B Testing | Practices | 31 | 3.8% |

</details>

## Movers

Change in share of postings since 2026-09-28, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| React | +0.64 | | AI Agents | -0.82 |
| CI/CD | +0.51 | | Kubernetes | -0.62 |
| Java | +0.34 | | LLMs | -0.50 |
| Airflow | +0.33 | | Evals | -0.48 |
| AI Safety | +0.26 | | Docker | -0.36 |
| Snowflake / BigQuery | +0.25 | | Python | -0.28 |
| dbt | +0.21 | | Rust | -0.27 |
| Speech / Audio | +0.20 | | Embeddings | -0.21 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,053 | 37.5% |
| swe | 463 | 16.5% |
| other | 448 | 16.0% |
| ops | 269 | 9.6% |
| product | 217 | 7.7% |
| infra | 147 | 5.2% |
| ml-ai | 83 | 3.0% |
| data | 80 | 2.9% |
| research | 46 | 1.6% |

## Disclosed pay, remote engineering roles

548 of 819 engineering postings (67%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $196,500 |
| Median | $225,800 |
| 75th | $257,500 |
| 90th | $283,000 |

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


<sub>Generated 2026-10-05T16:47:51+00:00 · 4 board(s) unreachable this run</sub>
