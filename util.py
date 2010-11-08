#!/usr/bin/env python
"""
Miscellaneous utilies for Project Euler problems.
"""

import math


primes = [2, 3, 5]

def isprime(n):
    """Test that n is a prime number.

    If the primes list does not yet include all primes up to sqrt(n),
    it is extended in a naive way until an answer is reached.
    """
    global primes
    if n in primes:
        return True
    for p in primes:
        if n % p == 0:
            return False
    # All primes after 3 are equivalent to either 1 or 5 mod 6.
    p = primes[-1]
    while primes[-1] < int(math.sqrt(n)):
        if p % 6 == 1:
            p += 4
        else:
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
    """Return the prime factorization of the input n as a dict.

    The returned list has primes as keys with exponents as values.
    """
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
    """Return a list of the all divisors of n, including 1 and n."""
    divisors = [1]
    pfac = getprimefactors(n)
    for p in pfac:
        pnew = []
        for x in xrange(1, pfac[p] + 1):
            pnew.extend([d * p**x for d in divisors])
        divisors.extend(pnew)
    return sorted(divisors)


def isamicable(x):
    """Test that x is an amicable number.

    If x is amicable, return its counterpart in the pair.
    If x isn't amicable, return 0.
    """
    def d(n):
        return sum(getdivisors(n)) - n
    y = d(x)
    if y > 1 and d(y) == x and y != x:
        return d(x)
    else:
        return 0


def binary(x):
    output = []
    while x:
        output.insert(0, str(x & 1))
        x >>= 1
    return ''.join(output)

