def test_rrf_scoring():
    from src.retrieval.reranker import reciprocal_rank_fusion
    dense = [{"id": "doc1"}]
    bm25 = [{"id": "doc1"}]
    res = reciprocal_rank_fusion(dense, bm25)
    assert len(res) == 1
    assert res[0]["id"] == "doc1"
