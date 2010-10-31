#!/usr/bin/env python
"""
The sum of the squares of the first ten natural numbers is,
1^(2) + 2^(2) + ... + 10^(2) = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^(2) = 55^(2) = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""

import sys


def main():
    if len(sys.argv) > 1:
        N = int(sys.argv[1])
    else:
        N = 100
    ssdiff = lambda prev, n: prev + n * n * (n - 1)
    prev = 0
    for n in xrange(N + 1):
        prev = ssdiff(prev, n)
        print '%4d: %10d' % (n, prev)


if __name__ == '__main__':
    main()
