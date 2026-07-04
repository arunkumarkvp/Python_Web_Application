# Backend (FastAPI + SQLAlchemy)

## Setup
1. Create and activate a virtual environment.
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Copy environment file:
   - `copy .env.example .env`
4. Run API:
   - `uvicorn app.main:app --reload`

## Endpoints
- `GET /health`
- `GET /notes`
- `POST /notes`
- `PUT /notes/{note_id}`
- `DELETE /notes/{note_id}`

## Notes
- Current user is hardcoded to `local-user` until Entra integration in Week 3.
- SQLite is used by default for local learning speed; switch `DATABASE_URL` later.
