# Python Web Application

Notes application built for a structured learning journey:
- Frontend: React (Vite)
- Backend: FastAPI
- Database: PostgreSQL-ready with SQLAlchemy (SQLite default for local quick start)
- Auth target: Microsoft Entra ID (planned in Week 3)

## Scope (Week 1 Day 1)

Build a small Notes app where a signed-in user can create and view personal notes. For local development in Week 1, user identity is temporarily simulated as a fixed local user.

## User Stories

1. As a user, I want to create a note with title and body so I can capture information quickly.
2. As a user, I want to view my notes in a list so I can read what I saved.
3. As a user, I want my notes isolated to my account so I do not see other users' data.

## Acceptance Criteria

1. The API exposes a health endpoint that returns success.
2. A note can be created with a non-empty title and non-empty body.
3. The notes list endpoint returns notes for the current user only.
4. The frontend can create a note and show the new note in the list.
5. The app runs locally with documented setup steps for frontend and backend.

## Project Layout

- frontend: React app for Notes UI
- backend: FastAPI app with SQLAlchemy models and CRUD endpoints
- docs: architecture and runbook notes (to be expanded)
- infra: Docker and Kubernetes assets (to be expanded)

## Quick Start

### Backend

1. Go to backend folder: `cd backend`
2. Create virtual environment and activate it
3. Install dependencies: `pip install -r requirements.txt`
4. Copy environment file: `copy .env.example .env`
5. Start API: `uvicorn app.main:app --reload`

### Frontend

1. Open a second terminal and go to frontend folder: `cd frontend`
2. Install dependencies: `npm install`
3. Copy environment file: `copy .env.example .env`
4. Start app: `npm run dev`

### Local URLs

- Frontend: http://localhost:5173
- Backend API docs: http://127.0.0.1:8000/docs
