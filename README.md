# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-10-29** — tracking **2,884 open remote roles** across **90 companies** (818 of them engineering roles). 1,669 postings disclose pay. **51 appeared today.**

<sub>Remote-only: 14,438 postings were collected across all locations and 20.0% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 818 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 364 | 44.5% |
| 2 | Observability | Practices | 262 | 32.0% |
| 3 | Machine Learning | ML Fundamentals | 244 | 29.8% |
| 4 | Distributed Systems | Practices | 242 | 29.6% |
| 5 | Go | Languages | 241 | 29.5% |
| 6 | LLMs | LLM & GenAI | 237 | 29.0% |
| 7 | AI Agents | LLM & GenAI | 224 | 27.4% |
| 8 | Kubernetes | Infra & Cloud | 216 | 26.4% |
| 9 | AWS | Infra & Cloud | 202 | 24.7% |
| 10 | TypeScript | Languages | 176 | 21.5% |
| 11 | Statistics | ML Fundamentals | 155 | 18.9% |
| 12 | SQL | Languages | 145 | 17.7% |
| 13 | Data Pipelines | Data Engineering | 125 | 15.3% |
| 14 | GCP | Infra & Cloud | 119 | 14.5% |
| 15 | Terraform | Infra & Cloud | 118 | 14.4% |
| 16 | CI/CD | Practices | 117 | 14.3% |
| 17 | React | Frameworks & Libraries | 113 | 13.8% |
| 18 | Java | Languages | 94 | 11.5% |
| 19 | Snowflake / BigQuery | Data Engineering | 78 | 9.5% |
| 20 | Azure | Infra & Cloud | 68 | 8.3% |
| 21 | Airflow | Data Engineering | 65 | 7.9% |
| 22 | Kafka | Data Engineering | 64 | 7.8% |
| 23 | Rust | Languages | 63 | 7.7% |
| 24 | Spark | Data Engineering | 62 | 7.6% |
| 25 | Evals | LLM & GenAI | 56 | 6.8% |
| 26 | Security | Practices | 54 | 6.6% |
| 27 | PyTorch | Frameworks & Libraries | 51 | 6.2% |
| 28 | AI Safety | LLM & GenAI | 45 | 5.5% |
| 29 | Docker | Infra & Cloud | 45 | 5.5% |
| 30 | dbt | Data Engineering | 44 | 5.4% |
| 31 | Recommender Systems | ML Fundamentals | 43 | 5.3% |
| 32 | Databricks | Data Engineering | 42 | 5.1% |
| 33 | Linux | Infra & Cloud | 42 | 5.1% |
| 34 | MCP | LLM & GenAI | 41 | 5.0% |
| 35 | Deep Learning | ML Fundamentals | 40 | 4.9% |
| 36 | Multimodal | LLM & GenAI | 38 | 4.6% |
| 37 | MLOps | Practices | 37 | 4.5% |
| 38 | RAG | LLM & GenAI | 33 | 4.0% |
| 39 | Fine-tuning | LLM & GenAI | 31 | 3.8% |
| 40 | TensorFlow | Frameworks & Libraries | 31 | 3.8% |

</details>

## Movers

Change in share of postings since 2026-10-22, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Snowflake / BigQuery | +0.34 | | Observability | -1.42 |
| Evals | +0.09 | | Distributed Systems | -0.79 |
| Security | +0.09 | | Terraform | -0.70 |
| Vector Databases | +0.06 | | GCP | -0.69 |
| Transformers | +0.03 | | AWS | -0.60 |
| RAG | +0.02 | | Python | -0.60 |
| LangChain | +0.02 | | Kubernetes | -0.55 |
| Linux | +0.01 | | Machine Learning | -0.51 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,128 | 39.1% |
| other | 455 | 15.8% |
| swe | 442 | 15.3% |
| ops | 258 | 8.9% |
| product | 225 | 7.8% |
| infra | 160 | 5.5% |
| ml-ai | 94 | 3.3% |
| data | 71 | 2.5% |
| research | 51 | 1.8% |

## Disclosed pay, remote engineering roles

547 of 818 engineering postings (67%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $195,000 |
| Median | $227,735 |
| 75th | $260,050 |
| 90th | $295,000 |

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


<sub>Generated 2026-10-29T14:56:15+00:00 · 4 board(s) unreachable this run</sub>
