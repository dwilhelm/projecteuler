#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from
left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

import time

from util import comb
from util import primes


def istruncatable(p):
    """Test if the number p is truncatable."""
    if p < 10 or not primes.isprime(p):
        return False
    for idx in xrange(1, len(str(p))):
        if not primes.isprime(int(str(p)[idx:])):
            return False
        if not primes.isprime(int(str(p)[:-idx])):
            return False
    return True


def testnum(num, truncatable):
    if istruncatable(int(num)) and num not in truncatable:
        truncatable.append(num)
        print truncatable


def main():
    """Use strings to build valid truncatable primes.

    Note that all truncatable primes must have prime first and last
    digits. Since all other digits will be the ones digit in some
    truncation, they cannot be even or 5. So all trunctable primes
    have the form abb...bba where the a are in the set (2, 3, 5, 7)
    and the b are in the set (1, 3, 7, 9).
    """
    enddigits = '2357'
    middigits = '1379'
    truncatables = []
    midlen = 0
    while len(truncatables) < 11:
        for n1 in enddigits:
            for n2 in enddigits:
                for midseq in comb.seqoflen(midlen, middigits):
                    testnum(n1 + ''.join(midseq) + n2, truncatables)
                    testnum(n2 + ''.join(midseq) + n1, truncatables)
        midlen += 1
    print sum([int(x) for x in truncatables])


if __name__ == '__main__':
    main()
