# Week 4 Checklist: Docker + AKS Deployment (Entra-Aware)

## Week Goal
Containerize the React + FastAPI application, deploy it to Azure Kubernetes Service (AKS), configure secure ingress with TLS, and ensure Microsoft Entra ID auth works in deployed environments.

Tech assumptions:
- Frontend: React (Vite)
- Backend: FastAPI
- Data: PostgreSQL + SQLAlchemy + Alembic
- Auth: Microsoft Entra ID
- Platform: Azure Container Registry (ACR) + AKS

---

## Day 1: Dockerize Frontend and Backend
- [ ] Create production-ready Dockerfile for frontend
- [ ] Create production-ready Dockerfile for backend
- [ ] Add .dockerignore files for both services
- [ ] Pass runtime config via environment variables
- [ ] Build local images and verify startup logs
- [ ] Confirm health endpoints in containers

Deliverables:
- [ ] Frontend image builds successfully
- [ ] Backend image builds successfully
- [ ] Images run correctly with env-driven config

---

## Day 2: Local Container Orchestration and Validation
- [ ] Add docker-compose for frontend, backend, and PostgreSQL
- [ ] Configure shared network and service discovery
- [ ] Add volume strategy for local DB persistence
- [ ] Run migrations automatically or via documented command
- [ ] Validate end-to-end app behavior in containers
- [ ] Validate Entra configuration values for local container runs

Deliverables:
- [ ] One command starts full local stack
- [ ] CRUD works end-to-end in containerized local setup
- [ ] Auth flow still works after containerization

---

## Day 3: Azure Provisioning (ACR + AKS + Managed DB)
- [ ] Create Azure resource group
- [ ] Create Azure Container Registry (ACR)
- [ ] Create AKS cluster with RBAC enabled
- [ ] Attach ACR to AKS
- [ ] Provision managed PostgreSQL (recommended) or document interim alternative
- [ ] Configure network access rules for database
- [ ] Document Azure resource naming and regions

Deliverables:
- [ ] AKS cluster reachable with kubectl context
- [ ] ACR ready for image push/pull
- [ ] Managed database provisioned and accessible

---

## Day 4: Kubernetes Manifests and Secrets
- [ ] Create namespace for app workloads
- [ ] Add Deployments for frontend and backend
- [ ] Add Services for frontend and backend
- [ ] Add ConfigMaps for non-sensitive configuration
- [ ] Add Secrets for sensitive settings (DB URL, Entra config where needed)
- [ ] Add liveness/readiness probes
- [ ] Add resource requests and limits

Deliverables:
- [ ] Pods become healthy and stable
- [ ] Services route traffic internally
- [ ] Configuration and secrets are externalized

---

## Day 5: Ingress, TLS, and Entra Redirect Updates
- [ ] Install NGINX Ingress Controller in AKS
- [ ] Configure Ingress routes for frontend and API
- [ ] Configure TLS certificates (cert-manager + issuer)
- [ ] Point DNS to ingress external IP
- [ ] Update Entra app registration redirect/logout URIs for deployed domain
- [ ] Validate OIDC login flow on deployed URL

Deliverables:
- [ ] App reachable over HTTPS
- [ ] Login/logout works in deployed environment
- [ ] API calls from frontend succeed with valid bearer tokens

---

## Day 6: Observability, Reliability, and Scaling Basics
- [ ] Enable centralized logs for AKS workloads
- [ ] Add basic metrics dashboard (CPU, memory, request/error rate)
- [ ] Configure Horizontal Pod Autoscaler for backend
- [ ] Add PodDisruptionBudget for backend
- [ ] Test rolling update behavior
- [ ] Test basic failure scenarios (pod restart, bad config rollback)

Deliverables:
- [ ] You can diagnose failures from logs/metrics
- [ ] Backend scales under load trigger conditions
- [ ] Rollouts are predictable and recoverable

---

## Day 7: CI/CD and Production Readiness Check
- [ ] Create CI pipeline: lint, test, build images
- [ ] Push versioned images to ACR on main branch
- [ ] Create CD pipeline to deploy to AKS
- [ ] Add migration step in release workflow
- [ ] Add smoke tests after deployment
- [ ] Add rollback strategy and manual approval gate for production
- [ ] Finalize deployment runbook

Deliverables:
- [ ] One pipeline run can deploy a validated release
- [ ] Smoke tests verify core app functionality after deploy
- [ ] Runbook supports repeatable deployment and rollback

---

## Week 4 Definition of Done
- [ ] Frontend and backend are containerized and reproducible
- [ ] Application is deployed to AKS and accessible via HTTPS
- [ ] Microsoft Entra ID works on deployed domain
- [ ] Secrets and config are managed outside container images
- [ ] Logs/metrics provide operational visibility
- [ ] CI/CD performs build, push, deploy, and smoke validation
- [ ] Rollback procedure is documented and tested

---

## Required Configuration Checklist

Frontend:
- [ ] Public app URL configured for deployed domain
- [ ] Entra authority and client ID configured per environment
- [ ] API base URL points to ingress/API domain
- [ ] Allowed redirect/logout URIs match Entra registration

Backend:
- [ ] Entra issuer/audience/JWKS settings match tenant and app registration
- [ ] CORS origins include deployed frontend domain
- [ ] Database connection string points to managed database
- [ ] Secure app secrets are injected via Kubernetes secrets

AKS/Kubernetes:
- [ ] Namespace isolation is in place
- [ ] Ingress TLS termination is active
- [ ] Resource limits and probes are configured
- [ ] Deployment strategy supports zero/low downtime updates

---

## Stretch Goals (Optional)
- [ ] Move secrets from Kubernetes Secrets to Azure Key Vault + CSI driver
- [ ] Add staging and production namespaces with promotion flow
- [ ] Add canary deployment strategy
- [ ] Add policy checks (image scanning, IaC validation, admission controls)
