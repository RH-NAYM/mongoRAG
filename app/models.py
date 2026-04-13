from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional


# -----------------------------
# RAG DOCUMENT (MongoDB)
# -----------------------------
class Document(BaseModel):
    text: str
    embedding: List[float]
    metadata: Optional[Dict[str, Any]] = None


# -----------------------------
# INGEST REQUEST (optional)
# -----------------------------
class IngestItem(BaseModel):
    text: str
    metadata: Optional[Dict[str, Any]] = None


# -----------------------------
# QUERY REQUEST (FastAPI /ask)
# -----------------------------
class QueryRequest(BaseModel):
    question: str
    top_k: int = Field(default=5, ge=1, le=20)


# -----------------------------
# QUERY RESPONSE
# -----------------------------
class QueryResponse(BaseModel):
    question: str
    answer: str
    context: List[str]
