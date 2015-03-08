import math

__author__ = 'edfeng'


def is_palindromic(n):
    s = str(n)
    l = len(s)
    if l % 2 == 0:
        return s[0:l / 2] == s[l / 2:][::-1]
    else:
        return s[0:l / 2] == s[int(math.ceil(l / 2.0)):][::-1]


def palindromes(xr1, xr2):
    ps = []
    for i in xr1:
        for j in xr2:
            product = i * j
            if is_palindromic(product):
                ps.append(product)
    return ps