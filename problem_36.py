#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
The decimal number, 585 = 1001001001_(2) (binary), is palindromic in
both bases.

Find the sum of all numbers, less than one million, which are palindromic
in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""

import math
import sys
import util


def ispal2(x):
    binary = util.binary(x)
    return binary == binary[::-1]


def main(n):
    ndigits = int(math.ceil(math.log10(n)))
    print ndigits
    pal10 = range(10)
    pal10 += [int(str(x) + str(x)[::-1]) for x in xrange(1, 10**(ndigits / 2))]
    pal10 += [int(str(x) + str(y) + str(x)[::-1])
              for x in xrange(1, 10**((ndigits - 1) / 2))
              for y in range(10)]
    pal10 = sorted(list(set(pal10)))
    goodnums = [x for x in pal10 if ispal2(x)]
    print goodnums, len(goodnums)
    print sum(goodnums)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(1000000)

