#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
In England the currency is made up of pound, £, and pence, p, and there
are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""

import sys


def maxcoincount(amount, coinvalue):
    return map(lambda x: amount / x, coinvalue)


def numwaystomake(amount, coinvalue, coincount):
    total = 0
    if len(coincount) < 2:
        return len(coincount)
    idx = len(coincount) - 1
    for num in xrange(coincount[idx], -1, -1):
        remaining = amount - num * coinvalue[idx]
        newcoincount = maxcoincount(remaining, coinvalue[:idx])
        if newcoincount[1:]:
            total += numwaystomake(remaining, coinvalue[:idx],
                                   newcoincount[:idx])
        else:
            total += 1
    return total


def main(N):
    coinvalue = [1, 2, 5, 10, 20, 50, 100, 200]
    maxcoincounts = maxcoincount(N, coinvalue)
    ans = numwaystomake(N, coinvalue, maxcoincounts)
    print '%d ways to make %d from %s' % (ans, N, maxcoincounts)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(200)

