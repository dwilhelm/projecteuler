"""
Utilities for dealing with different number bases
"""

def binary(x):
    output = []
    while x:
        output.insert(0, str(x & 1))
        x >>= 1
    return ''.join(output)

