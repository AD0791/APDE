# APDE — Alexandro Disla · Projets & Préparation

Personal workspace for **exam preparation**, **project documentation**, and **learning foundations** — mainly targeting banking/analyst roles and agentic AI.

---

## What’s in this repo

| Area | Purpose |
| ---- | ------- |
| **`preparation_examen/`** | Structured study material and practice for **UniBank Haiti** exams (Backend Analyst-Programmer & Data Analyst). |
| **`docs_project/`** | Technical design docs and references for concrete projects (e.g. credit scoring, CreditGuard AI). |
| **`foundation_agentic/`** | Theoretical foundations for **agentic AI** (LLMs, RAG, MCP, tools) — Tekkod Agentic Shift, Phase 1. |
| **`well_rounded/`** | Reference material for general software (e.g. Java/JVM/Spring Boot). |
| **`adminer/`** | Lightweight Docker setup to run [Adminer](https://www.adminer.org/) for DB administration. |

Root-level PDFs are resumes (EN/FR).

---

## Repository structure

```text
APDE/
├── README.md
├── preparation_examen/          # Exam prep (UniBank Haiti)
│   ├── backend/                # Analyste-Programmeur track
│   │   ├── Foundational/       # 8-day plan: BDD/SQL, OOP, SOLID, UML, DSA, Backend/Network/Frontend
│   │   ├── FULL/               # Full case studies (Backend, SQL, UML, DSA, DP, ERD, Frontend)
│   │   ├── java/               # Java advanced topics & project fundamentals
│   │   ├── revisions/          # Revision manuals, cheat sheets, simulation
│   │   └── tests/              # Practice exams (global, SQL, UML, DSA/DP, networking)
│   └── Data_analyst/           # Data Analyst track
│       ├── Foundational/       # 19 modules (viz, EDA, stats, SQL, ML, regression, BI, ethics, etc.)
│       ├── FULL/               # Full case studies (EDA, SQL, BI, DataViz, Stats, ML)
│       ├── revisions/          # Revision manuals, mnemonics, exam-focused stats
│       ├── special_cases/      # Outliers, missing values, ACP/ANOVA, N+1, etc.
│       ├── tests/              # Context-based tests per topic
│       └── out_of_scope/       # PowerBI, DAX (reference only)
│
├── docs_project/               # Project design & learning docs
│   ├── scoring/                # Credit scoring system
│   │   ├── design_document_credit_scoring.md   # Architecture (Python + Java, MySQL, Docker)
│   │   ├── scoring_credit_fondations_theoriques.md
│   │   ├── lecture_*.md, environnement_*.md
│   │   └── *.png               # Domain model, architectures, workflows, Docker
│   └── creditguard/            # CreditGuard AI design
│       └── design_creditguard_ai.pdf
│
├── foundation_agentic/         # Agentic AI foundations (Tekkod)
│   ├── agentic_foundation/
│   │   ├── guide_fondations_agentic_ai.md     # Full course: LLMs → RAG → MCP → tools
│   │   └── diagrams/                          # LLM evolution, attention, RAG, MCP, etc.
│   └── guide_pratique_frameworks_agentiques.pdf
│
├── well_rounded/               # General tech reference
│   └── java_jvm_springboot.pdf
│
├── adminer/
│   └── docker-compose.yml      # Adminer on port 8080
│
├── Alexandro_Disla_Resume.pdf
└── Alexandro_Disla_Resume_English.pdf
```

---

## Preparation examens (UniBank Haiti)

### Backend — Analyste-Programmeur

- **Format:** Written exam, 2–3 h, mix of theory and code.
- **Foundational:** 8-day plan (BDD/SQL, OOP, SOLID, UML, DSA, Backend/Network/Frontend).
- **FULL:** Case studies by domain (backend, SQL, UML, DSA, design patterns, ERD, frontend).
- **Tests:** Global exams (Intermediaire/Senior/TechLead), plus topic-specific (SQL, UML, DSA/DP, networking).

Start with: `preparation_examen/backend/Foundational/00_Vue_Ensemble.md`.

### Data Analyst

- **Context:** Data Analyst role in a commercial bank.
- **Foundational:** 19 modules (data viz, EDA, stats, SQL, ML, regression, time series, BI, ethics, etc.).
- **FULL:** Full case studies (EDA, SQL, BI, DataViz, Stats, ML).
- **Tests:** Context-based tests per topic; revision manuals and mnemonics.

Start with: `preparation_examen/Data_analyst/Foundational/00_Vue_Ensemble.md`.

---

## Project docs (designs & lectures)

### Credit scoring system (`docs_project/scoring/`)

Design of a **credit scoring analyst workbench** with:

- **Domain:** Client, LoanProduct, CreditApplication (score, risk level, status, interest rate).
- **Stacks:** Python (SQLAlchemy, Pandas, Jupyter) and Java (JPA + JDBC/DFlib) on the same MySQL DB.
- **Environment:** Docker, migrations (Alembic / Flyway), analytical queries and workflows.

Main entry: `docs_project/scoring/design_document_credit_scoring.md`.

### CreditGuard AI (`docs_project/creditguard/`)

Design document for the CreditGuard AI project: `design_creditguard_ai.pdf`.

---

## Agentic AI foundations

Material for **Tekkod — Agentic Shift, Phase 1 (Foundational Shift)**:

- **Topics:** LLMs, autoregressive prediction, prompt/context engineering, RAG, structured outputs (e.g. PydanticAI), Model Context Protocol (MCP), tool ecosystem (n8n, LangGraph, etc.).
- **Format:** Long-form markdown course + diagrams (evolution, attention, RAG, MCP, etc.).

Main entry: `foundation_agentic/agentic_foundation/guide_fondations_agentic_ai.md`.

---

## Adminer (database UI)

To run Adminer (e.g. for local MySQL during scoring work):

```bash
cd adminer && docker compose up -d
```

Then open <http://localhost:8080>.

---

## Conventions

- **Language:** Most prep and project docs are in **French**; some references and code are in English.
- **Formats:** Content is mainly **Markdown** (`.md`) and **PDF**; images are in the same folder as the doc that references them.
- **Ignored:** `.env`, `.docx`/`.doc`, `.txt`, `.cache` (see `.gitignore`).

---

## Quick links

| Goal | Where to look |
| ---- | -------------- |
| Backend exam plan | `preparation_examen/backend/Foundational/00_Vue_Ensemble.md` |
| Data Analyst exam plan | `preparation_examen/Data_analyst/Foundational/00_Vue_Ensemble.md` |
| Credit scoring architecture | `docs_project/scoring/design_document_credit_scoring.md` |
| Agentic AI course | `foundation_agentic/agentic_foundation/guide_fondations_agentic_ai.md` |
| Run Adminer | `adminer/docker-compose.yml` → `docker compose up -d` |

---

*APDE — Alexandro Disla. Last updated for repo structure as of 2025.*
