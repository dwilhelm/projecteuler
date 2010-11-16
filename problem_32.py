#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once; for example, the 5-digit number, 15234,
is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to
only include it once in your sum.
"""

from util import comb

def main():
    """Notes:

    Let x and y be the multiplicand and multiplier, where x has
    m digits and y has n digits. Then
    10^{m-1} <= x < 10^{m} and 10^{n-1} <= y < 10^{n} so
    10^{m+n-2} <= xy < 10^{m+n}

    For this problem, the number of digits of xy must be 9-m-n, so
    m+n-2 <= 9-(m+n) < m+n or
    -2 <= 9 - 2(m+n) < 0
    -11 <= -2(m+n) < -9
    9/2 < m+n <= 11/2
    and m+n = 5, since m+n must be an integer.

    WLOG m < n, so x has 1 or 2 digits and y has 4 or 3 digits.
    """
    alldigits = '123456789'
    products = []
    for p in comb.permoflen(4, alldigits):
        for m in xrange(1, 3):
            n = 5 - m
            remaining_x = [d for d in alldigits if d not in p]
            for x in comb.permoflen(m, remaining_x):
                remaining_y = [d for d in alldigits if d not in p + x]
                for y in comb.permoflen(n, remaining_y):
                    xval = int(''.join(x)) 
                    yval = int(''.join(y)) 
                    pval = int(''.join(p)) 
                    if xval * yval == pval and pval not in products:
                        products.append(pval)
                        print 'x=%s, y=%s, p=%s' % (x, y, p)
                    elif xval * yval > pval:
                        break  # all remaining y will also be too big
    print sum(products)


if __name__ == '__main__':
    main()
