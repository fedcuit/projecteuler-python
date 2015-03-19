import collections

from problems import mathutil


__author__ = 'edfeng'


def is_abundant_number(n):
    return sum(mathutil.proper_divisors(n)) > n


abundant_map = collections.OrderedDict({i: is_abundant_number(i) for i in xrange(1, 28123 + 1)})


def not_abundantify_number(n):
    return not any(map(lambda i: abundant_map[i] and abundant_map[n - i], range(1, n)))


def none_abundantify_numbers():
    return [i for i in xrange(1, 28123 + 1) if not_abundantify_number(i)]