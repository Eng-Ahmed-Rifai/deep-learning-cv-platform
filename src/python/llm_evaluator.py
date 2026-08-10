
// Updated at: 2026-08-10T20:18:33.395Z [Pulse 2/24]
def evaluate_hallucination_score(ground_truth: str, answer: str) -> float:
    """Estimate hallucination ratio via token overlap."""
    gt_tokens = set(ground_truth.lower().split())
    ans_tokens = set(answer.lower().split())
    if not ans_tokens:
        return 0.0
    return len(gt_tokens.intersection(ans_tokens)) / len(ans_tokens)
