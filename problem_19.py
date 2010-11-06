#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
You are given the following information, but you may prefer to do some
research for yourself.

    * 1 Jan 1900 was a Monday.
    * Thirty days has September,
      April, June and November.
      All the rest have thirty-one,
      Saving February alone,
      Which has twenty-eight, rain or shine.
      And on leap years, twenty-nine.
    * A leap year occurs on any year evenly divisible by 4, but not on
    a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?
"""


def isleapyear(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


def daysinmonth(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif isleapyear(year):
        return 29
    else:
        return 28


def main():
    dow = 1
    total = 0
    for year in xrange(1900, 2001):
        for month in xrange(1, 13):
            if dow == 0 and year > 1900:
                total += 1
                print '%2d %d %d total=%d' % (month, year, dow, total)
            days = daysinmonth(year, month)
            dow = (dow + days) % 7
    print total


if __name__ == '__main__':
    main()

