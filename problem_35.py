#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
The number, 197, is called a circular prime because all rotations of
the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31,
37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

import sys

from util import primes


def iscircular(p):
    """Test if the prime p is a circular prime."""
    p = str(p)
    for i in xrange(1, len(p)):
        if not primes.isprime(int(p[i:] + p[:i])):
            return False
    return True


def main(n):
    primes.genprimesto(n)
    print '%s...%d...%s' % (primes.plist[:4], len(primes.plist),
                            primes.plist[-4:])
    cir = [p for p in primes.plist if iscircular(p)]
    print '%s...%d...%s' % (cir[:4], len(cir), cir[-4:])
    print 'There are %d circular primes below %d' % (len(cir), n)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(100)
        main(1000000)

