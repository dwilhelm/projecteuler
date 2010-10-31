#!/usr/bin/env python
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import math
import sys

def lastmultiple(x, N):
    """Return the quotient for the largest multiple of x less than N."""
    return math.floor((N - 1) / x)

def summultiples(x, N):
    """Return the sum of all multiples of x less than N.

    Note that if M = lastmultiple(x, N), the sum S can be written as
    S = sum([x * k for k in range(1, M)])
      = x * sum([k for k in range(1, M)])
      = x * M * (M + 1) / 2
    """
    M = lastmultiple(x, N)
    return int(x * M * (M + 1) / 2)

def ans(N):
    return summultiples(3, N) + summultiples(5, N) - summultiples(15, N)

def main():
    if len(sys.argv) > 1:
        print ans(int(sys.argv[1]))
    else:
        print ans(10)
        print ans(1000)

if __name__ == '__main__':
    main()
