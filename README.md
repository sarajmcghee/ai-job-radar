# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-11-03** — tracking **2,896 open remote roles** across **90 companies** (816 of them engineering roles). 1,699 postings disclose pay. **46 appeared today.**

<sub>Remote-only: 14,512 postings were collected across all locations and 20.0% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 816 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 363 | 44.5% |
| 2 | Observability | Practices | 264 | 32.4% |
| 3 | Machine Learning | ML Fundamentals | 246 | 30.1% |
| 4 | Distributed Systems | Practices | 237 | 29.0% |
| 5 | LLMs | LLM & GenAI | 234 | 28.7% |
| 6 | Go | Languages | 227 | 27.8% |
| 7 | AI Agents | LLM & GenAI | 224 | 27.5% |
| 8 | Kubernetes | Infra & Cloud | 211 | 25.9% |
| 9 | AWS | Infra & Cloud | 194 | 23.8% |
| 10 | TypeScript | Languages | 174 | 21.3% |
| 11 | Statistics | ML Fundamentals | 160 | 19.6% |
| 12 | SQL | Languages | 148 | 18.1% |
| 13 | Data Pipelines | Data Engineering | 129 | 15.8% |
| 14 | CI/CD | Practices | 121 | 14.8% |
| 15 | GCP | Infra & Cloud | 118 | 14.5% |
| 16 | Terraform | Infra & Cloud | 116 | 14.2% |
| 17 | React | Frameworks & Libraries | 113 | 13.8% |
| 18 | Java | Languages | 97 | 11.9% |
| 19 | Snowflake / BigQuery | Data Engineering | 77 | 9.4% |
| 20 | Airflow | Data Engineering | 67 | 8.2% |
| 21 | Kafka | Data Engineering | 64 | 7.8% |
| 22 | Rust | Languages | 64 | 7.8% |
| 23 | Azure | Infra & Cloud | 63 | 7.7% |
| 24 | Spark | Data Engineering | 62 | 7.6% |
| 25 | Evals | LLM & GenAI | 55 | 6.7% |
| 26 | Security | Practices | 50 | 6.1% |
| 27 | Docker | Infra & Cloud | 49 | 6.0% |
| 28 | PyTorch | Frameworks & Libraries | 47 | 5.8% |
| 29 | Databricks | Data Engineering | 45 | 5.5% |
| 30 | MCP | LLM & GenAI | 44 | 5.4% |
| 31 | dbt | Data Engineering | 41 | 5.0% |
| 32 | Linux | Infra & Cloud | 40 | 4.9% |
| 33 | Recommender Systems | ML Fundamentals | 38 | 4.7% |
| 34 | MLOps | Practices | 37 | 4.5% |
| 35 | AI Safety | LLM & GenAI | 36 | 4.4% |
| 36 | Deep Learning | ML Fundamentals | 36 | 4.4% |
| 37 | Multimodal | LLM & GenAI | 35 | 4.3% |
| 38 | A/B Testing | Practices | 30 | 3.7% |
| 39 | TensorFlow | Frameworks & Libraries | 30 | 3.7% |
| 40 | Fine-tuning | LLM & GenAI | 28 | 3.4% |

</details>

## Movers

Change in share of postings since 2026-10-27, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Statistics | +0.40 | | Observability | -0.76 |
| Snowflake / BigQuery | +0.23 | | Kubernetes | -0.75 |
| SQL | +0.18 | | LLMs | -0.68 |
| Airflow | +0.17 | | AI Agents | -0.68 |
| Java | +0.16 | | AWS | -0.61 |
| Evals | +0.13 | | Terraform | -0.43 |
| LangChain | +0.10 | | TypeScript | -0.43 |
| Spark | +0.10 | | Go | -0.43 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,139 | 39.3% |
| other | 448 | 15.5% |
| swe | 441 | 15.2% |
| ops | 271 | 9.4% |
| product | 222 | 7.7% |
| infra | 155 | 5.4% |
| ml-ai | 93 | 3.2% |
| data | 74 | 2.6% |
| research | 53 | 1.8% |

## Disclosed pay, remote engineering roles

550 of 816 engineering postings (67%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $195,000 |
| Median | $227,735 |
| 75th | $260,450 |
| 90th | $300,000 |

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


<sub>Generated 2026-11-03T15:49:46+00:00 · 5 board(s) unreachable this run</sub>
