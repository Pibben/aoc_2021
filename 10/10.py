import itertools
import numpy as np
import re
import pprint


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
    lc = ['(', '[', '{', '<']
    rc = [')', ']', '}', '>']
    pt = [3, 57, 1197, 25137]
    with open('input') as file:
        lines = file.read().splitlines()

        sum = 0
        for line in lines:
            stack = []

            for c in line:
                if c in lc:
                    stack.append(c)
                else:
                    if lc.index(stack[-1]) != rc.index(c):
                        sum += pt[rc.index(c)]
                        break
                    else:
                        stack.pop()
        print(sum)
        assert(sum == 271245)


def f02():
    lc = ['(', '[', '{', '<']
    rc = [')', ']', '}', '>']
    pt = [1, 2, 3, 4]
    with open('input') as file:
        lines = file.read().splitlines()

        prod = []
        for line in lines:
            sum = 0
            stack = []

            for c in line:
                if c in lc:
                    stack.append(c)
                else:
                    d = stack.pop()
                    if lc.index(d) != rc.index(c):
                        sum += pt[rc.index(c)]
                        break
            if sum > 0:
                continue

            stack = []
            sum = 0
            for c in line:
                if c in lc:
                    stack.append(c)
                else:
                    d = stack.pop()
                    assert(rc.index(c) == lc.index(d))

            for c in stack[::-1]:
                sum *= 5
                sum += pt[lc.index(c)]
            prod.append(sum)

        result = sorted(prod)[len(prod)//2]
        print(result)
        assert(result == 1685293086)


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
