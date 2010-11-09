#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
A unit fraction contains 1 in the numerator. The decimal representation
of the unit fractions with denominators 2 to 10 are given:

    ^(1)/_(2)   =   0.5
    ^(1)/_(3)   =   0.(3)
    ^(1)/_(4)   =   0.25
    ^(1)/_(5)   =   0.2
    ^(1)/_(6)   =   0.1(6)
    ^(1)/_(7)   =   0.(142857)
    ^(1)/_(8)   =   0.125
    ^(1)/_(9)   =   0.(1)
    ^(1)/_(10)  =   0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It
can be seen that ^(1)/_(7) has a 6-digit recurring cycle.

Find the value of d < 1000 for which ^(1)/_(d) contains the longest
recurring cycle in its decimal fraction part.
"""

import sys


def cyclelen(x):
    a = 1
    remainders = []
    while a:
        q, r = a / x, a % x
        if r not in remainders:
            remainders.append(r)
        else:
            return len(remainders) - remainders.index(r)
        a = 10 * r
    return 0


def main(n):
    winner = 0
    maxlen = 0
    for x in xrange(2, n):
        clen = cyclelen(x)
        if clen > maxlen:
            winner = x
            maxlen = clen
            print '%d has cycle length %d' % (winner, maxlen)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(1000)
