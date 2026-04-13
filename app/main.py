# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from app.rag import retrieve
from app.llm import generate_answer

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/ask")
async def ask(q: Query):
    context = await retrieve(q.question)
    answer = generate_answer(q.question, context)

    return {
        "question": q.question,
        "answer": answer,
        "context_used": context
    }
