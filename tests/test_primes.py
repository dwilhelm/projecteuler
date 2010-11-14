#!/usr/bin/env python

import os.path
import sys
import time

pkgpath = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(pkgpath)

from util import primes


def main(n):
    t0 = time.clock()
    primes.genprimesto(n)
    t1 = time.clock() - t0
    print 'time 1 = %s' % t1
    p1 = primes.plist
    reload(primes)
    while primes.plist[-1] < n:
        primes.gennewprimes(1)
    t2 = time.clock() - t1
    print 'time 2 = %s' % t2
    p2 = [x for x in primes.plist if x < n]
    if p1 != p2:
        print 'failed'
        sys.exit(1)
    else:
        print 'passed'
        sys.exit(0)


if __name__ == '__main__':
    main(100000)

