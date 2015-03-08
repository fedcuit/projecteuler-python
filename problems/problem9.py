from problems.iterutil import product

__author__ = 'edfeng'


def pythagorean_triplets(n):
    for i in range(1, n):
        for j in range(1, n):
            for k in range(1, n):
                if i * i + j * j == k * k:
                    yield i, j, k


def the_triplet():
    return next(product(ns) for ns in pythagorean_triplets(1000) if sum(ns) == 1000)