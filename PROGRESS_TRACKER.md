# Progress Tracker

## Current Focus
- Current week: [x] Week 1-2  [ ] Week 3  [ ] Week 4
- Current day: Week 1, Day 1
- Date: 2026-07-04
- Planned session duration: 2 hours

---

## Linked Plans
- Master roadmap: [MASTER_ROADMAP.md](MASTER_ROADMAP.md)
- Week 1-2 checklist: [FIRST_2_WEEKS_PLAN_CHECKLIST.md](FIRST_2_WEEKS_PLAN_CHECKLIST.md)
- Week 3 checklist: [WEEK_3_ENTRA_ID_CHECKLIST.md](WEEK_3_ENTRA_ID_CHECKLIST.md)
- Week 4 checklist: [WEEK_4_DOCKER_AKS_CHECKLIST.md](WEEK_4_DOCKER_AKS_CHECKLIST.md)

---

## Today Plan
- Top 3 outcomes:
  - [x] Finalize 3 user stories and 5 acceptance criteria for Notes app
  - [x] Scaffold backend structure and health endpoint
  - [x] Create frontend scaffold and basic route shell

- Planned tasks:
  - [x] Write scope summary in README
  - [x] Create backend folders and initial FastAPI app file
  - [x] Create frontend app and confirm local run command

---

## Progress Log
Use one entry per day.

### Entry Template
- Date:
- Week/Day:
- Completed:
  - [ ]
  - [ ]
- In progress:
  - [ ]
- Blockers:
  -
- Decisions made:
  -
- Next actions:
  - [ ]
  - [ ]

### Entry: 2026-07-04
- Date: 2026-07-04
- Week/Day: Week 1, Day 1
- Completed:
  - [x] Created roadmap and checklist docs for Weeks 1-4
  - [x] Confirmed stack decisions: Microsoft Entra ID + SQLAlchemy
  - [x] Added Notes backend scaffold (health + CRUD endpoints)
  - [x] Added Notes frontend scaffold (create + list flow)
  - [x] Updated root README with scope, user stories, and acceptance criteria
- In progress:
  - [ ] Run app end-to-end and verify create/list from UI
- Blockers:
  - None currently
- Decisions made:
  - Use Microsoft Entra ID for auth
  - Use SQLAlchemy + Alembic for data layer
- Next actions:
  - [ ] Install frontend/backend dependencies
  - [ ] Run backend and frontend locally, then test note creation

---

## Weekly Gate Check

### Week 1-2 Gate
- [ ] Full CRUD works from UI to DB
- [ ] Migrations reproducible on clean setup
- [ ] Basic tests passing
- [ ] Local runbook validated

### Week 3 Gate
- [ ] Entra login/logout working in frontend
- [ ] Frontend calls protected API with bearer token
- [ ] Backend validates JWT and enforces scopes
- [ ] Auth tests and troubleshooting notes complete

### Week 4 Gate
- [ ] App running on AKS over HTTPS
- [ ] Entra auth working on deployed domain
- [ ] Config and secrets externalized
- [ ] CI/CD deployment and smoke checks passing

---

## Blocker Tracker
- Blocker:
- Impact:
- Owner:
- Opened on:
- Target resolution date:
- Status: [ ] Open  [ ] Mitigated  [ ] Resolved

---

## End-of-Week Retrospective
- What went well:
  -
- What was difficult:
  -
- What to improve next week:
  -
- Scope adjustments:
  -
