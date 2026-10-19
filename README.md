# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-10-19** — tracking **2,826 open remote roles** across **89 companies** (830 of them engineering roles). 1,653 postings disclose pay. **24 appeared today.**

<sub>Remote-only: 14,322 postings were collected across all locations and 19.7% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 830 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 366 | 44.1% |
| 2 | Observability | Practices | 273 | 32.9% |
| 3 | LLMs | LLM & GenAI | 257 | 31.0% |
| 4 | Machine Learning | ML Fundamentals | 250 | 30.1% |
| 5 | Distributed Systems | Practices | 246 | 29.6% |
| 6 | Go | Languages | 238 | 28.7% |
| 7 | AI Agents | LLM & GenAI | 234 | 28.2% |
| 8 | AWS | Infra & Cloud | 213 | 25.7% |
| 9 | Kubernetes | Infra & Cloud | 212 | 25.5% |
| 10 | TypeScript | Languages | 182 | 21.9% |
| 11 | Statistics | ML Fundamentals | 159 | 19.2% |
| 12 | SQL | Languages | 144 | 17.3% |
| 13 | Data Pipelines | Data Engineering | 130 | 15.7% |
| 14 | CI/CD | Practices | 128 | 15.4% |
| 15 | GCP | Infra & Cloud | 126 | 15.2% |
| 16 | React | Frameworks & Libraries | 125 | 15.1% |
| 17 | Terraform | Infra & Cloud | 116 | 14.0% |
| 18 | Java | Languages | 91 | 11.0% |
| 19 | Snowflake / BigQuery | Data Engineering | 81 | 9.8% |
| 20 | Airflow | Data Engineering | 71 | 8.6% |
| 21 | Azure | Infra & Cloud | 67 | 8.1% |
| 22 | Spark | Data Engineering | 61 | 7.3% |
| 23 | Kafka | Data Engineering | 59 | 7.1% |
| 24 | Rust | Languages | 58 | 7.0% |
| 25 | Evals | LLM & GenAI | 58 | 7.0% |
| 26 | PyTorch | Frameworks & Libraries | 54 | 6.5% |
| 27 | dbt | Data Engineering | 52 | 6.3% |
| 28 | AI Safety | LLM & GenAI | 51 | 6.1% |
| 29 | Docker | Infra & Cloud | 49 | 5.9% |
| 30 | Security | Practices | 48 | 5.8% |
| 31 | Recommender Systems | ML Fundamentals | 47 | 5.7% |
| 32 | MCP | LLM & GenAI | 46 | 5.5% |
| 33 | Linux | Infra & Cloud | 46 | 5.5% |
| 34 | Databricks | Data Engineering | 45 | 5.4% |
| 35 | Deep Learning | ML Fundamentals | 43 | 5.2% |
| 36 | MLOps | Practices | 40 | 4.8% |
| 37 | Multimodal | LLM & GenAI | 40 | 4.8% |
| 38 | RAG | LLM & GenAI | 35 | 4.2% |
| 39 | Prompt Engineering | LLM & GenAI | 34 | 4.1% |
| 40 | Fine-tuning | LLM & GenAI | 34 | 4.1% |

</details>

## Movers

Change in share of postings since 2026-10-12, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Databricks | +0.43 | | Machine Learning | -0.70 |
| AI Agents | +0.42 | | Distributed Systems | -0.56 |
| Fine-tuning | +0.34 | | Statistics | -0.51 |
| Spark | +0.33 | | Go | -0.43 |
| LLMs | +0.29 | | Rust | -0.35 |
| dbt | +0.25 | | Java | -0.32 |
| AWS | +0.24 | | Docker | -0.31 |
| GCP | +0.24 | | Python | -0.30 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,065 | 37.7% |
| swe | 447 | 15.8% |
| other | 429 | 15.2% |
| ops | 268 | 9.5% |
| product | 234 | 8.3% |
| infra | 156 | 5.5% |
| ml-ai | 95 | 3.4% |
| data | 81 | 2.9% |
| research | 51 | 1.8% |

## Disclosed pay, remote engineering roles

557 of 830 engineering postings (67%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $197,000 |
| Median | $227,735 |
| 75th | $260,000 |
| 90th | $289,530 |

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


<sub>Generated 2026-10-19T15:16:03+00:00 · 4 board(s) unreachable this run</sub>
