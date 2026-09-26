# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-09-26** — tracking **2,906 open remote roles** across **93 companies** (845 of them engineering roles). 1,653 postings disclose pay. **44 appeared today.**

<sub>Remote-only: 14,298 postings were collected across all locations and 20.3% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 845 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 385 | 45.6% |
| 2 | Observability | Practices | 310 | 36.7% |
| 3 | Distributed Systems | Practices | 280 | 33.1% |
| 4 | Machine Learning | ML Fundamentals | 263 | 31.1% |
| 5 | LLMs | LLM & GenAI | 260 | 30.8% |
| 6 | Go | Languages | 257 | 30.4% |
| 7 | AI Agents | LLM & GenAI | 238 | 28.2% |
| 8 | AWS | Infra & Cloud | 238 | 28.2% |
| 9 | Kubernetes | Infra & Cloud | 220 | 26.0% |
| 10 | TypeScript | Languages | 175 | 20.7% |
| 11 | Statistics | ML Fundamentals | 162 | 19.2% |
| 12 | GCP | Infra & Cloud | 153 | 18.1% |
| 13 | SQL | Languages | 147 | 17.4% |
| 14 | Data Pipelines | Data Engineering | 142 | 16.8% |
| 15 | CI/CD | Practices | 122 | 14.4% |
| 16 | Terraform | Infra & Cloud | 117 | 13.8% |
| 17 | React | Frameworks & Libraries | 114 | 13.5% |
| 18 | Java | Languages | 108 | 12.8% |
| 19 | Azure | Infra & Cloud | 101 | 12.0% |
| 20 | Kafka | Data Engineering | 78 | 9.2% |
| 21 | Snowflake / BigQuery | Data Engineering | 77 | 9.1% |
| 22 | Rust | Languages | 73 | 8.6% |
| 23 | Airflow | Data Engineering | 71 | 8.4% |
| 24 | Spark | Data Engineering | 67 | 7.9% |
| 25 | Docker | Infra & Cloud | 66 | 7.8% |
| 26 | Evals | LLM & GenAI | 57 | 6.7% |
| 27 | Security | Practices | 52 | 6.2% |
| 28 | Linux | Infra & Cloud | 50 | 5.9% |
| 29 | PyTorch | Frameworks & Libraries | 48 | 5.7% |
| 30 | MCP | LLM & GenAI | 45 | 5.3% |
| 31 | AI Safety | LLM & GenAI | 43 | 5.1% |
| 32 | Databricks | Data Engineering | 43 | 5.1% |
| 33 | Deep Learning | ML Fundamentals | 42 | 5.0% |
| 34 | MLOps | Practices | 41 | 4.9% |
| 35 | RAG | LLM & GenAI | 41 | 4.9% |
| 36 | dbt | Data Engineering | 41 | 4.9% |
| 37 | Prompt Engineering | LLM & GenAI | 38 | 4.5% |
| 38 | Recommender Systems | ML Fundamentals | 38 | 4.5% |
| 39 | Fine-tuning | LLM & GenAI | 36 | 4.3% |
| 40 | A/B Testing | Practices | 32 | 3.8% |

</details>

## Movers

Change in share of postings since 2026-09-19, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| AWS | +1.12 | | Snowflake / BigQuery | -0.54 |
| Observability | +1.01 | | Evals | -0.27 |
| Distributed Systems | +0.83 | | SQL | -0.25 |
| GCP | +0.81 | | dbt | -0.25 |
| Azure | +0.73 | | Statistics | -0.24 |
| Kubernetes | +0.66 | | A/B Testing | -0.23 |
| Docker | +0.62 | | CI/CD | -0.20 |
| LLMs | +0.48 | | Embeddings | -0.14 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,122 | 38.6% |
| swe | 485 | 16.7% |
| other | 453 | 15.6% |
| ops | 263 | 9.1% |
| product | 223 | 7.7% |
| infra | 156 | 5.4% |
| ml-ai | 84 | 2.9% |
| data | 72 | 2.5% |
| research | 48 | 1.7% |

## Disclosed pay, remote engineering roles

539 of 845 engineering postings (64%) publish a salary range. Figures are the midpoint of the posted band.

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
| Snorkel AI | $316,000 |
| Hightouch | $310,000 |
| Discord | $306,000 |
| GitLab | $301,800 |

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


<sub>Generated 2026-09-26T12:40:04+00:00 · 2 board(s) unreachable this run</sub>
