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


def listify(line):
    ret = []
    level = 0
    for c in line:
        if c == '[':
            level += 1
            assert(level <= 4)
        elif c == ']':
            level -= 1
            assert(level >= 0)
        elif c.isnumeric():
            ret.append([int(c), level])
    return ret


def add(a, b):
    ret = a + b

    for a in ret:
        a[1] += 1
    return ret


def explode_and_split(sum):
    def explode(s):
        exploded = False
        for i in range(len(s)):
            if s[i][1] == 5:
                exploded = True
                if i > 0:
                    s[i - 1][0] += s[i][0]
                if i < len(s) - 2:
                    s[i + 2][0] += s[i + 1][0]
                break
        if exploded:
            s[i] = [0, 4]
            if i < len(s) - 1:
                del s[i + 1]
        return exploded

    def split(s):
        splitted = False
        for i in range(len(s)):
            if s[i][0] >= 10:
                splitted = True
                break
        if splitted:
            num, level = s[i]

            s[i] = [num // 2, level + 1]
            s.insert(i + 1, [(num + 1) // 2, level + 1])
        return splitted

    while True:
        exploded = explode(sum)
        if exploded:
            continue

        splitted = split(sum)

        if not exploded and not splitted:
            break


def reduce(s):
    def reduce_level(level):
        reduced = False
        for i in range(len(s)):
            if s[i][1] == level:
                reduced = True
                assert(s[i + 1][1] == level)
                break
        if reduced:
            s[i] = [3*s[i][0] + 2 * s[i + 1][0], level - 1]
            if i < len(s) - 1:
                del s[i + 1]

        return reduced

    for level in range(4, 0, -1):
        while reduce_level(level):
            pass

    return s[0][0]


def f01():
    with open('input') as file:
        lines = file.read().splitlines()

        sum = listify(lines[0])

        lines = lines[1:]

        for line in lines:
            sum = add(sum, listify(line))

            explode_and_split(sum)

        result = reduce(sum)
        print(result)
        assert(result == 4033)


def f02():
    with open('input') as file:
        lines = file.read().splitlines()

        maxsum = 0

        for line in lines:
            for line2 in lines:
                if line == line2:
                    continue

                sum = add(listify(line), listify(line2))

                explode_and_split(sum)

                this = reduce(sum)
                maxsum = max(this, maxsum)

        print(maxsum)
        assert(maxsum == 4864)


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
