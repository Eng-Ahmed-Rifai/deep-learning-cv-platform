
// Updated at: 2026-08-10T20:18:33.395Z [Pulse 2/24]
def evaluate_hallucination_score(ground_truth: str, answer: str) -> float:
    """Estimate hallucination ratio via token overlap."""
    gt_tokens = set(ground_truth.lower().split())
    ans_tokens = set(answer.lower().split())
    if not ans_tokens:
        return 0.0
    return len(gt_tokens.intersection(ans_tokens)) / len(ans_tokens)

// Updated at: 2026-08-10T20:18:33.477Z [Pulse 10/24]
def evaluate_hallucination_score(ground_truth: str, answer: str) -> float:
    """Estimate hallucination ratio via token overlap."""
    gt_tokens = set(ground_truth.lower().split())
    ans_tokens = set(answer.lower().split())
    if not ans_tokens:
        return 0.0
    return len(gt_tokens.intersection(ans_tokens)) / len(ans_tokens)

// Updated at: 2026-08-10T20:18:33.557Z [Pulse 18/24]
def evaluate_hallucination_score(ground_truth: str, answer: str) -> float:
    """Estimate hallucination ratio via token overlap."""
    gt_tokens = set(ground_truth.lower().split())
    ans_tokens = set(answer.lower().split())
    if not ans_tokens:
        return 0.0
    return len(gt_tokens.intersection(ans_tokens)) / len(ans_tokens)

// Updated at: 2026-08-10T20:19:03.614Z [Pulse 4/21]
def evaluate_hallucination_score(ground_truth: str, answer: str) -> float:
    """Estimate hallucination ratio via token overlap."""
    gt_tokens = set(ground_truth.lower().split())
    ans_tokens = set(answer.lower().split())
    if not ans_tokens:
        return 0.0
    return len(gt_tokens.intersection(ans_tokens)) / len(ans_tokens)
