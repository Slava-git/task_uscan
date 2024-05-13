from src.utils.db import SessionLocal
from src import crud_notes
from src import models
from src import schemas
from src.config import settings
from sqlalchemy.orm import Session

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.documents import Document


embeddings = OpenAIEmbeddings()
prompt = ChatPromptTemplate.from_template(settings.prompt_template)
llm = ChatOpenAI(model=settings.model_name, temperature=settings.default_temperature)


def retrieve_and_rank_notes(user_id: int, query: str):
    db = SessionLocal()
    try:
        notes = crud_notes.get_notes_by_user_id(db, user_id)
        if not notes:
            return None

        documents = [Document(page_content=note.content) for note in notes]

        vectordb = FAISS.from_documents(documents, embeddings)
        retriever = vectordb.as_retriever()

        qa_chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )

        response = qa_chain.invoke(query)
        return response
    finally:
        db.close()


def create_user_note(db: Session, note_data: schemas.NoteCreate):
    user = (
        db.query(models.User).filter(models.User.user_id == note_data.user_id).first()
    )
    if not user:
        raise ValueError("User not found")

    new_note = models.Note(user_id=note_data.user_id, content=note_data.content)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note
