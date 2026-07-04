from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.note import Note
from app.schemas.note import NoteCreate, NoteRead, NoteUpdate
from app.services.note_service import NoteService

router = APIRouter(prefix="/notes", tags=["notes"])


def get_user_id() -> str:
    # Placeholder until Entra authentication is integrated in Week 3.
    return "local-user"


@router.get("", response_model=list[NoteRead], summary="List notes")
def list_notes(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=20, ge=1, le=100),
    db: Session = Depends(get_db),
    user_id: str = Depends(get_user_id),
) -> list[Note]:
    return NoteService.list_notes(db, user_id=user_id, skip=skip, limit=limit)


@router.post("", response_model=NoteRead, status_code=status.HTTP_201_CREATED, summary="Create note")
def create_note(
    payload: NoteCreate,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_user_id),
) -> Note:
    return NoteService.create_note(db, user_id=user_id, payload=payload)


@router.put("/{note_id}", response_model=NoteRead, summary="Update note")
def update_note(
    note_id: int,
    payload: NoteUpdate,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_user_id),
) -> Note:
    note = db.query(Note).filter(Note.id == note_id, Note.user_id == user_id).first()
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    return NoteService.update_note(db, note=note, payload=payload)


@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete note")
def delete_note(
    note_id: int,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_user_id),
) -> Response:
    note = db.query(Note).filter(Note.id == note_id, Note.user_id == user_id).first()
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    NoteService.delete_note(db, note=note)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
