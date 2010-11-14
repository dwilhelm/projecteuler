#!/usr/bin/env python
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import sys

from util import primes


def main(N):
    primes.genprimesto(N)
    print reduce(lambda a, b: a + b, primes.plist)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(10)
        main(2000000)
