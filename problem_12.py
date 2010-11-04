#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
The sequence of triangle numbers is generated by adding the natural
numbers. So the 7^(th) triangle number would be
1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five
divisors.

What is the value of the first triangle number to have over five hundred
divisors?
"""

import util


def numfactors(n):
    expcount = [x + 1 for x in util.getprimefactors(n).values()]
    return reduce(lambda a, b: a * b, expcount)


def main():
    idx = 2
    while True:
        n = idx * (idx + 1) / 2
        numfac = numfactors(n)
        print '%d has %d factors' % (n, numfac)
        if numfac > 500:
            return
        idx += 1


if __name__ == '__main__':
    main()
