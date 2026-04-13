# app/db.py
from motor.motor_asyncio import AsyncIOMotorClient
import os

# client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
client = AsyncIOMotorClient("mongodb+srv://rakibhedigital_db_user:gv5WvhaMGMlA8hJh@learningsession01.3ebpl24.mongodb.net")

# print(client)
db = client["rag_db"]
collection = db["documents"]


# print(collection)
