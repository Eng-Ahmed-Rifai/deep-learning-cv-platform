"""
RAG Pipeline & Embeddings Utilities
Author: AI Engineer Portfolio
"""

import math
from typing import List, Dict, Any

def cosine_similarity(vec_a: List[float], vec_b: List[float]) -> float:
    """Calculate cosine similarity between two vector embeddings."""
    if len(vec_a) != len(vec_b):
        raise ValueError("Vectors must be of equal length")
    
    dot_product = sum(a * b for a, b in zip(vec_a, vec_b))
    norm_a = math.sqrt(sum(a * a for a in vec_a))
    norm_b = math.sqrt(sum(b * b for b in vec_b))
    
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot_product / (norm_a * norm_b)

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    """Split text document into overlapping chunks for vector embedding index."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

class SimpleVectorStore:
    def __init__(self):
        self.documents: List[Dict[str, Any]] = []

    def add_document(self, doc_id: str, content: str, embedding: List[float]):
        self.documents.append({
            "id": doc_id,
            "content": content,
            "embedding": embedding
        })

    def search(self, query_embedding: List[float], top_k: int = 3) -> List[Dict[str, Any]]:
        scored_docs = []
        for doc in self.documents:
            score = cosine_similarity(query_embedding, doc["embedding"])
            scored_docs.append((score, doc))
        
        scored_docs.sort(key=lambda x: x[0], reverse=True)
        return [doc for score, doc in scored_docs[:top_k]]

// Updated at: 2026-08-10T20:18:33.415Z [Pulse 4/24]

def filter_by_threshold(docs, threshold=0.75):
    """Filter retrieved documents above confidence score threshold."""
    return [doc for doc in docs if doc.get("score", 0) >= threshold]

// Updated at: 2026-08-10T20:18:33.446Z [Pulse 7/24]

def filter_by_threshold(docs, threshold=0.75):
    """Filter retrieved documents above confidence score threshold."""
    return [doc for doc in docs if doc.get("score", 0) >= threshold]

// Updated at: 2026-08-10T20:18:33.467Z [Pulse 9/24]

def filter_by_threshold(docs, threshold=0.75):
    """Filter retrieved documents above confidence score threshold."""
    return [doc for doc in docs if doc.get("score", 0) >= threshold]

// Updated at: 2026-08-10T20:19:03.607Z [Pulse 3/21]

def filter_by_threshold(docs, threshold=0.75):
    """Filter retrieved documents above confidence score threshold."""
    return [doc for doc in docs if doc.get("score", 0) >= threshold]

// Updated at: 2026-08-10T20:19:03.890Z [Pulse 21/21]

def filter_by_threshold(docs, threshold=0.75):
    """Filter retrieved documents above confidence score threshold."""
    return [doc for doc in docs if doc.get("score", 0) >= threshold]
