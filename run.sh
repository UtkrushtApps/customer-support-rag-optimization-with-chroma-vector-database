#!/bin/bash
set -e

echo "[1/4] Starting Chroma database via docker-compose..."
docker-compose up -d
sleep 5
echo "[2/4] Creating support collection and table..."
python scripts/create_database.py
echo "[3/4] Processing and chunking documents, embedding, storing with metadata..."
python scripts/process_documents.py
echo "[4/4] Verifying setup and collection readiness..."
python scripts/verify_setup.py
echo "\nEnvironment setup completed! All document chunks and embeddings are ready."
