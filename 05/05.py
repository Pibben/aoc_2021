import numpy as np
import re


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

        def parse(s):
            return toInt(s.split(','))

        ls = []
        mx = 0
        my = 0
        for line in lines:
            start, end = line.split(" -> ")
            start = parse(start)
            end = parse(end)
            if start > end:
                start, end = end, start
            mx = max(mx, start[0])
            mx = max(mx, end[0])
            my = max(my, start[1])
            my = max(my, end[1])
            ls.append((start, end))

        m = np.zeros((mx + 1, my + 1))

        for (start, end) in ls:
            dx = end[0] - start[0]
            dy = end[1] - start[1]

            if dx and dy:
                continue

            if dx:
                y = end[1]
                for x in range(start[0], end[0] + 1):
                    m[x, y] += 1

            if dy:
                x = end[0]
                for y in range(start[1], end[1] + 1):
                    m[x, y] += 1

        result = np.count_nonzero(m >= 2)
        assert(result == 8060)
        print(result)


def f02():
    with open('input') as file:
        lines = file.read().splitlines()

        def parse(s):
            return toInt(s.split(','))

        ls = []
        mx = 0
        my = 0
        for line in lines:
            start, end = line.split(" -> ")
            start = parse(start)
            end = parse(end)
            if start[0] > end[0] or (start[0] == end[0] and start[1] > end[1]):
                start, end = end, start
            mx = max(mx, start[0])
            mx = max(mx, end[0])
            my = max(my, start[1])
            my = max(my, end[1])
            ls.append((start, end))

        m = np.zeros((mx + 1, my + 1))

        for (start, end) in ls:
            dx = end[0] - start[0]
            dy = end[1] - start[1]

            if dx:
                ddy = dy // dx
                assert(ddy == 1 or ddy == -1 or ddy == 0)
                y = start[1]
                for x in range(start[0], end[0] + 1):
                    m[x, y] += 1
                    y += ddy

            elif dy:
                x = end[0]
                for y in range(start[1], end[1] + 1):
                    m[x, y] += 1

        result = np.count_nonzero(m >= 2)
        assert(result == 21577)
        print(result)


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
