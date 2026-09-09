# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-09-09** — tracking **3,048 open remote roles** across **94 companies** (886 of them engineering roles). 1,726 postings disclose pay. **77 appeared today.**

<sub>Remote-only: 14,105 postings were collected across all locations and 21.6% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 886 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 422 | 47.6% |
| 2 | Observability | Practices | 302 | 34.1% |
| 3 | Distributed Systems | Practices | 287 | 32.4% |
| 4 | Machine Learning | ML Fundamentals | 270 | 30.5% |
| 5 | Go | Languages | 264 | 29.8% |
| 6 | AI Agents | LLM & GenAI | 256 | 28.9% |
| 7 | LLMs | LLM & GenAI | 256 | 28.9% |
| 8 | AWS | Infra & Cloud | 243 | 27.4% |
| 9 | Kubernetes | Infra & Cloud | 229 | 25.8% |
| 10 | TypeScript | Languages | 189 | 21.3% |
| 11 | Statistics | ML Fundamentals | 168 | 19.0% |
| 12 | SQL | Languages | 154 | 17.4% |
| 13 | GCP | Infra & Cloud | 150 | 16.9% |
| 14 | Data Pipelines | Data Engineering | 141 | 15.9% |
| 15 | CI/CD | Practices | 137 | 15.5% |
| 16 | Terraform | Infra & Cloud | 131 | 14.8% |
| 17 | Java | Languages | 125 | 14.1% |
| 18 | React | Frameworks & Libraries | 109 | 12.3% |
| 19 | Azure | Infra & Cloud | 103 | 11.6% |
| 20 | Snowflake / BigQuery | Data Engineering | 87 | 9.8% |
| 21 | Airflow | Data Engineering | 82 | 9.3% |
| 22 | Kafka | Data Engineering | 77 | 8.7% |
| 23 | Evals | LLM & GenAI | 75 | 8.5% |
| 24 | Rust | Languages | 73 | 8.2% |
| 25 | Spark | Data Engineering | 69 | 7.8% |
| 26 | Docker | Infra & Cloud | 62 | 7.0% |
| 27 | Linux | Infra & Cloud | 54 | 6.1% |
| 28 | Security | Practices | 51 | 5.8% |
| 29 | Databricks | Data Engineering | 48 | 5.4% |
| 30 | PyTorch | Frameworks & Libraries | 48 | 5.4% |
| 31 | dbt | Data Engineering | 48 | 5.4% |
| 32 | RAG | LLM & GenAI | 46 | 5.2% |
| 33 | Prompt Engineering | LLM & GenAI | 45 | 5.1% |
| 34 | A/B Testing | Practices | 44 | 5.0% |
| 35 | MCP | LLM & GenAI | 42 | 4.7% |
| 36 | Deep Learning | ML Fundamentals | 42 | 4.7% |
| 37 | Recommender Systems | ML Fundamentals | 41 | 4.6% |
| 38 | MLOps | Practices | 39 | 4.4% |
| 39 | AI Safety | LLM & GenAI | 37 | 4.2% |
| 40 | Fine-tuning | LLM & GenAI | 37 | 4.2% |

</details>

## Movers

Change in share of postings since 2026-09-02, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| AWS | +0.56 | | Machine Learning | -0.67 |
| Rust | +0.36 | | Data Pipelines | -0.35 |
| Distributed Systems | +0.31 | | AI Agents | -0.34 |
| Security | +0.28 | | dbt | -0.33 |
| Observability | +0.26 | | MLOps | -0.30 |
| A/B Testing | +0.19 | | PyTorch | -0.27 |
| SQL | +0.13 | | Statistics | -0.25 |
| React | +0.12 | | TensorFlow | -0.24 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,191 | 39.1% |
| swe | 515 | 16.9% |
| other | 452 | 14.8% |
| ops | 283 | 9.3% |
| product | 236 | 7.7% |
| infra | 151 | 5.0% |
| ml-ai | 94 | 3.1% |
| data | 80 | 2.6% |
| research | 46 | 1.5% |

## Disclosed pay, remote engineering roles

574 of 886 engineering postings (65%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $196,500 |
| Median | $228,950 |
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


<sub>Generated 2026-09-09T12:44:25+00:00 · 2 board(s) unreachable this run</sub>
