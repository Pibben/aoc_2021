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
            if start.islower():
                if start in path:
                    return []

            if start == 'end':
                return [path]

            sum = []

            for d in map[start]:
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

        def count(start, path, map, ex):
            if start.islower():
                if path.count(start) == (2 if start == ex else 1):
                    return set()

            if start == 'end':
                return {path}

            sum = set()

            for d in map[start]:
                new = count(d, path + (start,), map, ex)
                sum = sum.union(new)

            return sum

        paths = count('start', (), map, '')
        for a in map.keys():
            if a.islower() and a not in ['start', 'end']:
                paths2 = count('start', (), map, a)
                paths = paths.union(paths2)

        result = len(paths)
        print(result)
        assert(result == 84271)


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
