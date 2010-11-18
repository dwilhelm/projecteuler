#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime
factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct primes
factors. What is the first of these numbers?
"""

from util import primes


def main():
    num = 648
    pfact = map(primes.getprimefactors, range(num, num + 4))
    pfactcount = map(len, pfact)
    while min(pfactcount) < 4:
        if num % 10000 == 0:
            print num, pfactcount, pfact
        num += 1
        pfact = map(primes.getprimefactors, range(num, num + 4))
        pfactcount = map(len, pfact)
    print '%d is the answer. The seq has factors %s' % (num, pfact)


if __name__ == '__main__':
    main()
