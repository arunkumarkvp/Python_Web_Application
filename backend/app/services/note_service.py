from sqlalchemy.orm import Session

from app.models.note import Note
from app.schemas.note import NoteCreate, NoteUpdate


class NoteService:
    @staticmethod
    def list_notes(db: Session, user_id: str, skip: int = 0, limit: int = 20) -> list[Note]:
        return (
            db.query(Note)
            .filter(Note.user_id == user_id)
            .order_by(Note.updated_at.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )

    @staticmethod
    def create_note(db: Session, user_id: str, payload: NoteCreate) -> Note:
        note = Note(user_id=user_id, title=payload.title, body=payload.body)
        db.add(note)
        db.commit()
        db.refresh(note)
        return note

    @staticmethod
    def update_note(db: Session, note: Note, payload: NoteUpdate) -> Note:
        note.title = payload.title
        note.body = payload.body
        db.commit()
        db.refresh(note)
        return note

    @staticmethod
    def delete_note(db: Session, note: Note) -> None:
        db.delete(note)
        db.commit()
