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
    if d:
        return int(''.join(map(str, d)))
    else:
        return 0


def ispandigital(n):
    digitlist = digits(n)
    return sorted(digitlist) == range(1, len(digitlist) + 1)

