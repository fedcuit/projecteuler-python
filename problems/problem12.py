from problems.mathutil import factors

__author__ = 'edfeng'


def triangle_numbers():
    x = 1
    yield 1
    while True:
        x += 1
        yield sum(range(1, x + 1))


def factors_of_triangle_number(limit):
    return next(i for i in triangle_numbers() if len(factors(i)) > limit)