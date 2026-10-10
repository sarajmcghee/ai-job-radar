# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-10-10** — tracking **2,772 open remote roles** across **91 companies** (829 of them engineering roles). 1,641 postings disclose pay. **39 appeared today.**

<sub>Remote-only: 14,344 postings were collected across all locations and 19.3% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 829 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 371 | 44.8% |
| 2 | Observability | Practices | 271 | 32.7% |
| 3 | Distributed Systems | Practices | 267 | 32.2% |
| 4 | Go | Languages | 252 | 30.4% |
| 5 | Machine Learning | ML Fundamentals | 250 | 30.2% |
| 6 | LLMs | LLM & GenAI | 244 | 29.4% |
| 7 | AI Agents | LLM & GenAI | 226 | 27.3% |
| 8 | AWS | Infra & Cloud | 216 | 26.1% |
| 9 | Kubernetes | Infra & Cloud | 205 | 24.7% |
| 10 | TypeScript | Languages | 173 | 20.9% |
| 11 | Statistics | ML Fundamentals | 156 | 18.8% |
| 12 | SQL | Languages | 141 | 17.0% |
| 13 | CI/CD | Practices | 133 | 16.0% |
| 14 | GCP | Infra & Cloud | 133 | 16.0% |
| 15 | Data Pipelines | Data Engineering | 128 | 15.4% |
| 16 | React | Frameworks & Libraries | 120 | 14.5% |
| 17 | Terraform | Infra & Cloud | 113 | 13.6% |
| 18 | Java | Languages | 102 | 12.3% |
| 19 | Azure | Infra & Cloud | 77 | 9.3% |
| 20 | Snowflake / BigQuery | Data Engineering | 74 | 8.9% |
| 21 | Kafka | Data Engineering | 72 | 8.7% |
| 22 | Airflow | Data Engineering | 70 | 8.4% |
| 23 | Rust | Languages | 66 | 8.0% |
| 24 | Docker | Infra & Cloud | 60 | 7.2% |
| 25 | Spark | Data Engineering | 59 | 7.1% |
| 26 | Evals | LLM & GenAI | 53 | 6.4% |
| 27 | Linux | Infra & Cloud | 51 | 6.2% |
| 28 | AI Safety | LLM & GenAI | 50 | 6.0% |
| 29 | PyTorch | Frameworks & Libraries | 49 | 5.9% |
| 30 | Security | Practices | 48 | 5.8% |
| 31 | dbt | Data Engineering | 43 | 5.2% |
| 32 | MCP | LLM & GenAI | 42 | 5.1% |
| 33 | Recommender Systems | ML Fundamentals | 41 | 4.9% |
| 34 | MLOps | Practices | 40 | 4.8% |
| 35 | Deep Learning | ML Fundamentals | 40 | 4.8% |
| 36 | Databricks | Data Engineering | 39 | 4.7% |
| 37 | Multimodal | LLM & GenAI | 39 | 4.7% |
| 38 | RAG | LLM & GenAI | 35 | 4.2% |
| 39 | A/B Testing | Practices | 32 | 3.9% |
| 40 | GPU Clusters | Infra & Cloud | 32 | 3.9% |

</details>

## Movers

Change in share of postings since 2026-10-03, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Machine Learning | +0.69 | | Java | -0.61 |
| SQL | +0.53 | | RAG | -0.44 |
| TypeScript | +0.47 | | AI Agents | -0.42 |
| Kubernetes | +0.39 | | Data Pipelines | -0.39 |
| Multimodal | +0.39 | | Observability | -0.37 |
| CI/CD | +0.23 | | Spark | -0.31 |
| Snowflake / BigQuery | +0.23 | | Security | -0.29 |
| Docker | +0.22 | | LangChain | -0.28 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,032 | 37.2% |
| swe | 454 | 16.4% |
| other | 422 | 15.2% |
| ops | 264 | 9.5% |
| product | 225 | 8.1% |
| infra | 155 | 5.6% |
| data | 84 | 3.0% |
| ml-ai | 83 | 3.0% |
| research | 53 | 1.9% |

## Disclosed pay, remote engineering roles

561 of 829 engineering postings (68%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $197,050 |
| Median | $227,500 |
| 75th | $260,000 |
| 90th | $287,500 |

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
| Pika | $292,500 |
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


<sub>Generated 2026-10-10T14:13:55+00:00 · 4 board(s) unreachable this run</sub>
