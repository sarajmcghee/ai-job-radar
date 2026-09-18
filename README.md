# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-09-18** — tracking **2,969 open remote roles** across **94 companies** (836 of them engineering roles). 1,688 postings disclose pay. **71 appeared today.**

<sub>Remote-only: 14,174 postings were collected across all locations and 20.9% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 836 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 395 | 47.2% |
| 2 | Observability | Practices | 287 | 34.3% |
| 3 | Distributed Systems | Practices | 264 | 31.6% |
| 4 | Machine Learning | ML Fundamentals | 263 | 31.5% |
| 5 | Go | Languages | 253 | 30.3% |
| 6 | LLMs | LLM & GenAI | 245 | 29.3% |
| 7 | AI Agents | LLM & GenAI | 237 | 28.3% |
| 8 | AWS | Infra & Cloud | 224 | 26.8% |
| 9 | Kubernetes | Infra & Cloud | 215 | 25.7% |
| 10 | TypeScript | Languages | 172 | 20.6% |
| 11 | Statistics | ML Fundamentals | 160 | 19.1% |
| 12 | SQL | Languages | 154 | 18.4% |
| 13 | GCP | Infra & Cloud | 141 | 16.9% |
| 14 | Data Pipelines | Data Engineering | 136 | 16.3% |
| 15 | CI/CD | Practices | 128 | 15.3% |
| 16 | Terraform | Infra & Cloud | 113 | 13.5% |
| 17 | Java | Languages | 107 | 12.8% |
| 18 | React | Frameworks & Libraries | 100 | 12.0% |
| 19 | Azure | Infra & Cloud | 90 | 10.8% |
| 20 | Snowflake / BigQuery | Data Engineering | 80 | 9.6% |
| 21 | Airflow | Data Engineering | 72 | 8.6% |
| 22 | Rust | Languages | 70 | 8.4% |
| 23 | Kafka | Data Engineering | 69 | 8.3% |
| 24 | Evals | LLM & GenAI | 66 | 7.9% |
| 25 | Spark | Data Engineering | 64 | 7.7% |
| 26 | Docker | Infra & Cloud | 62 | 7.4% |
| 27 | Security | Practices | 51 | 6.1% |
| 28 | Linux | Infra & Cloud | 50 | 6.0% |
| 29 | PyTorch | Frameworks & Libraries | 49 | 5.9% |
| 30 | dbt | Data Engineering | 48 | 5.7% |
| 31 | Databricks | Data Engineering | 46 | 5.5% |
| 32 | Deep Learning | ML Fundamentals | 43 | 5.1% |
| 33 | MCP | LLM & GenAI | 42 | 5.0% |
| 34 | RAG | LLM & GenAI | 42 | 5.0% |
| 35 | Prompt Engineering | LLM & GenAI | 40 | 4.8% |
| 36 | MLOps | Practices | 39 | 4.7% |
| 37 | Recommender Systems | ML Fundamentals | 39 | 4.7% |
| 38 | AI Safety | LLM & GenAI | 38 | 4.5% |
| 39 | A/B Testing | Practices | 37 | 4.4% |
| 40 | Fine-tuning | LLM & GenAI | 34 | 4.1% |

</details>

## Movers

Change in share of postings since 2026-09-11, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Observability | +0.15 | | AI Agents | -0.97 |
| TensorFlow | +0.12 | | LLMs | -0.68 |
| Embeddings | +0.10 | | Python | -0.68 |
| Docker | +0.09 | | SQL | -0.55 |
| Security | +0.08 | | Java | -0.52 |
| PyTorch | +0.06 | | Kubernetes | -0.52 |
| NLP | +0.06 | | GCP | -0.50 |
| TypeScript | +0.05 | | AWS | -0.47 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,171 | 39.4% |
| swe | 475 | 16.0% |
| other | 460 | 15.5% |
| ops | 263 | 8.9% |
| product | 239 | 8.0% |
| infra | 155 | 5.2% |
| ml-ai | 84 | 2.8% |
| data | 76 | 2.6% |
| research | 46 | 1.5% |

## Disclosed pay, remote engineering roles

550 of 836 engineering postings (66%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $194,500 |
| Median | $228,500 |
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


<sub>Generated 2026-09-18T12:42:42+00:00 · 3 board(s) unreachable this run</sub>
