"""
Utilities relating to divisor and divisibility
"""

import primes


def gcd(x, y):
    """Return the greatest common divisor of inputs x and y."""
    while y:
        x, y = y, x % y
    return x


def getdivisors(n):
    """Return a list of the all divisors of n, including 1 and n."""
    divisors = [1]
    pfac = primes.getprimefactors(n)
    for p in pfac:
        pnew = []
        for x in xrange(1, pfac[p] + 1):
            pnew.extend([d * p**x for d in divisors])
        divisors.extend(pnew)
    return sorted(divisors)


def isamicable(x):
    """Test that x is an amicable number.

    An amicable pair consists of two integers for which the sum of the
    proper divisors of each is equal to the other.

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

