#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial
of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

import math


def getlimit():
    """Return the max number of digits m that a good number can have.

    Then the upper limit on the good range is 10**m.
    """
    m = 1
    C = math.log10(math.factorial(9)) + 1
    while m - math.log10(m) <= C:
        m += 1
    return m - 1


def main():
    m = getlimit()
    print m
    total = 0
    for x in xrange(10, 10**m):
        if x % 100000 == 0:
            print 'reached %7d' % x
        if x == sum([math.factorial(int(d)) for d in str(x)]):
            total += x
            print '%d is good, total = %d' % (x, total)
    print 'TOTAL = %d' % total


if __name__ == '__main__':
    main()
