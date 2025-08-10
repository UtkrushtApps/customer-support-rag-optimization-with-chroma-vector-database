## Task Overview

You are improving a customer support RAG assistant that answers user queries using a Chroma vector database of support documents (already embedded using sentence-transformers). Existing chunking and metadata logic are inadequate, causing poor search relevance and dilution in the returned context. Your goal is to implement an effective chunking and retrieval solution that attaches required metadata and delivers accurate, relevant responses for support scenarios.

### RAG System Gaps to Address
- Document chunks are too large, with no overlap, and lack metadata (category, priority, date).
- Retrieval logic is basic, resulting in irrelevant or incomplete responses.
- There is no batching, overlap, or context assembly, reducing answer quality and recall@k.

### What to Focus On
- Implementing chunking into ~200-token segments with 40-token overlap and batch embedding persistence.
- Attaching and storing metadata per chunk and ensuring it's used in retrieval queries.
- Configuring and executing top-k (k=5) cosine similarity search via Chroma.
- Building response context from retrieved results with attention to redundancy and citation.
- Measuring the effectiveness via recall@k using `sample_queries.txt` and manual spot checks.

### Vector Database Access
- **Chroma Host**: <DROPLET_IP>
- **API Port**: 8000
- **Collection Name**: "support_chunks"
- **Vector dimension**: 384 (sentence-transformers/all-MiniLM-L6-v2)
- **Chunk metadata**: chunk_id, doc_id, chunk_index, category, priority, date, content

You can use any Chroma SDK or REST client for query validation.

### Objectives
- Deliver better search recall and precision by optimizing chunk size and overlap.
- Ensure every chunk includes correct metadata (category, priority, date) for filtered queries.
- Verify retrieval improvements using sample queries and recall@k.

### How to Verify
- Run queries from `sample_queries.txt` using completed pipeline in `rag_retrieval.py`.
- Check that responses are relevant and cite the correct category and date.
- Evaluate recall@k and examine sample context assembly for redundancy or missing information.

#### Note: All database and embedding infrastructure is automated. Focus on chunking, metadata, and retrieval logic only.