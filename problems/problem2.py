import itertools

__author__ = 'edfeng'


def fibonacci_seq():
    x = 1
    y = 2
    while True:
        yield x
        x, y = y, y + x


def sum_of_fibs():
    """
    :return the sum of the even-valued terms in the Fibonacci sequence whose values do not exceed four million

    :rtype : numeric
    """
    return sum(filter(lambda x: x % 2 == 0,
                      itertools.takewhile(lambda fib: fib < 4000000, fibonacci_seq())))