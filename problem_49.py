#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms
are prime, and, (ii) each of the 4-digit numbers are permutations of
one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
primes, exhibiting this property, but there is one other 4-digit
increasing sequence.

What 12-digit number do you form by concatenating the three terms in
this sequence?
"""

from util import base
from util import primes


def findprogression(seq):
    for center in xrange(1, len(seq) - 1):
        for left in xrange(center):
            for right in xrange(center + 1, len(seq)):
                if seq[center] - seq[left] == seq[right] - seq[center]:
                    return [seq[left], seq[center], seq[right]]
    return []

def main():
    primes.genprimesto(10000)
    pool = [p for p in primes.plist if p > 1000]
    while pool:
        seqdigits = sorted(base.digits(pool[0]))
        seq = []
        for p in pool:
            if sorted(base.digits(p)) == seqdigits:
                seq.append(p)
                pool.remove(p)
        progression = findprogression(seq)
        if progression:
            print seq, progression, progression[1] - progression[0]
            print ''.join(map(str, progression))


if __name__ == '__main__':
    main()
