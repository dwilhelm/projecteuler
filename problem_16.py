#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
2^(15) = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^(1000)?
"""

import sys


def main(N):
    print sum([int(digit) for digit in str(2 ** N)])


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(15)
