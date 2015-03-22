import collections
import itertools

from gevent.pool import Pool

from problems import mathutil
from problems.iterutil import partition


__author__ = 'edfeng'


def is_abundant_number(n):
    return sum(mathutil.proper_divisors(n)) > n


abundant_map = collections.OrderedDict({i: is_abundant_number(i) for i in xrange(1, 28123 + 1)})


def not_abundantify_number(n):
    match = next((i for i in range(1, n) if abundant_map[i] and abundant_map[n - i]), None)
    return True if match is None else False


def none_abundantify_numbers(r):
    print 'starting thread with {}'.format(r[0])
    return [i for i in r if not_abundantify_number(i)]


def expected_sum():
    pool = Pool(10)
    return sum(itertools.chain.from_iterable(pool.map(none_abundantify_numbers, partition(range(1, 28123 + 1), 8))))