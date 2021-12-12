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
                map[beg] = [1]
            if end not in map:
                map[end] = [1]
            map[beg].append(end)
            map[end].append(beg)

        def count(start, path, map):
            if start.islower():
                if map[start][0] == 0:
                    return set()

            if start == 'end':
                #print(path + " " + end)
                return {path}

            map[start][0] -= 1

            sum = set()

            for d in map[start][1:]:
                nmap = copy.deepcopy(map)
                sum = sum.union(count(d, path + " " + start, nmap))
            return sum

        paths = count('start', '', map)
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
                map[beg] = [1]
            if end not in map:
                map[end] = [1]
            map[beg].append(end)
            map[end].append(beg)

        def count(start, path, map):
            if start.islower():
                if map[start][0] == 0:
                    return set()

            if start == 'end':
                #print(path + " " + end)
                return {path}

            map[start][0] -= 1

            sum = set()

            for d in map[start][1:]:
                nmap = copy.deepcopy(map)
                sum = sum.union(count(d, path + " " + start, nmap))
            return sum

        nmap = copy.deepcopy(map)
        paths = count('start', '', nmap)
        for a in map.keys():
            if a.islower() and a not in ['start', 'end']:
                #print(a)
                nmap = copy.deepcopy(map)
                nmap[a][0] = 2
                paths2 = count('start', '', nmap)
                #print(a, len(paths2))
                paths = paths.union(paths2)
                #map[a][0] = 1

        result = len(paths)
        print(result)
        assert(result == 84271)

def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
