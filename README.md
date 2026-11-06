# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-11-06** — tracking **2,875 open remote roles** across **88 companies** (807 of them engineering roles). 1,695 postings disclose pay. **141 appeared today.**

<sub>Remote-only: 14,569 postings were collected across all locations and 19.7% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 807 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 357 | 44.2% |
| 2 | Observability | Practices | 274 | 34.0% |
| 3 | LLMs | LLM & GenAI | 235 | 29.1% |
| 4 | Machine Learning | ML Fundamentals | 235 | 29.1% |
| 5 | Distributed Systems | Practices | 233 | 28.9% |
| 6 | AI Agents | LLM & GenAI | 228 | 28.3% |
| 7 | Go | Languages | 222 | 27.5% |
| 8 | Kubernetes | Infra & Cloud | 204 | 25.3% |
| 9 | AWS | Infra & Cloud | 187 | 23.2% |
| 10 | TypeScript | Languages | 175 | 21.7% |
| 11 | Statistics | ML Fundamentals | 152 | 18.8% |
| 12 | SQL | Languages | 143 | 17.7% |
| 13 | Data Pipelines | Data Engineering | 121 | 15.0% |
| 14 | CI/CD | Practices | 119 | 14.7% |
| 15 | GCP | Infra & Cloud | 116 | 14.4% |
| 16 | React | Frameworks & Libraries | 113 | 14.0% |
| 17 | Terraform | Infra & Cloud | 109 | 13.5% |
| 18 | Java | Languages | 96 | 11.9% |
| 19 | Snowflake / BigQuery | Data Engineering | 72 | 8.9% |
| 20 | Airflow | Data Engineering | 66 | 8.2% |
| 21 | Rust | Languages | 65 | 8.1% |
| 22 | Azure | Infra & Cloud | 61 | 7.6% |
| 23 | Kafka | Data Engineering | 59 | 7.3% |
| 24 | Spark | Data Engineering | 57 | 7.1% |
| 25 | Evals | LLM & GenAI | 57 | 7.1% |
| 26 | Security | Practices | 52 | 6.4% |
| 27 | MCP | LLM & GenAI | 49 | 6.1% |
| 28 | Linux | Infra & Cloud | 46 | 5.7% |
| 29 | Docker | Infra & Cloud | 45 | 5.6% |
| 30 | Databricks | Data Engineering | 43 | 5.3% |
| 31 | PyTorch | Frameworks & Libraries | 42 | 5.2% |
| 32 | dbt | Data Engineering | 41 | 5.1% |
| 33 | MLOps | Practices | 39 | 4.8% |
| 34 | AI Safety | LLM & GenAI | 35 | 4.3% |
| 35 | Recommender Systems | ML Fundamentals | 34 | 4.2% |
| 36 | Multimodal | LLM & GenAI | 33 | 4.1% |
| 37 | Deep Learning | ML Fundamentals | 33 | 4.1% |
| 38 | RAG | LLM & GenAI | 31 | 3.8% |
| 39 | Prompt Engineering | LLM & GenAI | 28 | 3.5% |
| 40 | A/B Testing | Practices | 27 | 3.3% |

</details>

## Movers

Change in share of postings since 2026-10-30, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Observability | +0.58 | | Machine Learning | -0.60 |
| MCP | +0.36 | | Go | -0.47 |
| Evals | +0.25 | | Terraform | -0.41 |
| Databricks | +0.15 | | AWS | -0.40 |
| dbt | +0.14 | | Kubernetes | -0.36 |
| Python | +0.13 | | PyTorch | -0.35 |
| MLOps | +0.08 | | Recommender Systems | -0.31 |
| TypeScript | +0.08 | | Kafka | -0.31 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,149 | 40.0% |
| swe | 436 | 15.2% |
| other | 419 | 14.6% |
| ops | 272 | 9.5% |
| product | 228 | 7.9% |
| infra | 158 | 5.5% |
| ml-ai | 88 | 3.1% |
| data | 73 | 2.5% |
| research | 52 | 1.8% |

## Disclosed pay, remote engineering roles

540 of 807 engineering postings (67%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $195,000 |
| Median | $228,500 |
| 75th | $260,450 |
| 90th | $299,500 |

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
| Cohere | $302,500 |

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


<sub>Generated 2026-11-06T15:40:35+00:00 · 5 board(s) unreachable this run</sub>
