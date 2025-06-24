import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

VECTOR_DB_URL = "http://localhost:6333"
VECTOR_DB_NAME = "vector_db"
DATA_DIR = os.path.join(BASE_DIR, "data")
EMBEDDINGS = "NeuML/pubmedbert-base-embeddings"

# ✅ Absolute path to model
# LLM_PATH = os.path.join(BASE_DIR, "models", "BioMistral-7B.Q4_K_M.gguf")
LLM_PATH = "/Users/priyaraut/.cache/huggingface/hub/models--BioMistral--BioMistral-7B-GGUF/snapshots/de8c2dfcead24fd23ccb33f6ca5ff015e9ecdb4b/ggml-model-Q2_K.gguf"

PROMPT_TEMPLATE = """Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}
Question: {question}

Only return the helpful answer. Answer must be detailed and well explained.
Helpful answer:
"""



