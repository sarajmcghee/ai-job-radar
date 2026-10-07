# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-10-07** — tracking **2,793 open remote roles** across **90 companies** (825 of them engineering roles). 1,626 postings disclose pay. **68 appeared today.**

<sub>Remote-only: 14,291 postings were collected across all locations and 19.5% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 825 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 370 | 44.8% |
| 2 | Observability | Practices | 286 | 34.7% |
| 3 | Distributed Systems | Practices | 270 | 32.7% |
| 4 | Machine Learning | ML Fundamentals | 247 | 29.9% |
| 5 | Go | Languages | 246 | 29.8% |
| 6 | LLMs | LLM & GenAI | 239 | 29.0% |
| 7 | AI Agents | LLM & GenAI | 216 | 26.2% |
| 8 | AWS | Infra & Cloud | 213 | 25.8% |
| 9 | Kubernetes | Infra & Cloud | 198 | 24.0% |
| 10 | TypeScript | Languages | 173 | 21.0% |
| 11 | Statistics | ML Fundamentals | 164 | 19.9% |
| 12 | SQL | Languages | 147 | 17.8% |
| 13 | Data Pipelines | Data Engineering | 132 | 16.0% |
| 14 | GCP | Infra & Cloud | 131 | 15.9% |
| 15 | React | Frameworks & Libraries | 129 | 15.6% |
| 16 | CI/CD | Practices | 125 | 15.2% |
| 17 | Terraform | Infra & Cloud | 115 | 13.9% |
| 18 | Java | Languages | 110 | 13.3% |
| 19 | Azure | Infra & Cloud | 83 | 10.1% |
| 20 | Airflow | Data Engineering | 75 | 9.1% |
| 21 | Snowflake / BigQuery | Data Engineering | 74 | 9.0% |
| 22 | Kafka | Data Engineering | 73 | 8.8% |
| 23 | Spark | Data Engineering | 61 | 7.4% |
| 24 | Rust | Languages | 60 | 7.3% |
| 25 | Docker | Infra & Cloud | 52 | 6.3% |
| 26 | Linux | Infra & Cloud | 51 | 6.2% |
| 27 | Security | Practices | 48 | 5.8% |
| 28 | AI Safety | LLM & GenAI | 47 | 5.7% |
| 29 | PyTorch | Frameworks & Libraries | 46 | 5.6% |
| 30 | dbt | Data Engineering | 45 | 5.5% |
| 31 | Evals | LLM & GenAI | 43 | 5.2% |
| 32 | Recommender Systems | ML Fundamentals | 40 | 4.8% |
| 33 | MLOps | Practices | 39 | 4.7% |
| 34 | Deep Learning | ML Fundamentals | 39 | 4.7% |
| 35 | MCP | LLM & GenAI | 38 | 4.6% |
| 36 | Databricks | Data Engineering | 37 | 4.5% |
| 37 | RAG | LLM & GenAI | 36 | 4.4% |
| 38 | Multimodal | LLM & GenAI | 34 | 4.1% |
| 39 | A/B Testing | Practices | 32 | 3.9% |
| 40 | Prompt Engineering | LLM & GenAI | 32 | 3.9% |

</details>

## Movers

Change in share of postings since 2026-09-30, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| React | +0.75 | | AI Agents | -1.35 |
| SQL | +0.63 | | Data Pipelines | -0.45 |
| Observability | +0.54 | | Evals | -0.39 |
| Terraform | +0.45 | | Security | -0.28 |
| Distributed Systems | +0.22 | | Kubernetes | -0.26 |
| Java | +0.22 | | GCP | -0.20 |
| AI Safety | +0.22 | | Python | -0.19 |
| TypeScript | +0.21 | | RAG | -0.15 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,037 | 37.1% |
| swe | 461 | 16.5% |
| other | 438 | 15.7% |
| ops | 266 | 9.5% |
| product | 227 | 8.1% |
| infra | 147 | 5.3% |
| data | 87 | 3.1% |
| ml-ai | 81 | 2.9% |
| research | 49 | 1.8% |

## Disclosed pay, remote engineering roles

550 of 825 engineering postings (67%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $196,500 |
| Median | $227,735 |
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


<sub>Generated 2026-10-07T15:03:34+00:00 · 4 board(s) unreachable this run</sub>
