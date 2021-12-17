import copy
import itertools
import numpy as np
import re
import pprint
import sys
import queue


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
        area = file.read().splitlines()[0][13:].split(', ')
        xlim = toInt(area[0][2:].split('..'))
        ylim = toInt(area[1][2:].split('..'))

        maxy = 0
        for ovx in range(0, 100):
            for ovy in range(-100, 100):
                x, y = 0, 0
                vx, vy = ovx, ovy
                thismaxy = 0
                while y > ylim[0]:
                    x += vx
                    y += vy
                    thismaxy = max(thismaxy, y)
                    if vx > 0:
                        vx -= 1
                    if vx < 0:
                        vx += 1
                    vy -= 1

                    if xlim[0] <= x <= xlim[1] and ylim[0] <= y <= ylim[1]:
                        maxy = max(maxy, thismaxy)
                        break

        print(maxy)
        assert(maxy == 4560)


def f02():
    with open('input') as file:
        area = file.read().splitlines()[0][13:].split(', ')
        xlim = toInt(area[0][2:].split('..'))
        ylim = toInt(area[1][2:].split('..'))

        foo = set()
        for ovx in range(0, xlim[1] + 1):
            for ovy in range(ylim[0] - 1, 500):
                x, y = 0, 0
                vx, vy = ovx, ovy
                while y > ylim[0]:
                    x += vx
                    y += vy

                    if x > xlim[1]:
                        break

                    if vx > 0:
                        vx -= 1
                    elif vx < 0:
                        vx += 1
                    else:
                        if not xlim[0] <= x <= xlim[1]:
                            break
                    vy -= 1

                    if xlim[0] <= x <= xlim[1] and ylim[0] <= y <= ylim[1]:
                        foo.add((ovx, ovy))
                        break

        result = len(foo)
        print(result)
        assert result == 3344


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
