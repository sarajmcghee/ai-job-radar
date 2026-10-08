# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-10-08** — tracking **2,802 open remote roles** across **91 companies** (836 of them engineering roles). 1,645 postings disclose pay. **59 appeared today.**

<sub>Remote-only: 14,344 postings were collected across all locations and 19.5% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 836 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 378 | 45.2% |
| 2 | Observability | Practices | 284 | 34.0% |
| 3 | Distributed Systems | Practices | 268 | 32.1% |
| 4 | Machine Learning | ML Fundamentals | 253 | 30.3% |
| 5 | Go | Languages | 248 | 29.7% |
| 6 | LLMs | LLM & GenAI | 246 | 29.4% |
| 7 | AI Agents | LLM & GenAI | 224 | 26.8% |
| 8 | AWS | Infra & Cloud | 216 | 25.8% |
| 9 | Kubernetes | Infra & Cloud | 202 | 24.2% |
| 10 | TypeScript | Languages | 177 | 21.2% |
| 11 | Statistics | ML Fundamentals | 163 | 19.5% |
| 12 | SQL | Languages | 148 | 17.7% |
| 13 | GCP | Infra & Cloud | 132 | 15.8% |
| 14 | Data Pipelines | Data Engineering | 132 | 15.8% |
| 15 | CI/CD | Practices | 128 | 15.3% |
| 16 | React | Frameworks & Libraries | 126 | 15.1% |
| 17 | Terraform | Infra & Cloud | 117 | 14.0% |
| 18 | Java | Languages | 104 | 12.4% |
| 19 | Azure | Infra & Cloud | 80 | 9.6% |
| 20 | Snowflake / BigQuery | Data Engineering | 78 | 9.3% |
| 21 | Airflow | Data Engineering | 75 | 9.0% |
| 22 | Kafka | Data Engineering | 74 | 8.9% |
| 23 | Rust | Languages | 62 | 7.4% |
| 24 | Spark | Data Engineering | 61 | 7.3% |
| 25 | Docker | Infra & Cloud | 55 | 6.6% |
| 26 | Linux | Infra & Cloud | 53 | 6.3% |
| 27 | Security | Practices | 48 | 5.7% |
| 28 | PyTorch | Frameworks & Libraries | 48 | 5.7% |
| 29 | AI Safety | LLM & GenAI | 47 | 5.6% |
| 30 | dbt | Data Engineering | 47 | 5.6% |
| 31 | Evals | LLM & GenAI | 44 | 5.3% |
| 32 | MCP | LLM & GenAI | 41 | 4.9% |
| 33 | Recommender Systems | ML Fundamentals | 40 | 4.8% |
| 34 | Databricks | Data Engineering | 39 | 4.7% |
| 35 | MLOps | Practices | 39 | 4.7% |
| 36 | Deep Learning | ML Fundamentals | 39 | 4.7% |
| 37 | Multimodal | LLM & GenAI | 36 | 4.3% |
| 38 | RAG | LLM & GenAI | 36 | 4.3% |
| 39 | Prompt Engineering | LLM & GenAI | 34 | 4.1% |
| 40 | A/B Testing | Practices | 32 | 3.8% |

</details>

## Movers

Change in share of postings since 2026-10-01, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| SQL | +0.64 | | AI Agents | -1.10 |
| Terraform | +0.54 | | Data Pipelines | -0.48 |
| Machine Learning | +0.49 | | Java | -0.39 |
| React | +0.47 | | Go | -0.31 |
| AWS | +0.39 | | Python | -0.24 |
| Snowflake / BigQuery | +0.33 | | Recommender Systems | -0.21 |
| Kubernetes | +0.33 | | Evals | -0.21 |
| AI Safety | +0.33 | | RAG | -0.21 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,032 | 36.8% |
| swe | 460 | 16.4% |
| other | 439 | 15.7% |
| ops | 269 | 9.6% |
| product | 226 | 8.1% |
| infra | 154 | 5.5% |
| data | 86 | 3.1% |
| ml-ai | 84 | 3.0% |
| research | 52 | 1.9% |

## Disclosed pay, remote engineering roles

562 of 836 engineering postings (67%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $196,000 |
| Median | $227,500 |
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


<sub>Generated 2026-10-08T15:13:12+00:00 · 4 board(s) unreachable this run</sub>
