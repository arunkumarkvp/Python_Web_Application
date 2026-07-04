# Week 3 Checklist: Microsoft Entra ID Integration (React + FastAPI)

## Week Goal
Implement secure login/logout with Microsoft Entra ID, enforce protected API access in FastAPI, and complete an end-to-end auth flow in local development.

Tech assumptions:
- Frontend: React (Vite)
- Backend: FastAPI
- Data: PostgreSQL + SQLAlchemy + Alembic
- Identity: Microsoft Entra ID (OIDC/OAuth2)

---

## Day 1: Entra App Registration and Auth Design
- [ ] Create Entra app registration for the React SPA
- [ ] Create Entra app registration for the FastAPI API (or expose API in one app if using a single-registration pattern)
- [ ] Configure redirect URI for local frontend (example: `http://localhost:5173`)
- [ ] Configure logout redirect URI
- [ ] Define API Application ID URI and scopes (example: `api://<app-id>/notes.read`, `api://<app-id>/notes.write`)
- [ ] Decide tenant model (single-tenant recommended for first implementation)
- [ ] Document auth architecture in project docs

Deliverables:
- [ ] Entra registrations created and documented
- [ ] Scopes defined and visible in Entra
- [ ] Auth flow diagram (login -> token -> API validation) written in docs

---

## Day 2: React Login/Logout with MSAL
- [ ] Install and configure MSAL libraries in frontend
- [ ] Add MSAL provider setup at app root
- [ ] Implement login button (interactive sign-in)
- [ ] Implement logout button
- [ ] Display authenticated user info (name/email/tenant) in UI
- [ ] Add route guard for protected pages
- [ ] Add silent token acquisition for API scope

Deliverables:
- [ ] User can sign in and sign out from frontend
- [ ] Protected route blocks unauthenticated users
- [ ] Frontend can request access token for custom API scope

---

## Day 3: FastAPI JWT Validation (Entra Tokens)
- [ ] Add bearer token extraction middleware/dependency
- [ ] Configure issuer, audience, tenant ID, and JWKS discovery URL
- [ ] Validate JWT signature using Entra JWKS keys
- [ ] Validate issuer (`iss`), audience (`aud`), expiration (`exp`), and not-before (`nbf`)
- [ ] Normalize auth errors into consistent `401/403` responses
- [ ] Add reusable `get_current_user` dependency

Deliverables:
- [ ] FastAPI rejects invalid/expired tokens
- [ ] FastAPI accepts valid Entra access tokens
- [ ] Standardized unauthorized/forbidden responses in API

---

## Day 4: Scope-Based Authorization and Protected Endpoints
- [ ] Add scope checks for critical endpoints (`notes.read`, `notes.write`)
- [ ] Protect list/read endpoints with read scope
- [ ] Protect create/update/delete endpoints with write scope
- [ ] Add ownership checks so users can only access their own notes
- [ ] Add test fixtures for authorized and unauthorized tokens

Deliverables:
- [ ] API enforces both authentication and authorization
- [ ] Scope failures return `403` with clear message
- [ ] Ownership protection is active for Note resources

---

## Day 5: Frontend-Backend Token Integration
- [ ] Attach access token in API client `Authorization: Bearer <token>` header
- [ ] Handle token acquisition failures gracefully in UI
- [ ] Implement retry behavior for transient auth errors
- [ ] Add global handling for `401`/`403` (prompt re-login or show access-denied)
- [ ] Verify full CRUD from UI with authenticated calls

Deliverables:
- [ ] UI successfully calls protected FastAPI endpoints
- [ ] Auth errors are visible and understandable to user
- [ ] End-to-end authenticated CRUD works locally

---

## Day 6: Testing + Security Hardening Pass
- [ ] Add backend tests for token validation edge cases (expired, wrong audience, wrong issuer)
- [ ] Add backend tests for scope enforcement
- [ ] Add frontend tests for guarded routes and auth states
- [ ] Verify CORS configuration for local frontend origin
- [ ] Confirm secrets/config are environment-driven and not hard-coded
- [ ] Document minimal threat model and known limitations

Deliverables:
- [ ] Automated tests cover key auth failure/success paths
- [ ] Security configuration reviewed and documented
- [ ] Local environment is stable and repeatable

---

## Day 7: Demo, Runbook, and Week 4 Handoff
- [ ] Prepare a 5-minute demo script (login -> list -> create -> logout -> unauthorized check)
- [ ] Write auth setup runbook (Entra settings + env vars + local run steps)
- [ ] Add troubleshooting section (common Entra/MSAL/JWT issues)
- [ ] Capture Week 4 prerequisites for Docker and containerized auth config
- [ ] Log remaining backlog items

Deliverables:
- [ ] Demo-ready auth-enabled app
- [ ] Complete Entra integration runbook
- [ ] Clear Docker/Kubernetes auth backlog for next week

---

## Week 3 Definition of Done
- [ ] Frontend login/logout works with Microsoft Entra ID
- [ ] Frontend acquires access token for custom API scope
- [ ] FastAPI validates Entra JWT tokens correctly
- [ ] Protected endpoints enforce scopes and ownership
- [ ] Authenticated CRUD works end-to-end from UI
- [ ] Tests cover critical auth and authorization scenarios
- [ ] Runbook allows another developer to reproduce setup

---

## Suggested Environment Variables Checklist

Frontend (`.env`):
- [ ] `VITE_ENTRA_CLIENT_ID`
- [ ] `VITE_ENTRA_TENANT_ID`
- [ ] `VITE_ENTRA_AUTHORITY` (example: `https://login.microsoftonline.com/<tenant-id>`)
- [ ] `VITE_API_SCOPE` (example: `api://<api-app-id>/notes.read`)
- [ ] `VITE_API_BASE_URL`

Backend (`.env`):
- [ ] `ENTRA_TENANT_ID`
- [ ] `ENTRA_ISSUER`
- [ ] `ENTRA_AUDIENCE` (API app/client ID or Application ID URI as used by your token strategy)
- [ ] `ENTRA_JWKS_URL`
- [ ] `CORS_ALLOWED_ORIGINS`

---

## Daily Time Box (Recommended)
- [ ] 20 min planning
- [ ] 90 min implementation
- [ ] 30 min test/debug
- [ ] 20 min docs update
- [ ] 20 min commit + backlog update
