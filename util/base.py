"""
Utilities for dealing with different number bases
"""

def binary(x):
    output = []
    while x:
        output.insert(0, str(x & 1))
        x >>= 1
    return ''.join(output)


def digits(n):
    return [int(x) for x in list(str(n))]


def numfromdigits(d):
    return int(''.join(map(str, d)))

