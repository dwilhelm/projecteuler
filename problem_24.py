#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
A permutation is an ordered arrangement of objects. For example, 3124
is one possible permutation of the digits 1, 2, 3 and 4. If all of
the permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2,
3, 4, 5, 6, 7, 8 and 9?
"""

import math
import sys


def main(n):
    digits = range(10)
    ans = []
    fac = map(math.factorial, range(9, 0, -1))
    print 'n=%7d ans=%s digits=%s' % (n, ans, digits)
    while len(fac):
        div = (n - 1) / fac[0]
        ans.append(str(digits.pop(div)))
        n -= div * fac[0]
        fac.pop(0)
        print 'n=%7d ans=%s digits=%s' % (n, ans, digits)
    ans.append(str(digits.pop()))
    print ''.join(ans)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(1000000)
