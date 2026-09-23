# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-09-23** — tracking **2,906 open remote roles** across **92 companies** (845 of them engineering roles). 1,644 postings disclose pay. **47 appeared today.**

<sub>Remote-only: 14,249 postings were collected across all locations and 20.4% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 845 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 386 | 45.7% |
| 2 | Observability | Practices | 311 | 36.8% |
| 3 | Distributed Systems | Practices | 281 | 33.3% |
| 4 | Go | Languages | 263 | 31.1% |
| 5 | LLMs | LLM & GenAI | 251 | 29.7% |
| 6 | Machine Learning | ML Fundamentals | 249 | 29.5% |
| 7 | AI Agents | LLM & GenAI | 235 | 27.8% |
| 8 | AWS | Infra & Cloud | 228 | 27.0% |
| 9 | Kubernetes | Infra & Cloud | 221 | 26.2% |
| 10 | TypeScript | Languages | 175 | 20.7% |
| 11 | Statistics | ML Fundamentals | 164 | 19.4% |
| 12 | SQL | Languages | 149 | 17.6% |
| 13 | GCP | Infra & Cloud | 147 | 17.4% |
| 14 | Data Pipelines | Data Engineering | 143 | 16.9% |
| 15 | CI/CD | Practices | 125 | 14.8% |
| 16 | Terraform | Infra & Cloud | 112 | 13.3% |
| 17 | React | Frameworks & Libraries | 111 | 13.1% |
| 18 | Java | Languages | 110 | 13.0% |
| 19 | Azure | Infra & Cloud | 96 | 11.4% |
| 20 | Rust | Languages | 80 | 9.5% |
| 21 | Snowflake / BigQuery | Data Engineering | 79 | 9.3% |
| 22 | Kafka | Data Engineering | 73 | 8.6% |
| 23 | Airflow | Data Engineering | 71 | 8.4% |
| 24 | Spark | Data Engineering | 64 | 7.6% |
| 25 | Evals | LLM & GenAI | 60 | 7.1% |
| 26 | Docker | Infra & Cloud | 58 | 6.9% |
| 27 | Security | Practices | 52 | 6.2% |
| 28 | MCP | LLM & GenAI | 49 | 5.8% |
| 29 | Linux | Infra & Cloud | 48 | 5.7% |
| 30 | PyTorch | Frameworks & Libraries | 46 | 5.4% |
| 31 | dbt | Data Engineering | 45 | 5.3% |
| 32 | Databricks | Data Engineering | 43 | 5.1% |
| 33 | Deep Learning | ML Fundamentals | 42 | 5.0% |
| 34 | RAG | LLM & GenAI | 42 | 5.0% |
| 35 | AI Safety | LLM & GenAI | 40 | 4.7% |
| 36 | MLOps | Practices | 38 | 4.5% |
| 37 | Recommender Systems | ML Fundamentals | 38 | 4.5% |
| 38 | Prompt Engineering | LLM & GenAI | 36 | 4.3% |
| 39 | A/B Testing | Practices | 33 | 3.9% |
| 40 | Fine-tuning | LLM & GenAI | 32 | 3.8% |

</details>

## Movers

Change in share of postings since 2026-09-16, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Observability | +1.57 | | SQL | -0.57 |
| Distributed Systems | +0.98 | | CI/CD | -0.42 |
| GCP | +0.74 | | Python | -0.31 |
| Azure | +0.68 | | Airflow | -0.24 |
| Statistics | +0.48 | | Evals | -0.23 |
| AWS | +0.45 | | AI Agents | -0.23 |
| Go | +0.41 | | Terraform | -0.15 |
| Rust | +0.36 | | Fine-tuning | -0.11 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,128 | 38.8% |
| swe | 493 | 17.0% |
| other | 444 | 15.3% |
| ops | 259 | 8.9% |
| product | 230 | 7.9% |
| infra | 155 | 5.3% |
| ml-ai | 80 | 2.8% |
| data | 71 | 2.4% |
| research | 46 | 1.6% |

## Disclosed pay, remote engineering roles

536 of 845 engineering postings (63%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $196,000 |
| Median | $228,500 |
| 75th | $260,000 |
| 90th | $290,000 |

<details><summary>Highest disclosed engineering bands by company</summary>

| Company | Top posted midpoint |
|---|---:|
| Anthropic | $675,000 |
| OpenAI | $455,500 |
| Pinterest | $371,087 |
| Reddit | $351,000 |
| Databricks | $343,425 |
| Agility Robotics | $329,500 |
| Snorkel AI | $316,000 |
| Hightouch | $310,000 |
| Discord | $306,000 |
| Lambda | $299,000 |

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


<sub>Generated 2026-09-23T13:20:46+00:00 · 2 board(s) unreachable this run</sub>
