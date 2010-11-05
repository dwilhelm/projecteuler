#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
The series, 1^(1) + 2^(2) + 3^(3) + ... + 10^(10) = 10405071317.

Find the last ten digits of the series, 1^(1) + 2^(2) + 3^(3) + ... +
1000^(1000).
"""

import sys


def main(n):
    print str(sum([x**x % 10**10 for x in range(1, n + 1)]))[-10:]


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(10)

