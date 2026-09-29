# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-09-29** — tracking **2,858 open remote roles** across **92 companies** (815 of them engineering roles). 1,641 postings disclose pay. **49 appeared today.**

<sub>Remote-only: 14,175 postings were collected across all locations and 20.2% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 815 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 378 | 46.4% |
| 2 | Observability | Practices | 281 | 34.5% |
| 3 | Distributed Systems | Practices | 267 | 32.8% |
| 4 | Machine Learning | ML Fundamentals | 257 | 31.5% |
| 5 | Go | Languages | 247 | 30.3% |
| 6 | LLMs | LLM & GenAI | 236 | 29.0% |
| 7 | AI Agents | LLM & GenAI | 231 | 28.3% |
| 8 | AWS | Infra & Cloud | 231 | 28.3% |
| 9 | Kubernetes | Infra & Cloud | 206 | 25.3% |
| 10 | TypeScript | Languages | 164 | 20.1% |
| 11 | Statistics | ML Fundamentals | 153 | 18.8% |
| 12 | SQL | Languages | 146 | 17.9% |
| 13 | Data Pipelines | Data Engineering | 146 | 17.9% |
| 14 | GCP | Infra & Cloud | 145 | 17.8% |
| 15 | CI/CD | Practices | 124 | 15.2% |
| 16 | Terraform | Infra & Cloud | 112 | 13.7% |
| 17 | Java | Languages | 106 | 13.0% |
| 18 | React | Frameworks & Libraries | 104 | 12.8% |
| 19 | Azure | Infra & Cloud | 92 | 11.3% |
| 20 | Kafka | Data Engineering | 76 | 9.3% |
| 21 | Snowflake / BigQuery | Data Engineering | 73 | 9.0% |
| 22 | Airflow | Data Engineering | 70 | 8.6% |
| 23 | Spark | Data Engineering | 63 | 7.7% |
| 24 | Rust | Languages | 62 | 7.6% |
| 25 | Docker | Infra & Cloud | 55 | 6.7% |
| 26 | Security | Practices | 53 | 6.5% |
| 27 | Linux | Infra & Cloud | 51 | 6.3% |
| 28 | Evals | LLM & GenAI | 51 | 6.3% |
| 29 | PyTorch | Frameworks & Libraries | 46 | 5.6% |
| 30 | AI Safety | LLM & GenAI | 44 | 5.4% |
| 31 | MCP | LLM & GenAI | 43 | 5.3% |
| 32 | Databricks | Data Engineering | 41 | 5.0% |
| 33 | dbt | Data Engineering | 41 | 5.0% |
| 34 | MLOps | Practices | 40 | 4.9% |
| 35 | Deep Learning | ML Fundamentals | 40 | 4.9% |
| 36 | RAG | LLM & GenAI | 38 | 4.7% |
| 37 | Recommender Systems | ML Fundamentals | 38 | 4.7% |
| 38 | A/B Testing | Practices | 33 | 4.0% |
| 39 | Fine-tuning | LLM & GenAI | 33 | 4.0% |
| 40 | TensorFlow | Frameworks & Libraries | 32 | 3.9% |

</details>

## Movers

Change in share of postings since 2026-09-22, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| AWS | +0.73 | | Snowflake / BigQuery | -0.48 |
| Machine Learning | +0.60 | | Rust | -0.41 |
| GCP | +0.41 | | Statistics | -0.38 |
| Python | +0.34 | | Observability | -0.37 |
| Azure | +0.33 | | A/B Testing | -0.35 |
| AI Safety | +0.31 | | Evals | -0.29 |
| Linux | +0.30 | | dbt | -0.28 |
| Terraform | +0.30 | | LLMs | -0.28 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,105 | 38.7% |
| other | 459 | 16.1% |
| swe | 455 | 15.9% |
| ops | 260 | 9.1% |
| product | 219 | 7.7% |
| infra | 154 | 5.4% |
| ml-ai | 81 | 2.8% |
| data | 76 | 2.7% |
| research | 49 | 1.7% |

## Disclosed pay, remote engineering roles

542 of 815 engineering postings (67%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $195,450 |
| Median | $227,735 |
| 75th | $260,050 |
| 90th | $290,000 |

<details><summary>Highest disclosed engineering bands by company</summary>

| Company | Top posted midpoint |
|---|---:|
| Anthropic | $675,000 |
| OpenAI | $455,500 |
| Pinterest | $371,087 |
| Reddit | $351,000 |
| Databricks | $343,425 |
| Agility Robotics | $329,500 |
| Instacart | $321,750 |
| Snorkel AI | $316,000 |
| Hightouch | $310,000 |
| Discord | $306,000 |

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


<sub>Generated 2026-09-29T14:36:33+00:00 · 3 board(s) unreachable this run</sub>
