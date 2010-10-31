#!/usr/bin/env python
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

import math
import sys


def isprime(primes, n):
    """Return if the input n is prime.

    This assumes that primes is a list that includes all primes less
    than or equal to sqrt(n).
    """
    assert primes[-1] >= long(math.floor(math.sqrt(n)))
    if n < 2:
        return False
    for p in primes:
        if n % p == 0:
            return False
    return True


def updatepfac(primes, n, pfac):
    """Update the prime factorization of n based on the current list.
    
    There must be at least one prime in the list."""
    count = 0
    p = primes[-1]
    while n % p == 0:
        n /= p
        count += 1
    if count:
        pfac[p] = count
        print 'updatepfac: n=%d, p=%d, pfac=%s' % (n, p, pfac)
    return n, pfac


def primefac(n):
    """Return the prime factorization of the input int n."""
    primes = [2]
    pfac = {}
    n, pfac = updatepfac(primes, n, pfac)
    primes.append(3)
    n, pfac = updatepfac(primes, n, pfac)
    x = primes[-1] + 2
    lim = math.floor(math.sqrt(n)) + 1
    while x < lim:
        if isprime(primes, x):
            primes.append(x)
            print '\tnew prime %d' % x
            n, pfac = updatepfac(primes, n, pfac)
            lim = math.floor(math.sqrt(n)) + 1
        x += 2
    if n > 1:
        # If some factor still hasn't been accounted for, it must be prime.
        # Note that the list primes is probably not complete any more.
        # There may be primes < n that aren't included since they
        # aren't factors of the original number N.
        primes.append(n)
        n, pfac = updatepfac(primes, n, pfac)
    print 'primes %s' % primes
    return pfac


def print_pfac(pfac):
    print 'The complete prime factorization is:'
    for p in pfac:
        print '  %6d ** %d' % (p, pfac[p])


def main():
    if len(sys.argv) > 1:
        print_pfac(primefac(int(sys.argv[1])))
    else:
        print_pfac(primefac(317584931803))
        print_pfac(primefac(600851475143))


if __name__ == '__main__':
    main()
