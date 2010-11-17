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


def ispandigital(n, start=1):
    """Test if the input n is pandigital.

    Let me be the number of digits of n.
    If start is 1 (default), then the test is if n is 1 to m pandigital.
    If start is 0, then the test is if n is 0 to m-1 pandigital.
    """
    digitlist = digits(n)
    return sorted(digitlist) == range(start, len(digitlist) + start)

