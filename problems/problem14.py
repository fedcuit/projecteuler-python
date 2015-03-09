__author__ = 'edfeng'


def collatz_seq(x):
    acc = []

    def seq(acc, x):
        acc.append(x)
        if x == 1 and not acc:  # handle the case that starts from 1
            return seq(acc, x * 3 + 1)

        if x == 1:  # sequence ends
            return

        if x % 2 == 0:
            return seq(acc, x / 2)
        else:
            return seq(acc, x * 3 + 1)

    seq(acc, x)
    return acc


def longest_chain():
    return max([(len(collatz_seq(i)), i) for i in xrange(1, 1000000)], key=lambda t: t[0])[1]
