# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-10-26** — tracking **2,888 open remote roles** across **90 companies** (826 of them engineering roles). 1,673 postings disclose pay. **20 appeared today.**

<sub>Remote-only: 14,455 postings were collected across all locations and 20.0% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 826 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 365 | 44.2% |
| 2 | Observability | Practices | 274 | 33.2% |
| 3 | Go | Languages | 247 | 29.9% |
| 4 | Distributed Systems | Practices | 246 | 29.8% |
| 5 | Machine Learning | ML Fundamentals | 241 | 29.2% |
| 6 | LLMs | LLM & GenAI | 239 | 28.9% |
| 7 | AI Agents | LLM & GenAI | 219 | 26.5% |
| 8 | Kubernetes | Infra & Cloud | 218 | 26.4% |
| 9 | AWS | Infra & Cloud | 213 | 25.8% |
| 10 | TypeScript | Languages | 180 | 21.8% |
| 11 | Statistics | ML Fundamentals | 155 | 18.8% |
| 12 | SQL | Languages | 143 | 17.3% |
| 13 | Data Pipelines | Data Engineering | 125 | 15.1% |
| 14 | GCP | Infra & Cloud | 125 | 15.1% |
| 15 | Terraform | Infra & Cloud | 122 | 14.8% |
| 16 | CI/CD | Practices | 120 | 14.5% |
| 17 | React | Frameworks & Libraries | 115 | 13.9% |
| 18 | Java | Languages | 93 | 11.3% |
| 19 | Snowflake / BigQuery | Data Engineering | 77 | 9.3% |
| 20 | Azure | Infra & Cloud | 73 | 8.8% |
| 21 | Airflow | Data Engineering | 66 | 8.0% |
| 22 | Kafka | Data Engineering | 65 | 7.9% |
| 23 | Rust | Languages | 65 | 7.9% |
| 24 | Spark | Data Engineering | 59 | 7.1% |
| 25 | Security | Practices | 58 | 7.0% |
| 26 | Evals | LLM & GenAI | 55 | 6.7% |
| 27 | PyTorch | Frameworks & Libraries | 52 | 6.3% |
| 28 | Docker | Infra & Cloud | 49 | 5.9% |
| 29 | dbt | Data Engineering | 48 | 5.8% |
| 30 | AI Safety | LLM & GenAI | 47 | 5.7% |
| 31 | MCP | LLM & GenAI | 44 | 5.3% |
| 32 | Linux | Infra & Cloud | 43 | 5.2% |
| 33 | Databricks | Data Engineering | 42 | 5.1% |
| 34 | Recommender Systems | ML Fundamentals | 42 | 5.1% |
| 35 | Deep Learning | ML Fundamentals | 40 | 4.8% |
| 36 | Multimodal | LLM & GenAI | 40 | 4.8% |
| 37 | MLOps | Practices | 35 | 4.2% |
| 38 | Fine-tuning | LLM & GenAI | 33 | 4.0% |
| 39 | TensorFlow | Frameworks & Libraries | 31 | 3.8% |
| 40 | RAG | LLM & GenAI | 31 | 3.8% |

</details>

## Movers

Change in share of postings since 2026-10-19, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Security | +0.38 | | Python | -0.94 |
| Observability | +0.27 | | Machine Learning | -0.79 |
| Kubernetes | +0.26 | | Statistics | -0.61 |
| AI Agents | +0.25 | | Databricks | -0.50 |
| Docker | +0.17 | | LLMs | -0.50 |
| Azure | +0.16 | | Data Pipelines | -0.50 |
| Rust | +0.12 | | React | -0.48 |
| Kafka | +0.11 | | CI/CD | -0.45 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,134 | 39.3% |
| swe | 446 | 15.4% |
| other | 431 | 14.9% |
| ops | 272 | 9.4% |
| product | 225 | 7.8% |
| infra | 160 | 5.5% |
| ml-ai | 92 | 3.2% |
| data | 73 | 2.5% |
| research | 55 | 1.9% |

## Disclosed pay, remote engineering roles

551 of 826 engineering postings (67%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $195,000 |
| Median | $226,200 |
| 75th | $260,000 |
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


<sub>Generated 2026-10-26T14:51:12+00:00 · 4 board(s) unreachable this run</sub>
