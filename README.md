# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-10-31** — tracking **2,886 open remote roles** across **90 companies** (827 of them engineering roles). 1,680 postings disclose pay. **62 appeared today.**

<sub>Remote-only: 14,525 postings were collected across all locations and 19.9% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 827 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 366 | 44.3% |
| 2 | Observability | Practices | 269 | 32.5% |
| 3 | Machine Learning | ML Fundamentals | 247 | 29.9% |
| 4 | Distributed Systems | Practices | 241 | 29.1% |
| 5 | Go | Languages | 240 | 29.0% |
| 6 | LLMs | LLM & GenAI | 237 | 28.7% |
| 7 | AI Agents | LLM & GenAI | 228 | 27.6% |
| 8 | Kubernetes | Infra & Cloud | 212 | 25.6% |
| 9 | AWS | Infra & Cloud | 199 | 24.1% |
| 10 | TypeScript | Languages | 174 | 21.0% |
| 11 | Statistics | ML Fundamentals | 161 | 19.5% |
| 12 | SQL | Languages | 150 | 18.1% |
| 13 | Data Pipelines | Data Engineering | 126 | 15.2% |
| 14 | CI/CD | Practices | 121 | 14.6% |
| 15 | GCP | Infra & Cloud | 119 | 14.4% |
| 16 | Terraform | Infra & Cloud | 118 | 14.3% |
| 17 | React | Frameworks & Libraries | 113 | 13.7% |
| 18 | Java | Languages | 100 | 12.1% |
| 19 | Snowflake / BigQuery | Data Engineering | 79 | 9.6% |
| 20 | Airflow | Data Engineering | 68 | 8.2% |
| 21 | Kafka | Data Engineering | 65 | 7.9% |
| 22 | Azure | Infra & Cloud | 64 | 7.7% |
| 23 | Rust | Languages | 64 | 7.7% |
| 24 | Spark | Data Engineering | 63 | 7.6% |
| 25 | Evals | LLM & GenAI | 58 | 7.0% |
| 26 | Security | Practices | 55 | 6.7% |
| 27 | Docker | Infra & Cloud | 50 | 6.0% |
| 28 | PyTorch | Frameworks & Libraries | 48 | 5.8% |
| 29 | Databricks | Data Engineering | 44 | 5.3% |
| 30 | MCP | LLM & GenAI | 43 | 5.2% |
| 31 | dbt | Data Engineering | 43 | 5.2% |
| 32 | Recommender Systems | ML Fundamentals | 41 | 5.0% |
| 33 | AI Safety | LLM & GenAI | 40 | 4.8% |
| 34 | Linux | Infra & Cloud | 40 | 4.8% |
| 35 | MLOps | Practices | 38 | 4.6% |
| 36 | Deep Learning | ML Fundamentals | 36 | 4.4% |
| 37 | Multimodal | LLM & GenAI | 35 | 4.2% |
| 38 | RAG | LLM & GenAI | 32 | 3.9% |
| 39 | TensorFlow | Frameworks & Libraries | 31 | 3.7% |
| 40 | A/B Testing | Practices | 30 | 3.6% |

</details>

## Movers

Change in share of postings since 2026-10-24, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Snowflake / BigQuery | +0.46 | | Observability | -1.16 |
| SQL | +0.30 | | Kubernetes | -0.73 |
| Java | +0.22 | | TypeScript | -0.57 |
| Evals | +0.22 | | GCP | -0.49 |
| Statistics | +0.19 | | LLMs | -0.48 |
| Airflow | +0.18 | | AWS | -0.41 |
| Security | +0.08 | | Data Pipelines | -0.39 |
| LangChain | +0.07 | | Machine Learning | -0.37 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,123 | 38.9% |
| other | 449 | 15.6% |
| swe | 445 | 15.4% |
| ops | 262 | 9.1% |
| product | 225 | 7.8% |
| infra | 159 | 5.5% |
| ml-ai | 96 | 3.3% |
| data | 74 | 2.6% |
| research | 53 | 1.8% |

## Disclosed pay, remote engineering roles

558 of 827 engineering postings (67%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $195,000 |
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
| Agility Robotics | $329,500 |
| Coinbase | $320,142 |
| Snorkel AI | $316,000 |
| Discord | $306,000 |
| GitLab | $301,800 |
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


<sub>Generated 2026-10-31T14:16:55+00:00 · 4 board(s) unreachable this run</sub>
