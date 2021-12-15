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
        lines = file.read().splitlines()
        lines = list(toInt(l) for l in lines)
        width = len(lines[0])
        height = len(lines)
        a = np.array(lines)
        #print(a)
        c = np.ones(a.shape, np.int32) * -1
        #print(c)
        c[0, 0] = a[0, 0]

        for y in range(height):
            for x in range(width):
                if x == 0 and y == 0:
                    continue
                if y == 0:
                    c[y, x] = c[y, x - 1] + a[y, x]
                elif x == 0:
                    c[y, x] = c[y - 1, x] + a[y, x]
                else:
                    c[y, x] = min(c[y - 1, x], c[y, x - 1]) + a[y, x]

        while True:
            new = np.zeros(a.shape, np.int32)
            for y in range(height):
                for x in range(width):
                    if x == 0 and y == 0:
                        continue
                    pot = []
                    for dy, dx in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                        if 0 <= dy + y < height:
                            if 0 <= dx + x < width:
                                pot.append(c[y + dy, x + dx])
                    new[y, x] = min(pot) + a[y, x]
            #print(new)
            if np.all(new == c):
                break
            c = new

        #print(c)
        print(c[height - 1, width - 1])


def f02():
    with open('input') as file:
        lines = file.read().splitlines()
        lines = list(toInt(l) for l in lines)
        width = len(lines[0])
        height = len(lines)
        aa = np.array(lines)

        a = np.ones((aa.shape[0] * 5, aa.shape[1] * 5), np.int32)

        for y in range(5):
            for x in range(5):
                a[y * height: (y + 1) * height, x * width: (x + 1) * width] = (aa + x + y - 1) % 9 + 1

        #print(a)
        width *= 5
        height *= 5

        #print(a)
        c = np.ones(a.shape, np.int32) * -1
        #print(c)
        c[0, 0] = a[0, 0]

        for y in range(height):
            for x in range(width):
                if x == 0 and y == 0:
                    continue
                if y == 0:
                    c[y, x] = c[y, x - 1] + a[y, x]
                elif x == 0:
                    c[y, x] = c[y - 1, x] + a[y, x]
                else:
                    c[y, x] = min(c[y - 1, x], c[y, x - 1]) + a[y, x]

        while True:
            new = np.zeros(a.shape, np.int32)
            for y in range(height):
                for x in range(width):
                    if x == 0 and y == 0:
                        continue
                    pot = []
                    for dy, dx in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                        if 0 <= dy + y < height:
                            if 0 <= dx + x < width:
                                pot.append(c[y + dy, x + dx])
                    new[y, x] = min(pot) + a[y, x]
            #print(new)
            if np.all(new == c):
                break
            c = new

        #print(c)
        print(c[height - 1, width - 1])


def main():
    #f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
