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


def popcache(cache, csize):
    fac = map(math.factorial, range(10))
    for x in range(csize):
        cache[x] = sum([fac[int(d)] for d in str(x)])


def main():
    m = getlimit()
    print 'Numbers have %d digits at most' % m
    csize = 10000
    cache = [0] * csize
    popcache(cache, csize)
    total = 0
    for x in xrange(10, 10**m):
        if x % 100000 == 0:
            print 'reached %7d' % x
        if x < csize:
            thissum = cache[x % csize]
        else:
            if x % csize < 10:
                thissum = cache[x % csize] + 3
            elif x % csize < 100:
                thissum = cache[x % csize] + 2
            elif x % csize < 1000:
                thissum = cache[x % csize] + 1
            else:
                thissum = cache[x % csize]
            thissum += cache[x / csize]
        if x == thissum:
            total += x
            print '%d is good, total = %d' % (x, total)
    print 'TOTAL = %d' % total


if __name__ == '__main__':
    main()
