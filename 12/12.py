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
        map = {}
        for line in lines:
            beg, end = line.split('-')
            if beg not in map:
                map[beg] = []
            if end not in map:
                map[end] = []
            map[beg].append(end)
            map[end].append(beg)

        def count(start, path, map):
            if start == 'end':
                return [path]

            sum = []

            for d in map[start]:
                if d.islower() and d in path:
                    continue
                new = count(d, path + [start], map)
                sum.extend(n for n in new if n not in sum)

            return list(sum)

        paths = count('start', [], map)
        result = len(paths)
        print(result)
        assert(result == 3576)


def f02():
    with open('input') as file:
        lines = file.read().splitlines()
        map = {}
        for line in lines:
            beg, end = line.split('-')
            if beg not in map:
                map[beg] = []
            if end not in map:
                map[end] = []
            map[beg].append(end)
            map[end].append(beg)

        def count(start, path, map, a):
            if start == 'end':
                return {path}

            sum = set()

            for d in map[start]:
                if d.islower():
                    if path.count(d) > 1:
                        continue
                    elif path.count(d) == 1:
                        if d not in ['start', 'end'] and a:
                            new = count(d, path + (start,), map, False)
                            sum = sum.union(new)
                        continue

                new = count(d, path + (start,), map, a)
                sum = sum.union(new)

            return sum

        paths = count('start', (), map, True)

        result = len(paths)
        print(result)
        assert(result == 84271)


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
