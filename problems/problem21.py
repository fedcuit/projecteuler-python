from problems import mathutil

__author__ = 'edfeng'


def sum_of_proper_divisor(n):
    return sum(sorted(mathutil.factors(n))[:-1])


def is_amicable_number(n):
    m = sum_of_proper_divisor(n)
    return n == sum_of_proper_divisor(m) and n != m if m != 0 else False


def amicables():
    n = 1
    while True:
        if is_amicable_number(n):
            yield n
        n += 1