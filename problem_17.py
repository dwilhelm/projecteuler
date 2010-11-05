#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred
and forty-two) contains 23 letters and 115 (one hundred and fifteen)
contains 20 letters. The use of "and" when writing out numbers is in
compliance with British usage.
"""

import sys


def getengdigit(n):
    """Return the english word for the digit n."""
    if n % 10 == 9:
        return 'nine '
    elif n % 10 == 8:
        return 'eight '
    elif n % 10 == 7:
        return 'seven '
    elif n % 10 == 6:
        return 'six '
    elif n % 10 == 5:
        return 'five '
    elif n % 10 == 4:
        return 'four '
    elif n % 10 == 3:
        return 'three '
    elif n % 10 == 2:
        return 'two '
    elif n % 10 == 1:
        return 'one '
    else:
        return ''


def getengfromtensones(n):
    """Return the english for the the tens digit for input n."""
    digitstr = ''
    if n >= 90:
        digitstr = 'ninety '
    elif n >= 80:
        digitstr = 'eighty '
    elif n >= 70:
        digitstr = 'seventy '
    elif n >= 60:
        digitstr = 'sixty '
    elif n >= 50:
        digitstr = 'fifty '
    elif n >= 40:
        digitstr = 'forty '
    elif n >= 30:
        digitstr = 'thirty '
    elif n >= 20:
        digitstr = 'twenty '
    elif n >= 10:
        if n == 19:
            return 'nineteen'
        elif n == 18:
            return 'eighteen'
        elif n == 17:
            return 'seventeen'
        elif n == 16:
            return 'sixteen'
        elif n == 15:
            return 'fifteen'
        elif n == 14:
            return 'fourteen'
        elif n == 13:
            return 'thirteen'
        elif n == 12:
            return 'twelve'
        elif n == 11:
            return 'eleven'
        elif n == 10:
            return 'ten'
    return digitstr + getengdigit(n)


def getengfromint(n):
    """Return the english representation of the input n.
    
    This assumes that n is less than 10000."""
    digitstr = ''
    if n % 10000 > 999:
        digitstr += getengdigit(int(str(n)[-4])) + 'thousand '
    if n % 1000 > 99:
        digitstr += getengdigit(int(str(n % 1000)[-3])) + 'hundred '
    if n > 99 and n % 100:
        digitstr += 'and '
    digitstr += getengfromtensones(n % 100)
    return digitstr


def main(n):
    count = 0
    for m in xrange(1, n + 1):
        english = [x for x in getengfromint(m).rstrip() if x != ' ']
        print ''.join(english)
        count += len(english)
    print count


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(5)
