# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-09-21** — tracking **2,959 open remote roles** across **93 companies** (843 of them engineering roles). 1,667 postings disclose pay. **18 appeared today.**

<sub>Remote-only: 14,200 postings were collected across all locations and 20.8% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 843 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 390 | 46.3% |
| 2 | Observability | Practices | 299 | 35.5% |
| 3 | Distributed Systems | Practices | 274 | 32.5% |
| 4 | Go | Languages | 256 | 30.4% |
| 5 | Machine Learning | ML Fundamentals | 256 | 30.4% |
| 6 | LLMs | LLM & GenAI | 252 | 29.9% |
| 7 | AI Agents | LLM & GenAI | 233 | 27.6% |
| 8 | AWS | Infra & Cloud | 222 | 26.3% |
| 9 | Kubernetes | Infra & Cloud | 221 | 26.2% |
| 10 | TypeScript | Languages | 179 | 21.2% |
| 11 | Statistics | ML Fundamentals | 166 | 19.7% |
| 12 | SQL | Languages | 153 | 18.1% |
| 13 | GCP | Infra & Cloud | 139 | 16.5% |
| 14 | Data Pipelines | Data Engineering | 139 | 16.5% |
| 15 | CI/CD | Practices | 127 | 15.1% |
| 16 | Terraform | Infra & Cloud | 111 | 13.2% |
| 17 | React | Frameworks & Libraries | 108 | 12.8% |
| 18 | Java | Languages | 107 | 12.7% |
| 19 | Azure | Infra & Cloud | 88 | 10.4% |
| 20 | Snowflake / BigQuery | Data Engineering | 80 | 9.5% |
| 21 | Rust | Languages | 73 | 8.7% |
| 22 | Kafka | Data Engineering | 72 | 8.5% |
| 23 | Airflow | Data Engineering | 70 | 8.3% |
| 24 | Spark | Data Engineering | 65 | 7.7% |
| 25 | Evals | LLM & GenAI | 63 | 7.5% |
| 26 | Docker | Infra & Cloud | 59 | 7.0% |
| 27 | Security | Practices | 51 | 6.0% |
| 28 | Linux | Infra & Cloud | 47 | 5.6% |
| 29 | PyTorch | Frameworks & Libraries | 47 | 5.6% |
| 30 | dbt | Data Engineering | 45 | 5.3% |
| 31 | Deep Learning | ML Fundamentals | 44 | 5.2% |
| 32 | Databricks | Data Engineering | 43 | 5.1% |
| 33 | MCP | LLM & GenAI | 42 | 5.0% |
| 34 | RAG | LLM & GenAI | 41 | 4.9% |
| 35 | AI Safety | LLM & GenAI | 39 | 4.6% |
| 36 | MLOps | Practices | 39 | 4.6% |
| 37 | Recommender Systems | ML Fundamentals | 38 | 4.5% |
| 38 | A/B Testing | Practices | 37 | 4.4% |
| 39 | Prompt Engineering | LLM & GenAI | 37 | 4.4% |
| 40 | Fine-tuning | LLM & GenAI | 33 | 3.9% |

</details>

## Movers

Change in share of postings since 2026-09-14, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Observability | +0.96 | | AI Agents | -0.70 |
| Statistics | +0.34 | | Python | -0.68 |
| Databricks | +0.26 | | SQL | -0.65 |
| TypeScript | +0.24 | | AWS | -0.61 |
| Distributed Systems | +0.19 | | Terraform | -0.48 |
| Spark | +0.16 | | Airflow | -0.42 |
| React | +0.15 | | Java | -0.38 |
| Embeddings | +0.14 | | Kubernetes | -0.36 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,160 | 39.2% |
| swe | 486 | 16.4% |
| other | 458 | 15.5% |
| ops | 257 | 8.7% |
| product | 241 | 8.1% |
| infra | 155 | 5.2% |
| ml-ai | 82 | 2.8% |
| data | 74 | 2.5% |
| research | 46 | 1.6% |

## Disclosed pay, remote engineering roles

542 of 843 engineering postings (64%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $196,185 |
| Median | $228,500 |
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


<sub>Generated 2026-09-21T14:51:07+00:00 · 2 board(s) unreachable this run</sub>
