from app.db import COLLECTION
from app.embedder import get_embedding


async def retrieve(query: str, k: int=5):
    query_vector = get_embedding(query)


    custom_pipeline = [
        {
            "$vectorSearch": {
                "index": "vector_index",
                "path": "embedding",
                "queryVector": query_vector,
                "numCandidates": 100,
                "limit": k
            }
        },
        {
            "$project": {
                "_id": 0,
                "text": 1,
                "score": {"$meta": "vectorSearchScore"}
            }
        }
    ]

    results = []

    async for doc in COLLECTION.aggregate(pipeline=custom_pipeline):
        results.append(doc["text"])

        return results
