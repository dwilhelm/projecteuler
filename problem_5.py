#!/usr/bin/env python
"""
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of
the numbers from 1 to 20?
"""

import sys


def primefac(primes, x):
    """Return the prime factorization of the input int x.
    
    This assumes that primes is a list of all prime numbers less than
    (or possibly equal to) the input x.
    """
    fac = {}
    for p in primes:
        count = 0
        while x % p == 0:
            x /= p
            count += 1
        if count:
            fac[p] = count
    if x > 1:
        fac[x] = 1
    return fac


def print_ans(N):
    """Print the desired number."""
    anspfac = getanspfac(N)
    print 'The prime factorization when N=%d is:' % N
    for p in anspfac:
        print '  %6d ** %d' % (p, anspfac[p])
    f = lambda x, y: x * y
    print reduce(f, [p**exp for p, exp in anspfac.items()])


def getanspfac(N):
    """Return the prime factorization of the desired number."""
    primes = [2]
    anspfac = {}
    for n in xrange(2, N+1):
        fac = primefac(primes, n)
        # if n is prime, add it to the list and update the answer
        if len(fac) == 1 and fac.values()[0] == 1:
            primes.append(n)
            anspfac[n] = 1
        # else update the answer based on the prime factorization of n
        else:
            for p in fac:
                anspfac[p] = max(anspfac[p], fac[p])
    return anspfac


def main():
    if len(sys.argv) > 1:
        print_ans(int(sys.argv[1]))
    else:
        print_ans(10)
        print_ans(20)


if __name__ == '__main__':
    main()
