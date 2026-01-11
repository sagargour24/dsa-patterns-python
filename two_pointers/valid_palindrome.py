def is_palindrome(s: str) -> bool:
    """Time: O(n), Space: O(1). Cleans string and compares ends."""
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]