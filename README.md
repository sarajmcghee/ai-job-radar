# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-11-04** — tracking **2,880 open remote roles** across **90 companies** (820 of them engineering roles). 1,701 postings disclose pay. **55 appeared today.**

<sub>Remote-only: 14,559 postings were collected across all locations and 19.8% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 820 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 365 | 44.5% |
| 2 | Observability | Practices | 267 | 32.6% |
| 3 | Machine Learning | ML Fundamentals | 248 | 30.2% |
| 4 | LLMs | LLM & GenAI | 237 | 28.9% |
| 5 | Distributed Systems | Practices | 236 | 28.8% |
| 6 | AI Agents | LLM & GenAI | 233 | 28.4% |
| 7 | Go | Languages | 230 | 28.0% |
| 8 | Kubernetes | Infra & Cloud | 212 | 25.9% |
| 9 | AWS | Infra & Cloud | 195 | 23.8% |
| 10 | TypeScript | Languages | 178 | 21.7% |
| 11 | Statistics | ML Fundamentals | 161 | 19.6% |
| 12 | SQL | Languages | 147 | 17.9% |
| 13 | Data Pipelines | Data Engineering | 129 | 15.7% |
| 14 | GCP | Infra & Cloud | 124 | 15.1% |
| 15 | CI/CD | Practices | 121 | 14.8% |
| 16 | React | Frameworks & Libraries | 116 | 14.1% |
| 17 | Terraform | Infra & Cloud | 115 | 14.0% |
| 18 | Java | Languages | 100 | 12.2% |
| 19 | Snowflake / BigQuery | Data Engineering | 76 | 9.3% |
| 20 | Airflow | Data Engineering | 69 | 8.4% |
| 21 | Azure | Infra & Cloud | 65 | 7.9% |
| 22 | Rust | Languages | 63 | 7.7% |
| 23 | Kafka | Data Engineering | 62 | 7.6% |
| 24 | Spark | Data Engineering | 61 | 7.4% |
| 25 | Evals | LLM & GenAI | 58 | 7.1% |
| 26 | Security | Practices | 51 | 6.2% |
| 27 | Docker | Infra & Cloud | 48 | 5.9% |
| 28 | MCP | LLM & GenAI | 47 | 5.7% |
| 29 | PyTorch | Frameworks & Libraries | 47 | 5.7% |
| 30 | Databricks | Data Engineering | 44 | 5.4% |
| 31 | dbt | Data Engineering | 43 | 5.2% |
| 32 | Linux | Infra & Cloud | 41 | 5.0% |
| 33 | MLOps | Practices | 39 | 4.8% |
| 34 | AI Safety | LLM & GenAI | 36 | 4.4% |
| 35 | Recommender Systems | ML Fundamentals | 36 | 4.4% |
| 36 | Deep Learning | ML Fundamentals | 35 | 4.3% |
| 37 | Multimodal | LLM & GenAI | 34 | 4.1% |
| 38 | RAG | LLM & GenAI | 31 | 3.8% |
| 39 | Prompt Engineering | LLM & GenAI | 30 | 3.7% |
| 40 | TensorFlow | Frameworks & Libraries | 30 | 3.7% |

</details>

## Movers

Change in share of postings since 2026-10-28, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Statistics | +0.37 | | Kubernetes | -0.73 |
| Evals | +0.33 | | AWS | -0.62 |
| Databricks | +0.29 | | Terraform | -0.54 |
| Java | +0.28 | | Observability | -0.54 |
| React | +0.22 | | LLMs | -0.51 |
| Snowflake / BigQuery | +0.19 | | Go | -0.42 |
| MCP | +0.18 | | Data Pipelines | -0.36 |
| Airflow | +0.15 | | Recommender Systems | -0.34 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,145 | 39.8% |
| swe | 443 | 15.4% |
| other | 428 | 14.9% |
| ops | 268 | 9.3% |
| product | 219 | 7.6% |
| infra | 158 | 5.5% |
| ml-ai | 94 | 3.3% |
| data | 73 | 2.5% |
| research | 52 | 1.8% |

## Disclosed pay, remote engineering roles

552 of 820 engineering postings (67%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $196,000 |
| Median | $228,500 |
| 75th | $260,450 |
| 90th | $299,500 |

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
| GitLab | $301,800 |

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


<sub>Generated 2026-11-04T15:57:32+00:00 · 5 board(s) unreachable this run</sub>
