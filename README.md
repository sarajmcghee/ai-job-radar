# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-11-23** — tracking **2,886 open remote roles** across **86 companies** (797 of them engineering roles). 1,706 postings disclose pay. **22 appeared today.**

<sub>Remote-only: 14,682 postings were collected across all locations and 19.7% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 797 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 358 | 44.9% |
| 2 | Observability | Practices | 271 | 34.0% |
| 3 | LLMs | LLM & GenAI | 238 | 29.9% |
| 4 | AI Agents | LLM & GenAI | 237 | 29.7% |
| 5 | Distributed Systems | Practices | 230 | 28.9% |
| 6 | Machine Learning | ML Fundamentals | 225 | 28.2% |
| 7 | Go | Languages | 223 | 28.0% |
| 8 | Kubernetes | Infra & Cloud | 216 | 27.1% |
| 9 | AWS | Infra & Cloud | 200 | 25.1% |
| 10 | TypeScript | Languages | 186 | 23.3% |
| 11 | Statistics | ML Fundamentals | 148 | 18.6% |
| 12 | CI/CD | Practices | 132 | 16.6% |
| 13 | SQL | Languages | 129 | 16.2% |
| 14 | GCP | Infra & Cloud | 125 | 15.7% |
| 15 | React | Frameworks & Libraries | 116 | 14.6% |
| 16 | Terraform | Infra & Cloud | 115 | 14.4% |
| 17 | Data Pipelines | Data Engineering | 103 | 12.9% |
| 18 | Java | Languages | 93 | 11.7% |
| 19 | Azure | Infra & Cloud | 66 | 8.3% |
| 20 | Snowflake / BigQuery | Data Engineering | 66 | 8.3% |
| 21 | Security | Practices | 64 | 8.0% |
| 22 | Airflow | Data Engineering | 64 | 8.0% |
| 23 | Evals | LLM & GenAI | 63 | 7.9% |
| 24 | Rust | Languages | 61 | 7.7% |
| 25 | Spark | Data Engineering | 59 | 7.4% |
| 26 | Kafka | Data Engineering | 57 | 7.2% |
| 27 | MCP | LLM & GenAI | 52 | 6.5% |
| 28 | Docker | Infra & Cloud | 46 | 5.8% |
| 29 | Linux | Infra & Cloud | 43 | 5.4% |
| 30 | PyTorch | Frameworks & Libraries | 42 | 5.3% |
| 31 | AI Safety | LLM & GenAI | 40 | 5.0% |
| 32 | Recommender Systems | ML Fundamentals | 38 | 4.8% |
| 33 | Databricks | Data Engineering | 35 | 4.4% |
| 34 | GPU Clusters | Infra & Cloud | 33 | 4.1% |
| 35 | MLOps | Practices | 32 | 4.0% |
| 36 | Deep Learning | ML Fundamentals | 32 | 4.0% |
| 37 | Multimodal | LLM & GenAI | 31 | 3.9% |
| 38 | dbt | Data Engineering | 31 | 3.9% |
| 39 | RAG | LLM & GenAI | 29 | 3.6% |
| 40 | Prompt Engineering | LLM & GenAI | 28 | 3.5% |

</details>

## Movers

Change in share of postings since 2026-11-16, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Observability | +0.41 | | Data Pipelines | -0.61 |
| Terraform | +0.34 | | dbt | -0.52 |
| Embeddings | +0.23 | | Databricks | -0.49 |
| Azure | +0.17 | | Statistics | -0.39 |
| AWS | +0.16 | | Snowflake / BigQuery | -0.34 |
| Multimodal | +0.15 | | Prompt Engineering | -0.26 |
| GPU Clusters | +0.15 | | Go | -0.24 |
| TypeScript | +0.14 | | Computer Vision | -0.20 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,184 | 41.0% |
| swe | 426 | 14.8% |
| other | 421 | 14.6% |
| ops | 269 | 9.3% |
| product | 215 | 7.4% |
| infra | 172 | 6.0% |
| ml-ai | 79 | 2.7% |
| data | 67 | 2.3% |
| research | 53 | 1.8% |

## Disclosed pay, remote engineering roles

540 of 797 engineering postings (68%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $197,095 |
| Median | $228,950 |
| 75th | $260,450 |
| 90th | $305,000 |

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
| Discord | $310,000 |
| Plaid | $308,520 |

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


<sub>Generated 2026-11-23T19:48:26+00:00 · 5 board(s) unreachable this run</sub>
