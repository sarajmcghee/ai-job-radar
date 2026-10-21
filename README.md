# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-10-21** — tracking **2,869 open remote roles** across **90 companies** (844 of them engineering roles). 1,676 postings disclose pay. **73 appeared today.**

<sub>Remote-only: 14,396 postings were collected across all locations and 19.9% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 844 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 375 | 44.4% |
| 2 | Observability | Practices | 292 | 34.6% |
| 3 | Distributed Systems | Practices | 260 | 30.8% |
| 4 | LLMs | LLM & GenAI | 256 | 30.3% |
| 5 | Machine Learning | ML Fundamentals | 251 | 29.7% |
| 6 | Go | Languages | 249 | 29.5% |
| 7 | AI Agents | LLM & GenAI | 238 | 28.2% |
| 8 | AWS | Infra & Cloud | 226 | 26.8% |
| 9 | Kubernetes | Infra & Cloud | 225 | 26.7% |
| 10 | TypeScript | Languages | 183 | 21.7% |
| 11 | Statistics | ML Fundamentals | 160 | 19.0% |
| 12 | SQL | Languages | 146 | 17.3% |
| 13 | Data Pipelines | Data Engineering | 136 | 16.1% |
| 14 | GCP | Infra & Cloud | 135 | 16.0% |
| 15 | CI/CD | Practices | 128 | 15.2% |
| 16 | Terraform | Infra & Cloud | 126 | 14.9% |
| 17 | React | Frameworks & Libraries | 121 | 14.3% |
| 18 | Java | Languages | 94 | 11.1% |
| 19 | Snowflake / BigQuery | Data Engineering | 84 | 10.0% |
| 20 | Azure | Infra & Cloud | 77 | 9.1% |
| 21 | Airflow | Data Engineering | 67 | 7.9% |
| 22 | Kafka | Data Engineering | 66 | 7.8% |
| 23 | Rust | Languages | 63 | 7.5% |
| 24 | Spark | Data Engineering | 62 | 7.3% |
| 25 | Evals | LLM & GenAI | 56 | 6.6% |
| 26 | Security | Practices | 53 | 6.3% |
| 27 | PyTorch | Frameworks & Libraries | 53 | 6.3% |
| 28 | dbt | Data Engineering | 53 | 6.3% |
| 29 | AI Safety | LLM & GenAI | 49 | 5.8% |
| 30 | Docker | Infra & Cloud | 48 | 5.7% |
| 31 | Linux | Infra & Cloud | 47 | 5.6% |
| 32 | MCP | LLM & GenAI | 46 | 5.5% |
| 33 | Databricks | Data Engineering | 46 | 5.5% |
| 34 | Recommender Systems | ML Fundamentals | 45 | 5.3% |
| 35 | Deep Learning | ML Fundamentals | 42 | 5.0% |
| 36 | MLOps | Practices | 39 | 4.6% |
| 37 | Multimodal | LLM & GenAI | 39 | 4.6% |
| 38 | Fine-tuning | LLM & GenAI | 36 | 4.3% |
| 39 | RAG | LLM & GenAI | 36 | 4.3% |
| 40 | Prompt Engineering | LLM & GenAI | 33 | 3.9% |

</details>

## Movers

Change in share of postings since 2026-10-14, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Observability | +0.60 | | SQL | -0.61 |
| AI Agents | +0.55 | | Statistics | -0.51 |
| GCP | +0.53 | | Python | -0.48 |
| AWS | +0.46 | | Machine Learning | -0.46 |
| Azure | +0.43 | | React | -0.33 |
| AI Safety | +0.29 | | Airflow | -0.31 |
| Security | +0.26 | | Docker | -0.26 |
| Fine-tuning | +0.25 | | Rust | -0.23 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,088 | 37.9% |
| swe | 460 | 16.0% |
| other | 433 | 15.1% |
| ops | 265 | 9.2% |
| product | 239 | 8.3% |
| infra | 159 | 5.5% |
| ml-ai | 95 | 3.3% |
| data | 80 | 2.8% |
| research | 50 | 1.7% |

## Disclosed pay, remote engineering roles

566 of 844 engineering postings (67%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $196,000 |
| Median | $226,200 |
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
| Pika | $300,000 |
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


<sub>Generated 2026-10-21T13:24:47+00:00 · 4 board(s) unreachable this run</sub>
