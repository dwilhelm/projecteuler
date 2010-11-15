#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
If p is the perimeter of a right angle triangle with integral length
sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

import math
import sys


def main(N):
    """WLOG, a < b. Note that for any solution a, b, c:

    1. a, b, c are positive integers
    2. a^2 + b^2 = c^2
    3. a + b + c = p

    Since a < c and b > 0, by eq 3,
    a = p - b - c < p - c < p - a, or
    a < p/2, giving an upper bound on a.

    From eq 2 and 3,
    a^2 + b^2 = (p-a-b)^2
              = p^2 - 2p(a+b) + (a+b)^2
              = p^2 - 2pa - 2pb + a^2 + 2ab + b^2
            0 = 2p(p/2 - a) + 2b(a-p)
     p(a-p/2) = b(a - p)
            b = p(a-p/2) / (a-p)

    So a, b, c is a solution iff the rhs is an integer. To test,
    instead of using floating point operations, use integer
    operations and verify that eq 2 holds.
    """
    solutions = {}
    pmaxnum = 0
    for p in xrange(3, N + 1):
        psol = []
        for a in xrange(1, p / 2):
            b = (p * (a - p/2)) / (a - p)
            if a > b:
                break
            c = p - a - b
            if a * a + b * b == c * c:
                psol.append((a, b, c))
        if psol:
            solutions[p] = psol
            print 'p = %d' % p
            for s in psol:
                print '\t%s' % str(s)
        if pmaxnum < len(psol):
            pmax = p
            pmaxnum = len(psol)
    print 'p = %d has the most solutions, with %d.' % (pmax, pmaxnum)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(1000)
