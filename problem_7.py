#!/usr/bin/env python
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
see that the 6th prime is 13.

What is the 10001st prime number?
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


def addprime(primes):
    p = primes[-1]
    while True:
        p += 2
        if isprime(primes, p):
            primes.append(p)
            return


def run(N):
    primes = [2, 3]
    while len(primes) < N:
        addprime(primes)
    print 'Prime number %d is %d.' % (N, primes[-1])


def main():
    if len(sys.argv) > 1:
        run(int(sys.argv[1]))
    else:
        run(6)
        run(10001)


if __name__ == '__main__':
    main()
