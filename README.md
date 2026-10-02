# AI Job Radar

> Daily snapshot of what AI and tech companies are hiring for in remote roles, built from public job-board APIs. Updated every morning by GitHub Actions.

**2026-10-02** — tracking **2,857 open remote roles** across **93 companies** (830 of them engineering roles). 1,657 postings disclose pay. **68 appeared today.**

<sub>Remote-only: 14,280 postings were collected across all locations and 20.0% of them were remote. Set `remote_only` to false in `config/settings.json` to track every location.</sub>

---

## Most-requested skills in remote engineering roles

Share of the 830 remote engineering postings that mention each skill.

![Top skills](docs/charts/top-skills.svg)

<details><summary>Full skill table</summary>

| # | Skill | Category | Postings | Share |
|---:|---|---|---:|---:|
| 1 | Python | Languages | 383 | 46.1% |
| 2 | Observability | Practices | 292 | 35.2% |
| 3 | Distributed Systems | Practices | 277 | 33.4% |
| 4 | Go | Languages | 258 | 31.1% |
| 5 | Machine Learning | ML Fundamentals | 248 | 29.9% |
| 6 | AI Agents | LLM & GenAI | 231 | 27.8% |
| 7 | LLMs | LLM & GenAI | 229 | 27.6% |
| 8 | AWS | Infra & Cloud | 226 | 27.2% |
| 9 | Kubernetes | Infra & Cloud | 203 | 24.5% |
| 10 | TypeScript | Languages | 167 | 20.1% |
| 11 | Statistics | ML Fundamentals | 155 | 18.7% |
| 12 | SQL | Languages | 147 | 17.7% |
| 13 | Data Pipelines | Data Engineering | 147 | 17.7% |
| 14 | GCP | Infra & Cloud | 142 | 17.1% |
| 15 | CI/CD | Practices | 134 | 16.1% |
| 16 | React | Frameworks & Libraries | 118 | 14.2% |
| 17 | Terraform | Infra & Cloud | 115 | 13.9% |
| 18 | Java | Languages | 110 | 13.3% |
| 19 | Azure | Infra & Cloud | 87 | 10.5% |
| 20 | Airflow | Data Engineering | 78 | 9.4% |
| 21 | Snowflake / BigQuery | Data Engineering | 77 | 9.3% |
| 22 | Kafka | Data Engineering | 76 | 9.2% |
| 23 | Spark | Data Engineering | 66 | 8.0% |
| 24 | Rust | Languages | 65 | 7.8% |
| 25 | Security | Practices | 54 | 6.5% |
| 26 | Docker | Infra & Cloud | 54 | 6.5% |
| 27 | Linux | Infra & Cloud | 47 | 5.7% |
| 28 | AI Safety | LLM & GenAI | 46 | 5.5% |
| 29 | PyTorch | Frameworks & Libraries | 46 | 5.5% |
| 30 | Evals | LLM & GenAI | 44 | 5.3% |
| 31 | dbt | Data Engineering | 44 | 5.3% |
| 32 | MCP | LLM & GenAI | 41 | 4.9% |
| 33 | Databricks | Data Engineering | 41 | 4.9% |
| 34 | MLOps | Practices | 41 | 4.9% |
| 35 | RAG | LLM & GenAI | 39 | 4.7% |
| 36 | Deep Learning | ML Fundamentals | 38 | 4.6% |
| 37 | Recommender Systems | ML Fundamentals | 38 | 4.6% |
| 38 | TensorFlow | Frameworks & Libraries | 32 | 3.9% |
| 39 | A/B Testing | Practices | 31 | 3.7% |
| 40 | Fine-tuning | LLM & GenAI | 30 | 3.6% |

</details>

## Movers

Change in share of postings since 2026-09-25, in percentage points.

| Rising | Δ pp | | Falling | Δ pp |
|---|---:|---|---|---:|
| CI/CD | +0.42 | | LLMs | -0.77 |
| Databricks | +0.31 | | Kubernetes | -0.47 |
| Speech / Audio | +0.29 | | Observability | -0.42 |
| Terraform | +0.28 | | TypeScript | -0.40 |
| AI Safety | +0.27 | | Evals | -0.39 |
| Java | +0.27 | | Docker | -0.34 |
| Distributed Systems | +0.26 | | Embeddings | -0.28 |
| React | +0.25 | | Statistics | -0.28 |

![Skill trends](docs/charts/trends.svg)

## Where the roles are

![Role families](docs/charts/families.svg)

| Role family | Postings | Share |
|---|---:|---:|
| gtm | 1,076 | 37.7% |
| swe | 474 | 16.6% |
| other | 464 | 16.2% |
| ops | 265 | 9.3% |
| product | 222 | 7.8% |
| infra | 149 | 5.2% |
| ml-ai | 82 | 2.9% |
| data | 77 | 2.7% |
| research | 48 | 1.7% |

## Disclosed pay, remote engineering roles

561 of 830 engineering postings (68%) publish a salary range. Figures are the midpoint of the posted band.

| Percentile | Midpoint |
|---|---:|
| 25th | $197,050 |
| Median | $227,735 |
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


<sub>Generated 2026-10-02T14:27:47+00:00 · 3 board(s) unreachable this run</sub>
