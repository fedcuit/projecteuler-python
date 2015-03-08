import sys

__author__ = 'edfeng'


def dividable(x, r):
    return all([x % d == 0 for d in r])


def smallest_number(r):
    return next(i for i in xrange(1, sys.maxint) if dividable(i, r))