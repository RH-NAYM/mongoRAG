# app/llm.py
import ollama

def generate_answer(query, context_chunks):
    context = "\n".join(context_chunks)

    prompt = f"""
You are a smart assistant.

Context:
{context}

Question:
{query}

Answer clearly:
"""

    response = ollama.chat(
        model="qwen3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]
