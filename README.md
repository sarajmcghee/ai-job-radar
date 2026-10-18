# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-10-18** — tracking **2,821 open remote roles** across **89 companies** (826 of them engineering roles). 1,650 postings disclose pay. **2 appeared today.**

<sub>Remote-only: 14,338 postings were collected across all locations and 19.7% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 826 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 365 | 44.2% |
| 2 | Observability | Practices | 275 | 33.3% |
| 3 | LLMs | LLM & GenAI | 254 | 30.8% |
| 4 | Distributed Systems | Practices | 247 | 29.9% |
| 5 | Machine Learning | ML Fundamentals | 247 | 29.9% |
| 6 | Go | Languages | 237 | 28.7% |
| 7 | AI Agents | LLM & GenAI | 229 | 27.7% |
| 8 | AWS | Infra & Cloud | 213 | 25.8% |
| 9 | Kubernetes | Infra & Cloud | 212 | 25.7% |
| 10 | TypeScript | Languages | 180 | 21.8% |
| 11 | Statistics | ML Fundamentals | 159 | 19.2% |
| 12 | SQL | Languages | 144 | 17.4% |
| 13 | Data Pipelines | Data Engineering | 130 | 15.7% |
| 14 | CI/CD | Practices | 129 | 15.6% |
| 15 | GCP | Infra & Cloud | 125 | 15.1% |
| 16 | React | Frameworks & Libraries | 124 | 15.0% |
| 17 | Terraform | Infra & Cloud | 116 | 14.0% |
| 18 | Java | Languages | 92 | 11.1% |
| 19 | Snowflake / BigQuery | Data Engineering | 81 | 9.8% |
| 20 | Airflow | Data Engineering | 72 | 8.7% |
| 21 | Azure | Infra & Cloud | 66 | 8.0% |
| 22 | Spark | Data Engineering | 62 | 7.5% |
| 23 | Kafka | Data Engineering | 61 | 7.4% |
| 24 | Rust | Languages | 58 | 7.0% |
| 25 | Evals | LLM & GenAI | 57 | 6.9% |
| 26 | PyTorch | Frameworks & Libraries | 53 | 6.4% |
| 27 | dbt | Data Engineering | 51 | 6.2% |
| 28 | AI Safety | LLM & GenAI | 50 | 6.1% |
| 29 | Security | Practices | 48 | 5.8% |
| 30 | Docker | Infra & Cloud | 48 | 5.8% |
| 31 | Linux | Infra & Cloud | 46 | 5.6% |
| 32 | MCP | LLM & GenAI | 45 | 5.4% |
| 33 | Databricks | Data Engineering | 45 | 5.4% |
| 34 | Recommender Systems | ML Fundamentals | 45 | 5.4% |
| 35 | Deep Learning | ML Fundamentals | 43 | 5.2% |
| 36 | MLOps | Practices | 40 | 4.8% |
| 37 | Multimodal | LLM & GenAI | 40 | 4.8% |
| 38 | Fine-tuning | LLM & GenAI | 34 | 4.1% |
| 39 | RAG | LLM & GenAI | 34 | 4.1% |
| 40 | Prompt Engineering | LLM & GenAI | 33 | 4.0% |

</details>

## Movers

Change in share of postings since 2026-10-11, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Fine-tuning | +0.39 | | Distributed Systems | -1.02 |
| Databricks | +0.30 | | Machine Learning | -0.86 |
| Spark | +0.29 | | Kafka | -0.73 |
| dbt | +0.27 | | Go | -0.68 |
| Snowflake / BigQuery | +0.25 | | Azure | -0.64 |
| Evals | +0.23 | | GCP | -0.54 |
| PyTorch | +0.22 | | AWS | -0.51 |
| Deep Learning | +0.22 | | Python | -0.47 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,067 | 37.8% |
| swe | 446 | 15.8% |
| other | 433 | 15.3% |
| ops | 267 | 9.5% |
| product | 228 | 8.1% |
| infra | 155 | 5.5% |
| ml-ai | 94 | 3.3% |
| data | 80 | 2.8% |
| research | 51 | 1.8% |

## Disclosed pay, remote engineering roles

553 of 826 engineering postings (67%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $197,000 |
| Median | $227,500 |
| 75th | $260,000 |
| 90th | $288,000 |

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
| Pika | $300,000 |
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


<sub>Generated 2026-10-18T12:27:44+00:00 · 4 board(s) unreachable this run</sub>
