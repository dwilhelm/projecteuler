#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Euler published the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive
values n = 0 to 39. However, when n = 40, 40^(2) + 40 + 41 = 40(40 + 1)
+ 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is
clearly divisible by 41.

Using computers, the incredible formula  n² − 79n + 1601 was
discovered, which produces 80 primes for the consecutive values n =
0 to 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n² + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic
expression that produces the maximum number of primes for consecutive
values of n, starting with n = 0.
"""

import sys
import util


def primeseq(a, b, N):
    primes = []
    f = lambda n, a, b: n * n + a * n + b
    for n in xrange(N):
        num = f(n, a, b)
        if num < 2 or not util.isprime(num):
            return primes
        else:
            primes.append(num)
    return primes


def main(N):
    maxnum = 0
    a_ans = 0
    b_ans = 0
    primes_ans = []
    util.genprimesto(2 * N)
    print util.primes[-1]
    for a in xrange(-N + 1, N):
        for b in xrange(-N + 1, N):
            primes = primeseq(a, b, N)
            if len(primes) >= maxnum:
                maxnum = len(primes)
                a_ans = a
                b_ans = b
                primes_ans = primes
                print '%4d: a=%d b=%d' % (len(primes), a, b)
    print primes_ans
    print 'a * b = %d * %d = %d' % (a_ans, b_ans, a_ans * b_ans)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(1000)
