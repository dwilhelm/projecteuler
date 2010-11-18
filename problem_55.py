#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like
196, never produce a palindrome. A number that never forms a palindrome
through the reverse and add process is called a Lychrel number. Due to the
theoretical nature of these numbers, and for the purpose of this problem,
we shall assume that a number is Lychrel until proven otherwise. In
addition you are given that for every number below ten-thousand, it
will either (i) become a palindrome in less than fifty iterations, or,
(ii) no one, with all the computing power that exists, has managed so
far to map it to a palindrome. In fact, 10677 is the first number to be
shown to require over fifty iterations before producing a palindrome:
4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel
numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?

NOTE: Wording was modified slightly on 24 April 2007 to emphasise the
theoretical nature of Lychrel numbers.
"""

import sys


def ispalindromic(num):
    return str(num) == str(num)[::-1]


def revadd(num):
    return int(str(num)) + int(str(num)[::-1])


def chklychrel(num, iterlimit):
    """Test if num could be a Lychrel number using iterlimit iterations.

    Return the number of iterations needed if num is not Lychrel.
    Return iterlimit if the number might be Lychrel.
    """
    numiter = 0
    for x in xrange(iterlimit):
        num = revadd(num)
        numiter += 1
        if ispalindromic(num):
            break
    return numiter


def main(N):
    NUMPASSES = 2
    baselist = xrange(1, N)
    iterlimit = 100
    for passnum in xrange(NUMPASSES):
        lychrels = []
        for num in xrange(1, N):
            result = chklychrel(num, iterlimit)
            if result == iterlimit:
                lychrels.append(num)
                print num
        print '%d Lychrel numbers below %d with %d iterations' % (
            len(lychrels), N, iterlimit)
        baselist = lychrels
        iterlimit *= 10


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(10000)
