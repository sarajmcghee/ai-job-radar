# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-10-23** — tracking **2,864 open remote roles** across **90 companies** (834 of them engineering roles). 1,669 postings disclose pay. **56 appeared today.**

<sub>Remote-only: 14,435 postings were collected across all locations and 19.8% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 834 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 367 | 44.0% |
| 2 | Observability | Practices | 275 | 33.0% |
| 3 | Distributed Systems | Practices | 251 | 30.1% |
| 4 | Go | Languages | 246 | 29.5% |
| 5 | Machine Learning | ML Fundamentals | 246 | 29.5% |
| 6 | LLMs | LLM & GenAI | 239 | 28.7% |
| 7 | AI Agents | LLM & GenAI | 224 | 26.9% |
| 8 | Kubernetes | Infra & Cloud | 218 | 26.1% |
| 9 | AWS | Infra & Cloud | 212 | 25.4% |
| 10 | TypeScript | Languages | 178 | 21.3% |
| 11 | Statistics | ML Fundamentals | 157 | 18.8% |
| 12 | SQL | Languages | 143 | 17.1% |
| 13 | Data Pipelines | Data Engineering | 129 | 15.5% |
| 14 | Terraform | Infra & Cloud | 124 | 14.9% |
| 15 | GCP | Infra & Cloud | 124 | 14.9% |
| 16 | CI/CD | Practices | 120 | 14.4% |
| 17 | React | Frameworks & Libraries | 114 | 13.7% |
| 18 | Java | Languages | 93 | 11.2% |
| 19 | Snowflake / BigQuery | Data Engineering | 78 | 9.4% |
| 20 | Azure | Infra & Cloud | 71 | 8.5% |
| 21 | Airflow | Data Engineering | 67 | 8.0% |
| 22 | Kafka | Data Engineering | 66 | 7.9% |
| 23 | Rust | Languages | 65 | 7.8% |
| 24 | Spark | Data Engineering | 60 | 7.2% |
| 25 | Security | Practices | 57 | 6.8% |
| 26 | Evals | LLM & GenAI | 56 | 6.7% |
| 27 | PyTorch | Frameworks & Libraries | 51 | 6.1% |
| 28 | dbt | Data Engineering | 50 | 6.0% |
| 29 | AI Safety | LLM & GenAI | 47 | 5.6% |
| 30 | Docker | Infra & Cloud | 47 | 5.6% |
| 31 | Linux | Infra & Cloud | 44 | 5.3% |
| 32 | Recommender Systems | ML Fundamentals | 44 | 5.3% |
| 33 | Databricks | Data Engineering | 43 | 5.2% |
| 34 | MCP | LLM & GenAI | 42 | 5.0% |
| 35 | Deep Learning | ML Fundamentals | 40 | 4.8% |
| 36 | Multimodal | LLM & GenAI | 39 | 4.7% |
| 37 | MLOps | Practices | 37 | 4.4% |
| 38 | Fine-tuning | LLM & GenAI | 33 | 4.0% |
| 39 | A/B Testing | Practices | 32 | 3.8% |
| 40 | GPU Clusters | Infra & Cloud | 32 | 3.8% |

</details>

## Movers

Change in share of postings since 2026-10-16, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Azure | +0.57 | | Python | -1.00 |
| AI Agents | +0.52 | | SQL | -0.84 |
| Security | +0.43 | | Machine Learning | -0.78 |
| AWS | +0.42 | | Statistics | -0.58 |
| Observability | +0.40 | | Data Pipelines | -0.42 |
| GCP | +0.37 | | Airflow | -0.38 |
| Kubernetes | +0.31 | | React | -0.36 |
| Terraform | +0.13 | | Distributed Systems | -0.27 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,109 | 38.7% |
| swe | 452 | 15.8% |
| other | 429 | 15.0% |
| ops | 264 | 9.2% |
| product | 228 | 8.0% |
| infra | 160 | 5.6% |
| ml-ai | 92 | 3.2% |
| data | 76 | 2.7% |
| research | 54 | 1.9% |

## Disclosed pay, remote engineering roles

556 of 834 engineering postings (67%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $197,000 |
| Median | $227,735 |
| 75th | $260,050 |
| 90th | $292,500 |

<details><summary>Highest disclosed engineering bands by company</summary>

| Company | Top posted midpoint |
|---|---:|
| Anthropic | $675,000 |
| OpenAI | $455,500 |
| Pinterest | $371,087 |
| Reddit | $351,000 |
| Agility Robotics | $329,500 |
| Coinbase | $320,142 |
| Snorkel AI | $316,000 |
| GitLab | $314,000 |
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


<sub>Generated 2026-10-23T13:05:17+00:00 · 4 board(s) unreachable this run</sub>
