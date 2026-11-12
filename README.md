# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-11-12** — tracking **2,921 open remote roles** across **86 companies** (821 of them engineering roles). 1,728 postings disclose pay. **42 appeared today.**

<sub>Remote-only: 14,666 postings were collected across all locations and 19.9% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 821 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 360 | 43.8% |
| 2 | Observability | Practices | 283 | 34.5% |
| 3 | LLMs | LLM & GenAI | 247 | 30.1% |
| 4 | Distributed Systems | Practices | 243 | 29.6% |
| 5 | AI Agents | LLM & GenAI | 240 | 29.2% |
| 6 | Go | Languages | 240 | 29.2% |
| 7 | Machine Learning | ML Fundamentals | 234 | 28.5% |
| 8 | Kubernetes | Infra & Cloud | 217 | 26.4% |
| 9 | AWS | Infra & Cloud | 194 | 23.6% |
| 10 | TypeScript | Languages | 185 | 22.5% |
| 11 | Statistics | ML Fundamentals | 153 | 18.6% |
| 12 | SQL | Languages | 147 | 17.9% |
| 13 | CI/CD | Practices | 132 | 16.1% |
| 14 | Data Pipelines | Data Engineering | 126 | 15.3% |
| 15 | React | Frameworks & Libraries | 123 | 15.0% |
| 16 | GCP | Infra & Cloud | 119 | 14.5% |
| 17 | Terraform | Infra & Cloud | 111 | 13.5% |
| 18 | Java | Languages | 95 | 11.6% |
| 19 | Snowflake / BigQuery | Data Engineering | 81 | 9.9% |
| 20 | Airflow | Data Engineering | 68 | 8.3% |
| 21 | Rust | Languages | 66 | 8.0% |
| 22 | Evals | LLM & GenAI | 63 | 7.7% |
| 23 | Azure | Infra & Cloud | 62 | 7.6% |
| 24 | Kafka | Data Engineering | 59 | 7.2% |
| 25 | Spark | Data Engineering | 57 | 6.9% |
| 26 | Security | Practices | 55 | 6.7% |
| 27 | MCP | LLM & GenAI | 53 | 6.5% |
| 28 | Databricks | Data Engineering | 48 | 5.8% |
| 29 | Docker | Infra & Cloud | 47 | 5.7% |
| 30 | Linux | Infra & Cloud | 45 | 5.5% |
| 31 | dbt | Data Engineering | 43 | 5.2% |
| 32 | MLOps | Practices | 38 | 4.6% |
| 33 | PyTorch | Frameworks & Libraries | 38 | 4.6% |
| 34 | AI Safety | LLM & GenAI | 37 | 4.5% |
| 35 | Prompt Engineering | LLM & GenAI | 36 | 4.4% |
| 36 | Recommender Systems | ML Fundamentals | 34 | 4.1% |
| 37 | A/B Testing | Practices | 33 | 4.0% |
| 38 | RAG | LLM & GenAI | 32 | 3.9% |
| 39 | Deep Learning | ML Fundamentals | 31 | 3.8% |
| 40 | Multimodal | LLM & GenAI | 28 | 3.4% |

</details>

## Movers

Change in share of postings since 2026-11-04, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Observability | +0.99 | | Machine Learning | -0.61 |
| CI/CD | +0.58 | | Python | -0.56 |
| Evals | +0.25 | | PyTorch | -0.40 |
| A/B Testing | +0.25 | | TensorFlow | -0.29 |
| Prompt Engineering | +0.25 | | Java | -0.26 |
| Distributed Systems | +0.23 | | Multimodal | -0.26 |
| Go | +0.21 | | Computer Vision | -0.26 |
| MCP | +0.20 | | Embeddings | -0.26 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,171 | 40.1% |
| swe | 456 | 15.6% |
| other | 420 | 14.4% |
| ops | 271 | 9.3% |
| product | 238 | 8.1% |
| infra | 160 | 5.5% |
| ml-ai | 87 | 3.0% |
| data | 69 | 2.4% |
| research | 49 | 1.7% |

## Disclosed pay, remote engineering roles

550 of 821 engineering postings (67%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $196,000 |
| Median | $228,500 |
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


<sub>Generated 2026-11-12T16:34:17+00:00 · 5 board(s) unreachable this run</sub>
