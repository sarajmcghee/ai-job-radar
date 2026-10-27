# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-10-27** — tracking **2,891 open remote roles** across **90 companies** (822 of them engineering roles). 1,677 postings disclose pay. **73 appeared today.**

<sub>Remote-only: 14,474 postings were collected across all locations and 20.0% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 822 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 363 | 44.2% |
| 2 | Observability | Practices | 271 | 33.0% |
| 3 | Distributed Systems | Practices | 242 | 29.4% |
| 4 | Go | Languages | 241 | 29.3% |
| 5 | Machine Learning | ML Fundamentals | 240 | 29.2% |
| 6 | LLMs | LLM & GenAI | 239 | 29.1% |
| 7 | AI Agents | LLM & GenAI | 222 | 27.0% |
| 8 | Kubernetes | Infra & Cloud | 215 | 26.2% |
| 9 | AWS | Infra & Cloud | 206 | 25.1% |
| 10 | TypeScript | Languages | 178 | 21.7% |
| 11 | Statistics | ML Fundamentals | 151 | 18.4% |
| 12 | SQL | Languages | 144 | 17.5% |
| 13 | Data Pipelines | Data Engineering | 123 | 15.0% |
| 14 | Terraform | Infra & Cloud | 120 | 14.6% |
| 15 | GCP | Infra & Cloud | 120 | 14.6% |
| 16 | CI/CD | Practices | 119 | 14.5% |
| 17 | React | Frameworks & Libraries | 114 | 13.9% |
| 18 | Java | Languages | 91 | 11.1% |
| 19 | Snowflake / BigQuery | Data Engineering | 77 | 9.4% |
| 20 | Azure | Infra & Cloud | 70 | 8.5% |
| 21 | Airflow | Data Engineering | 65 | 7.9% |
| 22 | Kafka | Data Engineering | 64 | 7.8% |
| 23 | Rust | Languages | 62 | 7.5% |
| 24 | Spark | Data Engineering | 59 | 7.2% |
| 25 | Security | Practices | 56 | 6.8% |
| 26 | Evals | LLM & GenAI | 56 | 6.8% |
| 27 | PyTorch | Frameworks & Libraries | 53 | 6.4% |
| 28 | AI Safety | LLM & GenAI | 47 | 5.7% |
| 29 | dbt | Data Engineering | 47 | 5.7% |
| 30 | Docker | Infra & Cloud | 46 | 5.6% |
| 31 | MCP | LLM & GenAI | 45 | 5.5% |
| 32 | Recommender Systems | ML Fundamentals | 43 | 5.2% |
| 33 | Linux | Infra & Cloud | 42 | 5.1% |
| 34 | Databricks | Data Engineering | 41 | 5.0% |
| 35 | Deep Learning | ML Fundamentals | 40 | 4.9% |
| 36 | Multimodal | LLM & GenAI | 40 | 4.9% |
| 37 | MLOps | Practices | 37 | 4.5% |
| 38 | Fine-tuning | LLM & GenAI | 32 | 3.9% |
| 39 | RAG | LLM & GenAI | 32 | 3.9% |
| 40 | TensorFlow | Frameworks & Libraries | 32 | 3.9% |

</details>

## Movers

Change in share of postings since 2026-10-20, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| AI Agents | +0.22 | | Python | -0.99 |
| Kafka | +0.09 | | Machine Learning | -0.87 |
| Evals | +0.08 | | Statistics | -0.75 |
| Security | +0.08 | | Data Pipelines | -0.75 |
| Rust | +0.06 | | Distributed Systems | -0.73 |
| Docker | +0.04 | | Observability | -0.52 |
| Vector Databases | +0.02 | | GCP | -0.52 |
| NLP | +0.01 | | LLMs | -0.52 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,126 | 38.9% |
| other | 456 | 15.8% |
| swe | 444 | 15.4% |
| ops | 262 | 9.1% |
| product | 225 | 7.8% |
| infra | 161 | 5.6% |
| ml-ai | 93 | 3.2% |
| data | 69 | 2.4% |
| research | 55 | 1.9% |

## Disclosed pay, remote engineering roles

547 of 822 engineering postings (67%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $195,450 |
| Median | $226,200 |
| 75th | $260,050 |
| 90th | $289,530 |

<details><summary>Highest disclosed engineering bands by company</summary>

| Company | Top posted midpoint |
|---|---:|
| Anthropic | $675,000 |
| OpenAI | $455,500 |
| Pinterest | $371,087 |
| Reddit | $351,000 |
| Agility Robotics | $329,500 |
| Coinbase | $320,142 |
| Snorkel AI | $316,000 |
| GitLab | $314,000 |
| Discord | $306,000 |
| Cohere | $300,000 |

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


<sub>Generated 2026-10-27T13:56:54+00:00 · 4 board(s) unreachable this run</sub>
