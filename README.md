# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-09-10** — tracking **3,003 open remote roles** across **94 companies** (874 of them engineering roles). 1,679 postings disclose pay. **65 appeared today.**

<sub>Remote-only: 14,087 postings were collected across all locations and 21.3% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 874 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 418 | 47.8% |
| 2 | Observability | Practices | 300 | 34.3% |
| 3 | Distributed Systems | Practices | 284 | 32.5% |
| 4 | Machine Learning | ML Fundamentals | 268 | 30.7% |
| 5 | Go | Languages | 263 | 30.1% |
| 6 | AI Agents | LLM & GenAI | 260 | 29.7% |
| 7 | LLMs | LLM & GenAI | 254 | 29.1% |
| 8 | AWS | Infra & Cloud | 239 | 27.3% |
| 9 | Kubernetes | Infra & Cloud | 225 | 25.7% |
| 10 | TypeScript | Languages | 183 | 20.9% |
| 11 | Statistics | ML Fundamentals | 165 | 18.9% |
| 12 | SQL | Languages | 155 | 17.7% |
| 13 | GCP | Infra & Cloud | 149 | 17.0% |
| 14 | Data Pipelines | Data Engineering | 141 | 16.1% |
| 15 | CI/CD | Practices | 135 | 15.4% |
| 16 | Terraform | Infra & Cloud | 127 | 14.5% |
| 17 | Java | Languages | 124 | 14.2% |
| 18 | React | Frameworks & Libraries | 104 | 11.9% |
| 19 | Azure | Infra & Cloud | 99 | 11.3% |
| 20 | Snowflake / BigQuery | Data Engineering | 85 | 9.7% |
| 21 | Airflow | Data Engineering | 82 | 9.4% |
| 22 | Kafka | Data Engineering | 74 | 8.5% |
| 23 | Rust | Languages | 73 | 8.4% |
| 24 | Evals | LLM & GenAI | 72 | 8.2% |
| 25 | Spark | Data Engineering | 70 | 8.0% |
| 26 | Docker | Infra & Cloud | 61 | 7.0% |
| 27 | Linux | Infra & Cloud | 54 | 6.2% |
| 28 | Security | Practices | 51 | 5.8% |
| 29 | Databricks | Data Engineering | 50 | 5.7% |
| 30 | RAG | LLM & GenAI | 48 | 5.5% |
| 31 | PyTorch | Frameworks & Libraries | 48 | 5.5% |
| 32 | dbt | Data Engineering | 46 | 5.3% |
| 33 | Prompt Engineering | LLM & GenAI | 44 | 5.0% |
| 34 | MCP | LLM & GenAI | 43 | 4.9% |
| 35 | A/B Testing | Practices | 42 | 4.8% |
| 36 | Recommender Systems | ML Fundamentals | 42 | 4.8% |
| 37 | Deep Learning | ML Fundamentals | 41 | 4.7% |
| 38 | MLOps | Practices | 39 | 4.5% |
| 39 | Fine-tuning | LLM & GenAI | 35 | 4.0% |
| 40 | AI Safety | LLM & GenAI | 34 | 3.9% |

</details>

## Movers

Change in share of postings since 2026-09-03, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| LLMs | +0.53 | | dbt | -0.86 |
| AWS | +0.41 | | Kubernetes | -0.54 |
| Distributed Systems | +0.28 | | Machine Learning | -0.44 |
| Security | +0.22 | | CI/CD | -0.35 |
| Airflow | +0.17 | | Docker | -0.29 |
| Observability | +0.16 | | Statistics | -0.25 |
| Databricks | +0.16 | | PyTorch | -0.19 |
| Computer Vision | +0.13 | | Evals | -0.19 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,164 | 38.8% |
| swe | 510 | 17.0% |
| other | 445 | 14.8% |
| ops | 283 | 9.4% |
| product | 237 | 7.9% |
| infra | 147 | 4.9% |
| ml-ai | 92 | 3.1% |
| data | 78 | 2.6% |
| research | 47 | 1.6% |

## Disclosed pay, remote engineering roles

562 of 874 engineering postings (64%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $196,285 |
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


<sub>Generated 2026-09-10T12:43:12+00:00 · 2 board(s) unreachable this run</sub>
