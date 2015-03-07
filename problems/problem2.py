import sys
import itertools

__author__ = 'edfeng'


def fibonacci_seq():
    the_one_before_previous = 1
    previous = 2
    for i in xrange(1, sys.maxint):
        if i == 1:
            yield 1
        if i == 2:
            yield 2

        if i > 2:
            new_value = previous + the_one_before_previous
            the_one_before_previous = previous
            previous = new_value
            yield new_value


def sum_of_fibs():
    """
    :return the sum of the even-valued terms in the Fibonacci sequence whose values do not exceed four million

    :rtype : numeric
    """
    return sum(filter(lambda x: x % 2 == 0,
                      itertools.takewhile(lambda fib: fib < 4000000, fibonacci_seq())))