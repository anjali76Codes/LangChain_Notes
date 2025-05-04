from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# ---------- 1. Embedding for a Query ---------------

# large dimension vectors more context is captured
embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

result = embedding.embed_query("Delhi is the capital of India")
print(str(result))


# ---------- 2. Embedding for Documents ---------------

documents = [
    "Delhi is the capital is India",
    "Kolkata is the capital of west bengal",
    "Paris is the capital of France",
]

result = embedding.embed_documents(documents)
