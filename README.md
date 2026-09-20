# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-09-20** — tracking **2,963 open remote roles** across **93 companies** (839 of them engineering roles). 1,677 postings disclose pay. **2 appeared today.**

<sub>Remote-only: 14,198 postings were collected across all locations and 20.9% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 839 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 393 | 46.8% |
| 2 | Observability | Practices | 294 | 35.0% |
| 3 | Distributed Systems | Practices | 270 | 32.2% |
| 4 | Machine Learning | ML Fundamentals | 257 | 30.6% |
| 5 | Go | Languages | 255 | 30.4% |
| 6 | LLMs | LLM & GenAI | 248 | 29.6% |
| 7 | AI Agents | LLM & GenAI | 231 | 27.5% |
| 8 | AWS | Infra & Cloud | 222 | 26.5% |
| 9 | Kubernetes | Infra & Cloud | 217 | 25.9% |
| 10 | TypeScript | Languages | 178 | 21.2% |
| 11 | Statistics | ML Fundamentals | 167 | 19.9% |
| 12 | SQL | Languages | 153 | 18.2% |
| 13 | GCP | Infra & Cloud | 140 | 16.7% |
| 14 | Data Pipelines | Data Engineering | 138 | 16.4% |
| 15 | CI/CD | Practices | 127 | 15.1% |
| 16 | Terraform | Infra & Cloud | 111 | 13.2% |
| 17 | Java | Languages | 107 | 12.8% |
| 18 | React | Frameworks & Libraries | 107 | 12.8% |
| 19 | Azure | Infra & Cloud | 88 | 10.5% |
| 20 | Snowflake / BigQuery | Data Engineering | 81 | 9.7% |
| 21 | Rust | Languages | 73 | 8.7% |
| 22 | Airflow | Data Engineering | 72 | 8.6% |
| 23 | Kafka | Data Engineering | 72 | 8.6% |
| 24 | Spark | Data Engineering | 65 | 7.7% |
| 25 | Evals | LLM & GenAI | 63 | 7.5% |
| 26 | Docker | Infra & Cloud | 60 | 7.2% |
| 27 | Security | Practices | 51 | 6.1% |
| 28 | PyTorch | Frameworks & Libraries | 48 | 5.7% |
| 29 | Linux | Infra & Cloud | 47 | 5.6% |
| 30 | dbt | Data Engineering | 46 | 5.5% |
| 31 | Deep Learning | ML Fundamentals | 45 | 5.4% |
| 32 | Databricks | Data Engineering | 44 | 5.2% |
| 33 | MCP | LLM & GenAI | 42 | 5.0% |
| 34 | RAG | LLM & GenAI | 41 | 4.9% |
| 35 | MLOps | Practices | 40 | 4.8% |
| 36 | AI Safety | LLM & GenAI | 39 | 4.6% |
| 37 | Recommender Systems | ML Fundamentals | 38 | 4.5% |
| 38 | A/B Testing | Practices | 37 | 4.4% |
| 39 | Prompt Engineering | LLM & GenAI | 37 | 4.4% |
| 40 | Fine-tuning | LLM & GenAI | 33 | 3.9% |

</details>

## Movers

Change in share of postings since 2026-09-13, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Observability | +0.68 | | AI Agents | -0.94 |
| Databricks | +0.29 | | SQL | -0.67 |
| Statistics | +0.26 | | Python | -0.52 |
| Spark | +0.17 | | LLMs | -0.45 |
| TypeScript | +0.17 | | AWS | -0.42 |
| Snowflake / BigQuery | +0.13 | | Kubernetes | -0.38 |
| Embeddings | +0.12 | | Terraform | -0.38 |
| Scala | +0.12 | | Data Pipelines | -0.37 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,168 | 39.4% |
| swe | 482 | 16.3% |
| other | 457 | 15.4% |
| ops | 260 | 8.8% |
| product | 239 | 8.1% |
| infra | 155 | 5.2% |
| ml-ai | 82 | 2.8% |
| data | 74 | 2.5% |
| research | 46 | 1.6% |

## Disclosed pay, remote engineering roles

545 of 839 engineering postings (65%) publish a salary range. Figures are the midpoint of the posted band.

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


<sub>Generated 2026-09-20T12:52:41+00:00 · 2 board(s) unreachable this run</sub>
