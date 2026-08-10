"""
RAG Faithfulness & Groundedness Metric Evaluator
Author: Junior AI Engineer
"""

from typing import List, Dict, Any

class FaithfulnessEvaluator:
    def __init__(self, token_overlap_threshold: float = 0.65):
        self.threshold = token_overlap_threshold

    def evaluate_groundedness(self, context_passages: List[str], generated_answer: str) -> Dict[str, Any]:
        """Measures what percentage of generated sentences are grounded in source context."""
        sentences = [s.strip() for s in generated_answer.split('.') if s.strip()]
        if not sentences:
            return {"score": 1.0, "is_grounded": True}

        context_tokens = set(" ".join(context_passages).lower().split())
        grounded_count = 0

        for sentence in sentences:
            sent_tokens = set(sentence.lower().split())
            if not sent_tokens:
                continue
            overlap = len(sent_tokens.intersection(context_tokens)) / len(sent_tokens)
            if overlap >= self.threshold:
                grounded_count += 1

        score = grounded_count / len(sentences)
        return {
            "score": round(score, 4),
            "grounded_sentences": grounded_count,
            "total_sentences": len(sentences),
            "is_grounded": score >= 0.8
        }
