#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
A googol (10^(100)) is a massive number: one followed by one-hundred
zeros; 100^(100) is almost unimaginably large: one followed by two-hundred
zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^(b), where a, b < 100, what
is the maximum digital sum?
"""

import sys

from util import base


def main(N):
    winner = 0
    for a in xrange(N):
        for b in xrange(N):
            digitalsum = sum(base.digits(a**b))
            if digitalsum > winner:
                print digitalsum, a, b, a**b
                winner = digitalsum
    print winner


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(100)
