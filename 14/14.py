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
        template, polylines = file.read().split('\n\n')

        poly = dict()
        for line in polylines.splitlines():
            a, b = line.split(' -> ')
            poly[a] = b

        def count(key, iter):
            if iter == 0 or key not in poly:
                return key
            return count(''.join((key[0], poly[key])), iter - 1)[:-1] + count(''.join((poly[key], key[1])), iter - 1)

        sum = ''
        for c in range(len(template) - 1):
            key = template[c:c + 2]
            sum += count(key, 10)[:-1]
        sum += template[-1]

        distinct = set(sum)
        c = sorted(sum.count(a) for a in distinct)
        result = c[-1] - c[0]
        print(result)
        assert(result == 3284)


def f02():
    with open('input') as file:
        template, polylines = file.read().split('\n\n')

        poly = dict()
        for line in polylines.splitlines():
            a, b = line.split(' -> ')
            poly[a] = b

        pairs = dict()
        for c in range(len(template) - 1):
            key = template[c:c + 2]
            if key not in pairs:
                pairs[key] = 1
            else:
                pairs[key] += 1

        def multiply(key, num, dst):
            if key in dst:
                dst[key] += num
            else:
                dst[key] = num

        for i in range(40):
            new_pairs = dict()
            for (v, k) in pairs.items():
                if v in poly:
                    p1 = v[0] + poly[v]
                    multiply(p1, k, new_pairs)
                    p2 = poly[v] + v[1]
                    multiply(p2, k, new_pairs)
                else:
                    new_pairs[k] = v

            pairs = new_pairs

        all_chars = {c for k in pairs.keys() for c in k}

         count = {c: sum(v if c == k[0] else 0 for (k, v) in pairs.items()) for c in all_chars}
        count[template[-1]] += 1

        c = sorted(count.values())
        result = c[-1] - c[0]
        print(result)
        assert(result == 4302675529689)


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
