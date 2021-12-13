import copy
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
    with open('input') as file:
        points, folds_block = file.read().split('\n\n')

        folds = []
        for f in folds_block.splitlines():
            #print(f)
            axis, num = f[11:].split('=')
            num = int(num)
            folds.append((axis, num))

        rem = set()
        for p in points.splitlines():
            x, y = toInt(p.split(','))

            for axis, num in folds[:1]:
                if axis == 'x':
                    if x > num:
                        x = x - 2 * (x - num)
                if axis == 'y':
                    if y > num:
                        y = y - 2 * (y - num)

            rem.add((x, y))

        result = len(rem)
        print(result)
        assert(result == 753)


def f02():
    with open('input') as file:
        points, folds_block = file.read().split('\n\n')

        folds = []
        for f in folds_block.splitlines():
            #print(f)
            axis, num = f[11:].split('=')
            num = int(num)
            folds.append((axis, num))

        rem = set()
        for p in points.splitlines():
            x, y = toInt(p.split(','))

            for axis, num in folds:
                if axis == 'x':
                    if x > num:
                        x = x - 2 * (x - num)
                if axis == 'y':
                    if y > num:
                        y = y - 2 * (y - num)

            rem.add((x, y))

        maxx, maxy = 0, 0
        for x, y in rem:
            maxx = max(maxx, x)
            maxy = max(maxy, y)

        canvas = [[' ' for i in range(maxx + 1)] for j in range(maxy + 1)]
        for x, y in rem:
            canvas[y][x] = '#'

        for l in canvas:
            print(l)


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
