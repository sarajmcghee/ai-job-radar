# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-11-25** — tracking **2,866 open remote roles** across **88 companies** (790 of them engineering roles). 1,712 postings disclose pay. **45 appeared today.**

<sub>Remote-only: 14,748 postings were collected across all locations and 19.4% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 790 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 351 | 44.4% |
| 2 | Observability | Practices | 275 | 34.8% |
| 3 | AI Agents | LLM & GenAI | 243 | 30.8% |
| 4 | LLMs | LLM & GenAI | 238 | 30.1% |
| 5 | Distributed Systems | Practices | 231 | 29.2% |
| 6 | Go | Languages | 226 | 28.6% |
| 7 | Machine Learning | ML Fundamentals | 222 | 28.1% |
| 8 | Kubernetes | Infra & Cloud | 218 | 27.6% |
| 9 | AWS | Infra & Cloud | 206 | 26.1% |
| 10 | TypeScript | Languages | 187 | 23.7% |
| 11 | Statistics | ML Fundamentals | 151 | 19.1% |
| 12 | CI/CD | Practices | 134 | 17.0% |
| 13 | GCP | Infra & Cloud | 129 | 16.3% |
| 14 | SQL | Languages | 122 | 15.4% |
| 15 | React | Frameworks & Libraries | 116 | 14.7% |
| 16 | Terraform | Infra & Cloud | 115 | 14.6% |
| 17 | Data Pipelines | Data Engineering | 101 | 12.8% |
| 18 | Java | Languages | 94 | 11.9% |
| 19 | Azure | Infra & Cloud | 71 | 9.0% |
| 20 | Security | Practices | 65 | 8.2% |
| 21 | Snowflake / BigQuery | Data Engineering | 64 | 8.1% |
| 22 | Evals | LLM & GenAI | 63 | 8.0% |
| 23 | Rust | Languages | 62 | 7.8% |
| 24 | Airflow | Data Engineering | 61 | 7.7% |
| 25 | Spark | Data Engineering | 56 | 7.1% |
| 26 | Kafka | Data Engineering | 55 | 7.0% |
| 27 | MCP | LLM & GenAI | 53 | 6.7% |
| 28 | Docker | Infra & Cloud | 45 | 5.7% |
| 29 | Linux | Infra & Cloud | 43 | 5.4% |
| 30 | AI Safety | LLM & GenAI | 41 | 5.2% |
| 31 | PyTorch | Frameworks & Libraries | 38 | 4.8% |
| 32 | Recommender Systems | ML Fundamentals | 37 | 4.7% |
| 33 | Databricks | Data Engineering | 34 | 4.3% |
| 34 | MLOps | Practices | 32 | 4.1% |
| 35 | Deep Learning | ML Fundamentals | 32 | 4.1% |
| 36 | GPU Clusters | Infra & Cloud | 31 | 3.9% |
| 37 | RAG | LLM & GenAI | 30 | 3.8% |
| 38 | Prompt Engineering | LLM & GenAI | 29 | 3.7% |
| 39 | Multimodal | LLM & GenAI | 29 | 3.7% |
| 40 | A/B Testing | Practices | 28 | 3.5% |

</details>

## Movers

Change in share of postings since 2026-11-18, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Terraform | +0.53 | | Snowflake / BigQuery | -0.60 |
| Observability | +0.48 | | Data Pipelines | -0.52 |
| CI/CD | +0.36 | | Databricks | -0.30 |
| Linux | +0.34 | | Machine Learning | -0.26 |
| Security | +0.29 | | dbt | -0.24 |
| AWS | +0.26 | | SQL | -0.16 |
| TypeScript | +0.25 | | Prompt Engineering | -0.15 |
| Go | +0.24 | | AI Safety | -0.13 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,176 | 41.0% |
| swe | 430 | 15.0% |
| other | 423 | 14.8% |
| ops | 264 | 9.2% |
| product | 213 | 7.4% |
| infra | 172 | 6.0% |
| ml-ai | 78 | 2.7% |
| data | 63 | 2.2% |
| research | 47 | 1.6% |

## Disclosed pay, remote engineering roles

538 of 790 engineering postings (68%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $196,500 |
| Median | $228,950 |
| 75th | $260,450 |
| 90th | $308,520 |

<details><summary>Highest disclosed engineering bands by company</summary>

| Company | Top posted midpoint |
|---|---:|
| Anthropic | $675,000 |
| OpenAI | $455,500 |
| Pinterest | $371,087 |
| Reddit | $351,000 |
| Harvey | $340,000 |
| Agility Robotics | $329,500 |
| Snorkel AI | $325,000 |
| Coinbase | $320,142 |
| Instacart | $312,500 |
| Discord | $310,000 |

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


<sub>Generated 2026-11-25T18:26:01+00:00 · 5 board(s) unreachable this run</sub>
