# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-10-01** — tracking **2,840 open remote roles** across **92 companies** (821 of them engineering roles). 1,635 postings disclose pay. **38 appeared today.**

<sub>Remote-only: 14,220 postings were collected across all locations and 20.0% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 821 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 377 | 45.9% |
| 2 | Observability | Practices | 283 | 34.5% |
| 3 | Distributed Systems | Practices | 272 | 33.1% |
| 4 | Machine Learning | ML Fundamentals | 252 | 30.7% |
| 5 | Go | Languages | 251 | 30.6% |
| 6 | LLMs | LLM & GenAI | 229 | 27.9% |
| 7 | AI Agents | LLM & GenAI | 227 | 27.6% |
| 8 | AWS | Infra & Cloud | 224 | 27.3% |
| 9 | Kubernetes | Infra & Cloud | 203 | 24.7% |
| 10 | TypeScript | Languages | 166 | 20.2% |
| 11 | Statistics | ML Fundamentals | 154 | 18.8% |
| 12 | GCP | Infra & Cloud | 145 | 17.7% |
| 13 | SQL | Languages | 142 | 17.3% |
| 14 | Data Pipelines | Data Engineering | 142 | 17.3% |
| 15 | CI/CD | Practices | 127 | 15.5% |
| 16 | React | Frameworks & Libraries | 113 | 13.8% |
| 17 | Java | Languages | 109 | 13.3% |
| 18 | Terraform | Infra & Cloud | 108 | 13.2% |
| 19 | Azure | Infra & Cloud | 90 | 11.0% |
| 20 | Kafka | Data Engineering | 75 | 9.1% |
| 21 | Snowflake / BigQuery | Data Engineering | 73 | 8.9% |
| 22 | Airflow | Data Engineering | 71 | 8.6% |
| 23 | Spark | Data Engineering | 63 | 7.7% |
| 24 | Rust | Languages | 63 | 7.7% |
| 25 | Docker | Infra & Cloud | 53 | 6.5% |
| 26 | Security | Practices | 52 | 6.3% |
| 27 | Linux | Infra & Cloud | 48 | 5.8% |
| 28 | Evals | LLM & GenAI | 45 | 5.5% |
| 29 | PyTorch | Frameworks & Libraries | 45 | 5.5% |
| 30 | AI Safety | LLM & GenAI | 44 | 5.4% |
| 31 | MLOps | Practices | 41 | 5.0% |
| 32 | dbt | Data Engineering | 41 | 5.0% |
| 33 | MCP | LLM & GenAI | 40 | 4.9% |
| 34 | Databricks | Data Engineering | 39 | 4.8% |
| 35 | Deep Learning | ML Fundamentals | 39 | 4.8% |
| 36 | Recommender Systems | ML Fundamentals | 38 | 4.6% |
| 37 | RAG | LLM & GenAI | 37 | 4.5% |
| 38 | Fine-tuning | LLM & GenAI | 32 | 3.9% |
| 39 | A/B Testing | Practices | 31 | 3.8% |
| 40 | TensorFlow | Frameworks & Libraries | 31 | 3.8% |

</details>

## Movers

Change in share of postings since 2026-09-24, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Machine Learning | +0.40 | | Observability | -0.74 |
| Speech / Audio | +0.31 | | LLMs | -0.74 |
| React | +0.30 | | Kubernetes | -0.66 |
| AI Safety | +0.19 | | Rust | -0.47 |
| CI/CD | +0.19 | | Evals | -0.42 |
| Kafka | +0.18 | | Docker | -0.40 |
| Recommender Systems | +0.18 | | Prompt Engineering | -0.39 |
| Transformers | +0.18 | | Python | -0.39 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,077 | 37.9% |
| other | 466 | 16.4% |
| swe | 465 | 16.4% |
| ops | 257 | 9.0% |
| product | 219 | 7.7% |
| infra | 150 | 5.3% |
| ml-ai | 81 | 2.9% |
| data | 78 | 2.7% |
| research | 47 | 1.7% |

## Disclosed pay, remote engineering roles

548 of 821 engineering postings (67%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $196,285 |
| Median | $227,735 |
| 75th | $260,000 |
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


<sub>Generated 2026-10-01T15:04:48+00:00 · 3 board(s) unreachable this run</sub>
