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


def get_minimas(a):
    result = []
    for y in range(len(a)):
        for x in range(len(a[0])):
            if x > 0 and a[y][x - 1] <= a[y][x]:
                continue
            if y > 0 and a[y - 1][x] <= a[y][x]:
                continue
            if x < len(a[0]) - 1 and a[y][x + 1] <= a[y][x]:
                continue
            if y < len(a) - 1 and a[y + 1][x] <= a[y][x]:
                continue

            result.append((y, x))
    return result


def f01():
    with open('input') as file:
        lines = file.read().splitlines()

        a = [toInt(list(a)) for a in lines]

        count = sum(a[y][x] + 1 for (y, x) in get_minimas(a))

        print(count)
        assert(count == 508)


def f02():
    with open('input') as file:
        lines = file.read().splitlines()
        width = len(lines[0])
        height = len(lines)

        a = [toInt(list(a)) for a in lines]

        minimas = set(get_minimas(a))

        lens = []

        for p in minimas:

            stack = [p]
            done = []

            while stack:

                y, x = stack.pop()

                for (yd, xd) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if 0 <= y + yd < height and 0 <= x + xd < width:
                        pp = (y + yd, x + xd)
                        if pp not in done and a[pp[0]][pp[1]] != 9:
                            done.append(pp)
                            stack.append(pp)

            lens.append(len(done))

        lens = sorted(lens, reverse=True)
        result = lens[0] * lens[1] * lens[2]
        print(result)
        assert(result == 1564640)


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
