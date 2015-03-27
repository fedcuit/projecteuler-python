from problems import mathutil

__author__ = 'edfeng'


def nth_fibonacci_with_specific_digits(n):
    return next(i for i, x in enumerate(mathutil.fibonacci_seq(), 1) if len(str(x)) == n)
