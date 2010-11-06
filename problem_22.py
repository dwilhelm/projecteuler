#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text
file containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each
name, multiply this value by its alphabetical position in the list to
obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the
list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

def num(letter):
    return ord(letter) - ord('A') + 1

def main():
    fd = open('names.txt')
    names = fd.read().split(',')
    names = sorted(n.strip('"') for n in names)
    scores = [0] * len(names)
    for idx in xrange(len(names)):
        scores[idx] = (idx + 1) * sum(num(x) for x in names[idx])
        print '%4d %12s %d' % (idx + 1, names[idx], scores[idx])
    print sum(scores)


if __name__ == '__main__':
    main()

