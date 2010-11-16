#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

import sys

from util import base
from util import comb
from util import primes


def ispandigital(n):
    digits = base.digits(n)
    return len(digits) == len(set(digits))


def main(n):
    for numdigits in xrange(n, 1, -1):
        for p in comb.permoflen(numdigits, range(numdigits, 0, -1)):
            num = base.numfromdigits(p)
            if primes.isprime(num):
                print num
                return
        print 'finished %d' % numdigits


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(9)
