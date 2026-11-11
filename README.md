# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-11-11** — tracking **2,922 open remote roles** across **86 companies** (820 of them engineering roles). 1,739 postings disclose pay. **60 appeared today.**

<sub>Remote-only: 14,680 postings were collected across all locations and 19.9% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 820 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 368 | 44.9% |
| 2 | Observability | Practices | 277 | 33.8% |
| 3 | Distributed Systems | Practices | 250 | 30.5% |
| 4 | AI Agents | LLM & GenAI | 243 | 29.6% |
| 5 | LLMs | LLM & GenAI | 243 | 29.6% |
| 6 | Go | Languages | 239 | 29.1% |
| 7 | Machine Learning | ML Fundamentals | 239 | 29.1% |
| 8 | Kubernetes | Infra & Cloud | 215 | 26.2% |
| 9 | AWS | Infra & Cloud | 189 | 23.0% |
| 10 | TypeScript | Languages | 183 | 22.3% |
| 11 | Statistics | ML Fundamentals | 146 | 17.8% |
| 12 | SQL | Languages | 144 | 17.6% |
| 13 | CI/CD | Practices | 132 | 16.1% |
| 14 | Data Pipelines | Data Engineering | 120 | 14.6% |
| 15 | React | Frameworks & Libraries | 118 | 14.4% |
| 16 | GCP | Infra & Cloud | 117 | 14.3% |
| 17 | Terraform | Infra & Cloud | 113 | 13.8% |
| 18 | Java | Languages | 99 | 12.1% |
| 19 | Snowflake / BigQuery | Data Engineering | 74 | 9.0% |
| 20 | Airflow | Data Engineering | 71 | 8.7% |
| 21 | Rust | Languages | 65 | 7.9% |
| 22 | Kafka | Data Engineering | 64 | 7.8% |
| 23 | Evals | LLM & GenAI | 64 | 7.8% |
| 24 | Spark | Data Engineering | 59 | 7.2% |
| 25 | Azure | Infra & Cloud | 59 | 7.2% |
| 26 | Security | Practices | 56 | 6.8% |
| 27 | MCP | LLM & GenAI | 50 | 6.1% |
| 28 | Docker | Infra & Cloud | 46 | 5.6% |
| 29 | Linux | Infra & Cloud | 46 | 5.6% |
| 30 | Databricks | Data Engineering | 44 | 5.4% |
| 31 | dbt | Data Engineering | 43 | 5.2% |
| 32 | PyTorch | Frameworks & Libraries | 42 | 5.1% |
| 33 | MLOps | Practices | 40 | 4.9% |
| 34 | Recommender Systems | ML Fundamentals | 38 | 4.6% |
| 35 | AI Safety | LLM & GenAI | 37 | 4.5% |
| 36 | RAG | LLM & GenAI | 34 | 4.1% |
| 37 | Deep Learning | ML Fundamentals | 33 | 4.0% |
| 38 | Prompt Engineering | LLM & GenAI | 32 | 3.9% |
| 39 | Multimodal | LLM & GenAI | 32 | 3.9% |
| 40 | A/B Testing | Practices | 28 | 3.4% |

</details>

## Movers

Change in share of postings since 2026-11-04, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Observability | +0.67 | | Machine Learning | -0.55 |
| CI/CD | +0.51 | | Python | -0.33 |
| Distributed Systems | +0.40 | | Snowflake / BigQuery | -0.23 |
| Recommender Systems | +0.35 | | Data Pipelines | -0.21 |
| Linux | +0.29 | | PyTorch | -0.20 |
| Evals | +0.28 | | Computer Vision | -0.19 |
| Go | +0.17 | | AI Safety | -0.18 |
| Fine-tuning | +0.17 | | Java | -0.16 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,178 | 40.3% |
| swe | 450 | 15.4% |
| other | 419 | 14.3% |
| ops | 272 | 9.3% |
| product | 233 | 8.0% |
| infra | 161 | 5.5% |
| ml-ai | 91 | 3.1% |
| data | 69 | 2.4% |
| research | 49 | 1.7% |

## Disclosed pay, remote engineering roles

554 of 820 engineering postings (68%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $196,285 |
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


<sub>Generated 2026-11-11T15:50:44+00:00 · 5 board(s) unreachable this run</sub>
