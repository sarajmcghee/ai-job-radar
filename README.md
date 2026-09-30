# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-09-30** — tracking **2,860 open remote roles** across **92 companies** (825 of them engineering roles). 1,643 postings disclose pay. **61 appeared today.**

<sub>Remote-only: 14,190 postings were collected across all locations and 20.2% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 825 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 375 | 45.5% |
| 2 | Observability | Practices | 282 | 34.2% |
| 3 | Distributed Systems | Practices | 266 | 32.2% |
| 4 | Machine Learning | ML Fundamentals | 254 | 30.8% |
| 5 | Go | Languages | 246 | 29.8% |
| 6 | LLMs | LLM & GenAI | 236 | 28.6% |
| 7 | AI Agents | LLM & GenAI | 229 | 27.8% |
| 8 | AWS | Infra & Cloud | 228 | 27.6% |
| 9 | Kubernetes | Infra & Cloud | 211 | 25.6% |
| 10 | TypeScript | Languages | 165 | 20.0% |
| 11 | Statistics | ML Fundamentals | 150 | 18.2% |
| 12 | SQL | Languages | 147 | 17.8% |
| 13 | GCP | Infra & Cloud | 146 | 17.7% |
| 14 | Data Pipelines | Data Engineering | 143 | 17.3% |
| 15 | CI/CD | Practices | 128 | 15.5% |
| 16 | Terraform | Infra & Cloud | 111 | 13.5% |
| 17 | React | Frameworks & Libraries | 111 | 13.5% |
| 18 | Java | Languages | 103 | 12.5% |
| 19 | Azure | Infra & Cloud | 92 | 11.2% |
| 20 | Kafka | Data Engineering | 75 | 9.1% |
| 21 | Snowflake / BigQuery | Data Engineering | 73 | 8.8% |
| 22 | Airflow | Data Engineering | 71 | 8.6% |
| 23 | Spark | Data Engineering | 65 | 7.9% |
| 24 | Rust | Languages | 58 | 7.0% |
| 25 | Security | Practices | 54 | 6.5% |
| 26 | Docker | Infra & Cloud | 54 | 6.5% |
| 27 | Linux | Infra & Cloud | 50 | 6.1% |
| 28 | Evals | LLM & GenAI | 49 | 5.9% |
| 29 | PyTorch | Frameworks & Libraries | 45 | 5.5% |
| 30 | AI Safety | LLM & GenAI | 44 | 5.3% |
| 31 | Databricks | Data Engineering | 42 | 5.1% |
| 32 | MCP | LLM & GenAI | 41 | 5.0% |
| 33 | MLOps | Practices | 41 | 5.0% |
| 34 | dbt | Data Engineering | 41 | 5.0% |
| 35 | Deep Learning | ML Fundamentals | 39 | 4.7% |
| 36 | Recommender Systems | ML Fundamentals | 38 | 4.6% |
| 37 | RAG | LLM & GenAI | 37 | 4.5% |
| 38 | A/B Testing | Practices | 32 | 3.9% |
| 39 | Fine-tuning | LLM & GenAI | 32 | 3.9% |
| 40 | TensorFlow | Frameworks & Libraries | 31 | 3.8% |

</details>

## Movers

Change in share of postings since 2026-09-23, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Machine Learning | +0.55 | | Observability | -0.71 |
| AWS | +0.42 | | Rust | -0.68 |
| GCP | +0.32 | | LLMs | -0.56 |
| AI Safety | +0.29 | | Statistics | -0.53 |
| Speech / Audio | +0.29 | | Go | -0.45 |
| Azure | +0.21 | | Evals | -0.40 |
| Linux | +0.17 | | dbt | -0.37 |
| Transformers | +0.16 | | Snowflake / BigQuery | -0.36 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,094 | 38.3% |
| other | 464 | 16.2% |
| swe | 463 | 16.2% |
| ops | 257 | 9.0% |
| product | 220 | 7.7% |
| infra | 154 | 5.4% |
| ml-ai | 81 | 2.8% |
| data | 78 | 2.7% |
| research | 49 | 1.7% |

## Disclosed pay, remote engineering roles

552 of 825 engineering postings (67%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $195,450 |
| Median | $227,735 |
| 75th | $260,050 |
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
| GitLab | $301,800 |

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


<sub>Generated 2026-09-30T14:35:38+00:00 · 3 board(s) unreachable this run</sub>
