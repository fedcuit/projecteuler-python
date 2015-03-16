import operator

__author__ = 'edfeng'


def primes():
    x = 2
    while True:
        if is_prime(x):
            yield x
        x += 1


def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def factors(n):
    return set(reduce(operator.add,
                      ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)