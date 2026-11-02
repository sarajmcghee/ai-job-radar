# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-11-02** — tracking **2,884 open remote roles** across **90 companies** (815 of them engineering roles). 1,682 postings disclose pay. **22 appeared today.**

<sub>Remote-only: 14,556 postings were collected across all locations and 19.8% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 815 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 359 | 44.0% |
| 2 | Observability | Practices | 264 | 32.4% |
| 3 | Machine Learning | ML Fundamentals | 244 | 29.9% |
| 4 | Distributed Systems | Practices | 239 | 29.3% |
| 5 | LLMs | LLM & GenAI | 237 | 29.1% |
| 6 | Go | Languages | 235 | 28.8% |
| 7 | AI Agents | LLM & GenAI | 225 | 27.6% |
| 8 | Kubernetes | Infra & Cloud | 207 | 25.4% |
| 9 | AWS | Infra & Cloud | 198 | 24.3% |
| 10 | TypeScript | Languages | 173 | 21.2% |
| 11 | Statistics | ML Fundamentals | 158 | 19.4% |
| 12 | SQL | Languages | 146 | 17.9% |
| 13 | Data Pipelines | Data Engineering | 127 | 15.6% |
| 14 | CI/CD | Practices | 120 | 14.7% |
| 15 | Terraform | Infra & Cloud | 117 | 14.4% |
| 16 | GCP | Infra & Cloud | 117 | 14.4% |
| 17 | React | Frameworks & Libraries | 113 | 13.9% |
| 18 | Java | Languages | 99 | 12.1% |
| 19 | Snowflake / BigQuery | Data Engineering | 77 | 9.4% |
| 20 | Airflow | Data Engineering | 66 | 8.1% |
| 21 | Azure | Infra & Cloud | 64 | 7.9% |
| 22 | Rust | Languages | 64 | 7.9% |
| 23 | Kafka | Data Engineering | 63 | 7.7% |
| 24 | Spark | Data Engineering | 62 | 7.6% |
| 25 | Evals | LLM & GenAI | 58 | 7.1% |
| 26 | Security | Practices | 55 | 6.7% |
| 27 | Docker | Infra & Cloud | 49 | 6.0% |
| 28 | PyTorch | Frameworks & Libraries | 48 | 5.9% |
| 29 | Databricks | Data Engineering | 44 | 5.4% |
| 30 | MCP | LLM & GenAI | 43 | 5.3% |
| 31 | AI Safety | LLM & GenAI | 41 | 5.0% |
| 32 | dbt | Data Engineering | 41 | 5.0% |
| 33 | Linux | Infra & Cloud | 40 | 4.9% |
| 34 | MLOps | Practices | 38 | 4.7% |
| 35 | Recommender Systems | ML Fundamentals | 38 | 4.7% |
| 36 | Deep Learning | ML Fundamentals | 37 | 4.5% |
| 37 | Multimodal | LLM & GenAI | 34 | 4.2% |
| 38 | RAG | LLM & GenAI | 31 | 3.8% |
| 39 | TensorFlow | Frameworks & Libraries | 31 | 3.8% |
| 40 | A/B Testing | Practices | 29 | 3.6% |

</details>

## Movers

Change in share of postings since 2026-10-26, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| Snowflake / BigQuery | +0.32 | | Observability | -1.12 |
| Evals | +0.25 | | Kubernetes | -1.09 |
| Statistics | +0.19 | | AWS | -0.63 |
| Java | +0.18 | | LLMs | -0.60 |
| SQL | +0.15 | | Terraform | -0.51 |
| Airflow | +0.11 | | TypeScript | -0.51 |
| LangChain | +0.11 | | GCP | -0.47 |
| Security | +0.08 | | Azure | -0.44 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,130 | 39.2% |
| other | 451 | 15.6% |
| swe | 442 | 15.3% |
| ops | 264 | 9.2% |
| product | 224 | 7.8% |
| infra | 154 | 5.3% |
| ml-ai | 96 | 3.3% |
| data | 71 | 2.5% |
| research | 52 | 1.8% |

## Disclosed pay, remote engineering roles

552 of 815 engineering postings (68%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $195,450 |
| Median | $227,500 |
| 75th | $260,450 |
| 90th | $290,000 |

<details><summary>Highest disclosed engineering bands by company</summary>

| Company | Top posted midpoint |
|---|---:|
| Anthropic | $675,000 |
| OpenAI | $455,500 |
| Pinterest | $371,087 |
| Reddit | $351,000 |
| Agility Robotics | $329,500 |
| Coinbase | $320,142 |
| Snorkel AI | $316,000 |
| Discord | $306,000 |
| GitLab | $301,800 |
| Cohere | $300,000 |

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


<sub>Generated 2026-11-02T17:48:27+00:00 · 5 board(s) unreachable this run</sub>
