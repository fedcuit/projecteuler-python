import operator

__author__ = 'edfeng'


def primes():
    x = 2
    while True:
        if is_prime(x):
            yield x
        x += 1


def natural_number(f):
    def wrapper(n):
        if type(n) is int and n > 0:
            return f(n)
        else:
            raise Exception("A natural number is wanted here")

    return wrapper


@natural_number
def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


@natural_number
def factors(n):
    return set(reduce(operator.add,
                      ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


@natural_number
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def proper_divisors(n):
    return sorted(factors(n))[:-1]