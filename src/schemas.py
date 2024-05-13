from pydantic import BaseModel
from typing import List, Optional


class NoteBase(BaseModel):
    content: str


class NoteCreate(NoteBase):
    pass


class Note(NoteBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: Optional[str] = None


class UserCreate(BaseModel):
    username: str
    email: str


class User(UserBase):
    user_id: int
    notes: List[Note] = []

    class Config:
        orm_mode = True


class NoteHelper(BaseModel):
    response: str
