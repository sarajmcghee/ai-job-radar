# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-10-24** — tracking **2,893 open remote roles** across **90 companies** (834 of them engineering roles). 1,679 postings disclose pay. **65 appeared today.**

<sub>Remote-only: 14,461 postings were collected across all locations and 20.0% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 834 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 366 | 43.9% |
| 2 | Observability | Practices | 272 | 32.6% |
| 3 | Go | Languages | 249 | 29.9% |
| 4 | Distributed Systems | Practices | 246 | 29.5% |
| 5 | Machine Learning | ML Fundamentals | 246 | 29.5% |
| 6 | LLMs | LLM & GenAI | 239 | 28.7% |
| 7 | AI Agents | LLM & GenAI | 221 | 26.5% |
| 8 | Kubernetes | Infra & Cloud | 217 | 26.0% |
| 9 | AWS | Infra & Cloud | 213 | 25.5% |
| 10 | TypeScript | Languages | 182 | 21.8% |
| 11 | Statistics | ML Fundamentals | 156 | 18.7% |
| 12 | SQL | Languages | 141 | 16.9% |
| 13 | Data Pipelines | Data Engineering | 124 | 14.9% |
| 14 | GCP | Infra & Cloud | 124 | 14.9% |
| 15 | Terraform | Infra & Cloud | 122 | 14.6% |
| 16 | CI/CD | Practices | 120 | 14.4% |
| 17 | React | Frameworks & Libraries | 115 | 13.8% |
| 18 | Java | Languages | 93 | 11.2% |
| 19 | Snowflake / BigQuery | Data Engineering | 77 | 9.2% |
| 20 | Azure | Infra & Cloud | 72 | 8.6% |
| 21 | Airflow | Data Engineering | 66 | 7.9% |
| 22 | Kafka | Data Engineering | 66 | 7.9% |
| 23 | Rust | Languages | 66 | 7.9% |
| 24 | Spark | Data Engineering | 60 | 7.2% |
| 25 | Security | Practices | 58 | 7.0% |
| 26 | Evals | LLM & GenAI | 55 | 6.6% |
| 27 | PyTorch | Frameworks & Libraries | 52 | 6.2% |
| 28 | AI Safety | LLM & GenAI | 48 | 5.8% |
| 29 | Docker | Infra & Cloud | 48 | 5.8% |
| 30 | dbt | Data Engineering | 47 | 5.6% |
| 31 | MCP | LLM & GenAI | 45 | 5.4% |
| 32 | Databricks | Data Engineering | 43 | 5.2% |
| 33 | Linux | Infra & Cloud | 43 | 5.2% |
| 34 | Recommender Systems | ML Fundamentals | 43 | 5.2% |
| 35 | Deep Learning | ML Fundamentals | 40 | 4.8% |
| 36 | Multimodal | LLM & GenAI | 40 | 4.8% |
| 37 | MLOps | Practices | 36 | 4.3% |
| 38 | A/B Testing | Practices | 33 | 4.0% |
| 39 | Fine-tuning | LLM & GenAI | 33 | 4.0% |
| 40 | TensorFlow | Frameworks & Libraries | 31 | 3.7% |

</details>

## Movers

Change in share of postings since 2026-10-17, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Observability | +0.73 | | Python | -0.92 |
| Security | +0.40 | | SQL | -0.73 |
| Azure | +0.39 | | Machine Learning | -0.49 |
| AI Agents | +0.34 | | Data Pipelines | -0.46 |
| AWS | +0.15 | | Statistics | -0.43 |
| GCP | +0.15 | | Distributed Systems | -0.40 |
| Rust | +0.14 | | Airflow | -0.40 |
| Kubernetes | +0.14 | | dbt | -0.32 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,128 | 39.0% |
| swe | 452 | 15.6% |
| other | 427 | 14.8% |
| ops | 272 | 9.4% |
| product | 232 | 8.0% |
| infra | 161 | 5.6% |
| ml-ai | 93 | 3.2% |
| data | 73 | 2.5% |
| research | 55 | 1.9% |

## Disclosed pay, remote engineering roles

554 of 834 engineering postings (66%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $195,450 |
| Median | $226,200 |
| 75th | $260,050 |
| 90th | $290,000 |

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


<sub>Generated 2026-10-24T12:26:56+00:00 · 4 board(s) unreachable this run</sub>
