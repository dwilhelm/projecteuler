#!/usr/bin/env python

p = [a*b for a in range(100, 999) for b in range(a, 999)
     if str(a*b) == str(a*b)[::-1]]
print sorted(p)[-1]

