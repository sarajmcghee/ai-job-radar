# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-09-15** — tracking **2,987 open remote roles** across **94 companies** (851 of them engineering roles). 1,682 postings disclose pay. **49 appeared today.**

<sub>Remote-only: 14,143 postings were collected across all locations and 21.1% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 851 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 407 | 47.8% |
| 2 | Observability | Practices | 289 | 34.0% |
| 3 | Distributed Systems | Practices | 277 | 32.5% |
| 4 | Go | Languages | 262 | 30.8% |
| 5 | Machine Learning | ML Fundamentals | 260 | 30.6% |
| 6 | AI Agents | LLM & GenAI | 247 | 29.0% |
| 7 | LLMs | LLM & GenAI | 240 | 28.2% |
| 8 | AWS | Infra & Cloud | 231 | 27.1% |
| 9 | Kubernetes | Infra & Cloud | 225 | 26.4% |
| 10 | TypeScript | Languages | 178 | 20.9% |
| 11 | SQL | Languages | 154 | 18.1% |
| 12 | Statistics | ML Fundamentals | 152 | 17.9% |
| 13 | Data Pipelines | Data Engineering | 144 | 16.9% |
| 14 | GCP | Infra & Cloud | 141 | 16.6% |
| 15 | CI/CD | Practices | 130 | 15.3% |
| 16 | Terraform | Infra & Cloud | 126 | 14.8% |
| 17 | Java | Languages | 114 | 13.4% |
| 18 | React | Frameworks & Libraries | 102 | 12.0% |
| 19 | Azure | Infra & Cloud | 90 | 10.6% |
| 20 | Airflow | Data Engineering | 78 | 9.2% |
| 21 | Rust | Languages | 73 | 8.6% |
| 22 | Kafka | Data Engineering | 72 | 8.5% |
| 23 | Snowflake / BigQuery | Data Engineering | 72 | 8.5% |
| 24 | Spark | Data Engineering | 68 | 8.0% |
| 25 | Evals | LLM & GenAI | 68 | 8.0% |
| 26 | Docker | Infra & Cloud | 60 | 7.1% |
| 27 | Linux | Infra & Cloud | 53 | 6.2% |
| 28 | Security | Practices | 52 | 6.1% |
| 29 | PyTorch | Frameworks & Libraries | 48 | 5.6% |
| 30 | dbt | Data Engineering | 47 | 5.5% |
| 31 | RAG | LLM & GenAI | 45 | 5.3% |
| 32 | Deep Learning | ML Fundamentals | 43 | 5.1% |
| 33 | A/B Testing | Practices | 40 | 4.7% |
| 34 | Databricks | Data Engineering | 40 | 4.7% |
| 35 | MCP | LLM & GenAI | 39 | 4.6% |
| 36 | MLOps | Practices | 39 | 4.6% |
| 37 | Recommender Systems | ML Fundamentals | 39 | 4.6% |
| 38 | AI Safety | LLM & GenAI | 38 | 4.5% |
| 39 | Fine-tuning | LLM & GenAI | 37 | 4.3% |
| 40 | Prompt Engineering | LLM & GenAI | 37 | 4.3% |

</details>

## Movers

Change in share of postings since 2026-09-08, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| AWS | +0.47 | | Statistics | -0.62 |
| Data Pipelines | +0.25 | | dbt | -0.50 |
| Databricks | +0.16 | | Java | -0.42 |
| Spark | +0.14 | | Snowflake / BigQuery | -0.41 |
| NLP | +0.13 | | SQL | -0.37 |
| Rust | +0.12 | | LLMs | -0.34 |
| GCP | +0.10 | | AI Safety | -0.31 |
| Fine-tuning | +0.10 | | MCP | -0.24 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,183 | 39.6% |
| swe | 494 | 16.5% |
| other | 455 | 15.2% |
| ops | 271 | 9.1% |
| product | 227 | 7.6% |
| infra | 151 | 5.1% |
| ml-ai | 86 | 2.9% |
| data | 75 | 2.5% |
| research | 45 | 1.5% |

## Disclosed pay, remote engineering roles

557 of 851 engineering postings (65%) publish a salary range. Figures are the midpoint of the posted band.

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


<sub>Generated 2026-09-15T13:08:17+00:00 · 2 board(s) unreachable this run</sub>
