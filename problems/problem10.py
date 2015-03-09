import itertools

from problems import mathutil


__author__ = 'edfeng'


def sum_of_primes(end):
    return sum(itertools.takewhile(lambda x: x < end, mathutil.primes()))