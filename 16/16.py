import copy
import functools
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
        data = file.read()[:-1]

        dbin = bin(int(data, 16))[2:].zfill(len(data) * 4)

        versions = []

        def parse(pack, idx):
            version = int(pack[idx:idx+3], 2)
            versions.append(version)
            idx += 3
            type_id = int(pack[idx:idx+3], 2)
            idx += 3

            if type_id == 4:
                while True:
                    flag = int(pack[idx], 2)
                    idx += 1
                    literal = int(pack[idx:idx+4], 2)
                    idx += 4
                    if not flag:
                        break
            else:
                length_type_id = int(pack[idx], 2)
                idx += 1
                if length_type_id == 0:
                    sub_len = int(pack[idx:idx+15], 2)
                    idx += 15
                    oidx = idx
                    while idx < oidx + sub_len:
                        idx = parse(pack, idx)
                else:
                    num_sub = int(pack[idx:idx+11], 2)
                    idx += 11
                    for _ in range(num_sub):
                        idx = parse(pack, idx)
            return idx

        parse(dbin, 0)
        result = sum(versions)
        print(result)
        assert(result == 957)


def f02():
    with open('input') as file:
        data = file.read()[:-1]

        dbin = bin(int(data, 16))[2:].zfill(len(data) * 4)

        def get_values(pack, idx):
            length_type_id = int(pack[idx], 2)
            idx += 1
            values = []
            if length_type_id == 0:
                sub_len = int(pack[idx:idx+15], 2)
                idx += 15
                oidx = idx
                while idx < oidx + sub_len:
                    idx, value = parse(pack, idx)
                    values.extend(value)
            else:
                num_sub = int(pack[idx:idx+11], 2)
                idx += 11
                for _ in range(num_sub):
                    idx, value = parse(pack, idx)
                    values.extend(value)

            return idx, values

        def parse(pack, idx):
            version = int(pack[idx:idx+3], 2)

            idx += 3
            type_id = int(pack[idx:idx+3], 2)
            idx += 3

            if type_id == 0:
                idx, values = get_values(pack, idx)
                return idx, [sum(values)]

            elif type_id == 1:
                idx, values = get_values(pack, idx)
                return idx, [functools.reduce(lambda a, b: a*b, values)]
            elif type_id == 2:
                idx, values = get_values(pack, idx)
                return idx, [min(values)]
            elif type_id == 3:
                idx, values = get_values(pack, idx)
                return idx, [max(values)]
            elif type_id == 5:
                idx, values = get_values(pack, idx)
                assert(len(values) == 2)
                return idx, [1 if values[0] > values[1] else 0]
            elif type_id == 6:
                idx, values = get_values(pack, idx)
                assert(len(values) == 2)
                return idx, [1 if values[0] < values[1] else 0]
            elif type_id == 7:
                idx, values = get_values(pack, idx)
                assert(len(values) == 2)
                return idx, [1 if values[0] == values[1] else 0]
            elif type_id == 4:
                value = 0
                while True:
                    value *= 16
                    flag = int(pack[idx], 2)
                    idx += 1
                    literal = int(pack[idx:idx+4], 2)
                    value += literal
                    idx += 4
                    if not flag:
                        break
                return idx, [value]

            assert False

        _, values = parse(dbin, 0)
        assert(len(values) == 1)
        result = values[0]
        print(result)
        assert(result == 744953223228)


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
