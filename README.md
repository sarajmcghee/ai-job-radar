# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-10-14** — tracking **2,777 open remote roles** across **89 companies** (824 of them engineering roles). 1,632 postings disclose pay. **54 appeared today.**

<sub>Remote-only: 14,251 postings were collected across all locations and 19.5% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 824 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 361 | 43.8% |
| 2 | Observability | Practices | 276 | 33.5% |
| 3 | Distributed Systems | Practices | 255 | 30.9% |
| 4 | Go | Languages | 245 | 29.7% |
| 5 | LLMs | LLM & GenAI | 245 | 29.7% |
| 6 | Machine Learning | ML Fundamentals | 245 | 29.7% |
| 7 | AI Agents | LLM & GenAI | 223 | 27.1% |
| 8 | Kubernetes | Infra & Cloud | 211 | 25.6% |
| 9 | AWS | Infra & Cloud | 205 | 24.9% |
| 10 | TypeScript | Languages | 173 | 21.0% |
| 11 | Statistics | ML Fundamentals | 155 | 18.8% |
| 12 | SQL | Languages | 139 | 16.9% |
| 13 | CI/CD | Practices | 130 | 15.8% |
| 14 | Data Pipelines | Data Engineering | 123 | 14.9% |
| 15 | React | Frameworks & Libraries | 121 | 14.7% |
| 16 | GCP | Infra & Cloud | 119 | 14.4% |
| 17 | Terraform | Infra & Cloud | 114 | 13.8% |
| 18 | Java | Languages | 90 | 10.9% |
| 19 | Snowflake / BigQuery | Data Engineering | 73 | 8.9% |
| 20 | Airflow | Data Engineering | 68 | 8.3% |
| 21 | Kafka | Data Engineering | 66 | 8.0% |
| 22 | Rust | Languages | 66 | 8.0% |
| 23 | Azure | Infra & Cloud | 64 | 7.8% |
| 24 | Spark | Data Engineering | 59 | 7.2% |
| 25 | Evals | LLM & GenAI | 57 | 6.9% |
| 26 | Docker | Infra & Cloud | 53 | 6.4% |
| 27 | PyTorch | Frameworks & Libraries | 50 | 6.1% |
| 28 | AI Safety | LLM & GenAI | 49 | 5.9% |
| 29 | Linux | Infra & Cloud | 47 | 5.7% |
| 30 | Security | Practices | 45 | 5.5% |
| 31 | dbt | Data Engineering | 45 | 5.5% |
| 32 | MCP | LLM & GenAI | 44 | 5.3% |
| 33 | Recommender Systems | ML Fundamentals | 42 | 5.1% |
| 34 | Databricks | Data Engineering | 41 | 5.0% |
| 35 | Deep Learning | ML Fundamentals | 39 | 4.7% |
| 36 | MLOps | Practices | 37 | 4.5% |
| 37 | Multimodal | LLM & GenAI | 37 | 4.5% |
| 38 | RAG | LLM & GenAI | 33 | 4.0% |
| 39 | GPU Clusters | Infra & Cloud | 33 | 4.0% |
| 40 | Prompt Engineering | LLM & GenAI | 31 | 3.8% |

</details>

## Movers

Change in share of postings since 2026-10-07, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Kubernetes | +0.65 | | Java | -0.80 |
| Evals | +0.45 | | Azure | -0.74 |
| Snowflake / BigQuery | +0.43 | | Distributed Systems | -0.61 |
| MCP | +0.30 | | Data Pipelines | -0.53 |
| GPU Clusters | +0.26 | | GCP | -0.51 |
| TypeScript | +0.23 | | Kafka | -0.48 |
| SQL | +0.22 | | Observability | -0.33 |
| Databricks | +0.22 | | AWS | -0.28 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,056 | 38.0% |
| swe | 451 | 16.2% |
| other | 418 | 15.1% |
| ops | 266 | 9.6% |
| product | 213 | 7.7% |
| infra | 156 | 5.6% |
| ml-ai | 85 | 3.1% |
| data | 79 | 2.8% |
| research | 53 | 1.9% |

## Disclosed pay, remote engineering roles

552 of 824 engineering postings (67%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $197,050 |
| Median | $227,735 |
| 75th | $260,000 |
| 90th | $287,500 |

<details><summary>Highest disclosed engineering bands by company</summary>

| Company | Top posted midpoint |
|---|---:|
| Anthropic | $675,000 |
| OpenAI | $455,500 |
| Pinterest | $371,087 |
| Reddit | $351,000 |
| Agility Robotics | $329,500 |
| Snorkel AI | $316,000 |
| Discord | $306,000 |
| GitLab | $301,800 |
| Pika | $292,500 |
| Vercel | $290,000 |

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


<sub>Generated 2026-10-14T13:19:24+00:00 · 4 board(s) unreachable this run</sub>
