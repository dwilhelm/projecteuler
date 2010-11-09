#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
An irrational decimal fraction is created by concatenating the positive
integers:

0.123456789101112131415161718192021...

It can be seen that the 12^(th) digit of the fractional part is 1.

If d_(n) represents the n^(th) digit of the fractional part, find the
value of the following expression.

d_(1) × d_(10) × d_(100) × d_(1000) × d_(10000) × d_(100000)
× d_(1000000)
"""

import math
import sys


def main(n):
    data = []
    i = 1
    while len(data) < n:
        data.append(str(i))
        i += 1
    d = lambda n: int(''.join(data)[n - 1])
    ans = 1
    for x in xrange(int(math.log10(n)) + 1):
        print 10**x, d(10**x)
        ans *= d(10**x)
    print 'answer is %d' % ans


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(1000000)
