# First 2 Weeks Plan Checklist

## Goal
Build a simple, deployable web application foundation with:
- React frontend
- FastAPI backend
- PostgreSQL database
- SQLAlchemy ORM + Alembic migrations
- Microsoft Entra ID for OAuth/OIDC (planned integration)
- Core CRUD flow
- Test baseline
- Clear runbook for local setup

---

## Week 1: Architecture + Backend Core
Target outcome: API with one core resource, database persistence, migrations, and tests running locally.

### Day 1: Scope and Setup
- [ ] Define one tiny app feature (example: Notes with title, body, tags)
- [ ] Write 3 user stories
- [ ] Write 5 acceptance criteria
- [ ] Create frontend and backend projects

Deliverables:
- [ ] Project initialized
- [ ] README includes scope, user stories, and acceptance criteria

### Day 2: Backend Skeleton
- [ ] Create FastAPI app structure
- [ ] Add `/health` endpoint
- [ ] Add environment-based configuration
- [ ] Add SQLAlchemy base/session setup scaffold
- [ ] Add local run scripts/commands

Deliverables:
- [ ] Health endpoint returns success
- [ ] Environment config loads correctly

### Day 3: Database Model + Migration
- [ ] Install PostgreSQL locally (or run via container)
- [ ] Create first SQLAlchemy model: Note (`id`, `user_id`, `title`, `body`, `created_at`, `updated_at`)
- [ ] Set up migration tooling (Alembic)
- [ ] Generate and apply initial migration

Deliverables:
- [ ] Schema created from migration
- [ ] Model maps correctly to DB table

### Day 4: CRUD Endpoints
- [ ] Implement create Note endpoint
- [ ] Implement list Notes endpoint
- [ ] Implement update Note endpoint
- [ ] Implement delete Note endpoint
- [ ] Add pagination on list endpoint
- [ ] Add input validation and clear error responses

Deliverables:
- [ ] Full CRUD works via API
- [ ] Manual test collection prepared (curl/Postman)

### Day 5: Service Layer + Tests
- [ ] Move business logic into service layer
- [ ] Add unit tests for service methods
- [ ] Add integration tests for API endpoints
- [ ] Add one-command test run

Deliverables:
- [ ] Test suite passes locally
- [ ] Coverage for create/list/update/delete paths

### Day 6: API Quality Pass
- [ ] Standardize response schemas
- [ ] Add request/response examples in API docs
- [ ] Add centralized exception handling
- [ ] Validate OpenAPI documentation quality

Deliverables:
- [ ] Clean API docs
- [ ] Consistent error format

### Day 7: Buffer + Review
- [ ] Resolve technical debt from Days 1-6
- [ ] Refactor naming and module boundaries
- [ ] Write short retrospective notes

Deliverables:
- [ ] Stable backend baseline
- [ ] Week 1 retrospective captured

### Week 1 Definition of Done
- [ ] CRUD works end-to-end against PostgreSQL
- [ ] Migrations are reproducible on a clean setup
- [ ] Automated tests run in one command
- [ ] API docs are understandable for a new developer

---

## Week 2: React Frontend + API Integration
Target outcome: Usable UI connected to backend CRUD with solid loading/error handling.

### Day 1: Frontend Foundation
- [ ] Create React app (Vite)
- [ ] Add routing structure
- [ ] Add base layout and navigation
- [ ] Create API client module

Deliverables:
- [ ] Frontend runs locally
- [ ] Route structure ready for Notes screens

### Day 2: Notes List Screen
- [ ] Build Notes list view
- [ ] Fetch and render Notes from backend
- [ ] Add loading state
- [ ] Add empty state
- [ ] Add basic error state with retry

Deliverables:
- [ ] Notes list shows real backend data
- [ ] Retry works for failed fetch

### Day 3: Create and Edit Flows
- [ ] Build create Note form with validation
- [ ] Build edit Note form with prefilled values
- [ ] Handle API errors clearly in UI
- [ ] Refresh list after create/edit

Deliverables:
- [ ] Create and edit work from UI
- [ ] Validation errors are user-friendly

### Day 4: Delete + UX Polish
- [ ] Add delete action with confirmation
- [ ] Improve feedback (success/error toasts or messages)
- [ ] Improve form UX and empty states
- [ ] Add responsive behavior for mobile

Deliverables:
- [ ] Full CRUD from frontend UI
- [ ] UX is demo-ready

### Day 5: Frontend Tests + Cleanup
- [ ] Add component tests for list/form/error states
- [ ] Add API client tests (or mocked integration tests)
- [ ] Clean module boundaries and naming
- [ ] Remove dead code and unused styles

Deliverables:
- [ ] Tests cover key user-facing states
- [ ] Frontend codebase is stable and readable

### Day 6: Local End-to-End Runbook
- [ ] Define command sequence to run DB + backend + frontend
- [ ] Document required environment variables
- [ ] Add troubleshooting section for common issues
- [ ] Validate docs from a clean restart

Deliverables:
- [ ] New machine setup is documented
- [ ] Local setup instructions are verified

### Day 7: Demo + Gap Analysis
- [ ] Prepare short demo script
- [ ] Identify Microsoft Entra ID integration points for Week 3
- [ ] List Docker and deployment prerequisites
- [ ] Build Week 3 backlog

Deliverables:
- [ ] Demo-ready app
- [ ] Clear backlog for Entra ID + Docker

### Week 2 Definition of Done
- [ ] UI performs full CRUD against backend
- [ ] Loading, error, and empty states are implemented
- [ ] Runbook is complete and tested
- [ ] You can demo confidently in under 5 minutes

---

## Daily Time Box (Recommended)
- [ ] 20 min planning (choose 1-2 outcomes)
- [ ] 90 min implementation
- [ ] 30 min testing/debugging
- [ ] 20 min documentation updates
- [ ] 20 min commit and backlog update

---

## Quick Start (Tomorrow)
- [ ] Finalize Notes app user stories and acceptance criteria
- [ ] Scaffold backend and health endpoint
- [ ] Add PostgreSQL connection and Note model
- [ ] Create first migration
- [ ] Verify create/list endpoints manually
