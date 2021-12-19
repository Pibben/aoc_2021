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


def get_pose(vec, i):
    a, b, c = vec
# Rx 0     Rx 90   Rx 180    Rx 270
#  1 0 0    1 0  0   1  0  0   1 0  0
#  0 1 0    0 0 -1   0 -1  0   0 0  1
#  0 0 1    0 1  0   0  0 -1   0 -1 0
#  a b c    a c -b   a -b -c   a -c b

# Ry 0     Ry 90    Ry 180    Ry 270
#  1 0 0    0  0 1   1 0  0    -1 0 0
#  0 1 0    0  1 0   0 1  0     0 1 0
#  0 0 1    -1 0 0   0 0 -1     0 0 -1
#  a b c    -c b a   a b -c    -a b -c

# Ry 0     Ry 90    Ry 180    Ry 270
#  1 0 0
#  0 1 0
#  0 0 1


def f01():
    with open('input') as file:
        scanners = file.read().split('\n\n')



def f02():
    pass

def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
