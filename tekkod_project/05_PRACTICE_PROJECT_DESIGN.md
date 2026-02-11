# Practice Project — "TaskVault"

> **Purpose**: A small, focused React Native CLI project that exercises the exact skills you need for the STS rebuild: fetching data from a REST API, performing CRUD operations against a SQLite database (running in Docker with Adminer), managing state with Redux Toolkit, and navigating between screens. Build this before touching STS.

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Architecture Diagram](#2-architecture-diagram)
3. [Technology Stack](#3-technology-stack)
4. [Backend Setup — Docker + SQLite + Adminer](#4-backend-setup)
5. [API Design — FastAPI REST Server](#5-api-design)
6. [React Native Project Setup](#6-react-native-project-setup)
7. [Project Structure](#7-project-structure)
8. [Feature Specifications](#8-feature-specifications)
9. [Screen-by-Screen Breakdown](#9-screen-by-screen-breakdown)
10. [State Management Design](#10-state-management-design)
11. [API Layer Design](#11-api-layer-design)
12. [Navigation Design](#12-navigation-design)
13. [Styling System](#13-styling-system)
14. [Commands Reference](#14-commands-reference)
15. [Build & Dev Workflow](#15-build--dev-workflow)
16. [Skills Checklist — What You'll Prove](#16-skills-checklist)

---

## 1. Project Overview

**TaskVault** is a personal task management app with two data sources:

1. **Remote API** — Fetches random user data from [JSONPlaceholder](https://jsonplaceholder.typicode.com) (public, free, no auth needed) to practice API fetching, loading states, and list rendering.
2. **Local API** — Your own FastAPI server backed by SQLite in Docker, where you perform full CRUD (Create, Read, Update, Delete) on personal tasks.

### What You'll Build

| Feature | STS Skill It Maps To |
|---------|---------------------|
| Fetch users list from API | Feed list, challenge list, leaderboard |
| Pull-to-refresh + pagination | Feed infinite scroll |
| Task CRUD (create, read, update, delete) | Profile edit, challenge accept, quiz submit |
| Redux Toolkit state management | Entire STS state layer |
| Axios with interceptors | STS API layer rebuild |
| Stack + Tab navigation | STS navigation (identical structure) |
| Form inputs with validation | Login, signup, OTP screens |
| Loading/error states | Global loading spinner, error alerts |
| AsyncStorage for persistence | Token storage, user data |
| TypeScript throughout | STS rebuild requirement |

---

## 2. Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           TASKVAULT ARCHITECTURE                         │
│                                                                          │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │                      REACT NATIVE APP                            │    │
│  │                    (Your phone / emulator)                        │    │
│  │                                                                   │    │
│  │  ┌────────────────────────────────────────────────────────────┐  │    │
│  │  │                   NAVIGATION                                │  │    │
│  │  │                                                             │  │    │
│  │  │  ┌──────────────────────────────────────────────────────┐  │  │    │
│  │  │  │            Stack Navigator                            │  │  │    │
│  │  │  │                                                       │  │  │    │
│  │  │  │  Splash Screen                                        │  │  │    │
│  │  │  │       ↓                                               │  │  │    │
│  │  │  │  ┌──────────────────────────────────────────────┐     │  │  │    │
│  │  │  │  │         Tab Navigator (Bottom Tabs)          │     │  │  │    │
│  │  │  │  │                                              │     │  │  │    │
│  │  │  │  │  ┌──────────┐  ┌───────────┐  ┌──────────┐  │     │  │  │    │
│  │  │  │  │  │  Users   │  │   Tasks   │  │ Settings │  │     │  │  │    │
│  │  │  │  │  │  (API)   │  │  (CRUD)   │  │          │  │     │  │  │    │
│  │  │  │  │  └──────────┘  └───────────┘  └──────────┘  │     │  │  │    │
│  │  │  │  └──────────────────────────────────────────────┘     │  │  │    │
│  │  │  │       ↓                    ↓                          │  │  │    │
│  │  │  │  User Detail         Task Form                        │  │  │    │
│  │  │  │  Screen              Screen                           │  │  │    │
│  │  │  └──────────────────────────────────────────────────────┘  │  │    │
│  │  └────────────────────────────────────────────────────────────┘  │    │
│  │                              │                                    │    │
│  │  ┌───────────────────────────▼────────────────────────────────┐  │    │
│  │  │                    STATE (Redux Toolkit)                    │  │    │
│  │  │                                                             │  │    │
│  │  │  ┌──────────┐  ┌──────────┐  ┌──────────┐                 │  │    │
│  │  │  │  Users   │  │  Tasks   │  │    UI    │                 │  │    │
│  │  │  │  Slice   │  │  Slice   │  │  Slice   │                 │  │    │
│  │  │  │ (remote) │  │ (local)  │  │ (loading │                 │  │    │
│  │  │  │          │  │          │  │  /toast)  │                 │  │    │
│  │  │  └────┬─────┘  └────┬─────┘  └──────────┘                 │  │    │
│  │  └───────┼──────────────┼─────────────────────────────────────┘  │    │
│  │          │              │                                         │    │
│  │  ┌───────▼──────────────▼─────────────────────────────────────┐  │    │
│  │  │                    API LAYER (Axios)                         │  │    │
│  │  │          Instance + Interceptors + Error Handling            │  │    │
│  │  └───────┬──────────────┬─────────────────────────────────────┘  │    │
│  │          │              │                                         │    │
│  └──────────┼──────────────┼─────────────────────────────────────────┘    │
│             │              │                                              │
│      ┌──────▼────┐  ┌─────▼──────────────────────────────────────────┐   │
│      │ Public    │  │        DOCKER ENVIRONMENT                       │   │
│      │ API       │  │                                                 │   │
│      │           │  │  ┌─────────────┐    ┌──────────────────────┐   │   │
│      │ JSON      │  │  │  FastAPI    │    │  Adminer             │   │   │
│      │ Placeholder│  │  │  Server     │    │  (DB GUI)            │   │   │
│      │           │  │  │  Port 8000  │    │  Port 8080           │   │   │
│      │ GET /users│  │  │             │    │                      │   │   │
│      │ GET /posts│  │  │  ┌────────┐ │    │  Browse tables       │   │   │
│      │           │  │  │  │ SQLite │ │    │  Run queries         │   │   │
│      └───────────┘  │  │  │   DB   │ │    │  View data           │   │   │
│                     │  │  └────────┘ │    │                      │   │   │
│                     │  └─────────────┘    └──────────────────────┘   │   │
│                     │        ↕ Volume mount (persistent data)        │   │
│                     └────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Technology Stack

### React Native App

| Tool | Version | Role | STS Equivalent |
|------|---------|------|----------------|
| React Native CLI | 0.76+ | Framework | RN 0.65 → 0.76+ |
| TypeScript | 5.x | Type safety | JS → TS migration |
| React Navigation v7 | latest | Navigation | React Navigation v6 → v7 |
| Redux Toolkit | latest | State management | Redux + Thunk → RTK |
| Axios | 1.x | HTTP client | Axios 0.21 → 1.x |
| AsyncStorage | latest | Local persistence | Same library |
| React Native Vector Icons | latest | Icons | Same library |
| React Native Elements (RNEUI) | v4 | UI components | RN Elements v3 → RNEUI v4 |

### Backend (Docker)

| Tool | Role |
|------|------|
| Docker + Docker Compose | Container orchestration |
| Python 3.12 + FastAPI | REST API server (async, auto-docs) |
| SQLModel (SQLAlchemy + Pydantic) | ORM + validation for SQLite |
| Uvicorn | ASGI server (runs FastAPI) |
| Adminer | Web-based DB browser (port 8080) |

---

## 4. Backend Setup

### Docker Architecture

```
docker-compose.yml
│
├── api-server (FastAPI + Uvicorn + SQLite)
│   ├── Port: 8000
│   ├── SQLite DB: /data/taskvault.db
│   ├── Swagger UI: http://localhost:8000/docs
│   ├── ReDoc: http://localhost:8000/redoc
│   └── Volume: ./data → /data (persistent)
│
└── adminer (Web DB Browser)
    ├── Port: 8080
    └── Connects to SQLite via volume
```

### docker-compose.yml

```yaml
version: "3.8"

services:
  api:
    build:
      context: ./backend
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    volumes:
      - ./backend/data:/data
      - ./backend/app:/app/app         # Hot reload: mount source (uvicorn --reload)
    environment:
      - DB_PATH=/data/taskvault.db
    restart: unless-stopped

  adminer:
    image: adminer:latest
    ports:
      - "8080:8080"
    environment:
      - ADMINER_DEFAULT_SERVER=sqlite
      - ADMINER_DESIGN=dracula
    volumes:
      - ./backend/data:/data           # Same volume — can see the DB
    restart: unless-stopped
```

### Backend Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /app

# Install uv (ultra-fast Python package manager)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Install dependencies via uv
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

# Copy application code
COPY app/ ./app/

# Create data directory for SQLite
RUN mkdir -p /data

EXPOSE 8000

# Run with --reload for dev (watches /app/app/ for changes via volume mount)
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

### Backend Project Structure

```
backend/
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml           ← Python project config + dependencies (managed by uv)
├── uv.lock                  ← Lockfile (deterministic installs, committed to git)
├── data/                    ← SQLite DB lives here (git-ignored, volume-mounted)
│   └── taskvault.db
└── app/
    ├── __init__.py
    ├── main.py              ← FastAPI app entry + CORS + lifespan (startup/shutdown)
    ├── database.py          ← SQLModel engine + session + create_tables()
    ├── models.py            ← SQLModel models (Task) + Pydantic schemas
    ├── seed.py              ← Seed data inserted on first run
    └── routers/
        ├── __init__.py
        └── tasks.py         ← CRUD route handlers (APIRouter)
```

### pyproject.toml

```toml
[project]
name = "taskvault-api"
version = "1.0.0"
description = "Practice CRUD API for React Native development"
requires-python = ">=3.12"
dependencies = [
    "fastapi>=0.115.0",
    "uvicorn[standard]>=0.34.0",
    "sqlmodel>=0.0.22",
    "aiosqlite>=0.21.0",
]
```

Generate the lockfile (run once locally, commit `uv.lock` to git):

```bash
uv lock
```

### Database Schema — SQLModel (Python ORM)

SQLModel combines SQLAlchemy (database ORM) and Pydantic (data validation) into one. You define your table AND your API schemas in a single place.

```python
# app/models.py
from datetime import datetime
from enum import Enum
from typing import Optional

from sqlmodel import Field, SQLModel


class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    done = "done"


class TaskPriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


# ========================
# DATABASE TABLE MODEL (creates the SQLite table)
# ========================
class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(min_length=1, max_length=200)
    description: str = Field(default="")
    status: TaskStatus = Field(default=TaskStatus.pending)
    priority: TaskPriority = Field(default=TaskPriority.medium)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


# ========================
# REQUEST SCHEMAS (what the client sends)
# ========================
class TaskCreate(SQLModel):
    title: str = Field(min_length=1, max_length=200)
    description: str = Field(default="")
    priority: TaskPriority = Field(default=TaskPriority.medium)


class TaskUpdate(SQLModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None
```

This generates the equivalent SQL:

```sql
CREATE TABLE IF NOT EXISTS task (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    title       VARCHAR(200) NOT NULL,
    description TEXT DEFAULT '',
    status      VARCHAR(11) DEFAULT 'pending',
    priority    VARCHAR(6) DEFAULT 'medium',
    created_at  DATETIME,
    updated_at  DATETIME
);
```

### Seed Data

```python
# app/seed.py
from app.models import Task, TaskStatus, TaskPriority

SEED_TASKS = [
    Task(title="Learn React Native Core", description="Study View, Text, FlatList, StyleSheet",
         status=TaskStatus.in_progress, priority=TaskPriority.high),
    Task(title="Set up Redux Toolkit", description="Configure store, create slices",
         status=TaskStatus.pending, priority=TaskPriority.high),
    Task(title="Build API layer with Axios", description="Create instance, add interceptors",
         status=TaskStatus.pending, priority=TaskPriority.medium),
    Task(title="Practice navigation", description="Stack + Tab navigation patterns",
         status=TaskStatus.pending, priority=TaskPriority.medium),
    Task(title="Study Firebase docs", description="FCM setup and notification handling",
         status=TaskStatus.done, priority=TaskPriority.low),
]
```

---

## 5. API Design

### Endpoints

```
┌──────────────────────────────────────────────────────────────────┐
│                    TASKVAULT API ENDPOINTS                         │
│                    Base URL: http://localhost:8000                 │
├──────────┬────────────────────┬──────────────────────────────────┤
│  Method  │  Endpoint          │  Description                     │
├──────────┼────────────────────┼──────────────────────────────────┤
│  GET     │  /api/tasks        │  List all tasks (with filters)   │
│  GET     │  /api/tasks/{id}   │  Get single task                 │
│  POST    │  /api/tasks        │  Create new task                 │
│  PUT     │  /api/tasks/{id}   │  Update existing task            │
│  DELETE  │  /api/tasks/{id}   │  Delete task                     │
│  GET     │  /api/health       │  Health check                    │
├──────────┼────────────────────┼──────────────────────────────────┤
│                    QUERY PARAMETERS                               │
├──────────┼────────────────────┼──────────────────────────────────┤
│  GET     │  ?status=pending   │  Filter by status                │
│  GET     │  ?priority=high    │  Filter by priority              │
│  GET     │  ?page=1&limit=10  │  Pagination                      │
│  GET     │  ?search=react     │  Search by title                 │
└──────────┴────────────────────┴──────────────────────────────────┘
```

### Request/Response Examples

```
GET /api/tasks?status=pending&page=1&limit=10

Response 200:
{
  "success": true,
  "data": [
    {
      "id": 1,
      "title": "Learn React Native Core",
      "description": "Study View, Text, FlatList, StyleSheet",
      "status": "pending",
      "priority": "high",
      "created_at": "2026-02-10T10:00:00.000Z",
      "updated_at": "2026-02-10T10:00:00.000Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 25,
    "totalPages": 3
  }
}

──────────────────────────────────────

POST /api/tasks
Body: {
  "title": "Build navigation",
  "description": "Stack + Tab setup",
  "priority": "high"
}

Response 201:
{
  "success": true,
  "data": {
    "id": 6,
    "title": "Build navigation",
    "description": "Stack + Tab setup",
    "status": "pending",
    "priority": "high",
    "created_at": "2026-02-11T14:00:00.000Z",
    "updated_at": "2026-02-11T14:00:00.000Z"
  }
}

──────────────────────────────────────

PUT /api/tasks/6
Body: {
  "status": "in_progress"
}

Response 200:
{
  "success": true,
  "data": { ...updatedTask }
}

──────────────────────────────────────

DELETE /api/tasks/6

Response 200:
{
  "success": true,
  "message": "Task deleted"
}
```

### FastAPI Route Handlers (Python)

This is what the actual backend code looks like. FastAPI auto-generates Swagger docs from these type annotations.

```python
# app/routers/tasks.py
from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select, func

from app.database import get_session
from app.models import Task, TaskCreate, TaskUpdate, TaskStatus, TaskPriority

router = APIRouter(prefix="/api/tasks", tags=["tasks"])


@router.get("/")
def list_tasks(
    status: Optional[TaskStatus] = None,
    priority: Optional[TaskPriority] = None,
    search: Optional[str] = None,
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=10, ge=1, le=100),
    session: Session = Depends(get_session),
):
    """List all tasks with optional filters and pagination."""
    query = select(Task)

    if status:
        query = query.where(Task.status == status)
    if priority:
        query = query.where(Task.priority == priority)
    if search:
        query = query.where(Task.title.contains(search))

    # Count total before pagination
    total = session.exec(select(func.count()).select_from(query.subquery())).one()

    # Apply pagination
    offset = (page - 1) * limit
    tasks = session.exec(query.offset(offset).limit(limit)).all()

    return {
        "success": True,
        "data": tasks,
        "pagination": {
            "page": page,
            "limit": limit,
            "total": total,
            "totalPages": (total + limit - 1) // limit,
        },
    }


@router.get("/{task_id}")
def get_task(task_id: int, session: Session = Depends(get_session)):
    """Get a single task by ID."""
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"success": True, "data": task}


@router.post("/", status_code=201)
def create_task(body: TaskCreate, session: Session = Depends(get_session)):
    """Create a new task."""
    task = Task.model_validate(body)
    session.add(task)
    session.commit()
    session.refresh(task)
    return {"success": True, "data": task}


@router.put("/{task_id}")
def update_task(task_id: int, body: TaskUpdate, session: Session = Depends(get_session)):
    """Update an existing task (partial update)."""
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    update_data = body.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(task, key, value)
    task.updated_at = datetime.utcnow()

    session.add(task)
    session.commit()
    session.refresh(task)
    return {"success": True, "data": task}


@router.delete("/{task_id}")
def delete_task(task_id: int, session: Session = Depends(get_session)):
    """Delete a task."""
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    session.delete(task)
    session.commit()
    return {"success": True, "message": "Task deleted"}
```

### FastAPI App Entry Point

```python
# app/main.py
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import create_db_and_tables
from app.routers import tasks


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Runs on startup: create tables + seed data."""
    create_db_and_tables()
    yield


app = FastAPI(
    title="TaskVault API",
    description="Practice CRUD API for React Native development",
    version="1.0.0",
    lifespan=lifespan,
)

# Allow all origins (for mobile dev — phone/emulator hitting localhost)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(tasks.router)


@app.get("/api/health")
def health_check():
    return {"status": "ok", "service": "taskvault-api"}
```

### Database Connection

```python
# app/database.py
import os
from sqlmodel import SQLModel, Session, create_engine

DB_PATH = os.environ.get("DB_PATH", "./data/taskvault.db")
DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(DATABASE_URL, echo=False)


def create_db_and_tables():
    """Create all tables defined by SQLModel subclasses."""
    SQLModel.metadata.create_all(engine)
    _seed_if_empty()


def get_session():
    """FastAPI dependency — yields a DB session per request."""
    with Session(engine) as session:
        yield session


def _seed_if_empty():
    """Insert seed data if the tasks table is empty."""
    from app.models import Task
    from app.seed import SEED_TASKS

    with Session(engine) as session:
        count = session.query(Task).count()
        if count == 0:
            for task in SEED_TASKS:
                session.add(task)
            session.commit()
```

### FastAPI Bonus — Built-in Swagger UI

```
┌──────────────────────────────────────────────────────────────────┐
│  One of the biggest advantages of FastAPI over Express:           │
│                                                                   │
│  When you visit http://localhost:8000/docs you get an             │
│  INTERACTIVE API explorer auto-generated from your Python         │
│  type annotations. You can:                                       │
│                                                                   │
│  • See all endpoints with their parameters                        │
│  • Try each endpoint directly in the browser                      │
│  • See request/response schemas (from Pydantic models)            │
│  • No Postman or curl needed for testing                          │
│                                                                   │
│  This means you can:                                              │
│  1. Start Docker                                                  │
│  2. Open http://localhost:8000/docs                               │
│  3. Test all CRUD operations visually                             │
│  4. THEN connect your React Native app                            │
│                                                                   │
│  The validation you define in TaskCreate/TaskUpdate Pydantic       │
│  models automatically returns 422 errors with clear messages      │
│  when the client sends bad data.                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## 6. React Native Project Setup

### Step-by-step Initialization

```bash
# ========================
# 1. CREATE THE PROJECT (React Native CLI with TypeScript)
# ========================
npx @react-native-community/cli init TaskVault --template react-native-template-typescript

cd TaskVault

# ========================
# 2. INSTALL NAVIGATION
# ========================
yarn add @react-navigation/native @react-navigation/stack @react-navigation/bottom-tabs
yarn add react-native-screens react-native-safe-area-context react-native-gesture-handler

# ========================
# 3. INSTALL STATE MANAGEMENT
# ========================
yarn add @reduxjs/toolkit react-redux

# ========================
# 4. INSTALL API & STORAGE
# ========================
yarn add axios @react-native-async-storage/async-storage

# ========================
# 5. INSTALL UI LIBRARIES
# ========================
yarn add @rneui/themed @rneui/base react-native-vector-icons

# ========================
# 6. LINK NATIVE DEPENDENCIES (Android)
# ========================
cd android && ./gradlew clean && cd ..

# For iOS (only on Mac):
# cd ios && pod install && cd ..

# ========================
# 7. VERIFY SETUP
# ========================
npx react-native run-android
```

### Configure TypeScript Path Aliases

**babel.config.js**:
```javascript
module.exports = {
  presets: ['module:@react-native/babel-preset'],
  plugins: [
    [
      'module-resolver',
      {
        root: ['./src'],
        alias: {
          '@screens': './src/screens',
          '@components': './src/components',
          '@store': './src/store',
          '@api': './src/api',
          '@navigation': './src/navigation',
          '@themes': './src/themes',
          '@utils': './src/utils',
          '@types': './src/types',
        },
      },
    ],
  ],
};
```

Install the Babel plugin:
```bash
yarn add --dev babel-plugin-module-resolver
```

**tsconfig.json** (add paths):
```json
{
  "compilerOptions": {
    "baseUrl": "./src",
    "paths": {
      "@screens/*": ["screens/*"],
      "@components/*": ["components/*"],
      "@store/*": ["store/*"],
      "@api/*": ["api/*"],
      "@navigation/*": ["navigation/*"],
      "@themes/*": ["themes/*"],
      "@utils/*": ["utils/*"],
      "@types/*": ["types/*"]
    }
  }
}
```

---

## 7. Project Structure

```
TaskVault/
├── android/                         ← Native Android project
├── ios/                             ← Native iOS project
├── backend/                         ← Docker backend
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── pyproject.toml               ← Python deps (FastAPI, SQLModel, Uvicorn)
│   ├── uv.lock                      ← Deterministic lockfile (committed to git)
│   ├── data/                        ← SQLite DB (volume-mounted)
│   └── app/
│       ├── __init__.py
│       ├── main.py                  ← FastAPI app entry + CORS + lifespan
│       ├── database.py              ← SQLModel engine + session
│       ├── models.py                ← SQLModel models + Pydantic schemas
│       ├── seed.py                  ← Seed data
│       └── routers/
│           ├── __init__.py
│           └── tasks.py             ← CRUD route handlers (APIRouter)
│
├── src/                             ← React Native source
│   ├── api/                         ← Axios configuration
│   │   ├── client.ts                ← Axios instance + interceptors
│   │   ├── endpoints.ts             ← API endpoint constants
│   │   └── index.ts
│   │
│   ├── store/                       ← Redux Toolkit
│   │   ├── index.ts                 ← configureStore
│   │   ├── hooks.ts                 ← Typed useSelector/useDispatch
│   │   └── slices/
│   │       ├── usersSlice.ts        ← Remote users (JSONPlaceholder)
│   │       ├── tasksSlice.ts        ← Local tasks (CRUD)
│   │       └── uiSlice.ts           ← Loading, toast, error states
│   │
│   ├── navigation/                  ← React Navigation
│   │   ├── AppNavigator.tsx         ← Root NavigationContainer
│   │   ├── StackNavigator.tsx       ← Stack screens
│   │   ├── TabNavigator.tsx         ← Bottom tabs
│   │   └── types.ts                 ← Navigation type definitions
│   │
│   ├── screens/                     ← Screen components
│   │   ├── SplashScreen.tsx
│   │   ├── UsersScreen.tsx          ← API data list
│   │   ├── UserDetailScreen.tsx     ← API detail view
│   │   ├── TasksScreen.tsx          ← Task CRUD list
│   │   ├── TaskFormScreen.tsx       ← Create/Edit task form
│   │   └── SettingsScreen.tsx       ← App settings
│   │
│   ├── components/                  ← Reusable components
│   │   ├── UserCard.tsx             ← User list item
│   │   ├── TaskCard.tsx             ← Task list item with swipe actions
│   │   ├── LoadingOverlay.tsx       ← Global loading spinner
│   │   ├── ErrorBanner.tsx          ← Error display
│   │   ├── EmptyState.tsx           ← Empty list placeholder
│   │   └── StatusBadge.tsx          ← Status/priority badges
│   │
│   ├── themes/                      ← Styling constants
│   │   ├── colors.ts
│   │   ├── typography.ts
│   │   ├── spacing.ts
│   │   └── index.ts
│   │
│   ├── types/                       ← TypeScript type definitions
│   │   ├── user.ts                  ← User type (from JSONPlaceholder)
│   │   ├── task.ts                  ← Task type (from your API)
│   │   └── api.ts                   ← API response types
│   │
│   ├── utils/                       ← Utility functions
│   │   ├── storage.ts               ← AsyncStorage helpers
│   │   └── validation.ts            ← Form validation
│   │
│   └── App.tsx                      ← Root component (Provider + Navigation)
│
├── index.js                         ← RN entry point
├── app.json
├── package.json
├── tsconfig.json
├── babel.config.js
└── .prettierrc
```

---

## 8. Feature Specifications

### Feature 1: Users List (Remote API)

**Maps to STS**: Feed list, Challenge list, Leaderboard

```
┌─────────────────────────────────┐
│  Users                    🔍    │  ← Header with search
├─────────────────────────────────┤
│  ↓ Pull to refresh              │
│                                  │
│  ┌───────────────────────────┐  │
│  │ 👤 Leanne Graham          │  │  ← UserCard component
│  │    @Bret                   │  │
│  │    leanne@april.biz        │  │
│  │    Romaguera-Crona    →    │  │  ← Tap to see detail
│  └───────────────────────────┘  │
│                                  │
│  ┌───────────────────────────┐  │
│  │ 👤 Ervin Howell            │  │
│  │    @Antonette              │  │
│  │    ervin@melissa.tv        │  │
│  │    Deckow-Crist       →    │  │
│  └───────────────────────────┘  │
│                                  │
│  ... (FlatList with 10 users)   │
│                                  │
│  ┌───────────────────────────┐  │
│  │    Loading more...         │  │  ← Pagination footer
│  └───────────────────────────┘  │
│                                  │
├─────────┬───────────┬───────────┤
│  Users  │   Tasks   │ Settings  │  ← Bottom tabs
│  (•)    │           │           │
└─────────┴───────────┴───────────┘
```

**Data source**: `GET https://jsonplaceholder.typicode.com/users`

**Skills practiced**:
- `FlatList` with `renderItem`, `keyExtractor`
- Pull-to-refresh (`RefreshControl`)
- Loading states
- Error handling
- Navigation to detail screen with params

### Feature 2: Tasks CRUD (Local API)

**Maps to STS**: Profile edit, Challenge accept/complete, Quiz submit

```
┌─────────────────────────────────┐
│  My Tasks                  ＋   │  ← Header with Add button
├─────────────────────────────────┤
│  ┌─ Filter: All | Pending | ─┐ │  ← Status filter tabs
│  │  In Progress | Done        │ │
│  └────────────────────────────┘ │
│                                  │
│  ┌───────────────────────────┐  │
│  │ ● Learn React Native Core │  │  ← TaskCard
│  │   Study View, Text, Flat. │  │
│  │   🔴 HIGH    🟡 In Prog  │  │  ← Priority + Status badges
│  │   Feb 10, 2026            │  │
│  │              ✏️  🗑️       │  │  ← Edit / Delete buttons
│  └───────────────────────────┘  │
│                                  │
│  ┌───────────────────────────┐  │
│  │ ○ Set up Redux Toolkit    │  │
│  │   Configure store, create │  │
│  │   🔴 HIGH    ⚪ Pending   │  │
│  │   Feb 10, 2026            │  │
│  │              ✏️  🗑️       │  │
│  └───────────────────────────┘  │
│                                  │
│  ... (FlatList with tasks)      │
│                                  │
├─────────┬───────────┬───────────┤
│  Users  │   Tasks   │ Settings  │
│         │   (•)     │           │
└─────────┴───────────┴───────────┘
```

**Data source**: `http://<your-ip>:8000/api/tasks`

**Skills practiced**:
- Full CRUD operations via Axios
- Redux Toolkit async thunks (fetchTasks, createTask, updateTask, deleteTask)
- Form screen (TextInput, picker for status/priority)
- Optimistic UI updates
- Confirmation dialogs before delete
- Filter/search

### Feature 3: Task Form (Create / Edit)

**Maps to STS**: Signup multi-step form, Profile edit

```
┌─────────────────────────────────┐
│  ← Back     New Task     Save   │  ← Header with Save button
├─────────────────────────────────┤
│                                  │
│  Title *                         │
│  ┌───────────────────────────┐  │
│  │ Build navigation           │  │  ← TextInput
│  └───────────────────────────┘  │
│                                  │
│  Description                     │
│  ┌───────────────────────────┐  │
│  │ Set up Stack + Tab        │  │  ← Multiline TextInput
│  │ navigators with proper    │  │
│  │ TypeScript types          │  │
│  └───────────────────────────┘  │
│                                  │
│  Priority                        │
│  ┌──────┐ ┌────────┐ ┌──────┐  │
│  │ Low  │ │ Medium │ │ High │  │  ← Segmented control
│  └──────┘ └────────┘ └──────┘  │
│                 ●                │
│  Status                          │
│  ┌─────────┐ ┌──────────┐ ┌──┐ │
│  │ Pending │ │ Progress │ │D │ │
│  └─────────┘ └──────────┘ └──┘ │
│       ●                          │
│                                  │
│  ┌───────────────────────────┐  │
│  │        Save Task           │  │  ← Submit button
│  └───────────────────────────┘  │
│                                  │
└─────────────────────────────────┘
```

**Skills practiced**:
- Controlled form inputs
- Form validation (title required, min length)
- Conditional rendering (Create vs Edit mode)
- Keyboard avoidance (`KeyboardAvoidingView`)
- Navigation params (passing task data for edit mode)

---

## 9. Screen-by-Screen Breakdown

| Screen | Type | Purpose | Key Components | Redux Slice |
|--------|------|---------|---------------|-------------|
| `SplashScreen` | Stack | App init, check stored settings | Lottie animation or logo | ui |
| `UsersScreen` | Tab | List users from JSONPlaceholder | FlatList, UserCard, SearchBar | users |
| `UserDetailScreen` | Stack | User profile + their posts | ScrollView, sections | users |
| `TasksScreen` | Tab | Task list with CRUD | FlatList, TaskCard, filters | tasks |
| `TaskFormScreen` | Stack | Create/Edit task form | TextInput, pickers, validation | tasks |
| `SettingsScreen` | Tab | App settings, clear storage | Switches, buttons | ui |

---

## 10. State Management Design

### Store Shape

```typescript
// store/index.ts
import { configureStore } from '@reduxjs/toolkit';
import usersReducer from './slices/usersSlice';
import tasksReducer from './slices/tasksSlice';
import uiReducer from './slices/uiSlice';

export const store = configureStore({
  reducer: {
    users: usersReducer,
    tasks: tasksReducer,
    ui: uiReducer,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
```

### Typed Hooks

```typescript
// store/hooks.ts
import { useDispatch, useSelector, TypedUseSelectorHook } from 'react-redux';
import type { RootState, AppDispatch } from './index';

export const useAppDispatch = () => useDispatch<AppDispatch>();
export const useAppSelector: TypedUseSelectorHook<RootState> = useSelector;
```

### Users Slice (Remote Data)

```
┌─────────────────────────────────────────────┐
│              usersSlice                       │
│                                               │
│  State:                                       │
│  ├── items: User[]          (fetched users)   │
│  ├── selectedUser: User | null                │
│  ├── loading: boolean                         │
│  ├── error: string | null                     │
│  └── searchQuery: string                      │
│                                               │
│  Async Thunks:                                │
│  ├── fetchUsers()           GET /users        │
│  └── fetchUserById(id)      GET /users/:id    │
│                                               │
│  Reducers:                                    │
│  ├── setSearchQuery(query)                    │
│  └── clearSelectedUser()                      │
└─────────────────────────────────────────────┘
```

### Tasks Slice (Local CRUD)

```
┌─────────────────────────────────────────────┐
│              tasksSlice                       │
│                                               │
│  State:                                       │
│  ├── items: Task[]          (all tasks)       │
│  ├── loading: boolean                         │
│  ├── error: string | null                     │
│  ├── filter: 'all'|'pending'|'in_progress'|'done'│
│  └── pagination: { page, total, totalPages }  │
│                                               │
│  Async Thunks:                                │
│  ├── fetchTasks(filters)    GET /api/tasks    │
│  ├── createTask(data)       POST /api/tasks   │
│  ├── updateTask({id, data}) PUT /api/tasks/{id}│
│  └── deleteTask(id)         DELETE /api/tasks/{id}│
│                                               │
│  Reducers:                                    │
│  └── setFilter(status)                        │
└─────────────────────────────────────────────┘
```

### UI Slice (Global State)

```
┌─────────────────────────────────────────────┐
│              uiSlice                         │
│                                               │
│  State:                                       │
│  ├── globalLoading: boolean                   │
│  ├── toast: { visible, title, message, type } │
│  └── theme: 'light' | 'dark'                 │
│                                               │
│  Reducers:                                    │
│  ├── showLoading()                            │
│  ├── hideLoading()                            │
│  ├── showToast({ title, message, type })      │
│  ├── hideToast()                              │
│  └── toggleTheme()                            │
└─────────────────────────────────────────────┘
```

---

## 11. API Layer Design

### Axios Client Setup

```
┌─────────────────────────────────────────────────────────────┐
│                    API LAYER ARCHITECTURE                     │
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  client.ts — Axios Instance                          │    │
│  │                                                       │    │
│  │  ┌───────────────────────────────────────────────┐   │    │
│  │  │  Request Interceptor                           │   │    │
│  │  │  • Log request method + URL                    │   │    │
│  │  │  • Attach any stored token (if you add auth)   │   │    │
│  │  └───────────────────────────────────────────────┘   │    │
│  │                      ↓                                │    │
│  │  ┌───────────────────────────────────────────────┐   │    │
│  │  │  HTTP Request                                  │   │    │
│  │  │  axios.get / .post / .put / .delete            │   │    │
│  │  └───────────────────────────────────────────────┘   │    │
│  │                      ↓                                │    │
│  │  ┌───────────────────────────────────────────────┐   │    │
│  │  │  Response Interceptor                          │   │    │
│  │  │  • Transform response data                     │   │    │
│  │  │  • Handle 4xx/5xx errors uniformly             │   │    │
│  │  │  • Log errors                                  │   │    │
│  │  └───────────────────────────────────────────────┘   │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
│  Two client instances:                                        │
│  ┌──────────────────────┐  ┌──────────────────────┐         │
│  │ publicApi             │  │ localApi             │         │
│  │ base: jsonplaceholder │  │ base: localhost:8000 │         │
│  │ (read-only, public)   │  │ (CRUD, your server)  │         │
│  └──────────────────────┘  └──────────────────────┘         │
└─────────────────────────────────────────────────────────────┘
```

### Example Client Code

```typescript
// src/api/client.ts
import axios from 'axios';
import { Platform } from 'react-native';

// Android emulator uses 10.0.2.2 to reach host machine's localhost
// Physical device uses your machine's local IP (e.g., 192.168.x.x)
const LOCAL_BASE = Platform.select({
  android: 'http://10.0.2.2:8000',       // Android emulator
  ios: 'http://localhost:8000',            // iOS simulator
  default: 'http://localhost:8000',
});

// Public API client (JSONPlaceholder)
export const publicApi = axios.create({
  baseURL: 'https://jsonplaceholder.typicode.com',
  timeout: 10000,
});

// Local API client (your Docker server)
export const localApi = axios.create({
  baseURL: `${LOCAL_BASE}/api`,
  timeout: 10000,
  headers: { 'Content-Type': 'application/json' },
});

// Response interceptor — normalize errors
[publicApi, localApi].forEach((client) => {
  client.interceptors.response.use(
    (response) => response,
    (error) => {
      const message = error.response?.data?.message
        || error.message
        || 'Something went wrong';
      console.error(`[API Error] ${error.config?.url}: ${message}`);
      return Promise.reject({ message, status: error.response?.status });
    }
  );
});
```

---

## 12. Navigation Design

### Navigation Tree

```
┌──────────────────────────────────────────────────────────┐
│                 NavigationContainer                        │
│                                                            │
│  ┌──────────────────────────────────────────────────┐     │
│  │              Stack.Navigator                      │     │
│  │                                                    │     │
│  │  ┌────────────────────────────────────────────┐   │     │
│  │  │  "Splash"         → SplashScreen           │   │     │
│  │  │  (headerShown: false)                       │   │     │
│  │  └────────────────────────────────────────────┘   │     │
│  │                     ↓                              │     │
│  │  ┌────────────────────────────────────────────┐   │     │
│  │  │  "Main"           → TabNavigator           │   │     │
│  │  │  (headerShown: false)                       │   │     │
│  │  │                                             │   │     │
│  │  │  ┌──────────┬──────────┬──────────────┐    │   │     │
│  │  │  │  Users   │  Tasks   │  Settings     │    │   │     │
│  │  │  │  Tab     │  Tab     │  Tab          │    │   │     │
│  │  │  └──────────┴──────────┴──────────────┘    │   │     │
│  │  └────────────────────────────────────────────┘   │     │
│  │                     ↓                              │     │
│  │  ┌────────────────────────────────────────────┐   │     │
│  │  │  "UserDetail"     → UserDetailScreen       │   │     │
│  │  │  (slides in from right)                     │   │     │
│  │  └────────────────────────────────────────────┘   │     │
│  │                                                    │     │
│  │  ┌────────────────────────────────────────────┐   │     │
│  │  │  "TaskForm"       → TaskFormScreen         │   │     │
│  │  │  (slides in from right)                     │   │     │
│  │  │  params: { task?: Task }                    │   │     │
│  │  └────────────────────────────────────────────┘   │     │
│  │                                                    │     │
│  └──────────────────────────────────────────────────┘     │
└──────────────────────────────────────────────────────────┘
```

### Navigation Types (TypeScript)

```typescript
// src/navigation/types.ts
import type { StackScreenProps } from '@react-navigation/stack';
import type { BottomTabScreenProps } from '@react-navigation/bottom-tabs';
import type { Task } from '@types/task';

// Stack params
export type RootStackParamList = {
  Splash: undefined;
  Main: undefined;
  UserDetail: { userId: number };
  TaskForm: { task?: Task };              // undefined = create, task = edit
};

// Tab params
export type MainTabParamList = {
  Users: undefined;
  Tasks: undefined;
  Settings: undefined;
};

// Screen props (use these in screen components)
export type UserDetailProps = StackScreenProps<RootStackParamList, 'UserDetail'>;
export type TaskFormProps = StackScreenProps<RootStackParamList, 'TaskForm'>;
export type UsersScreenProps = BottomTabScreenProps<MainTabParamList, 'Users'>;
```

---

## 13. Styling System

### Color Palette

```typescript
// src/themes/colors.ts
export const COLORS = {
  // Primary
  PRIMARY: '#4A6CF7',
  PRIMARY_LIGHT: '#E8EEFF',
  PRIMARY_DARK: '#3451B2',

  // Status
  SUCCESS: '#22C55E',
  WARNING: '#F59E0B',
  ERROR: '#EF4444',
  INFO: '#3B82F6',

  // Neutral
  WHITE: '#FFFFFF',
  BACKGROUND: '#F8FAFC',
  CARD: '#FFFFFF',
  BORDER: '#E2E8F0',
  TEXT_PRIMARY: '#1E293B',
  TEXT_SECONDARY: '#64748B',
  TEXT_MUTED: '#94A3B8',
  PLACEHOLDER: '#CBD5E1',

  // Priority
  PRIORITY_HIGH: '#EF4444',
  PRIORITY_MEDIUM: '#F59E0B',
  PRIORITY_LOW: '#22C55E',
} as const;
```

### Typography

```typescript
// src/themes/typography.ts
import { StyleSheet } from 'react-native';
import { COLORS } from './colors';

export const TYPOGRAPHY = StyleSheet.create({
  h1: { fontSize: 28, fontWeight: '700', color: COLORS.TEXT_PRIMARY, lineHeight: 36 },
  h2: { fontSize: 22, fontWeight: '700', color: COLORS.TEXT_PRIMARY, lineHeight: 28 },
  h3: { fontSize: 18, fontWeight: '600', color: COLORS.TEXT_PRIMARY, lineHeight: 24 },
  body: { fontSize: 16, fontWeight: '400', color: COLORS.TEXT_PRIMARY, lineHeight: 24 },
  bodySmall: { fontSize: 14, fontWeight: '400', color: COLORS.TEXT_SECONDARY, lineHeight: 20 },
  caption: { fontSize: 12, fontWeight: '500', color: COLORS.TEXT_MUTED, lineHeight: 16 },
  button: { fontSize: 16, fontWeight: '600', color: COLORS.WHITE, lineHeight: 24 },
});
```

---

## 14. Commands Reference

### Docker Backend

```bash
# ========================
# START BACKEND
# ========================
cd backend
docker compose up -d                  # Start FastAPI server + Adminer in background
docker compose logs -f api            # Watch API server logs (uvicorn output)
docker compose ps                     # Check running containers

# ========================
# ACCESS FASTAPI DOCS (built-in!)
# ========================
# Swagger UI:  http://localhost:8000/docs     ← Interactive API testing
# ReDoc:       http://localhost:8000/redoc    ← Beautiful API documentation
# Health:      http://localhost:8000/api/health

# ========================
# ACCESS ADMINER (DB Browser)
# ========================
# Open: http://localhost:8080
# System: SQLite3
# Database: /data/taskvault.db
# (No username/password needed for SQLite)

# ========================
# STOP BACKEND
# ========================
docker compose down                   # Stop containers
docker compose down -v                # Stop + remove volumes (reset DB)

# ========================
# REBUILD AFTER CODE CHANGES
# ========================
docker compose up -d --build          # Rebuild image and restart
# Note: uvicorn --reload watches for file changes via volume mount,
# so most Python changes are picked up automatically without rebuilding.

# ========================
# RESET DATABASE
# ========================
rm backend/data/taskvault.db          # Delete DB file
docker compose restart api            # Server recreates it with seed data
```

### React Native App

```bash
# ========================
# DEVELOPMENT
# ========================
npx react-native start                        # Start Metro bundler
npx react-native start --reset-cache          # Start with cache cleared

npx react-native run-android                  # Build + install + run on Android
npx react-native run-android --device         # Run on physical device only
npx react-native run-android --variant=debug  # Explicit debug build

# ========================
# ANDROID EMULATOR
# ========================
emulator -list-avds                            # List available emulators
emulator -avd Pixel_7_API_34                   # Start emulator by name
adb devices                                    # List connected devices
adb reverse tcp:8000 tcp:8000                  # Forward port (physical device)

# ========================
# DEBUGGING
# ========================
npx react-native log-android                   # View Android logs
adb logcat *:E                                 # View Android error logs only
npx react-native doctor                        # Check environment setup

# ========================
# CLEANING (when builds fail)
# ========================
cd android && ./gradlew clean && cd ..         # Clean Android build
rm -rf node_modules && yarn install            # Reset dependencies
npx react-native start --reset-cache          # Clear Metro cache
watchman watch-del-all                         # Clear watchman (if installed)

# ========================
# TYPE CHECKING
# ========================
npx tsc --noEmit                               # Check TypeScript errors
npx tsc --noEmit --watch                       # Watch mode
```

---

## 15. Build & Dev Workflow

### Daily Development Flow

```
┌──────────────────────────────────────────────────────────────┐
│                    DEVELOPMENT WORKFLOW                        │
│                                                                │
│  Terminal 1:                                                   │
│  $ cd backend && docker compose up -d                          │
│  ✓ FastAPI server running on http://localhost:8000             │
│  ✓ Swagger docs at http://localhost:8000/docs                  │
│  ✓ Adminer running on http://localhost:8080                    │
│                                                                │
│  Terminal 2:                                                   │
│  $ npx react-native start                                     │
│  ✓ Metro bundler running on http://localhost:8081              │
│                                                                │
│  Terminal 3:                                                   │
│  $ npx react-native run-android                                │
│  ✓ App installed and running on emulator/device                │
│                                                                │
│  Now:                                                          │
│  • Edit src/ files → Metro auto-reloads the app               │
│  • Edit backend/ files → Uvicorn auto-reloads (--reload flag) │
│  • View DB → Open http://localhost:8080 in browser             │
│  • Shake phone or Ctrl+M → Open React Native DevTools         │
│                                                                │
│  Physical device extra step:                                   │
│  $ adb reverse tcp:8000 tcp:8000                               │
│  $ adb reverse tcp:8081 tcp:8081                               │
│  (Forwards ports from device to your machine)                  │
└──────────────────────────────────────────────────────────────┘
```

### Build Sequence Diagram

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│  Write   │    │  Metro   │    │  Gradle  │    │  Device  │
│  Code    │───►│  Bundles │───►│  Builds  │───►│  Runs    │
│  (TSX)   │    │  JS      │    │  APK     │    │  App     │
└──────────┘    └──────────┘    └──────────┘    └──────────┘
     │               │               │               │
     │  Save file    │  < 1 sec      │  First time   │  Hot
     │───────────────►  hot reload   │  only: 2-5min │  reload
     │               │               │               │  < 1sec
     │               │               │               │
```

---

## 16. Skills Checklist — What You'll Prove

After completing TaskVault, check off each skill:

### React Native Core
- [ ] Built screens using `View`, `Text`, `TextInput`, `Image`
- [ ] Used `FlatList` with `renderItem`, `keyExtractor`, `ListEmptyComponent`
- [ ] Implemented pull-to-refresh with `RefreshControl`
- [ ] Created reusable components with props and TypeScript types
- [ ] Used `StyleSheet.create` for all styles
- [ ] Handled platform differences with `Platform.select`

### Navigation
- [ ] Set up `NavigationContainer` + `Stack.Navigator`
- [ ] Set up `Bottom Tab Navigator` with custom icons
- [ ] Navigated between screens with `navigation.navigate` and params
- [ ] Read params with `route.params`
- [ ] Customized headers (title, buttons, visibility)
- [ ] Used TypeScript for navigation types (`RootStackParamList`)

### State Management
- [ ] Created Redux store with `configureStore`
- [ ] Built slices with `createSlice` (sync reducers)
- [ ] Built async thunks with `createAsyncThunk` (API calls)
- [ ] Handled `pending`, `fulfilled`, `rejected` states
- [ ] Used `useAppSelector` and `useAppDispatch` hooks
- [ ] Managed global UI state (loading, toast/error)

### API Layer
- [ ] Created Axios instances with `axios.create`
- [ ] Made GET, POST, PUT, DELETE requests
- [ ] Used query parameters for filtering/pagination
- [ ] Added request/response interceptors
- [ ] Handled errors (network, 4xx, 5xx)
- [ ] Connected Android device/emulator to localhost API

### Forms & Validation
- [ ] Built controlled form with `TextInput` + `useState`
- [ ] Validated required fields and showed error messages
- [ ] Used `KeyboardAvoidingView` for keyboard handling
- [ ] Implemented create AND edit flows in one form screen

### Docker & Backend
- [ ] Wrote `docker-compose.yml` with multiple services
- [ ] Built FastAPI server with CRUD endpoints and auto-generated Swagger docs
- [ ] Used SQLModel (SQLAlchemy + Pydantic) for SQLite ORM + validation
- [ ] Used SQLite for persistent storage
- [ ] Browsed database with Adminer
- [ ] Tested API endpoints via FastAPI Swagger UI (`/docs`)
- [ ] Understood port forwarding for mobile development

### TypeScript
- [ ] Typed all props, state, and function parameters
- [ ] Created interfaces for API response types
- [ ] Used navigation type parameters
- [ ] Used typed Redux hooks

---

### Completion Criteria

When all checkboxes above are checked, you are ready to start the STS rebuild. Every pattern in TaskVault maps directly to something in the STS codebase:

```
┌─────────────────────────────────────────────────────────────────┐
│              TASKVAULT → STS SKILL MAPPING                       │
│                                                                  │
│  TaskVault Feature              STS Equivalent                   │
│  ─────────────────              ──────────────                   │
│  Users list (FlatList)     →    Feed list, Challenge list        │
│  Pull to refresh           →    Feed refresh                     │
│  User detail screen        →    Feed detail, Challenge detail    │
│  Task CRUD                 →    Profile edit, Quiz submit        │
│  Task form (create/edit)   →    Signup flow, Edit profile        │
│  Status filter tabs        →    Feed filter, Tag filter          │
│  Redux async thunks        →    All API-driven actions           │
│  Axios interceptors        →    Auth header, 401 handling        │
│  Stack + Tab navigation    →    Exact same STS structure         │
│  Loading/error overlays    →    Global LoadingIndicator, Alert   │
│  AsyncStorage              →    Token & user data storage        │
│  TypeScript types          →    Entire rebuild is TypeScript     │
│  Docker backend            →    Understanding API contracts      │
└─────────────────────────────────────────────────────────────────┘
```

---

> **Timeline**: This project should take **2-3 focused days**. Day 1: Backend + project setup + navigation. Day 2: Redux + API layer + Users screen. Day 3: Tasks CRUD + form + polish. By the end, you'll have muscle memory for every pattern the STS rebuild requires.
