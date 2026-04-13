from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

CLIENT = AsyncIOMotorClient(os.getenv("MONGO_URI"))

DB = CLIENT["testing_rag_pipeline"]

COLLECTION = DB["data"]
