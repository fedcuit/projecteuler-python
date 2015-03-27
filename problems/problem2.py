import itertools

from problems.mathutil import fibonacci_seq


__author__ = 'edfeng'


def sum_of_fibs():
    """
    :return the sum of the even-valued terms in the Fibonacci sequence whose values do not exceed four million

    :rtype : numeric
    """
    return sum(filter(lambda x: x % 2 == 0,
                      itertools.takewhile(lambda fib: fib < 4000000, fibonacci_seq())))