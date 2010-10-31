#!/usr/bin/env python
"""
Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Find the sum of all the even-valued terms in the sequence which do not
exceed four million.
"""

import sys


def ans(N):
    parents = [1, 2]
    total = 2
    next = sum(parents)
    while next < N:
        if next & 1 == 0:
            total += next
        parents = [parents[1], next]
        next = sum(parents)
    return total


def main():
    if len(sys.argv) > 1:
        N = int(sys.argv[1])
    else:
        N = 4000000
    print ans(N)


if __name__ == '__main__':
    main()
