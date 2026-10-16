# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-10-16** — tracking **2,805 open remote roles** across **89 companies** (824 of them engineering roles). 1,646 postings disclose pay. **55 appeared today.**

<sub>Remote-only: 14,293 postings were collected across all locations and 19.6% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 824 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 371 | 45.0% |
| 2 | Observability | Practices | 271 | 32.9% |
| 3 | Distributed Systems | Practices | 249 | 30.2% |
| 4 | Machine Learning | ML Fundamentals | 248 | 30.1% |
| 5 | LLMs | LLM & GenAI | 245 | 29.7% |
| 6 | Go | Languages | 241 | 29.2% |
| 7 | AI Agents | LLM & GenAI | 226 | 27.4% |
| 8 | AWS | Infra & Cloud | 210 | 25.5% |
| 9 | Kubernetes | Infra & Cloud | 208 | 25.2% |
| 10 | TypeScript | Languages | 173 | 21.0% |
| 11 | Statistics | ML Fundamentals | 158 | 19.2% |
| 12 | SQL | Languages | 147 | 17.8% |
| 13 | Data Pipelines | Data Engineering | 132 | 16.0% |
| 14 | CI/CD | Practices | 127 | 15.4% |
| 15 | GCP | Infra & Cloud | 122 | 14.8% |
| 16 | React | Frameworks & Libraries | 117 | 14.2% |
| 17 | Terraform | Infra & Cloud | 114 | 13.8% |
| 18 | Java | Languages | 93 | 11.3% |
| 19 | Snowflake / BigQuery | Data Engineering | 80 | 9.7% |
| 20 | Airflow | Data Engineering | 72 | 8.7% |
| 21 | Kafka | Data Engineering | 65 | 7.9% |
| 22 | Azure | Infra & Cloud | 63 | 7.6% |
| 23 | Spark | Data Engineering | 62 | 7.5% |
| 24 | Rust | Languages | 61 | 7.4% |
| 25 | Evals | LLM & GenAI | 56 | 6.8% |
| 26 | PyTorch | Frameworks & Libraries | 52 | 6.3% |
| 27 | AI Safety | LLM & GenAI | 50 | 6.1% |
| 28 | dbt | Data Engineering | 50 | 6.1% |
| 29 | Security | Practices | 49 | 5.9% |
| 30 | Docker | Infra & Cloud | 47 | 5.7% |
| 31 | Linux | Infra & Cloud | 46 | 5.6% |
| 32 | MCP | LLM & GenAI | 45 | 5.5% |
| 33 | Databricks | Data Engineering | 45 | 5.5% |
| 34 | Recommender Systems | ML Fundamentals | 45 | 5.5% |
| 35 | Deep Learning | ML Fundamentals | 41 | 5.0% |
| 36 | Multimodal | LLM & GenAI | 40 | 4.9% |
| 37 | MLOps | Practices | 39 | 4.7% |
| 38 | RAG | LLM & GenAI | 33 | 4.0% |
| 39 | Prompt Engineering | LLM & GenAI | 32 | 3.9% |
| 40 | Fine-tuning | LLM & GenAI | 32 | 3.9% |

</details>

## Movers

Change in share of postings since 2026-10-09, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Snowflake / BigQuery | +0.49 | | Azure | -0.96 |
| Fine-tuning | +0.41 | | Distributed Systems | -0.87 |
| Spark | +0.37 | | GCP | -0.79 |
| SQL | +0.37 | | AWS | -0.54 |
| Databricks | +0.31 | | Machine Learning | -0.52 |
| Evals | +0.30 | | Kafka | -0.49 |
| MCP | +0.27 | | Go | -0.40 |
| dbt | +0.23 | | Java | -0.39 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,054 | 37.6% |
| swe | 445 | 15.9% |
| other | 435 | 15.5% |
| ops | 264 | 9.4% |
| product | 228 | 8.1% |
| infra | 156 | 5.6% |
| ml-ai | 90 | 3.2% |
| data | 82 | 2.9% |
| research | 51 | 1.8% |

## Disclosed pay, remote engineering roles

554 of 824 engineering postings (67%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $197,050 |
| Median | $227,735 |
| 75th | $260,000 |
| 90th | $288,000 |

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


<sub>Generated 2026-10-16T13:02:10+00:00 · 4 board(s) unreachable this run</sub>
