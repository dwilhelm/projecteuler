#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
The n^(th) term of the sequence of triangle numbers is given by, t_(n)
= ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t_(10). If the word
value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text
file containing nearly two-thousand common English words, how many are
triangle words?
"""

import math


t = [0]


def score(word):
    return sum([ord(c) - ord('A') + 1 for c in word.upper()])


def istriangular(n):
    global t
    while t[-1] < n:
        m = len(t)
        t.append(m * (m + 1) / 2)
    return n in t


def main():
    words = [x.strip('"') for x in open('words.txt', 'r').read().split(',')]
    total = 0
    for word in open('words.txt', 'r').read().split(','):
        word = word.strip('"')
        print word, score(word)
        if istriangular(score(word)):
            total += 1
    print total


if __name__ == '__main__':
    main()

