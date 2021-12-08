import itertools

import numpy as np
import re


def toInt(c):
    return [int(e) for e in c]


def msplit(s, ds=None):
    if ds is None:
        ds = ' '

    patt = '|'.join(ds)
    res = re.split(patt, s)
    res = [e for e in res if e != '']
    res = [int(e) if e.isnumeric() else e for e in res]

    return res


def f01():
    with open('input') as file:
        lines = file.read().splitlines()

        sum = 0
        for line in lines:
            pre, post = line.split('|')
            for p in post.split(' '):
                # print(p)
                if len(p) in [2, 3, 4, 7]:
                    sum += 1
        print(sum)


#  55555
# 4     0
# 4     0
#  66666
# 3     1
# 3     1
#  22222

segments = [
    {0, 1, 2, 3, 4, 5},
    {0, 1},
    {0, 2, 3, 5, 6},
    {0, 1, 2, 5, 6},
    {0, 1, 4, 6},
    {1, 2, 4, 5, 6},
    {1, 2, 3, 4, 5, 6},
    {0, 1, 5},
    {0, 1, 2, 3, 4, 5, 6},
    {0, 1, 2, 4, 5, 6}]


def solve(pre):
    signals = [p for p in pre.split(' ')]

    for per in itertools.permutations(['a', 'b', 'c', 'd', 'e', 'f', 'g']):
        per = dict(zip(per, range(7)))

        found_all = True
        for signal in signals:
            candidate = set(per[s] for s in signal)

            if candidate not in segments:
                found_all = False
                break

        if found_all:
            return per

    return None


def decode(key, post):
    numbers = []
    for p in post.strip().split(' '):
        digit = set(key[i] for i in p)
        numbers.append(segments.index(digit))

    return int(''.join([str(a) for a in numbers]))


def f02():
    with open('input') as file:
        lines = file.read().splitlines()

        sum = 0
        for line in lines:
            pre, post = line.split('|')

            key = solve(pre.strip())

            assert key

            sum += decode(key, post.strip())

        print(sum)


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
