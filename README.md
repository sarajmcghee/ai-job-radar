# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-08-31** — tracking **3,203 open remote roles** across **94 companies** (945 of them engineering roles). 1,750 postings disclose pay. **11 appeared today.**

<sub>Remote-only: 14,216 postings were collected across all locations and 22.5% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 945 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 455 | 48.1% |
| 2 | Distributed Systems | Practices | 337 | 35.7% |
| 3 | Observability | Practices | 323 | 34.2% |
| 4 | Go | Languages | 292 | 30.9% |
| 5 | Machine Learning | ML Fundamentals | 286 | 30.3% |
| 6 | Kubernetes | Infra & Cloud | 276 | 29.2% |
| 7 | AWS | Infra & Cloud | 275 | 29.1% |
| 8 | AI Agents | LLM & GenAI | 269 | 28.5% |
| 9 | LLMs | LLM & GenAI | 266 | 28.1% |
| 10 | TypeScript | Languages | 212 | 22.4% |
| 11 | GCP | Infra & Cloud | 202 | 21.4% |
| 12 | SQL | Languages | 187 | 19.8% |
| 13 | Statistics | ML Fundamentals | 175 | 18.5% |
| 14 | Azure | Infra & Cloud | 158 | 16.7% |
| 15 | Terraform | Infra & Cloud | 150 | 15.9% |
| 16 | Data Pipelines | Data Engineering | 150 | 15.9% |
| 17 | Java | Languages | 144 | 15.2% |
| 18 | CI/CD | Practices | 141 | 14.9% |
| 19 | React | Frameworks & Libraries | 116 | 12.3% |
| 20 | Kafka | Data Engineering | 96 | 10.2% |
| 21 | Airflow | Data Engineering | 90 | 9.5% |
| 22 | Spark | Data Engineering | 89 | 9.4% |
| 23 | Snowflake / BigQuery | Data Engineering | 83 | 8.8% |
| 24 | Docker | Infra & Cloud | 80 | 8.5% |
| 25 | Evals | LLM & GenAI | 77 | 8.1% |
| 26 | Rust | Languages | 76 | 8.0% |
| 27 | Linux | Infra & Cloud | 66 | 7.0% |
| 28 | Security | Practices | 61 | 6.5% |
| 29 | PyTorch | Frameworks & Libraries | 56 | 5.9% |
| 30 | RAG | LLM & GenAI | 53 | 5.6% |
| 31 | Databricks | Data Engineering | 51 | 5.4% |
| 32 | dbt | Data Engineering | 50 | 5.3% |
| 33 | MLOps | Practices | 49 | 5.2% |
| 34 | MCP | LLM & GenAI | 46 | 4.9% |
| 35 | Prompt Engineering | LLM & GenAI | 46 | 4.9% |
| 36 | Recommender Systems | ML Fundamentals | 44 | 4.7% |
| 37 | A/B Testing | Practices | 43 | 4.6% |
| 38 | Deep Learning | ML Fundamentals | 43 | 4.6% |
| 39 | AI Safety | LLM & GenAI | 42 | 4.4% |
| 40 | Embeddings | LLM & GenAI | 39 | 4.1% |

</details>

## Movers

Change in share of postings since 2026-08-27, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| SQL | +0.27 | | Airflow | -1.07 |
| Machine Learning | +0.23 | | Distributed Systems | -1.03 |
| AI Agents | +0.20 | | Go | -0.77 |
| Snowflake / BigQuery | +0.20 | | TypeScript | -0.71 |
| Evals | +0.19 | | Observability | -0.66 |
| LLMs | +0.17 | | Java | -0.58 |
| Databricks | +0.14 | | Statistics | -0.36 |
| AI Safety | +0.11 | | GCP | -0.34 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,221 | 38.1% |
| swe | 550 | 17.2% |
| other | 517 | 16.1% |
| ops | 279 | 8.7% |
| product | 241 | 7.5% |
| infra | 178 | 5.6% |
| ml-ai | 99 | 3.1% |
| data | 75 | 2.3% |
| research | 43 | 1.3% |

## Disclosed pay, remote engineering roles

572 of 945 engineering postings (61%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $187,450 |
| Median | $226,200 |
| 75th | $260,000 |
| 90th | $289,530 |

<details><summary>Highest disclosed engineering bands by company</summary>

| Company | Top posted midpoint |
|---|---:|
| Anthropic | $675,000 |
| OpenAI | $418,500 |
| Pinterest | $371,087 |
| Reddit | $351,000 |
| Vanta | $349,500 |
| Databricks | $343,425 |
| Agility Robotics | $329,500 |
| Mercury | $325,900 |
| Snorkel AI | $316,000 |
| Hightouch | $310,000 |

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


<sub>Generated 2026-08-31T15:50:35+00:00 · 1 board(s) unreachable this run</sub>
