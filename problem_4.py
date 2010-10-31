#!/usr/bin/env python
"""
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import sys


def ispalindrome(n):
    return str(n) == str(n)[::-1]


def run(ndigits):
    pals = {}
    for x in xrange(10 ** (ndigits - 1), 10 ** ndigits):
        for y in xrange(x, 10 ** ndigits):
            if ispalindrome(x * y):
                pals[x * y] = (x, y)
    largest = max(pals.keys())
    #print sorted(pals.keys())
    print '%d = %d * %d' % ((largest,) + pals[largest])


def main():
    if len(sys.argv) > 1:
        run(int(sys.argv[1]))
    else:
        run(2)
        run(3)


if __name__ == '__main__':
    main()
