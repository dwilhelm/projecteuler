#!/usr/bin/env python
"""
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of
the numbers from 1 to 20?
"""

import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

def main():
    if len(sys.argv) > 1:
        N = int(sys.argv[1])
        print reduce(lcm, range(1, N))
    else:
        print reduce(lcm, range(1, 10))
        print reduce(lcm, range(1, 20))

if __name__ == '__main__':
    main()
    
