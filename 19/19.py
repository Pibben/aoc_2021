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


def get_pose(vec, i):
    a, b, c = vec

    tab = [(a, b, c),
           (a, -b, -c),
           (-a, b, -c),
           (-a, -b, c),

           (a, c, -b),
           (a, -c, b),
           (-a, c, b),
           (-a, -c, -b),

           (b, a, -c),
           (b, -a, c),
           (-b, a, c),
           (-b, -a, -c),

           (b, c, a),
           (b, -c, -a),
           (-b, c, -a),
           (-b, -c, a),

           (c, a, b),
           (c, -a, -b),
           (-c, a, -b),
           (-c, -a, b),

           (c, b, -a),
           (c, -b, a),
           (-c, b, a),
           (-c, -b, -a)
    ]

    tab = [tuple(t) for t in tab]

    assert(len(tab) == 24)

    return tab[i]


def transform(coords, perm):
    return [get_pose(c, perm) for c in coords]


def add(a, b):
    return a[0] + b[0], a[1] + b[1], a[2] + b[2]


def diff(a, b):
    return a[0] - b[0], a[1] - b[1], a[2] - b[2]


def translate(coords, offset):
    return set(add(coord, offset) for coord in coords)


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])


def match(a, b, scanner_loc):
    b = set(b)
    for perm in range(24):
        pts = a[perm]   # new
        for ptt in b:   # old
            for pt in pts:
                offset = diff(ptt, pt)
                dist = diff(offset, scanner_loc)
                if max(abs(d) for d in dist) > 2000:
                    continue

                translated = translate(pts, offset)

                count = len(b.intersection(translated))

                if count >= 12:
                    return offset, translated

    return None


def f01():
    with open('input') as file:
        scanner_blocks = file.read().split('\n\n')

        scanners = []

        for sb in scanner_blocks:
            lines = sb.splitlines()[1:]
            coords = []
            for line in lines:
                coords.append(tuple(toInt(line.split(','))))
            transcoords = [transform(coords, perm) for perm in range(24)]
            scanners.append(transcoords)

        scanners[0] = scanners[0][0]

        not_done = set(range(1, len(scanners)))

        scanner_loc = {0: (0, 0, 0)}

        stack = [0]

        while stack:

            d = stack.pop()

            for nd in not_done:
                #print(d, nd, stack, not_done)

                res = match(scanners[nd], scanners[d], scanner_loc[d])
                if res is not None:
                    scanner_loc[nd] = res[0]
                    translated = res[1]
                    scanners[nd] = translated

                    stack.append(nd)

            for dd in stack:
                if dd in not_done:
                    not_done.remove(dd)

        if not_done:
            print("Failed")

        total = set()
        for sc in scanners:
            total = total.union(set(sc))


        result = len(total)
        print(result)
        assert(result == 440)

        result = max(manhattan(a, b) for a in scanner_loc.values() for b in scanner_loc.values())
        print(result)
        assert(result == 13382)


def f02():
    pass


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
