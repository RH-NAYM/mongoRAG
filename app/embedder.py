# # app/embedder.py
# from sentence_transformers import SentenceTransformer

# model = SentenceTransformer("intfloat/e5-base-v2")

# def get_embedding(text: str):
#     return model.encode(text).tolist()








# from sentence_transformers import SentenceTransformer

# model = SentenceTransformer("intfloat/e5-base-v2")

# def get_embedding(text: str):
#     return model.encode(text, convert_to_numpy=True).tolist()





from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-m3")

def get_embedding(text: str, is_query=False):
    if is_query:
        text = f"Represent this sentence for searching relevant passages: {text}"
    else:
        text = f"Represent this passage: {text}"

    return model.encode(text, normalize_embeddings=True).tolist()
