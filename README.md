# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-10-13** — tracking **2,785 open remote roles** across **90 companies** (820 of them engineering roles). 1,649 postings disclose pay. **53 appeared today.**

<sub>Remote-only: 14,311 postings were collected across all locations and 19.5% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 820 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 368 | 44.9% |
| 2 | Observability | Practices | 272 | 33.2% |
| 3 | Distributed Systems | Practices | 253 | 30.9% |
| 4 | Go | Languages | 247 | 30.1% |
| 5 | Machine Learning | ML Fundamentals | 247 | 30.1% |
| 6 | LLMs | LLM & GenAI | 244 | 29.8% |
| 7 | AI Agents | LLM & GenAI | 221 | 27.0% |
| 8 | AWS | Infra & Cloud | 206 | 25.1% |
| 9 | Kubernetes | Infra & Cloud | 203 | 24.8% |
| 10 | TypeScript | Languages | 171 | 20.9% |
| 11 | Statistics | ML Fundamentals | 158 | 19.3% |
| 12 | SQL | Languages | 139 | 17.0% |
| 13 | CI/CD | Practices | 131 | 16.0% |
| 14 | Data Pipelines | Data Engineering | 126 | 15.4% |
| 15 | GCP | Infra & Cloud | 122 | 14.9% |
| 16 | React | Frameworks & Libraries | 120 | 14.6% |
| 17 | Terraform | Infra & Cloud | 113 | 13.8% |
| 18 | Java | Languages | 97 | 11.8% |
| 19 | Snowflake / BigQuery | Data Engineering | 71 | 8.7% |
| 20 | Airflow | Data Engineering | 70 | 8.5% |
| 21 | Azure | Infra & Cloud | 66 | 8.0% |
| 22 | Kafka | Data Engineering | 66 | 8.0% |
| 23 | Rust | Languages | 65 | 7.9% |
| 24 | Spark | Data Engineering | 60 | 7.3% |
| 25 | Docker | Infra & Cloud | 55 | 6.7% |
| 26 | Evals | LLM & GenAI | 55 | 6.7% |
| 27 | PyTorch | Frameworks & Libraries | 50 | 6.1% |
| 28 | AI Safety | LLM & GenAI | 49 | 6.0% |
| 29 | Security | Practices | 48 | 5.9% |
| 30 | Linux | Infra & Cloud | 48 | 5.9% |
| 31 | dbt | Data Engineering | 44 | 5.4% |
| 32 | MCP | LLM & GenAI | 43 | 5.2% |
| 33 | Recommender Systems | ML Fundamentals | 42 | 5.1% |
| 34 | Databricks | Data Engineering | 39 | 4.8% |
| 35 | Deep Learning | ML Fundamentals | 39 | 4.8% |
| 36 | MLOps | Practices | 38 | 4.6% |
| 37 | Multimodal | LLM & GenAI | 37 | 4.5% |
| 38 | RAG | LLM & GenAI | 35 | 4.3% |
| 39 | GPU Clusters | Infra & Cloud | 32 | 3.9% |
| 40 | A/B Testing | Practices | 31 | 3.8% |

</details>

## Movers

Change in share of postings since 2026-10-06, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Evals | +0.37 | | Distributed Systems | -1.14 |
| Machine Learning | +0.34 | | Observability | -0.84 |
| Kubernetes | +0.30 | | Azure | -0.82 |
| Fine-tuning | +0.29 | | GCP | -0.67 |
| Snowflake / BigQuery | +0.29 | | Java | -0.64 |
| LLMs | +0.23 | | Data Pipelines | -0.57 |
| SQL | +0.20 | | Kafka | -0.54 |
| GPU Clusters | +0.19 | | AWS | -0.52 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,057 | 38.0% |
| swe | 448 | 16.1% |
| other | 425 | 15.3% |
| ops | 265 | 9.5% |
| product | 218 | 7.8% |
| infra | 153 | 5.5% |
| ml-ai | 85 | 3.1% |
| data | 81 | 2.9% |
| research | 53 | 1.9% |

## Disclosed pay, remote engineering roles

557 of 820 engineering postings (68%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $197,050 |
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


<sub>Generated 2026-10-13T15:34:18+00:00 · 4 board(s) unreachable this run</sub>
