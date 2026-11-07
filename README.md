# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-11-07** — tracking **2,910 open remote roles** across **88 companies** (812 of them engineering roles). 1,720 postings disclose pay. **90 appeared today.**

<sub>Remote-only: 14,630 postings were collected across all locations and 19.9% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 812 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 359 | 44.2% |
| 2 | Observability | Practices | 274 | 33.7% |
| 3 | LLMs | LLM & GenAI | 241 | 29.7% |
| 4 | Machine Learning | ML Fundamentals | 237 | 29.2% |
| 5 | Distributed Systems | Practices | 236 | 29.1% |
| 6 | AI Agents | LLM & GenAI | 234 | 28.8% |
| 7 | Go | Languages | 227 | 28.0% |
| 8 | Kubernetes | Infra & Cloud | 207 | 25.5% |
| 9 | AWS | Infra & Cloud | 189 | 23.3% |
| 10 | TypeScript | Languages | 180 | 22.2% |
| 11 | Statistics | ML Fundamentals | 153 | 18.8% |
| 12 | SQL | Languages | 144 | 17.7% |
| 13 | Data Pipelines | Data Engineering | 124 | 15.3% |
| 14 | CI/CD | Practices | 121 | 14.9% |
| 15 | React | Frameworks & Libraries | 117 | 14.4% |
| 16 | GCP | Infra & Cloud | 116 | 14.3% |
| 17 | Terraform | Infra & Cloud | 110 | 13.5% |
| 18 | Java | Languages | 96 | 11.8% |
| 19 | Snowflake / BigQuery | Data Engineering | 72 | 8.9% |
| 20 | Airflow | Data Engineering | 67 | 8.3% |
| 21 | Rust | Languages | 63 | 7.8% |
| 22 | Azure | Infra & Cloud | 62 | 7.6% |
| 23 | Kafka | Data Engineering | 60 | 7.4% |
| 24 | Evals | LLM & GenAI | 60 | 7.4% |
| 25 | Spark | Data Engineering | 58 | 7.1% |
| 26 | Security | Practices | 52 | 6.4% |
| 27 | MCP | LLM & GenAI | 49 | 6.0% |
| 28 | Linux | Infra & Cloud | 47 | 5.8% |
| 29 | Docker | Infra & Cloud | 45 | 5.5% |
| 30 | Databricks | Data Engineering | 44 | 5.4% |
| 31 | PyTorch | Frameworks & Libraries | 43 | 5.3% |
| 32 | dbt | Data Engineering | 40 | 4.9% |
| 33 | MLOps | Practices | 39 | 4.8% |
| 34 | Recommender Systems | ML Fundamentals | 35 | 4.3% |
| 35 | AI Safety | LLM & GenAI | 34 | 4.2% |
| 36 | Multimodal | LLM & GenAI | 33 | 4.1% |
| 37 | Deep Learning | ML Fundamentals | 33 | 4.1% |
| 38 | Prompt Engineering | LLM & GenAI | 31 | 3.8% |
| 39 | RAG | LLM & GenAI | 31 | 3.8% |
| 40 | A/B Testing | Practices | 28 | 3.4% |

</details>

## Movers

Change in share of postings since 2026-10-31, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Observability | +0.37 | | Machine Learning | -0.76 |
| Linux | +0.31 | | AWS | -0.40 |
| MCP | +0.25 | | Terraform | -0.39 |
| TypeScript | +0.23 | | Go | -0.39 |
| Prompt Engineering | +0.19 | | Snowflake / BigQuery | -0.33 |
| Evals | +0.18 | | Kubernetes | -0.30 |
| Azure | +0.14 | | Kafka | -0.27 |
| dbt | +0.12 | | PyTorch | -0.25 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,168 | 40.1% |
| swe | 445 | 15.3% |
| other | 415 | 14.3% |
| ops | 283 | 9.7% |
| product | 232 | 8.0% |
| infra | 157 | 5.4% |
| ml-ai | 89 | 3.1% |
| data | 72 | 2.5% |
| research | 49 | 1.7% |

## Disclosed pay, remote engineering roles

541 of 812 engineering postings (67%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $195,000 |
| Median | $227,735 |
| 75th | $260,450 |
| 90th | $292,500 |

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


<sub>Generated 2026-11-07T14:41:03+00:00 · 5 board(s) unreachable this run</sub>
