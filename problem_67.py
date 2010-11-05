#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click
and 'Save Link/Target As...'), a 15K text file containing a triangle
with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not
possible to try every route to solve this problem, as there are 2^(99)
altogether! If you could check one trillion (10^(12)) routes every second
it would take over twenty billion years to check them all. There is an
efficient algorithm to solve it. ;o)
"""


def getnext(data, y):
    nextrow = [0] * len(data[y])
    for x in xrange(len(data[y])):
        if data[y + 1][x] < data[y + 1][x + 1]:
            nextrow[x] = data[y + 1][x + 1]
        else:
            nextrow[x] = data[y + 1][x]
    return nextrow


def main():
    fd = open('triangle.txt')
    data = [[int(x) for x in line.split(' ')] for line in fd.readlines()]
    for row in data:
        print row
    ans = [0] * len(data)
    for y in xrange(len(data) - 2, -1, -1):
        ans = getnext(data, y)
        data[y] = [ans[i] + data[y][i] for i in range(len(ans))]
        print 'row: %d, ans=%s' % (y, ans)
        for row in data:
            print row
    print data[0][0]


if __name__ == '__main__':
    main()
