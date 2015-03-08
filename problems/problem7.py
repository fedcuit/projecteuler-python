__author__ = 'edfeng'


def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def primes():
    x = 2
    while True:
        if is_prime(x):
            yield x
        x += 1


def take(n, iterable):
    firsts = []
    if n > 0:
        it = iter(iterable)
        for _ in range(n):
            firsts.append(next(it))

    return firsts


def nth_prime(n):
    return take(n, primes())[-1]