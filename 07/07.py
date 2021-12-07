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
        crabs = toInt(file.read().split(','))

        def fuel(n):
            return sum(abs(n-a) for a in crabs)

        result = min(fuel(a) for a in range(min(crabs), max(crabs)))
        print(result)
        assert(result == 352331)

def f02():
    with open('input') as file:
        crabs = toInt(file.read().split(','))

        def fuel(n):
            def dist(a):
                return abs(n - a)
            return sum(dist(a) * (1 + dist(a)) // 2 for a in crabs)

        result = min(fuel(a) for a in range(min(crabs), max(crabs)))
        print(result)
        assert(result == 99266250)



def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
