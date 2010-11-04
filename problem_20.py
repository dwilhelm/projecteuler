#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
n! means n × (n − 1) × ... × 3 × 2 × 1

Find the sum of the digits in the number 100!
"""

import sys


def main(N):
    fac = reduce(lambda a, b: a * b, range(1, N + 1))
    print sum([int(digit) for digit in str(fac)])


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(100)
