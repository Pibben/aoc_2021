import itertools

import numpy as np
import re
import scipy
import pprint
import scipy.ndimage


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


def f02():
    with open('input2') as file:
        lines = file.read().splitlines()
        width = len(lines[0])
        height = len(lines)

        a = [toInt(list(a)) for a in lines]

        minimas = set(get_minimas(a))
        labels = [[-1 for i in range(width)] for j in range(height)]

        count = 0
        for (y, x) in minimas:
            labels[y][x] = count
            count += 1

        pprint.pprint(labels)

        for (y, x) in minimas:

            l = labels[y][x]

            assert(l != -1)

            for yd in range(-1, 2):
                if 0 <= y + yd < height:
                    for xd in range(-1, 2):
                        if 0 <= x + xd < width:
                            if labels[y + yd][x + xd] == -1:
                                minimas.add((y + yd, x + xd))
                                labels[y + yd][x + xd] = l

            print(minimas)
            pprint.pprint(labels)


        #print(m)

        #print(count)


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
