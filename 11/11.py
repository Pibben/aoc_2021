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
        lines = [toInt(line) for line in lines]

        width = len(lines[0])
        height = len(lines)

        count = 0

        for i in range(100):
            lcount = 0
            for y in range(height):
                for x in range(width):
                    lines[y][x] += 1

            while True:
                got_flash = False

                for y in range(height):
                    for x in range(width):
                        if lines[y][x] is not None and lines[y][x] > 9:
                            lines[y][x] = None
                            got_flash = True
                            lcount += 1
                            for dy in range(-1, 2):
                                if 0 <= y + dy < height:
                                    for dx in range(-1, 2):
                                        if 0 <= x + dx < width and not (dx == 0 and dy == 0) and lines[y + dy][x + dx] is not None:
                                            lines[y + dy][x + dx] += 1
                if not got_flash:
                    break

            for y in range(height):
                for x in range(width):
                    if lines[y][x] is None or lines[y][x] > 9:
                        lines[y][x] = 0

            count += lcount

        print(count)
        assert(count == 1694)


def f02():
    with open('input') as file:
        lines = file.read().splitlines()
        lines = [toInt(line) for line in lines]

        width = len(lines[0])
        height = len(lines)

        count = 0

        for i in range(300000):
            lcount = 0
            for y in range(height):
                for x in range(width):
                    lines[y][x] += 1

            while True:
                got_flash = False

                for y in range(height):
                    for x in range(width):
                        if lines[y][x] is not None and lines[y][x] > 9:
                            lines[y][x] = None
                            got_flash = True
                            lcount += 1
                            for dy in range(-1, 2):
                                if 0 <= y + dy < height:
                                    for dx in range(-1, 2):
                                        if 0 <= x + dx < width and not (dx == 0 and dy == 0) and lines[y + dy][x + dx] is not None:
                                            lines[y + dy][x + dx] += 1
                if not got_flash:
                    break

            for y in range(height):
                for x in range(width):
                    if lines[y][x] is None or lines[y][x] > 9:
                        lines[y][x] = 0

            count += lcount
            if lcount == (width * height):
                result = i + 1
                print(result)
                assert(result == 346)
                break


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
