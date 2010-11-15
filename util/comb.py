"""
Combinatorics utilities
"""

def seqoflen(n, items):
    """Generate all sequences of length n from items as lists."""
    assert type(n) == int
    if not n:
        yield []
        return
    for item in list(items):
        for seq in seqoflen(n - 1, items):
            yield [item] + seq

