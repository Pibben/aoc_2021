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
        lines = file.read().splitlines()
        height = len(lines)
        width = len(lines[0])
        lines = [list(l) for l in lines]

        for i in range(1000):
            did_move = False
            for heard in ['>', 'v']:
                cpy = copy.deepcopy(lines)
                for y in range(height):
                    for x in range(width):
                        c = lines[y][x]
                        if c == heard:
                            ny, nx = ((y + 1) % height, x) if heard == 'v' else (y, (x + 1) % width)
                            if lines[ny][nx] == '.':
                                did_move = True
                                cpy[ny][nx] = c
                                cpy[y][x] = '.'
                lines = cpy

            if not did_move:
                break

        result = i + 1
        print(result)
        assert(result == 560)


def f02():
    pass

def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
