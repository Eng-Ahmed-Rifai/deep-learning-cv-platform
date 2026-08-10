"""
Document Chunker & Text Normalization Pipeline
Author: Junior AI Engineer
"""

from typing import List, Dict, Any

class TokenAwareChunker:
    def __init__(self, chunk_size: int = 512, chunk_overlap: int = 64):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split_text(self, text: str) -> List[Dict[str, Any]]:
        """Splits document text into overlapping chunks for embedding generation."""
        words = text.split()
        chunks = []
        start = 0
        chunk_id = 0

        while start < len(words):
            end = start + self.chunk_size
            chunk_words = words[start:end]
            chunk_text = " ".join(chunk_words)

            chunks.append({
                "chunk_id": chunk_id,
                "text": chunk_text,
                "token_count": len(chunk_words)
            })

            chunk_id += 1
            start += self.chunk_size - self.chunk_overlap

        return chunks

    def sanitize_text(self, text: str) -> str:
        """Removes duplicate whitespace and sanitizes text input."""
        return " ".join(text.split())
