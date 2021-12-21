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


def calc_dot(points):
    def dist(a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2

    def dot(p, m1, m2):
        d1 = diff(m1, p)
        d2 = diff(m2, p)
        return d1[0] * d2[0] + d1[1] * d2[1] + d1[2] * d2[2]

    ret = []
    for p1 in points:
        m1 = None
        m2 = None
        d1 = sys.maxsize
        d2 = sys.maxsize
        for p2 in points:
            if p1 == p2:
                continue
            d = dist(p1, p2)
            if d < d1:
                d2 = d1
                m2 = m1
                d1 = d
                m1 = p2
            elif d < d2:
                d2 = d
                m2 = p2
        ret.append(dot(p1, m1, m2))
    return ret


def match(a, b):
    d1, d2 = calc_dot(a[0]), calc_dot(b)
    overlap = len(set(d1).intersection(d2))
    if overlap == 12:
        for ptt in b:   # old
            for perm in range(24):
                pts = a[perm]  # new
                for pt in pts:
                    offset = diff(ptt, pt)

                    translated = translate(pts, offset)

                    count = len(set(b).intersection(translated))

                    if count >= 12:
                        return offset, translated

    return None


def f01():
    with open('input') as file:
        scanner_blocks = file.read().split('\n\n')

        scanners = []

        for sb in scanner_blocks:
            lines = sb.splitlines()[1:]
            coords = [tuple(toInt(line.split(','))) for line in lines]
            transcoords = [transform(coords, perm) for perm in range(24)]
            scanners.append(transcoords)

        scanners[0] = scanners[0][0]

        not_done = set(range(1, len(scanners)))
        scanner_loc = {0: (0, 0, 0)}
        stack = [0]

        while stack:
            d = stack.pop()

            for nd in not_done:
                res = match(scanners[nd], scanners[d])
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
