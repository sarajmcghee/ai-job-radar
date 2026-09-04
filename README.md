# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-09-04** — tracking **3,059 open remote roles** across **95 companies** (880 of them engineering roles). 1,715 postings disclose pay. **57 appeared today.**

<sub>Remote-only: 14,052 postings were collected across all locations and 21.8% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 880 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 428 | 48.6% |
| 2 | Observability | Practices | 299 | 34.0% |
| 3 | Distributed Systems | Practices | 283 | 32.2% |
| 4 | Machine Learning | ML Fundamentals | 277 | 31.5% |
| 5 | Go | Languages | 270 | 30.7% |
| 6 | AI Agents | LLM & GenAI | 262 | 29.8% |
| 7 | LLMs | LLM & GenAI | 250 | 28.4% |
| 8 | Kubernetes | Infra & Cloud | 241 | 27.4% |
| 9 | AWS | Infra & Cloud | 238 | 27.0% |
| 10 | TypeScript | Languages | 187 | 21.2% |
| 11 | Statistics | ML Fundamentals | 174 | 19.8% |
| 12 | SQL | Languages | 156 | 17.7% |
| 13 | GCP | Infra & Cloud | 149 | 16.9% |
| 14 | Data Pipelines | Data Engineering | 144 | 16.4% |
| 15 | CI/CD | Practices | 140 | 15.9% |
| 16 | Terraform | Infra & Cloud | 136 | 15.5% |
| 17 | Java | Languages | 131 | 14.9% |
| 18 | React | Frameworks & Libraries | 112 | 12.7% |
| 19 | Azure | Infra & Cloud | 105 | 11.9% |
| 20 | Snowflake / BigQuery | Data Engineering | 84 | 9.5% |
| 21 | Airflow | Data Engineering | 81 | 9.2% |
| 22 | Kafka | Data Engineering | 75 | 8.5% |
| 23 | Rust | Languages | 75 | 8.5% |
| 24 | Spark | Data Engineering | 72 | 8.2% |
| 25 | Evals | LLM & GenAI | 72 | 8.2% |
| 26 | Docker | Infra & Cloud | 66 | 7.5% |
| 27 | Linux | Infra & Cloud | 56 | 6.4% |
| 28 | PyTorch | Frameworks & Libraries | 54 | 6.1% |
| 29 | Security | Practices | 52 | 5.9% |
| 30 | Databricks | Data Engineering | 48 | 5.5% |
| 31 | RAG | LLM & GenAI | 47 | 5.3% |
| 32 | MCP | LLM & GenAI | 46 | 5.2% |
| 33 | dbt | Data Engineering | 45 | 5.1% |
| 34 | A/B Testing | Practices | 44 | 5.0% |
| 35 | Prompt Engineering | LLM & GenAI | 44 | 5.0% |
| 36 | Deep Learning | ML Fundamentals | 43 | 4.9% |
| 37 | Recommender Systems | ML Fundamentals | 43 | 4.9% |
| 38 | MLOps | Practices | 40 | 4.5% |
| 39 | AI Safety | LLM & GenAI | 37 | 4.2% |
| 40 | TensorFlow | Frameworks & Libraries | 37 | 4.2% |

</details>

## Movers

Change in share of postings since 2026-08-28, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Statistics | +0.33 | | Distributed Systems | -3.05 |
| Machine Learning | +0.25 | | GCP | -2.61 |
| AI Agents | +0.19 | | Azure | -2.57 |
| MCP | +0.16 | | AWS | -1.75 |
| Databricks | +0.15 | | Kubernetes | -1.51 |
| CI/CD | +0.14 | | Airflow | -1.37 |
| Rust | +0.10 | | TypeScript | -1.20 |
| A/B Testing | +0.10 | | Kafka | -1.07 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,194 | 39.0% |
| swe | 515 | 16.8% |
| other | 467 | 15.3% |
| ops | 286 | 9.3% |
| product | 232 | 7.6% |
| infra | 150 | 4.9% |
| ml-ai | 95 | 3.1% |
| data | 78 | 2.5% |
| research | 42 | 1.4% |

## Disclosed pay, remote engineering roles

560 of 880 engineering postings (64%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $195,000 |
| Median | $228,500 |
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


<sub>Generated 2026-09-04T12:30:40+00:00 · 2 board(s) unreachable this run</sub>
