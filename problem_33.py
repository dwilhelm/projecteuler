#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
The fraction ^(49)/_(98) is a curious fraction, as an inexperienced
mathematician in attempting to simplify it may incorrectly believe that
^(49)/_(98) = ^(4)/_(8), which is correct, is obtained by cancelling
the 9s.

We shall consider fractions like, ^(30)/_(50) = ^(3)/_(5), to be trivial
examples.

There are exactly four non-trivial examples of this type of fraction,
less than one in value, and containing two digits in the numerator
and denominator.

If the product of these four fractions is given in its lowest common
terms, find the value of the denominator.
"""

from util import base
from util import divisors

def main():
    """Note that since multiples of 10 are considered trivial, digits
    of zero are never present in the fractions of interest.
    """
    curious = []
    for x in xrange(11, 100):
        if x % 10 == 0:
            continue
        for y in xrange(x + 1, 100):
            if y % 10 == 0:
                continue
            xd = base.digits(x)
            yd = base.digits(y)
            d = list(set(xd) & set(yd))
            if d:
                d = d[0]
                xd.remove(d)
                yd.remove(d)
                xprime = base.numfromdigits(xd)
                yprime = base.numfromdigits(yd)
                if x * yprime == xprime * y:
                    curious.append((xprime, yprime))
                    print '%d / %d, %d / %d' % (x, y, xprime, yprime)
    num = 1
    den = 1
    for x, y in curious:
        num *= x
        den *= y
    g = divisors.gcd(num, den)
    print '%d / %d reduces to %d / %d, gcd %d' % (num, den, num/g, den/g, g)


if __name__ == '__main__':
    main()
