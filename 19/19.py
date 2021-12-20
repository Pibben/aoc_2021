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
    return [add(coord, offset) for coord in coords]


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])


def f01():
    with open('input2') as file:
        scanner_blocks = file.read().split('\n\n')

        scanners = []

        for sb in scanner_blocks:
            lines = sb.splitlines()[1:]
            coords = []
            for line in lines:
                coords.append(tuple(toInt(line.split(','))))
            scanners.append(coords)

        total = set(scanners[0])

        done = [False] * len(scanners)
        done[0] = True

        scanner_loc = [(0, 0, 0)]

        while not all(done):
            did_one = False
            for i in range(len(scanners)):
                if done[i]:
                    continue

                sc = scanners[i]
                found = False
                for perm in range(24):
                    pts = transform(sc, perm)
                    for pt in pts:
                        for ptt in total:
                            offset = diff(ptt, pt)
                            translated = set(translate(pts, offset))

                            count = len(total.intersection(translated))

                            if count >= 12:
                                scanner_loc.append(offset)
                                found = True
                                break
                        if found:
                            break
                    if found:
                        break

                if found:
                    total = total.union(translated)
                    done[i] = True
                    did_one = True
            if not did_one:
                print("Failed")
                break

        result = len(total)
        print(result)
        #assert(result == 440)

        result = max(manhattan(a, b) for a in scanner_loc for b in scanner_loc)
        print(result)
        #assert(result == 13382)


def f02():
    pass


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
