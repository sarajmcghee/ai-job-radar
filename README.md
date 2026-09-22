# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-09-22** — tracking **2,930 open remote roles** across **92 companies** (839 of them engineering roles). 1,653 postings disclose pay. **41 appeared today.**

<sub>Remote-only: 14,199 postings were collected across all locations and 20.6% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 839 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 387 | 46.1% |
| 2 | Observability | Practices | 305 | 36.4% |
| 3 | Distributed Systems | Practices | 279 | 33.3% |
| 4 | Go | Languages | 261 | 31.1% |
| 5 | Machine Learning | ML Fundamentals | 251 | 29.9% |
| 6 | LLMs | LLM & GenAI | 248 | 29.6% |
| 7 | AI Agents | LLM & GenAI | 234 | 27.9% |
| 8 | AWS | Infra & Cloud | 227 | 27.1% |
| 9 | Kubernetes | Infra & Cloud | 220 | 26.2% |
| 10 | TypeScript | Languages | 176 | 21.0% |
| 11 | Statistics | ML Fundamentals | 165 | 19.7% |
| 12 | SQL | Languages | 150 | 17.9% |
| 13 | GCP | Infra & Cloud | 144 | 17.2% |
| 14 | Data Pipelines | Data Engineering | 142 | 16.9% |
| 15 | CI/CD | Practices | 127 | 15.1% |
| 16 | Terraform | Infra & Cloud | 110 | 13.1% |
| 17 | React | Frameworks & Libraries | 106 | 12.6% |
| 18 | Java | Languages | 105 | 12.5% |
| 19 | Azure | Infra & Cloud | 93 | 11.1% |
| 20 | Snowflake / BigQuery | Data Engineering | 78 | 9.3% |
| 21 | Rust | Languages | 77 | 9.2% |
| 22 | Kafka | Data Engineering | 72 | 8.6% |
| 23 | Airflow | Data Engineering | 70 | 8.3% |
| 24 | Spark | Data Engineering | 63 | 7.5% |
| 25 | Evals | LLM & GenAI | 62 | 7.4% |
| 26 | Docker | Infra & Cloud | 57 | 6.8% |
| 27 | Security | Practices | 52 | 6.2% |
| 28 | Linux | Infra & Cloud | 48 | 5.7% |
| 29 | MCP | LLM & GenAI | 47 | 5.6% |
| 30 | PyTorch | Frameworks & Libraries | 47 | 5.6% |
| 31 | Deep Learning | ML Fundamentals | 44 | 5.2% |
| 32 | dbt | Data Engineering | 44 | 5.2% |
| 33 | Databricks | Data Engineering | 42 | 5.0% |
| 34 | RAG | LLM & GenAI | 41 | 4.9% |
| 35 | AI Safety | LLM & GenAI | 40 | 4.8% |
| 36 | Recommender Systems | ML Fundamentals | 39 | 4.6% |
| 37 | MLOps | Practices | 38 | 4.5% |
| 38 | A/B Testing | Practices | 36 | 4.3% |
| 39 | Prompt Engineering | LLM & GenAI | 35 | 4.2% |
| 40 | Embeddings | LLM & GenAI | 33 | 3.9% |

</details>

## Movers

Change in share of postings since 2026-09-15, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Observability | +1.22 | | SQL | -0.69 |
| Distributed Systems | +0.46 | | Python | -0.62 |
| Statistics | +0.43 | | AI Agents | -0.42 |
| Go | +0.28 | | Terraform | -0.37 |
| Azure | +0.27 | | Java | -0.31 |
| Rust | +0.22 | | Airflow | -0.28 |
| Snowflake / BigQuery | +0.19 | | Evals | -0.27 |
| MCP | +0.19 | | Fine-tuning | -0.20 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,144 | 39.0% |
| swe | 484 | 16.5% |
| other | 449 | 15.3% |
| ops | 261 | 8.9% |
| product | 237 | 8.1% |
| infra | 158 | 5.4% |
| ml-ai | 81 | 2.8% |
| data | 70 | 2.4% |
| research | 46 | 1.6% |

## Disclosed pay, remote engineering roles

536 of 839 engineering postings (64%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $195,500 |
| Median | $228,085 |
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


<sub>Generated 2026-09-22T13:05:26+00:00 · 2 board(s) unreachable this run</sub>
