# APDE — Alexandro Disla · Projets & Préparation

Personal workspace for **exam preparation**, **project documentation**, **freelance project intelligence**, and **learning foundations** — targeting banking/analyst roles, agentic AI, and cross-platform mobile development.

---

## What’s in this repo

| Area | Purpose |
| ---- | ------- |
| **`preparation_examen/`** | Structured study material and practice for **UniBank Haiti** exams (Backend Analyst-Programmer & Data Analyst). |
| **`docs_project/`** | Technical design docs and references for concrete projects (e.g. credit scoring, CreditGuard AI). |
| **`foundation_agentic/`** | Theoretical foundations for **agentic AI** (LLMs, RAG, MCP, tools) — Tekkod Agentic Shift, Phase 1. |
| **`well_rounded/`** | Reference material for general software (e.g. Java/JVM/Spring Boot). |
| **`tekkod_project/`** | Full intelligence base for the **STS Mobile App rebuild** (freelance contract) — React Native masterclass, codebase analysis, skills curriculum, practice project design, and TypeScript deep-dive. |
| **`adminer/`** | Lightweight Docker setup to run [Adminer](https://www.adminer.org/) for DB administration. |

Root-level PDFs are resumes (EN/FR). `ai-coding-tools-comparison.md` is a comparison of AI coding assistants.

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
├── tekkod_project/              # STS Mobile App — Freelance project intelligence
│   ├── 01_REACT_NATIVE_MASTER.md       # RN CLI guide (architecture, environment, build/sign/ship)
│   ├── 02_EXPO_MASTER.md               # Expo overview (workflows, EAS, pricing, decision matrix)
│   ├── 03_STS_CODEBASE_MASTER.md       # Full STS codebase dissection (every screen, dep, pattern)
│   ├── 04_STS_SKILLS_DEVELOPMENT_GUIDE.md  # Skill curriculum for all STS dependencies
│   ├── 05_PRACTICE_PROJECT_DESIGN.md   # "TaskVault" — practice RN CLI project (FastAPI + Docker)
│   ├── 06_TYPESCRIPT_MASTERCLASS.md    # TypeScript deep-dive (compiler → generics → RN patterns)
│   ├── RN_FUNDAMENTALS.md             # React Native fundamentals (web-to-mobile bridge)
│   └── STS Contract mobile app upgrade + changes.pdf  # Client contract (PDF)
│
├── adminer/
│   └── docker-compose.yml      # Adminer on port 8080
│
├── ai-coding-tools-comparison.md
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

## Tekkod Project — STS Mobile App Rebuild

Complete knowledge base for the **Steam The Streets (STS)** mobile app freelance contract. The project is a full React Native upgrade (0.65 → 0.76+, New Architecture, Hermes, TypeScript migration) with an 11-week timeline.

### Documents (read in order)

| # | Document | What it covers |
|---|----------|---------------|
| 01 | `01_REACT_NATIVE_MASTER.md` | RN CLI vs Expo, Old vs New Architecture (Bridge → JSI/Fabric/TurboModules), Linux environment setup, iOS builds via EAS, native modules, signing & shipping |
| 02 | `02_EXPO_MASTER.md` | Expo workflows (Go, Managed, Bare), EAS Build/Update/Submit, Expo Router vs React Navigation, pricing breakdown, decision matrix for STS |
| 03 | `03_STS_CODEBASE_MASTER.md` | Full codebase dissection — every screen (30+), every dependency (40+), Redux store shape, API layer, auth/MFA flow, Firebase, anti-patterns, and 7-phase rebuild roadmap |
| 04 | `04_STS_SKILLS_DEVELOPMENT_GUIDE.md` | Curriculum for every dependency in the STS stack — React Native core, React Navigation, Redux Toolkit, Axios, AsyncStorage, Firebase, Notifee, UI libs, media, build system — with deep docs and STS-specific usage |
| 05 | `05_PRACTICE_PROJECT_DESIGN.md` | "TaskVault" — a small practice RN CLI project with FastAPI + SQLite + Docker + Adminer backend, full CRUD, Redux Toolkit, typed Axios, architecture diagrams, and skills checklist |
| 06 | `06_TYPESCRIPT_MASTERCLASS.md` | TypeScript from compiler internals to advanced type gymnastics — 5-phase pipeline, generics, conditional/mapped types, utility types, and every RN pattern (hooks, navigation, RTK, Axios) fully typed |
| — | `RN_FUNDAMENTALS.md` | React Native fundamentals for developers coming from web React |

Start with: `tekkod_project/03_STS_CODEBASE_MASTER.md` (understand what exists), then `04_STS_SKILLS_DEVELOPMENT_GUIDE.md` (learn the tools), then `06_TYPESCRIPT_MASTERCLASS.md` (master the language).

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
| STS codebase analysis | `tekkod_project/03_STS_CODEBASE_MASTER.md` |
| STS skills curriculum | `tekkod_project/04_STS_SKILLS_DEVELOPMENT_GUIDE.md` |
| Practice project (TaskVault) | `tekkod_project/05_PRACTICE_PROJECT_DESIGN.md` |
| TypeScript masterclass | `tekkod_project/06_TYPESCRIPT_MASTERCLASS.md` |
| Backend exam plan | `preparation_examen/backend/Foundational/00_Vue_Ensemble.md` |
| Data Analyst exam plan | `preparation_examen/Data_analyst/Foundational/00_Vue_Ensemble.md` |
| Credit scoring architecture | `docs_project/scoring/design_document_credit_scoring.md` |
| Agentic AI course | `foundation_agentic/agentic_foundation/guide_fondations_agentic_ai.md` |
| Run Adminer | `adminer/docker-compose.yml` → `docker compose up -d` |

---

*APDE — Alexandro Disla. Last updated February 2026.*
