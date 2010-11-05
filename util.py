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
    global primes
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
    global primes
    if n <= primes[-1]:
        return
    primes = [2] + range(3, n, 2)
    idx = 1
    while primes[idx] <= math.sqrt(primes[-1]):
        p = primes[idx]
        primes = [x for x in primes if x <= p or x % p]
        idx += 1


def gennewprimes(n):
    """Extend the primes list by n more entries."""
    p = primes[-1]
    added = 0
    while added < n:
        p += 2
        if isprime(p):
            primes.append(p)
            added += 1


def getprimefactors(n):
    """Return the prime factorization of the input n."""
    assert n > 1
    primefactors = {}
    count = 0
    while n & 1 == 0:
        count += 1
        n >>= 1
    if count:
        primefactors[2] = count
        count = 0
    for x in xrange(3, int(math.floor(math.sqrt(n))) + 1, 2):
        while n % x == 0:
            count += 1
            n /= x
        if count:
            primefactors[x] = count
            count = 0
    if n > 1:
        primefactors[n] = 1  # n is prime
    return primefactors


def getdivisors(n):
    """Return a list of the all divisors of the input n."""
    divisors = [1]
    pfac = getprimefactors(n)
    for p in pfac:
        pnew = []
        for x in xrange(1, pfac[p] + 1):
            pnew.extend([d * p**x for d in divisors])
        divisors.extend(pnew)
    return sorted(divisors)


def isamicable(a):
    """Return whether or not the input is an amicable number.

    If it is, return its pair. If it isn't, return 0."""
    def d(n):
        return sum(getdivisors(n)) - n
    suma = d(a)
    if suma > 1 and d(suma) == a and suma != a:
        return d(a)
    else:
        return 0

