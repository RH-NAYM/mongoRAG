import ollama

MODEL = "qwen2.5:latest"   # fix model name (gemma4 doesn't exist)  ||   gemma:7b-instruct  ||  gemma4:latest

def build_prompt(query, context_chunks):
    context = "\n\n".join(context_chunks)


    response = f"""
                You are Sherlock, a strict AI assistant.

                Rules:
                - Answer ONLY using the provided context
                - If the answer is not in the context, say: "I don't know"
                - Be concise and accurate
                - Support both Bangla and English

                Context:
                {context}

                Question:
                {query}

                Answer:
                """

    return response


def generate_answer(query, context_chunks):
    # 🚨 handle empty context
    if not context_chunks:
        return "I don't know"

    prompt = build_prompt(query, context_chunks)

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a strict RAG assistant. Do not hallucinate."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature": 0.2,
            "num_ctx": 4096,
            "num_gpu": 1
        }
    )

    return response["message"]["content"]
