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
    with open('input4') as file:
        grid = np.zeros((101, 101, 101), np.int32)
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

                if not -50 <= coord[0] <= 50:
                    bad = True
                if not -50 <= coord[1] <= 50:
                    bad = True

                coord[0] += offset
                coord[1] += offset

                lim.append(coord)
                assert(coord[1] >= coord[0])
                #print(coord)
           # print(lim)
            if not bad:
                grid[lim[0][0]:lim[0][1] + 1, lim[1][0]:lim[1][1] + 1, lim[2][0]:lim[2][1] + 1] = (1 if state == 'on' else 0)

        result = np.sum(grid)
        print(result)
        #assert(result == 620241)


def f02():
    def calc_area(cube):
        lim, _ = cube
        area = 1
        for i in range(3):
            area *= (lim[i][1] - lim[i][0])
        return area

    def get_overlap(old_cube, new_cube):
        lim1, old_state = old_cube
        lim2, _ = new_cube

        c = []
        for i in range(3):
            if lim1[i][0] >= lim2[i][1] or lim2[i][0] >= lim1[i][1]:
                return None
            else:
                c.append([max(lim1[i][0], lim2[i][0]), min(lim1[i][1], lim2[i][1])])

        return (c, -old_state)

    with open('input') as file:
        lines = file.read().splitlines()
        sum = 0
        cubes = []
        for line in lines:
            state, coords = line.split(' ')
            state = 1 if state == 'on' else 0
            coords = coords.split(',')

            lim = []
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
                overlap_cube = get_overlap(cube, new_cube)
                if overlap_cube is not None:
                    new_cubes.append(overlap_cube)

            cubes.extend(new_cubes)

        sum = 0
        for c in cubes:
            a = calc_area(c)
            sum += a * c[1]
        print(sum)
        assert(sum == 1284561759639324)


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
