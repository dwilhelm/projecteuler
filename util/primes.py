"""
Utilies relating to primes and primality
"""

import math


plist = [2, 3, 5]

def isprime(n):
    """Test that n is a prime number.

    If the primes list does not yet include all primes up to sqrt(n),
    it is extended in a naive way until an answer is reached.
    """
    global plist
    if n in plist:
        return True
    for p in plist:
        if n % p == 0:
            return False
    # All primes after 3 are equivalent to either 1 or 5 mod 6.
    p = plist[-1]
    while plist[-1] < int(math.sqrt(n)):
        if p % 6 == 1:
            p += 4
        else:
            p += 2
        if isprime(p):
            plist.append(p)
            if n % p == 0:
                return False
    return True


def genprimesto(n):
    """Extend the primes list up to, but not including n."""
    global plist
    if n <= plist[-1]:
        return
    plist = [2] + range(3, n, 2)
    idx = 1
    while plist[idx] <= math.sqrt(plist[-1]):
        p = plist[idx]
        plist = [x for x in plist if x <= p or x % p]
        idx += 1


def gennewprimes(n):
    """Extend the primes list by n more entries."""
    p = plist[-1]
    added = 0
    while added < n:
        p += 2
        if isprime(p):
            plist.append(p)
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

