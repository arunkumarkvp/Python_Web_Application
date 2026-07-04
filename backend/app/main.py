from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.health import router as health_router
from app.api.routes.notes import router as notes_router
from app.core.config import settings
from app.db.session import Base, engine
from app.models import Note  # noqa: F401

app = FastAPI(title=settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in settings.cors_allowed_origins.split(",")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup() -> None:
    # Temporary table creation for local learning flow; Alembic will own schema in next step.
    Base.metadata.create_all(bind=engine)


app.include_router(health_router)
app.include_router(notes_router)
