from typing import List
import math

def cosine_similarity(v1: List[float], v2: List[float]) -> float:
    """
    Calculates Cosine Similarity (A . B) / (||A|| * ||B||).
    Essential for Vector Search ranking in RAG pipelines.
    """
    if len(v1) != len(v2): raise ValueError("Dimensions must match")
    dot = sum(a * b for a, b in zip(v1, v2))
    mag_a = math.sqrt(sum(a**2 for a in v1))
    mag_b = math.sqrt(sum(b**2 for b in v2))
    return 0.0 if mag_a * mag_b == 0 else dot / (mag_a * mag_b)