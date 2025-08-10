import os
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

# Placeholder support document metadata categories
CATEGORIES = ["Login", "Billing", "Troubleshooting", "Enterprise", "Technical"]
PRIORITIES = ["Low", "Medium", "High", "Urgent"]

# Dummy metadata assignment
import random
from datetime import datetime, timedelta

def chunk_text(text, chunk_size=200, overlap=40):
    tokens = text.split()
    chunks = []
    i = 0
    while i < len(tokens):
        chunk = tokens[i:i+chunk_size]
        chunk_text = ' '.join(chunk)
        chunks.append({
            'content': chunk_text,
            'start_token': i
        })
        i += chunk_size - overlap
    return chunks

def assign_metadata(idx):
    category = random.choice(CATEGORIES)
    priority = random.choice(PRIORITIES)
    date = (datetime(2023,1,1) + timedelta(days=idx%365)).strftime("%Y-%m-%d")
    return category, priority, date

if __name__ == "__main__":
    model = SentenceTransformer('all-MiniLM-L6-v2')
    doc_path = 'data/documents/support_corpus.txt'
    with open(doc_path, 'r', encoding='utf-8') as f:
        text = f.read()
    chunks = chunk_text(text)
    print(f"[+] Document chunked into {len(chunks)} segments.")
    emb_texts = [c['content'] for c in chunks]
    print("[*] Generating embeddings ...")
    embeddings = model.encode(emb_texts, show_progress_bar=True, batch_size=32, normalize_embeddings=True)
    print(f"[*] Generated {len(embeddings)} embeddings.")
    client = chromadb.Client(Settings(chroma_api_impl="rest", chroma_server_host="chromadb", chroma_server_http_port=8000))
    collection = client.get_collection("support_chunks")
    metadatas = []
    ids = []
    for idx, chunk in enumerate(chunks):
        category, priority, date = assign_metadata(idx)
        metadatas.append({
            "chunk_id": str(idx),
            "doc_id": "support_corpus",
            "chunk_index": idx,
            "category": category,
            "priority": priority,
            "date": date,
            "content": chunk['content']
        })
        ids.append(str(idx))
    print("[*] Persisting chunks with metadata in Chroma collection...")
    collection.upsert(ids=ids, embeddings=embeddings.tolist(), metadatas=metadatas)
    print("[+] Processed chunks and metadata successfully stored.")