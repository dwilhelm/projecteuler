#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Starting in the top left corner of a 2×2 grid, there are 6 routes
(without backtracking) to the bottom right corner.

How many routes are there through a 20×20 grid?
"""

# Since the only available directions are right and down, the number
# of routes is just the number of ways to arrange 40 objects made up
# of two groups of 20 identical objects.

import math

print math.factorial(40) / (math.factorial(20) * math.factorial(20))
