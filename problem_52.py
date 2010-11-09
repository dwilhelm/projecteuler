#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
It can be seen that the number, 125874, and its double, 251748, contain
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
"""

import math
import sys


def digits(n):
    return sorted([int(d) for d in str(n)])


def found(x, N):
    for n in xrange(2, N + 1):
        if digits(x) != digits(n * x):
            return False
    return True


def main(N):
    """Find the smallest positive integer x such that 2x, 3x, ..., Nx
    contain the same digits.

    Since all multiples have the same number of digits, the first digit
    cannot be greater than floor(10 / N).
    """
    freedigits = 1
    while True:
        for f in xrange(1, 10 / N + 1):
            for d in xrange(1, 10**freedigits):
                x = f * 10**freedigits + d
                if found(x, N):
                    print 'found x = %d' % x
                    print map(lambda n: n * x, range(1, N + 1))
                    return
        freedigits += 1


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(6)

