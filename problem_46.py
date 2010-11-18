#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
It was proposed by Christian Goldbach that every odd composite number
can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^(2)
15 = 7 + 2×2^(2)
21 = 3 + 2×3^(2)
25 = 7 + 2×3^(2)
27 = 19 + 2×2^(2)
33 = 31 + 2×1^(2)

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of
a prime and twice a square?
"""

import math

from util import primes


def goldbachform(num):
    for s in range(int(math.sqrt(num))):
        maybeprime = num - 2 * s * s
        if primes.isprime(maybeprime):
            return (maybeprime, s)
    return ()


def main():
    done = False
    num = 9
    while not done:
        if not primes.isprime(num):
            gb = goldbachform(num)
            if gb:
                pass
                print '%d = %d + 2 * %d^2' % (num, gb[0], gb[1])
            else:
                print '%d is special' % num
                done = True
        num += 2


if __name__ == '__main__':
    main()
