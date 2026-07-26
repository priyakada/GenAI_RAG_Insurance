import os
import pickle
import faiss
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import google.generativeai as genai

# Load API key
load_dotenv("api.env")      # If you created .env instead, use load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Gemini Model
model = genai.GenerativeModel("models/gemini-3.6-flash")

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index("vector_store/claims.index")

# Load documents
with open("vector_store/documents.pkl", "rb") as f:
    documents = pickle.load(f)


def ask_question(question):
    # Convert question to embedding
    query_embedding = embedding_model.encode([question])

    # Search top 3 relevant records
    distances, indices = index.search(query_embedding, 3)

    context = "\n".join([documents[i] for i in indices[0]])

    prompt = f"""
You are an Insurance Claims AI Assistant.

Use ONLY the information below to answer the question.

Context:
{context}

Question:
{question}

Answer:
"""

    response = model.generate_content(prompt)

    return response.text