# scripts/ingest.py
import asyncio
from app.db import COLLECTION
from app.embedder import get_embedding
import json






with open("utils/data.json", 'r') as f:
    data = json.load(f)




"""
data = [
    {
        "text": "RAG pipeline improves answer quality by retrieving relevant documents before generation.",
        "metadata": {
            "source": "ai",
            "lang": "en"
        }
    }
]
"""


async def run():
    docs = []

    for item in data:
        docs.append({
            "text": item["text"],
            "embedding": get_embedding(item["text"]),
            "metadata": item["metadata"]
        })

    await COLLECTION.insert_many(docs)

asyncio.run(run())
