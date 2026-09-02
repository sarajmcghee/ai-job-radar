# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-09-02** — tracking **3,041 open remote roles** across **93 companies** (851 of them engineering roles). 1,695 postings disclose pay. **60 appeared today.**

<sub>Remote-only: 14,004 postings were collected across all locations and 21.7% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 851 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 414 | 48.6% |
| 2 | Observability | Practices | 286 | 33.6% |
| 3 | Distributed Systems | Practices | 278 | 32.7% |
| 4 | Machine Learning | ML Fundamentals | 275 | 32.3% |
| 5 | Go | Languages | 262 | 30.8% |
| 6 | AI Agents | LLM & GenAI | 254 | 29.8% |
| 7 | LLMs | LLM & GenAI | 249 | 29.3% |
| 8 | AWS | Infra & Cloud | 227 | 26.7% |
| 9 | Kubernetes | Infra & Cloud | 225 | 26.4% |
| 10 | TypeScript | Languages | 177 | 20.8% |
| 11 | Statistics | ML Fundamentals | 167 | 19.6% |
| 12 | GCP | Infra & Cloud | 150 | 17.6% |
| 13 | SQL | Languages | 147 | 17.3% |
| 14 | Data Pipelines | Data Engineering | 139 | 16.3% |
| 15 | Java | Languages | 127 | 14.9% |
| 16 | Terraform | Infra & Cloud | 126 | 14.8% |
| 17 | CI/CD | Practices | 124 | 14.6% |
| 18 | Azure | Infra & Cloud | 105 | 12.3% |
| 19 | React | Frameworks & Libraries | 102 | 12.0% |
| 20 | Snowflake / BigQuery | Data Engineering | 87 | 10.2% |
| 21 | Airflow | Data Engineering | 78 | 9.2% |
| 22 | Evals | LLM & GenAI | 75 | 8.8% |
| 23 | Kafka | Data Engineering | 74 | 8.7% |
| 24 | Spark | Data Engineering | 71 | 8.3% |
| 25 | Docker | Infra & Cloud | 64 | 7.5% |
| 26 | Rust | Languages | 62 | 7.3% |
| 27 | PyTorch | Frameworks & Libraries | 56 | 6.6% |
| 28 | Linux | Infra & Cloud | 54 | 6.3% |
| 29 | Databricks | Data Engineering | 51 | 6.0% |
| 30 | Security | Practices | 49 | 5.8% |
| 31 | RAG | LLM & GenAI | 47 | 5.5% |
| 32 | MCP | LLM & GenAI | 46 | 5.4% |
| 33 | Prompt Engineering | LLM & GenAI | 46 | 5.4% |
| 34 | Deep Learning | ML Fundamentals | 44 | 5.2% |
| 35 | MLOps | Practices | 43 | 5.1% |
| 36 | Recommender Systems | ML Fundamentals | 43 | 5.1% |
| 37 | A/B Testing | Practices | 42 | 4.9% |
| 38 | dbt | Data Engineering | 41 | 4.8% |
| 39 | AI Safety | LLM & GenAI | 38 | 4.5% |
| 40 | TensorFlow | Frameworks & Libraries | 38 | 4.5% |

</details>

## Movers

Change in share of postings since 2026-08-27, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Machine Learning | +0.79 | | Distributed Systems | -3.18 |
| Databricks | +0.39 | | Azure | -2.46 |
| AI Agents | +0.36 | | GCP | -2.42 |
| Evals | +0.35 | | Kubernetes | -1.90 |
| LLMs | +0.31 | | AWS | -1.89 |
| Snowflake / BigQuery | +0.27 | | TypeScript | -1.40 |
| MCP | +0.26 | | Go | -1.39 |
| Deep Learning | +0.19 | | Airflow | -1.33 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,210 | 39.8% |
| swe | 490 | 16.1% |
| other | 467 | 15.4% |
| ops | 279 | 9.2% |
| product | 234 | 7.7% |
| infra | 144 | 4.7% |
| ml-ai | 100 | 3.3% |
| data | 74 | 2.4% |
| research | 43 | 1.4% |

## Disclosed pay, remote engineering roles

539 of 851 engineering postings (63%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $194,250 |
| Median | $228,500 |
| 75th | $260,050 |
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


<sub>Generated 2026-09-02T12:32:47+00:00 · 2 board(s) unreachable this run</sub>
