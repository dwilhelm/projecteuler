#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We
will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3,
4, and 5, giving the pandigital, 918273645, which is the concatenated
product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed
as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

from util import base


def catproduct(n, seq):
    output = ''
    for idx in xrange(len(seq)):
        output += str(n * seq[idx])
    return int(output)


def main():
    winner = 0
    for n in xrange(2, 10):
        num = base.numfromdigits(range(1, 9 / n + 1))
        while num and num < 10**(10 / n):
            cprod = catproduct(num, range(1, n + 1))
            if base.ispandigital(cprod) and cprod > winner:
                winner = cprod
                print 'new lead %d, num %d, n %s' % (winner, num, n)
            if num == 192:
                print num, range(1, n + 1), cprod
            num += 1


if __name__ == '__main__':
    main()
