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


def do(iter):
    with open('input') as file:
        start = toInt(file.read().split(','))

    def count(p, s):
        if s == 0:
            return 1
        if (p, s) in count.mem:
            return count.mem[(p, s)]

        if p > 0:
            r = count(p - 1, s - 1)
        else:
            r = count(6, s - 1) + count(8, s - 1)

        count.mem[(p, s)] = r
        return r
    count.mem = {}

    return sum(count(a, iter) for a in start)


def f01():
    print(do(80))


def f02():
    print(do(256))


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
