#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made
up of each of the digits 0 to 9 in some order, but it also has a rather
interesting sub-string divisibility property.

Let d_(1) be the 1^(st) digit, d_(2) be the 2^(nd) digit, and so on. In
this way, we note the following:

    * d_(2)d_(3)d_(4)=406 is divisible by 2
    * d_(3)d_(4)d_(5)=063 is divisible by 3
    * d_(4)d_(5)d_(6)=635 is divisible by 5
    * d_(5)d_(6)d_(7)=357 is divisible by 7
    * d_(6)d_(7)d_(8)=572 is divisible by 11
    * d_(7)d_(8)d_(9)=728 is divisible by 13
    * d_(8)d_(9)d_(10)=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from util import comb
from util import base


def isgood(num):
    num = str(num)
    if int(num[2:5]) % 3 != 0:
        return False
    if int(num[3:6]) % 5 != 0:
        return False
    if int(num[4:7]) % 7 != 0:
        return False
    if int(num[5:8]) % 11 != 0:
        return False
    if int(num[6:9]) % 13 != 0:
        return False
    if int(num[7:10]) % 17 != 0:
        return False
    return True


def main():
    total = 0
    for p in comb.permoflen(10, range(10)):
        if p[3] & 1:
            continue
        p = base.numfromdigits(p)
        if isgood(p):
            total += p
            print p
    print total


if __name__ == '__main__':
    main()
