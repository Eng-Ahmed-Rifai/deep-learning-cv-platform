"""
Hybrid Search & Reciprocal Rank Fusion (RRF) Reranker
Author: Junior AI Engineer
"""

import math
from typing import List, Dict, Any

def reciprocal_rank_fusion(
    dense_results: List[Dict[str, Any]], 
    bm25_results: List[Dict[str, Any]], 
    k: int = 60
) -> List[Dict[str, Any]]:
    """Combines dense vector and BM25 search rankings using Reciprocal Rank Fusion."""
    rrf_scores: Dict[str, float] = {}
    doc_map: Dict[str, Dict[str, Any]] = {}

    for rank, doc in enumerate(dense_results):
        doc_id = doc["id"]
        doc_map[doc_id] = doc
        rrf_scores[doc_id] = rrf_scores.get(doc_id, 0.0) + (1.0 / (k + rank + 1))

    for rank, doc in enumerate(bm25_results):
        doc_id = doc["id"]
        doc_map[doc_id] = doc
        rrf_scores[doc_id] = rrf_scores.get(doc_id, 0.0) + (1.0 / (k + rank + 1))

    sorted_docs = sorted(rrf_scores.items(), key=lambda item: item[1], reverse=True)

    fused_results = []
    for doc_id, score in sorted_docs:
        doc = doc_map[doc_id].copy()
        doc["rrf_score"] = score
        fused_results.append(doc)

    return fused_results

def normalize_scores(results):
    """Normalize fusion scores between 0 and 1."""
    if not results:
        return results
    max_score = max(r.get("rrf_score", 1.0) for r in results)
    for r in results:
        r["normalized_score"] = round(r.get("rrf_score", 0.0) / max_score, 4)
    return results

def normalize_scores(results):
    """Normalize fusion scores between 0 and 1."""
    if not results:
        return results
    max_score = max(r.get("rrf_score", 1.0) for r in results)
    for r in results:
        r["normalized_score"] = round(r.get("rrf_score", 0.0) / max_score, 4)
    return results
