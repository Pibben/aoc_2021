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


def printgrid(map):
    maxx = 0
    minx = 0
    maxy = 0
    miny = 0
    for ((y, x), _) in map.items():
        maxx = max(maxx, x)
        maxy = max(maxy, y)
        minx = min(minx, x)
        miny = min(miny, y)

    canvas = [[' ' for _ in range(maxx - minx + 1)] for _ in range(maxy - miny + 1)]
    for ((y, x), v) in map.items():
        canvas[y - miny][x - minx] = '#' if v else '.'

    for line in canvas:
        print(''.join(line))
    print('\n')


def do(iters):
    with open('input') as file:
        enh, grid = file.read().split('\n\n')

        grid = grid.splitlines()
        height = len(grid)
        width = len(grid[0])

        map = {}

        for y in range(height):
            for x in range(width):
                if grid[y][x] == '#':
                    map[(y, x)] = 1
                else:
                    map[(y, x)] = 0

        rest = 0

        for i in range(iters):

            newmap = map.copy()
            for ((y, x), v) in map.items():
                if v != rest:
                    for dy in range(-1, 2):
                        for dx in range(-1, 2):
                            if (y + dy, x + dx) not in newmap:
                                newmap[(y + dy, x + dx)] = rest

            map = newmap
            newmap = {}

            for ((y, x), v) in map.items():
                binlist = []
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if (y + dy, x + dx) not in map:
                            binlist.append(rest)
                        else:
                            binlist.append(map[(dy + y, dx + x)])

                binstr = ''.join([str(b) for b in binlist])
                bin = int(binstr, 2)

                assert(0 <= bin < 512)
                newmap[(y, x)] = 1 if enh[bin] == '#' else 0

            map = newmap.copy()

            if rest == 1:
                rest = 1 if enh[511] == '#' else 0
            else:
                rest = 1 if enh[0] == '#' else 0

        return sum(map.values())


def f01():
    result = do(2)
    print(result)
    assert(result == 5786)


def f02():
    result = do(50)
    print(result)
    assert(result == 16757)

def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
