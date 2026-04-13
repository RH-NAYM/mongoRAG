# app/rag.py
from app.db import collection
from app.embedder import get_embedding

async def retrieve(query: str, k: int = 5):
    query_vector = get_embedding(query)

    pipeline = [
        {
            "$vectorSearch": {
                "queryVector": query_vector,
                "path": "embedding",
                "numCandidates": 100,
                "limit": k
            }
        }
    ]

    results = []
    async for doc in collection.aggregate(pipeline):
        results.append(doc["text"])

    return results
