# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-11-14** — tracking **2,919 open remote roles** across **86 companies** (815 of them engineering roles). 1,742 postings disclose pay. **39 appeared today.**

<sub>Remote-only: 14,689 postings were collected across all locations and 19.9% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 815 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 350 | 42.9% |
| 2 | Observability | Practices | 276 | 33.9% |
| 3 | LLMs | LLM & GenAI | 250 | 30.7% |
| 4 | Go | Languages | 243 | 29.8% |
| 5 | Distributed Systems | Practices | 238 | 29.2% |
| 6 | AI Agents | LLM & GenAI | 236 | 29.0% |
| 7 | Machine Learning | ML Fundamentals | 226 | 27.7% |
| 8 | Kubernetes | Infra & Cloud | 218 | 26.7% |
| 9 | TypeScript | Languages | 194 | 23.8% |
| 10 | AWS | Infra & Cloud | 193 | 23.7% |
| 11 | Statistics | ML Fundamentals | 151 | 18.5% |
| 12 | SQL | Languages | 140 | 17.2% |
| 13 | CI/CD | Practices | 134 | 16.4% |
| 14 | React | Frameworks & Libraries | 129 | 15.8% |
| 15 | GCP | Infra & Cloud | 121 | 14.8% |
| 16 | Data Pipelines | Data Engineering | 121 | 14.8% |
| 17 | Terraform | Infra & Cloud | 110 | 13.5% |
| 18 | Java | Languages | 91 | 11.2% |
| 19 | Snowflake / BigQuery | Data Engineering | 79 | 9.7% |
| 20 | Evals | LLM & GenAI | 64 | 7.9% |
| 21 | Azure | Infra & Cloud | 62 | 7.6% |
| 22 | Airflow | Data Engineering | 62 | 7.6% |
| 23 | Rust | Languages | 60 | 7.4% |
| 24 | Kafka | Data Engineering | 59 | 7.2% |
| 25 | Security | Practices | 58 | 7.1% |
| 26 | MCP | LLM & GenAI | 55 | 6.7% |
| 27 | Spark | Data Engineering | 54 | 6.6% |
| 28 | Databricks | Data Engineering | 48 | 5.9% |
| 29 | Docker | Infra & Cloud | 48 | 5.9% |
| 30 | Linux | Infra & Cloud | 45 | 5.5% |
| 31 | dbt | Data Engineering | 40 | 4.9% |
| 32 | AI Safety | LLM & GenAI | 37 | 4.5% |
| 33 | PyTorch | Frameworks & Libraries | 37 | 4.5% |
| 34 | A/B Testing | Practices | 35 | 4.3% |
| 35 | MLOps | Practices | 35 | 4.3% |
| 36 | Prompt Engineering | LLM & GenAI | 34 | 4.2% |
| 37 | Recommender Systems | ML Fundamentals | 33 | 4.0% |
| 38 | Deep Learning | ML Fundamentals | 31 | 3.8% |
| 39 | RAG | LLM & GenAI | 31 | 3.8% |
| 40 | Multimodal | LLM & GenAI | 27 | 3.3% |

</details>

## Movers

Change in share of postings since 2026-11-07, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| dbt | +0.61 | | Python | -0.64 |
| CI/CD | +0.43 | | Machine Learning | -0.29 |
| Kubernetes | +0.41 | | PyTorch | -0.28 |
| Go | +0.31 | | Java | -0.26 |
| A/B Testing | +0.30 | | MLOps | -0.22 |
| Distributed Systems | +0.28 | | NLP | -0.21 |
| AWS | +0.27 | | Airflow | -0.21 |
| React | +0.26 | | Multimodal | -0.21 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,177 | 40.3% |
| swe | 451 | 15.5% |
| other | 425 | 14.6% |
| ops | 281 | 9.6% |
| product | 221 | 7.6% |
| infra | 164 | 5.6% |
| ml-ai | 85 | 2.9% |
| data | 66 | 2.3% |
| research | 49 | 1.7% |

## Disclosed pay, remote engineering roles

549 of 815 engineering postings (67%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $195,450 |
| Median | $228,500 |
| 75th | $260,450 |
| 90th | $289,530 |

<details><summary>Highest disclosed engineering bands by company</summary>

| Company | Top posted midpoint |
|---|---:|
| Anthropic | $675,000 |
| OpenAI | $455,500 |
| Pinterest | $371,087 |
| Reddit | $351,000 |
| Harvey | $340,000 |
| Agility Robotics | $329,500 |
| Coinbase | $320,142 |
| Snorkel AI | $316,000 |
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


<sub>Generated 2026-11-14T14:46:01+00:00 · 5 board(s) unreachable this run</sub>
