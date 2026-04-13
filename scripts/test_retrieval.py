import asyncio
from app.rag import retrieve
from app.embedder import get_embedding

async def test():
    while True:
        query = input("Ask your Question (type 'exit' to quit): ")

        if query.lower() == "exit":
            print("👋 Exiting...")
            break

        # generate query embedding properly
        query_vector = get_embedding(query)

        print("\nQuery:", query)
        print("Vector size:", len(query_vector))

        results = await retrieve(query)

        print("\n🔍 Retrieved Context:\n")

        if not results:
            print("❌ No results returned from vector search")
            continue

        for i, r in enumerate(results):
            print(f"{i+1}. {r}")

asyncio.run(test())
