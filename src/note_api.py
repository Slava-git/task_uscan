from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import schemas
from . import crud_notes
from .utils.db import SessionLocal
from .services.note_service import retrieve_and_rank_notes

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/notes/", response_model=schemas.Note)
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    return crud_notes.create_user_note(db=db, note=note, user_id=1)


@app.get("/notes/", response_model=List[schemas.Note])
def read_notes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_notes.get_notes(db, skip=skip, limit=limit)


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud_notes.create_user(db=db, user=user)


@app.get("/search/{user_id}", response_model=schemas.NoteHelper)
def search_notes(user_id: int, query: str, db: Session = Depends(get_db)):
    response = retrieve_and_rank_notes(user_id, query)
    if response is None:
        raise HTTPException(status_code=404, detail="No notes found for the given user")
    return {"response": response}
