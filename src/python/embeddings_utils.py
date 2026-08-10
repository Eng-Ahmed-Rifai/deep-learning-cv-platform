
// Updated at: 2026-08-10T20:18:33.486Z [Pulse 11/24]
import math

def l2_normalize(vector):
    """Normalize embedding vector using L2 norm."""
    norm = math.sqrt(sum(x * x for x in vector))
    if norm == 0:
        return vector
    return [x / norm for x in vector]
