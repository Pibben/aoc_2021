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


def parse(s, zero, one):
    s = s.replace(zero, '0')
    s = s.replace(one, '1')
    return int(s, 2)


def f01():
    with open('input') as file:
        lines = file.read().splitlines()

        length = len(lines[0])

        c0 = [0] * length
        c1 = [0] * length

        for line in lines:
            for a in range(len(line)):
                if line[a] == '0':
                    c0[a] += 1
                if line[a] == '1':
                    c1[a] += 1

        gamma = [' '] * length

        for a in range(length):
            if c0[a] > c1[a]:
                gamma[a] = '0'
            else:
                gamma[a] = '1'

        epsilon = [' '] * length

        for a in range(length):
            if c0[a] < c1[a]:
                epsilon[a] = '0'
            else:
                epsilon[a] = '1'

        print(int("".join(gamma), 2) * int("".join(epsilon), 2))


def f02():
    def getCount(lines):
        length = len(lines[0])

        c0 = [0] * length
        c1 = [0] * length

        for line in lines:
            for a in range(len(line)):
                if line[a] == '0':
                    c0[a] += 1
                if line[a] == '1':
                    c1[a] += 1

        return c0, c1

    with open('input') as file:
        lines = file.read().splitlines()

        length = len(lines[0])

        oxy = lines
        co2 = lines
        for pos in range(length):
            oxykeep = []
            c0, c1 = getCount(oxy)
            for line in oxy:
                if line[pos] == '0' and c1[pos] < c0[pos]:
                    oxykeep.append(line)
                if line[pos] == '1' and c1[pos] >= c0[pos]:
                    oxykeep.append(line)

            oxy = oxykeep
            if len(oxy) == 1:
                break

        for pos in range(length):
            co2keep = []
            c0, c1 = getCount(co2)
            for line in co2:
                if line[pos] == '0' and c1[pos] >= c0[pos]:
                    co2keep.append(line)
                if line[pos] == '1' and c1[pos] < c0[pos]:
                    co2keep.append(line)

            co2 = co2keep
            if len(co2) == 1:
                break

        print(int(co2[0], 2) * int(oxy[0], 2))


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
