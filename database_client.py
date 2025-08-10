import chromadb
from chromadb.config import Settings

class ChromaDBClient:
    def __init__(self):
        self.client = chromadb.Client(Settings(chroma_api_impl="rest", chroma_server_host="chromadb", chroma_server_http_port=8000))
        self.collection = self.client.get_collection("support_chunks")

    def query_top_k(self, query_embedding, k=5, filters=None):
        """
        Search for most similar chunks by cosine distance, with optional filters on category/priority/date.
        Returns: list of dicts with content and metadata
        """
        # IMPLEMENT: Candidate should complete this
        pass

    def close(self):
        pass  # No explicit close needed for Chroma REST
