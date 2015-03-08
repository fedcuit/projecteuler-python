from problems.iterutil import take
from problems.mathutil import primes

__author__ = 'edfeng'


def nth_prime(n):
    return take(n, primes())[-1]