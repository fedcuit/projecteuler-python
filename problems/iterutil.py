__author__ = 'edfeng'


def take(n, iterable):
    firsts = []
    if n > 0:
        it = iter(iterable)
        for _ in range(n):
            firsts.append(next(it))

    return firsts


def product(iterable):
    return reduce(lambda acc, x: acc * x, iterable, 1)