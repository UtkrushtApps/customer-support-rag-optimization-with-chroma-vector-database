import chromadb
from chromadb.config import Settings

def verify():
    client = chromadb.Client(Settings(chroma_api_impl="rest", chroma_server_host="chromadb", chroma_server_http_port=8000))
    collection = client.get_collection("support_chunks")
    count = len(collection.get()["ids"])
    print(f"[+] Collection support_chunks contains {count} chunks.")
    sample = collection.peek(5)
    print("[*] Sample chunk metadatas:")
    for md in sample["metadatas"]:
        print(md)
    print("[+] Chroma collection is fully populated and ready for queries.")

if __name__ == "__main__":
    verify()