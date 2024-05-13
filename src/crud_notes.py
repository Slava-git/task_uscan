from . import models
from sqlalchemy.orm import Session
from . import schemas


def get_notes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Note).offset(skip).limit(limit).all()


def add_note_to_db(db: Session, note_data: schemas.NoteCreate, user_id: int):
    db_note = models.Note(**note_data.dict(), user_id=user_id)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_notes_by_user_id(db: Session, user_id: int):
    return db.query(models.Note).filter(models.Note.user_id == user_id).all()
