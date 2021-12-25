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


def do_block(block, w, z):
    regs = {'x': 0, 'y': 0, 'z': z, 'w': w}
    for line in block:
        instr = line.split(' ')

        if instr[0] == 'add':
            if instr[2][0] == '-' or instr[2].isnumeric():
                num = int(instr[2])
                regs[instr[1]] += num
            else:
                regs[instr[1]] += regs[instr[2]]
        elif instr[0] == 'mul':
            if instr[2][0] == '-' or instr[2].isnumeric():
                num = int(instr[2])
                regs[instr[1]] *= num
            else:
                regs[instr[1]] *= regs[instr[2]]
        elif instr[0] == 'mod':
            if instr[2][0] == '-' or instr[2].isnumeric():
                num = int(instr[2])
                if num <= 0 or regs[instr[1]] < 0:
                    return None
                regs[instr[1]] %= num
            else:
                if regs[instr[2]] <= 0 or regs[instr[1]] < 0:
                    return None
                regs[instr[1]] %= regs[instr[2]]
        elif instr[0] == 'div':
            if instr[2][0] == '-' or instr[2].isnumeric():
                num = int(instr[2])
                if num == 0:
                    return None
                regs[instr[1]] //= num
            else:
                if regs[instr[2]] == 0:
                    return None
                regs[instr[1]] //= regs[instr[2]]
        elif instr[0] == 'eql':
            if instr[2][0] == '-' or instr[2].isnumeric():
                num = int(instr[2])
                regs[instr[1]] = int(regs[instr[1]] == num)
            else:
                regs[instr[1]] = int(regs[instr[1]] == regs[instr[2]])
        else:
            assert False

    return regs['z']


def f01():
    with open('input') as file:
        lines = file.read()
        blocks = lines.split('inp w\n')
        blocks = blocks[1:]
        blocks = [b.splitlines() for b in blocks]

        regs = {0: []}
        for b in range(len(blocks)):
            new = {}
            block = blocks[b]
            for i in range(9, 0, -1):
                for r, ii in regs.items():
                    this = do_block(block, i, r)
                    if this > 10000000:
                        continue
                    if this not in new:
                        new[this] = ii + [i]
                    assert(len(new[this]) == b + 1)
            regs = new
        result = int(''.join(str(a) for a in regs[0]))
        print(result)
        assert(result == 49917929934999)


def f02():
    with open('input') as file:
        lines = file.read()
        blocks = lines.split('inp w\n')
        blocks = blocks[1:]
        blocks = [b.splitlines() for b in blocks]

        regs = {0: []}
        for b in range(len(blocks)):
            new = {}
            block = blocks[b]
            for i in range(1, 10):
                for r, ii in regs.items():
                    this = do_block(block, i, r)
                    if this > 10000000:
                        continue
                    if this not in new:
                        new[this] = ii + [i]
                    assert(len(new[this]) == b + 1)
            regs = new
        result = int(''.join(str(a) for a in regs[0]))
        print(result)
        assert(result == 11911316711816)


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
