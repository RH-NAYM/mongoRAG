from fastapi import FastAPI, HTTPException
from app.models import QueryModel
from app.rag import retrieve
from app.llm import generate_answer

app = FastAPI(title="Mongo RAG API")




@app.post("/ask")
async def ask(q: QueryModel):
    try:
        # 1. Retrieve context
        context = await retrieve(q.question)

        # 2. Handle empty retrieval (IMPORTANT)
        if not context:
            return {
                "question": q.question,
                "answer": "I don't know (no relevant context found)",
                "context_used": []
            }

        # 3. Generate answer
        answer = generate_answer(q.question, context)

        return {
            "question": q.question,
            "answer": answer,
            "context_used": context
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
