__author__ = 'edfeng'

base = ord('A') - 1


def alpha_value(s):
    return sum([ord(i) - base for i in s])


if __name__ == '__main__':
    with open('p022_names.txt', 'r') as f:
        lines = f.readlines()
        words = sorted([name.strip('"') for line in lines for name in line.split(',')])
        assert sum([alpha_value(word) * i for i, word in enumerate(words, 1)]) == 871198282