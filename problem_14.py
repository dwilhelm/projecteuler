#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
The following iterative sequence is defined for the set of positive
integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def getnext(n):
    """Return the next number in the sequence."""
    if n & 1:
        return 3 * n + 1
    else:
        return n / 2


def getseqlen(seqlen, n):
    """Return the length of the sequence starting with n."""
    count = 0
    m = n
    while m > n - 1:
        m = getnext(m)
        count += 1
    seqlen[n] = seqlen[m] + count
    return seqlen[n]


def main(N):
    maxlen = 1
    seqlen = [0] * (N + 1)
    for n in xrange(2, N):
        nlen = getseqlen(seqlen, n)
        if nlen > maxlen:
            maxlen = nlen
            start = n
            print 'start %d has length %d' % (start, seqlen[start])


if __name__ == '__main__':
    main(1000000)
