# app/test_data.py
import asyncio
from app.db import collection

async def show_data():
    docs = collection.find().limit(5)

    print("\n📦 Sample Documents:\n")
    async for doc in docs:
        print(doc)
        print("-" * 50)

asyncio.run(show_data())
