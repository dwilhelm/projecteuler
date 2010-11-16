#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, ^(5)C_(3) = 10.

In general,
^(n)C_(r) = n! / r!(n−r)!
where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million:
^(23)C_(10) = 1144066.

How many, not necessarily distinct, values of  ^(n)C_(r), for
1 ≤ n ≤ 100, are greater than one-million?
"""

import pdb
import sys

def ncr(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))


def main(nlim, N):
    """Notes:
    
    Use the fact that C(n, r) = C(n-1, r-1) + C(n-1, r).
    """
    total = 0
    c = [[1]]
    for n in xrange(1, nlim + 1):
        row = [1]
        for r in xrange(1, n):
            cthis = c[n - 1][r - 1] + c[n - 1][r]
            row.append(cthis)
            if cthis > N:
                total += 1
        row.append(1)
        c.append(row)
    print total


if __name__ == '__main__':
    n = 100
    N = 1000000
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    if len(sys.argv) > 2:
        N = int(sys.argv[2])
    main(n, N)
