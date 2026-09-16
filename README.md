# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-09-16** — tracking **2,990 open remote roles** across **94 companies** (846 of them engineering roles). 1,686 postings disclose pay. **65 appeared today.**

<sub>Remote-only: 14,171 postings were collected across all locations and 21.1% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 846 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 409 | 48.3% |
| 2 | Observability | Practices | 285 | 33.7% |
| 3 | Distributed Systems | Practices | 268 | 31.7% |
| 4 | Machine Learning | ML Fundamentals | 262 | 31.0% |
| 5 | Go | Languages | 260 | 30.7% |
| 6 | AI Agents | LLM & GenAI | 246 | 29.1% |
| 7 | LLMs | LLM & GenAI | 245 | 29.0% |
| 8 | AWS | Infra & Cloud | 227 | 26.8% |
| 9 | Kubernetes | Infra & Cloud | 223 | 26.4% |
| 10 | TypeScript | Languages | 178 | 21.0% |
| 11 | SQL | Languages | 155 | 18.3% |
| 12 | Statistics | ML Fundamentals | 154 | 18.2% |
| 13 | Data Pipelines | Data Engineering | 144 | 17.0% |
| 14 | GCP | Infra & Cloud | 135 | 16.0% |
| 15 | CI/CD | Practices | 132 | 15.6% |
| 16 | Terraform | Infra & Cloud | 122 | 14.4% |
| 17 | Java | Languages | 114 | 13.5% |
| 18 | React | Frameworks & Libraries | 105 | 12.4% |
| 19 | Azure | Infra & Cloud | 86 | 10.2% |
| 20 | Airflow | Data Engineering | 78 | 9.2% |
| 21 | Snowflake / BigQuery | Data Engineering | 74 | 8.7% |
| 22 | Kafka | Data Engineering | 72 | 8.5% |
| 23 | Rust | Languages | 72 | 8.5% |
| 24 | Spark | Data Engineering | 69 | 8.2% |
| 25 | Evals | LLM & GenAI | 69 | 8.2% |
| 26 | Docker | Infra & Cloud | 62 | 7.3% |
| 27 | Linux | Infra & Cloud | 52 | 6.1% |
| 28 | Security | Practices | 51 | 6.0% |
| 29 | PyTorch | Frameworks & Libraries | 48 | 5.7% |
| 30 | dbt | Data Engineering | 47 | 5.6% |
| 31 | RAG | LLM & GenAI | 45 | 5.3% |
| 32 | Deep Learning | ML Fundamentals | 43 | 5.1% |
| 33 | Databricks | Data Engineering | 40 | 4.7% |
| 34 | AI Safety | LLM & GenAI | 39 | 4.6% |
| 35 | MLOps | Practices | 39 | 4.6% |
| 36 | MCP | LLM & GenAI | 38 | 4.5% |
| 37 | A/B Testing | Practices | 38 | 4.5% |
| 38 | Prompt Engineering | LLM & GenAI | 38 | 4.5% |
| 39 | Recommender Systems | ML Fundamentals | 38 | 4.5% |
| 40 | Fine-tuning | LLM & GenAI | 36 | 4.3% |

</details>

## Movers

Change in share of postings since 2026-09-09, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| CI/CD | +0.31 | | LLMs | -0.70 |
| Data Pipelines | +0.25 | | Snowflake / BigQuery | -0.54 |
| Spark | +0.24 | | dbt | -0.50 |
| LangChain | +0.14 | | GCP | -0.47 |
| NLP | +0.13 | | Statistics | -0.45 |
| RAG | +0.12 | | Distributed Systems | -0.38 |
| Go | +0.10 | | Azure | -0.37 |
| Security | +0.10 | | Evals | -0.36 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,181 | 39.5% |
| swe | 490 | 16.4% |
| other | 460 | 15.4% |
| ops | 271 | 9.1% |
| product | 232 | 7.8% |
| infra | 150 | 5.0% |
| ml-ai | 86 | 2.9% |
| data | 74 | 2.5% |
| research | 46 | 1.5% |

## Disclosed pay, remote engineering roles

556 of 846 engineering postings (66%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $194,500 |
| Median | $228,085 |
| 75th | $260,000 |
| 90th | $290,000 |

<details><summary>Highest disclosed engineering bands by company</summary>

| Company | Top posted midpoint |
|---|---:|
| Anthropic | $675,000 |
| OpenAI | $455,500 |
| Pinterest | $371,087 |
| Reddit | $351,000 |
| Vanta | $349,500 |
| Databricks | $343,425 |
| Agility Robotics | $329,500 |
| Mercury | $325,900 |
| Snorkel AI | $316,000 |
| Hightouch | $310,000 |

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


<sub>Generated 2026-09-16T13:06:12+00:00 · 2 board(s) unreachable this run</sub>
