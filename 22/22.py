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
        grid = np.zeros((100, 100, 100), np.int32)
        offset = 50
        lines = file.read().splitlines()
        for line in lines:
            state, coords = line.split(' ')
            coords = coords.split(',')
            lim = []
            bad = False
            for coord in coords:
                coord = coord[2:]
                coord = toInt(coord.split('..'))

                coord[0] += offset
                coord[1] += offset
                if not 0 <= coord[0] <= 100:
                    bad = True
                if not 0 <= coord[1] <= 100:
                    bad = True
                lim.append(coord)
                #print(coord)
            #print(lim)
            if not bad:
                #print(lim, state)
                grid[lim[0][0]:lim[0][1] + 1, lim[1][0]:lim[1][1] + 1, lim[2][0]:lim[2][1] + 1] = 1 if state == 'on' else 0

        result = np.sum(grid)
        print(result)
        assert(result == 620241)


def f02():
    def calc_area(cube):
        lim, _ = cube
        area = 1
        for i in range(3):
            area *= (lim[i][1] - lim[i][0])
        return area

    def count_overlap(old_cube, new_cube):
        print(old_cube, new_cube, "-> ", end='')
        lim1, old_state = old_cube
        lim2, new_state = new_cube

        if old_state == 0 and new_state == 0:
            print([])
            return []
        if old_state == 0 and new_state == 1:
            print([])
            return []

        c = []
        for i in range(3):
            if lim1[0][0] >= lim2[0][1]:
                print([])
                return []
            else:
                c.append([max(lim1[i][0], lim2[i][0]), min(lim1[i][1], lim2[i][1])])

        if old_state == 1 and new_state == 1:
            print([(c, -1)])
            return [(c, -1)]
        if old_state == 1 and new_state == 0:
            print([(c, -1)])
            return [(c, -1)]
        if old_state == -1 and new_state == 1:
            print([(c, 1)])
            return [(c, -1)]
        if old_state == -1 and new_state == 0:
            print([(c, 1)])
            return [(c, 1)]

        assert False

    def print_coords(cube):
        coords, _ = cube
        lst = []
        for x in range(coords[0][0], coords[0][1]):
            for y in range(coords[1][0], coords[1][1]):
                for z in range(coords[2][0], coords[2][1]):
                    lst.append((x, y, z))

        pprint.pprint(sorted(lst))

    with open('input3') as file:
        lines = file.read().splitlines()
        sum = 0
        cubes = []
        for line in lines:
            state, coords = line.split(' ')
            state = 1 if state == 'on' else 0
            coords = coords.split(',')
            lim = []
            bad = False
            for coord in coords:
                coord = coord[2:]
                coord = toInt(coord.split('..'))
                coord[1] += 1

                lim.append(coord)
            new_cube = (lim, state)

            if not cubes:
                cubes.append(new_cube)
                continue

            if new_cube[1] != 0:
                new_cubes = [new_cube]
            else:
                new_cubes = []

            for cube in cubes:
                new_cubes.extend(count_overlap(cube, new_cube))
                #print(cube, new_cube, sum)

            cubes.extend(new_cubes)
        #pprint.pprint(cubes)


        sum = 0
        for c in cubes:
            print(c)
            #print_coords(c)
            a = calc_area(c)
            sum += a * c[1]
            print(a, c[1], sum)

        print(sum)

        #print(sum)
        #assert(sum == 620241)


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
