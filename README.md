# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-08-27** — tracking **3,257 open remote roles** across **94 companies** (969 of them engineering roles). 1,773 postings disclose pay. **1 appeared today.**

<sub>Remote-only: 14,254 postings were collected across all locations and 22.9% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 969 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 463 | 47.8% |
| 2 | Distributed Systems | Practices | 365 | 37.7% |
| 3 | Observability | Practices | 342 | 35.3% |
| 4 | Go | Languages | 312 | 32.2% |
| 5 | Kubernetes | Infra & Cloud | 290 | 29.9% |
| 6 | AWS | Infra & Cloud | 288 | 29.7% |
| 7 | Machine Learning | ML Fundamentals | 288 | 29.7% |
| 8 | AI Agents | LLM & GenAI | 268 | 27.7% |
| 9 | LLMs | LLM & GenAI | 266 | 27.5% |
| 10 | TypeScript | Languages | 228 | 23.5% |
| 11 | GCP | Infra & Cloud | 216 | 22.3% |
| 12 | SQL | Languages | 184 | 19.0% |
| 13 | Statistics | ML Fundamentals | 182 | 18.8% |
| 14 | Azure | Infra & Cloud | 169 | 17.4% |
| 15 | Java | Languages | 156 | 16.1% |
| 16 | Terraform | Infra & Cloud | 153 | 15.8% |
| 17 | Data Pipelines | Data Engineering | 150 | 15.5% |
| 18 | CI/CD | Practices | 147 | 15.2% |
| 19 | React | Frameworks & Libraries | 117 | 12.1% |
| 20 | Airflow | Data Engineering | 112 | 11.6% |
| 21 | Kafka | Data Engineering | 97 | 10.0% |
| 22 | Spark | Data Engineering | 90 | 9.3% |
| 23 | Docker | Infra & Cloud | 88 | 9.1% |
| 24 | Snowflake / BigQuery | Data Engineering | 82 | 8.5% |
| 25 | Rust | Languages | 78 | 8.0% |
| 26 | Evals | LLM & GenAI | 72 | 7.4% |
| 27 | Linux | Infra & Cloud | 66 | 6.8% |
| 28 | Security | Practices | 63 | 6.5% |
| 29 | PyTorch | Frameworks & Libraries | 56 | 5.8% |
| 30 | Recommender Systems | ML Fundamentals | 52 | 5.4% |
| 31 | Databricks | Data Engineering | 51 | 5.3% |
| 32 | RAG | LLM & GenAI | 51 | 5.3% |
| 33 | MLOps | Practices | 49 | 5.1% |
| 34 | dbt | Data Engineering | 49 | 5.1% |
| 35 | MCP | LLM & GenAI | 45 | 4.6% |
| 36 | Prompt Engineering | LLM & GenAI | 45 | 4.6% |
| 37 | A/B Testing | Practices | 43 | 4.4% |
| 38 | Deep Learning | ML Fundamentals | 42 | 4.3% |
| 39 | AI Safety | LLM & GenAI | 39 | 4.0% |
| 40 | Embeddings | LLM & GenAI | 39 | 4.0% |

</details>

## Movers

_Trend lines appear once a second day has been collected. Each morning's run appends to `data/trends.csv`._

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,235 | 37.9% |
| swe | 572 | 17.6% |
| other | 526 | 16.1% |
| ops | 275 | 8.4% |
| product | 252 | 7.7% |
| infra | 179 | 5.5% |
| ml-ai | 104 | 3.2% |
| data | 74 | 2.3% |
| research | 40 | 1.2% |

## Disclosed pay, remote engineering roles

584 of 969 engineering postings (60%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $187,450 |
| Median | $226,200 |
| 75th | $259,500 |
| 90th | $283,000 |

<details><summary>Highest disclosed engineering bands by company</summary>

| Company | Top posted midpoint |
|---|---:|
| Anthropic | $675,000 |
| OpenAI | $418,500 |
| Pinterest | $371,087 |
| Reddit | $351,000 |
| Databricks | $343,425 |
| Agility Robotics | $329,500 |
| Mercury | $325,900 |
| Snorkel AI | $316,000 |
| Hightouch | $310,000 |
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


<sub>Generated 2026-08-27T20:10:43+00:00 · 0 board(s) unreachable this run</sub>
