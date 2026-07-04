# Master Roadmap: Web App Learning and Deployment Journey

## Objective
Learn, build, secure, and deploy a production-style web application using:
- React frontend
- FastAPI backend
- PostgreSQL with SQLAlchemy + Alembic
- Microsoft Entra ID authentication
- Docker + Azure Kubernetes Service (AKS)

---

## How to Use This Roadmap
1. Work week-by-week in order.
2. Treat each week's Definition of Done as a gate.
3. Do not move to the next week until the current gate is complete.
4. Keep a short weekly retrospective: what worked, what blocked, what to improve.

---

## Week-by-Week Plan

### Week 1-2: App Foundations and CRUD Delivery
Focus: backend + frontend foundations, data model, CRUD, tests, and runbook.

Checklist:
- [FIRST_2_WEEKS_PLAN_CHECKLIST.md](FIRST_2_WEEKS_PLAN_CHECKLIST.md)

Exit gate:
- [ ] Full CRUD works from UI to DB
- [ ] Migrations are reproducible
- [ ] Basic tests pass
- [ ] Local runbook is validated

---

### Week 3: Microsoft Entra ID Integration
Focus: login/logout, token acquisition, JWT validation in FastAPI, scope-based authorization.

Checklist:
- [WEEK_3_ENTRA_ID_CHECKLIST.md](WEEK_3_ENTRA_ID_CHECKLIST.md)

Exit gate:
- [ ] Entra login/logout works in frontend
- [ ] Frontend calls protected API with bearer token
- [ ] Backend validates JWT and enforces scopes
- [ ] Auth tests and troubleshooting notes are complete

---

### Week 4: Docker + AKS Deployment
Focus: containerization, AKS deployment, ingress/TLS, Entra-aware deployed auth flow, CI/CD.

Checklist:
- [WEEK_4_DOCKER_AKS_CHECKLIST.md](WEEK_4_DOCKER_AKS_CHECKLIST.md)

Exit gate:
- [ ] App is running on AKS over HTTPS
- [ ] Entra auth works on deployed domain
- [ ] Config/secrets are externalized
- [ ] CI/CD deploys and validates successfully

---

## Milestones
- [ ] Milestone A: Local backend CRUD + tests
- [ ] Milestone B: Full frontend CRUD integration
- [ ] Milestone C: End-to-end auth with Entra ID
- [ ] Milestone D: Containerized app running locally
- [ ] Milestone E: App deployed to AKS with HTTPS and auth
- [ ] Milestone F: CI/CD with smoke tests and rollback strategy

---

## Recommended Weekly Cadence
- Monday: plan and scope
- Tuesday-Thursday: implementation
- Friday: testing and hardening
- Saturday: docs and runbook updates
- Sunday: demo + retrospective + backlog prep

---

## Risk Checks (Review Weekly)
- [ ] Scope creep (too many features)
- [ ] Missing tests on critical flows
- [ ] Environment config drift between local and cloud
- [ ] Auth configuration mismatch (redirect URIs, audience, issuer)
- [ ] Deployment changes without rollback plan

---

## Optional Next Phase (After Week 4)
- Add Key Vault integration for secrets
- Add staging and production promotion workflow
- Add advanced observability and alerting
- Add performance/load tests and SLOs
- Start spec-driven workflow (spec templates + PR enforcement)
