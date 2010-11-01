#!/usr/bin/env python
"""
Miscellaneous utilies for Project Euler problems.
"""

import math


primes = [2, 3, 5]

def isprime(n):
    """Return if the input n is prime.

    This assumes that primes is a list that includes all primes less
    than or equal to sqrt(n).
    """
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n & 1 == 0:
        return False
    elif n in primes:
        return True
    for p in primes:
        if n % p == 0:
            return False
    p = primes[-1]
    while primes[-1] < math.floor(math.sqrt(n)):
        p += 2
        if isprime(p):
            primes.append(p)
            if n % p == 0:
                return False
    return True


def genprimesto(n):
    """Extend the primes list up to, but not including n."""
    for p in xrange(primes[-1] + 2, n, 2):
        if isprime(p):
            primes.append(p)


def gennewprimes(n):
    """Extend the primes list by n more entries."""
    p = primes[-1]
    added = 0
    while added < n:
        p += 2
        if isprime(p):
            primes.append(p)
            added += 1

