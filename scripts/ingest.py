# scripts/ingest.py
import asyncio
from app.db import collection
from app.embedder import get_embedding

data = [
    {
        "text": "RAG stands for Retrieval Augmented Generation. It combines retrieval with LLM generation.",
        "metadata": {"source": "ai", "lang": "en"}
    },
    {
        "text": "MongoDB একটি NoSQL database যা document-based storage ব্যবহার করে।",
        "metadata": {"source": "db", "lang": "bn"}
    },
    {
        "text": "FastAPI is a high-performance Python web framework for building APIs.",
        "metadata": {"source": "backend", "lang": "en"}
    },
    {
        "text": "Embedding হলো text কে vector-এ convert করার একটি process যা semantic search-এ ব্যবহার হয়।",
        "metadata": {"source": "ai", "lang": "bn"}
    },
    {
        "text": "Vector search helps find similar meaning texts using embeddings instead of keywords.",
        "metadata": {"source": "ai", "lang": "en"}
    },
    {
        "text": "Ollama ব্যবহার করে local machine-এ LLM run করা যায় without external API.",
        "metadata": {"source": "llm", "lang": "bn"}
    },
]

async def run():
    docs = []

    for item in data:
        docs.append({
            "text": item["text"],
            "embedding": get_embedding(item["text"]),  # 🔥 FIX HERE
            "metadata": item["metadata"]
        })

    await collection.insert_many(docs)

asyncio.run(run())
