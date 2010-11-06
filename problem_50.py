#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime
below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to
a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

import sys
import util


def getmaxwinlen(n):
    winlen = 1
    total = util.primes[0]
    p = util.primes[-1]
    while total <= p:
        winlen += 1
        total += util.primes[winlen - 1]
    return winlen - 1


def primeforlen(winlen):
    for idx in xrange(len(util.primes) - winlen):
        p = sum(util.primes[idx : idx + winlen])
        if p in util.primes:
            return (p, idx, winlen)
        elif p > util.primes[-1]:
            break
    return (0, 0, 0)


def main(n):
    util.genprimesto(n)
    maxwinlen = getmaxwinlen(n)
    print 'maxwinlen is %d' % maxwinlen
    for winlen in xrange(maxwinlen, -1, -1):
        print 'trying %d' % winlen
        p, idx, maxlen = primeforlen(winlen)
        if p:
            break
        winlen += 1
    print '%d is the sum of %d terms starting at index %d' % (p, maxlen, idx)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(100)
        main(1000)
        main(1000000)
