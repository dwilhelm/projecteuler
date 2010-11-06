#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Surprisingly there are only three numbers that can be written as the
sum of fourth powers of their digits:

    1634 = 1^(4) + 6^(4) + 3^(4) + 4^(4)
    8208 = 8^(4) + 2^(4) + 0^(4) + 8^(4)
    9474 = 9^(4) + 4^(4) + 7^(4) + 4^(4)

As 1 = 1^(4) is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth
powers of their digits.
"""

import math
import sys


def ispossiblelen(m, n):
    """Return if it's possible for an m-digit number to be groovy.

    For this problem, "groovy" means that the number is equal to the
    sum of its digits each raised to the n-th power.

    Let G := sum_{i=0}^{m-1} d_i * 10^i = sum_{i=0}^{m-1} d_i^n.
    Since G has m digits, 10^{m-1} <= G < 10^m and since d_i <= 9
    for all i, G <= m * 9^n, or 10^{m-1} <= m * 9^n.

    Taking the log of both sides and rewriting,
    log(10^{m-1}) <= log(m * 9^n),
    m-1 <= log(m) + n * log(9),
    m - log(m) <= n * log(9) + 1

    So if m doesn't satisfy the above inequality, it's impossible for
    an m-digit number to be groovy. The left hand side is increasing
    for m > 1, so once a bad value of m is reached, all larger m are
    also out.
    """
    if m - math.log10(m) < n * math.log10(9) + 1:
        return True
    else:
        return False

def main(n):
    groovynums = []
    numdigits = 0
    while ispossiblelen(numdigits + 1, n):
        numdigits += 1
    print 'Numbers can have at most %d digits.' % numdigits
    for x in xrange(2, 10**numdigits):
        if sum(int(d)**n for d in str(x)) == x:
            print '%d is groovy' % x
            groovynums.append(x)
    print '%d is the sum' % sum(groovynums)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(5)
