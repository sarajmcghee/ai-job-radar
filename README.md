# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-10-20** — tracking **2,837 open remote roles** across **89 companies** (837 of them engineering roles). 1,648 postings disclose pay. **60 appeared today.**

<sub>Remote-only: 14,344 postings were collected across all locations and 19.8% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 837 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 372 | 44.4% |
| 2 | Observability | Practices | 281 | 33.6% |
| 3 | LLMs | LLM & GenAI | 254 | 30.3% |
| 4 | Distributed Systems | Practices | 250 | 29.9% |
| 5 | Machine Learning | ML Fundamentals | 249 | 29.7% |
| 6 | Go | Languages | 244 | 29.2% |
| 7 | AI Agents | LLM & GenAI | 235 | 28.1% |
| 8 | Kubernetes | Infra & Cloud | 218 | 26.0% |
| 9 | AWS | Infra & Cloud | 215 | 25.7% |
| 10 | TypeScript | Languages | 184 | 22.0% |
| 11 | Statistics | ML Fundamentals | 162 | 19.4% |
| 12 | SQL | Languages | 145 | 17.3% |
| 13 | Data Pipelines | Data Engineering | 134 | 16.0% |
| 14 | GCP | Infra & Cloud | 129 | 15.4% |
| 15 | CI/CD | Practices | 126 | 15.1% |
| 16 | React | Frameworks & Libraries | 122 | 14.6% |
| 17 | Terraform | Infra & Cloud | 119 | 14.2% |
| 18 | Java | Languages | 95 | 11.4% |
| 19 | Snowflake / BigQuery | Data Engineering | 86 | 10.3% |
| 20 | Azure | Infra & Cloud | 71 | 8.5% |
| 21 | Airflow | Data Engineering | 69 | 8.2% |
| 22 | Spark | Data Engineering | 62 | 7.4% |
| 23 | Kafka | Data Engineering | 60 | 7.2% |
| 24 | Rust | Languages | 57 | 6.8% |
| 25 | Evals | LLM & GenAI | 55 | 6.6% |
| 26 | Security | Practices | 53 | 6.3% |
| 27 | dbt | Data Engineering | 53 | 6.3% |
| 28 | PyTorch | Frameworks & Libraries | 52 | 6.2% |
| 29 | AI Safety | LLM & GenAI | 48 | 5.7% |
| 30 | Databricks | Data Engineering | 47 | 5.6% |
| 31 | Docker | Infra & Cloud | 47 | 5.6% |
| 32 | Linux | Infra & Cloud | 47 | 5.6% |
| 33 | Recommender Systems | ML Fundamentals | 46 | 5.5% |
| 34 | MCP | LLM & GenAI | 44 | 5.3% |
| 35 | Deep Learning | ML Fundamentals | 42 | 5.0% |
| 36 | Multimodal | LLM & GenAI | 39 | 4.7% |
| 37 | MLOps | Practices | 38 | 4.5% |
| 38 | Fine-tuning | LLM & GenAI | 34 | 4.1% |
| 39 | TensorFlow | Frameworks & Libraries | 33 | 3.9% |
| 40 | RAG | LLM & GenAI | 33 | 3.9% |

</details>

## Movers

Change in share of postings since 2026-10-13, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| AI Agents | +0.74 | | Machine Learning | -0.64 |
| Observability | +0.48 | | Statistics | -0.53 |
| Kubernetes | +0.48 | | Python | -0.36 |
| GCP | +0.48 | | Rust | -0.33 |
| AWS | +0.36 | | Docker | -0.28 |
| Azure | +0.35 | | Kafka | -0.27 |
| Snowflake / BigQuery | +0.31 | | Go | -0.20 |
| Data Pipelines | +0.27 | | A/B Testing | -0.19 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,060 | 37.4% |
| swe | 455 | 16.0% |
| other | 435 | 15.3% |
| ops | 265 | 9.3% |
| product | 240 | 8.5% |
| infra | 157 | 5.5% |
| ml-ai | 94 | 3.3% |
| data | 81 | 2.9% |
| research | 50 | 1.8% |

## Disclosed pay, remote engineering roles

562 of 837 engineering postings (67%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $196,285 |
| Median | $227,000 |
| 75th | $260,000 |
| 90th | $289,530 |

<details><summary>Highest disclosed engineering bands by company</summary>

| Company | Top posted midpoint |
|---|---:|
| Anthropic | $675,000 |
| OpenAI | $455,500 |
| Pinterest | $371,087 |
| Reddit | $351,000 |
| Agility Robotics | $329,500 |
| Snorkel AI | $316,000 |
| Discord | $306,000 |
| GitLab | $301,800 |
| Pika | $300,000 |
| Vercel | $290,000 |

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


<sub>Generated 2026-10-20T13:19:01+00:00 · 4 board(s) unreachable this run</sub>
