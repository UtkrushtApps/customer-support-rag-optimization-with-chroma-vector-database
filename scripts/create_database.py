import chromadb
from chromadb.config import Settings

def create_collection():
    client = chromadb.Client(Settings(chroma_api_impl="rest", chroma_server_host="chromadb", chroma_server_http_port=8000))
    collections = client.list_collections()
    if "support_chunks" not in [col.name for col in collections]:
        client.create_collection("support_chunks", metadata={"hnsw:space": "cosine"})
    print("[*] Chroma collection support_chunks is ready.")

if __name__ == "__main__":
    create_collection()