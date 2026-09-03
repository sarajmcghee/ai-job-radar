# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-09-03** — tracking **3,059 open remote roles** across **94 companies** (873 of them engineering roles). 1,716 postings disclose pay. **77 appeared today.**

<sub>Remote-only: 14,010 postings were collected across all locations and 21.8% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 873 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 427 | 48.9% |
| 2 | Observability | Practices | 298 | 34.1% |
| 3 | Distributed Systems | Practices | 283 | 32.4% |
| 4 | Machine Learning | ML Fundamentals | 280 | 32.1% |
| 5 | Go | Languages | 268 | 30.7% |
| 6 | AI Agents | LLM & GenAI | 265 | 30.4% |
| 7 | LLMs | LLM & GenAI | 251 | 28.8% |
| 8 | Kubernetes | Infra & Cloud | 244 | 27.9% |
| 9 | AWS | Infra & Cloud | 238 | 27.3% |
| 10 | TypeScript | Languages | 186 | 21.3% |
| 11 | Statistics | ML Fundamentals | 173 | 19.8% |
| 12 | SQL | Languages | 154 | 17.6% |
| 13 | GCP | Infra & Cloud | 152 | 17.4% |
| 14 | Data Pipelines | Data Engineering | 141 | 16.2% |
| 15 | CI/CD | Practices | 137 | 15.7% |
| 16 | Terraform | Infra & Cloud | 136 | 15.6% |
| 17 | Java | Languages | 127 | 14.5% |
| 18 | React | Frameworks & Libraries | 110 | 12.6% |
| 19 | Azure | Infra & Cloud | 106 | 12.1% |
| 20 | Snowflake / BigQuery | Data Engineering | 85 | 9.7% |
| 21 | Airflow | Data Engineering | 79 | 9.0% |
| 22 | Kafka | Data Engineering | 75 | 8.6% |
| 23 | Rust | Languages | 74 | 8.5% |
| 24 | Evals | LLM & GenAI | 73 | 8.4% |
| 25 | Spark | Data Engineering | 72 | 8.2% |
| 26 | Docker | Infra & Cloud | 69 | 7.9% |
| 27 | Linux | Infra & Cloud | 55 | 6.3% |
| 28 | PyTorch | Frameworks & Libraries | 55 | 6.3% |
| 29 | Security | Practices | 52 | 6.0% |
| 30 | Databricks | Data Engineering | 50 | 5.7% |
| 31 | RAG | LLM & GenAI | 48 | 5.5% |
| 32 | MCP | LLM & GenAI | 47 | 5.4% |
| 33 | Prompt Engineering | LLM & GenAI | 45 | 5.2% |
| 34 | dbt | Data Engineering | 45 | 5.2% |
| 35 | A/B Testing | Practices | 44 | 5.0% |
| 36 | Deep Learning | ML Fundamentals | 43 | 4.9% |
| 37 | Recommender Systems | ML Fundamentals | 43 | 4.9% |
| 38 | MLOps | Practices | 41 | 4.7% |
| 39 | AI Safety | LLM & GenAI | 38 | 4.4% |
| 40 | TensorFlow | Frameworks & Libraries | 37 | 4.2% |

</details>

## Movers

Change in share of postings since 2026-08-27, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Machine Learning | +0.65 | | Distributed Systems | -3.05 |
| AI Agents | +0.52 | | Azure | -2.45 |
| Databricks | +0.36 | | GCP | -2.41 |
| Evals | +0.26 | | AWS | -1.58 |
| MCP | +0.24 | | TypeScript | -1.36 |
| Deep Learning | +0.12 | | Airflow | -1.32 |
| CI/CD | +0.12 | | Go | -1.32 |
| Scala | +0.11 | | Kubernetes | -1.25 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,210 | 39.6% |
| swe | 508 | 16.6% |
| other | 461 | 15.1% |
| ops | 286 | 9.3% |
| product | 229 | 7.5% |
| infra | 148 | 4.8% |
| ml-ai | 97 | 3.2% |
| data | 78 | 2.5% |
| research | 42 | 1.4% |

## Disclosed pay, remote engineering roles

556 of 873 engineering postings (64%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $195,000 |
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


<sub>Generated 2026-09-03T12:35:27+00:00 · 2 board(s) unreachable this run</sub>
