import pandas as pd
import os
import pickle
import faiss
from sentence_transformers import SentenceTransformer

# Load Gold Dataset
df = pd.read_csv("data/gold_claims.csv")

# Convert each row into text
documents = []

for _, row in df.iterrows():
    text = (
        f"Claim ID: {row['claim_id']}, "
        f"Customer: {row['customer_name']}, "
        f"Policy: {row['policy_type']}, "
        f"Claim Amount: {row['claim_amount']}, "
        f"Status: {row['claim_status']}, "
        f"Hospital: {row['hospital_name']}, "
        f"Diagnosis: {row['diagnosis']}, "
        f"City: {row['city']}"
    )
    documents.append(text)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings
embeddings = model.encode(documents)

# Create FAISS index
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save index
os.makedirs("vector_store", exist_ok=True)

faiss.write_index(index, "vector_store/claims.index")

# Save documents
with open("vector_store/documents.pkl", "wb") as f:
    pickle.dump(documents, f)

print("Vector database created successfully!")
print(f"Indexed {len(documents)} records.")