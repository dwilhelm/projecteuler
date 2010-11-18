"""
Operations on mathematical objects
"""

def exp(base, exponent, modulus):
    """Return base**exponent as a number.

    If modulus is given, then the answer and all intermediate steps are
    mod modulus. This can greatly speed calculation.
    """
    trackexp = 1
    while trackexp < exponent:
        trackexp <<= 1
    print 'start: trackexp=%d, exponent=%d' % (trackexp, exponent)
    num = 1
    while trackexp:
        if trackexp & exponent:
            num = num * num * base
        else:
            num = num * num
        if modulus:
            num %= modulus
        trackexp >>= 1
        print 'trackexp=%d, num=%d' % (trackexp, num)
    return num

