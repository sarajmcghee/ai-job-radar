# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-09-17** — tracking **2,943 open remote roles** across **94 companies** (830 of them engineering roles). 1,671 postings disclose pay. **45 appeared today.**

<sub>Remote-only: 14,127 postings were collected across all locations and 20.8% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 830 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 395 | 47.6% |
| 2 | Observability | Practices | 283 | 34.1% |
| 3 | Distributed Systems | Practices | 263 | 31.7% |
| 4 | Machine Learning | ML Fundamentals | 260 | 31.3% |
| 5 | Go | Languages | 258 | 31.1% |
| 6 | LLMs | LLM & GenAI | 240 | 28.9% |
| 7 | AI Agents | LLM & GenAI | 235 | 28.3% |
| 8 | AWS | Infra & Cloud | 222 | 26.7% |
| 9 | Kubernetes | Infra & Cloud | 214 | 25.8% |
| 10 | TypeScript | Languages | 173 | 20.8% |
| 11 | Statistics | ML Fundamentals | 155 | 18.7% |
| 12 | SQL | Languages | 152 | 18.3% |
| 13 | Data Pipelines | Data Engineering | 141 | 17.0% |
| 14 | GCP | Infra & Cloud | 135 | 16.3% |
| 15 | CI/CD | Practices | 126 | 15.2% |
| 16 | Terraform | Infra & Cloud | 111 | 13.4% |
| 17 | Java | Languages | 108 | 13.0% |
| 18 | React | Frameworks & Libraries | 102 | 12.3% |
| 19 | Azure | Infra & Cloud | 87 | 10.5% |
| 20 | Snowflake / BigQuery | Data Engineering | 74 | 8.9% |
| 21 | Airflow | Data Engineering | 73 | 8.8% |
| 22 | Rust | Languages | 69 | 8.3% |
| 23 | Evals | LLM & GenAI | 68 | 8.2% |
| 24 | Kafka | Data Engineering | 67 | 8.1% |
| 25 | Spark | Data Engineering | 64 | 7.7% |
| 26 | Docker | Infra & Cloud | 61 | 7.3% |
| 27 | Security | Practices | 50 | 6.0% |
| 28 | Linux | Infra & Cloud | 50 | 6.0% |
| 29 | PyTorch | Frameworks & Libraries | 48 | 5.8% |
| 30 | dbt | Data Engineering | 46 | 5.5% |
| 31 | Deep Learning | ML Fundamentals | 43 | 5.2% |
| 32 | RAG | LLM & GenAI | 43 | 5.2% |
| 33 | Databricks | Data Engineering | 40 | 4.8% |
| 34 | MLOps | Practices | 40 | 4.8% |
| 35 | AI Safety | LLM & GenAI | 38 | 4.6% |
| 36 | Recommender Systems | ML Fundamentals | 38 | 4.6% |
| 37 | MCP | LLM & GenAI | 37 | 4.5% |
| 38 | A/B Testing | Practices | 37 | 4.5% |
| 39 | Prompt Engineering | LLM & GenAI | 36 | 4.3% |
| 40 | Fine-tuning | LLM & GenAI | 34 | 4.1% |

</details>

## Movers

Change in share of postings since 2026-09-10, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Data Pipelines | +0.29 | | LLMs | -0.86 |
| CI/CD | +0.15 | | AI Agents | -0.80 |
| LangChain | +0.11 | | GCP | -0.60 |
| Embeddings | +0.10 | | Python | -0.55 |
| Go | +0.09 | | Java | -0.53 |
| TensorFlow | +0.06 | | SQL | -0.46 |
| Docker | +0.04 | | Snowflake / BigQuery | -0.44 |
| Spark | +0.04 | | Terraform | -0.40 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,154 | 39.2% |
| swe | 477 | 16.2% |
| other | 461 | 15.7% |
| ops | 265 | 9.0% |
| product | 233 | 7.9% |
| infra | 149 | 5.1% |
| ml-ai | 85 | 2.9% |
| data | 73 | 2.5% |
| research | 46 | 1.6% |

## Disclosed pay, remote engineering roles

544 of 830 engineering postings (66%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $194,250 |
| Median | $227,735 |
| 75th | $259,500 |
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
| Snorkel AI | $316,000 |
| Hightouch | $310,000 |
| Lambda | $299,000 |

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


<sub>Generated 2026-09-17T13:03:39+00:00 · 2 board(s) unreachable this run</sub>
