from problems import mathutil

__author__ = 'edfeng'


def sum_of_digits_in_factorial(n):
    print mathutil.factorial(n)
    return sum([int(i) for i in str(mathutil.factorial(n))])