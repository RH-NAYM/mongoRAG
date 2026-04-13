from sentence_transformers import SentenceTransformer

model = SentenceTransformer("intfloat/e5-base-v2")


def get_embedding(txt: str):
    embedded_numpy_data = model.encode(
        inputs=txt,
        convert_to_numpy=True
    ).tolist()

    return embedded_numpy_data
