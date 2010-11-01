#!/usr/bin/env python
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c,
for which, a^(2) + b^(2) = c^(2)

For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import math


def main():
    N = 1000
    for c in xrange(2, N):
        for b in xrange(1, c):
            a = N - b - c
            if a * a + b * b == c * c:
               print 'a=%d b=%d c=%d' % (a, b, c)
               print 'abc=%d' % (a * b * c)
               return
        c += 1


if __name__ == '__main__':
    main()
