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

    def play(pos, score, die, player, die_state, rolls):
        pp = pos[player]
        pp += die
        while pp > 10:
            pp -= 10
        sp = score[player]
        sp += pp
        if sp >= 1000:
            return score[1 - player], rolls
        else:
            pos = (pos[0], pp) if player == 1 else (pp, pos[1])
            score = (score[0], sp) if player == 1 else (sp, score[1])
            other = 1 - player

            sum = 0
            for _ in range(3):
                sum += die_state
                die_state += 1
                if die_state > 100:
                    die_state = 1

            return play(pos, score, sum, other, die_state, rolls + 3)

    pos = (7, 6)
    #pos = (4, 8)

    a, b = play(pos, (0, 0), 6, 0, 4, 3)

    result = a * b
    print(result)
    assert(result == 671580)


def f02():

    def roll(pos, score, player):
        c = []
        for d1 in [1, 2, 3]:
            for d2 in [1, 2, 3]:
                for d3 in [1, 2, 3]:
                    c.append(count(pos, score, d1 + d2 + d3, player))

        return sum(cc[0] for cc in c), sum(cc[1] for cc in c)

    def count(pos, score, die, player):
        if (pos, score, die, player) in count.map:
            return count.map[(pos, score, die, player)]
        pp = pos[player]
        pp += die
        while pp > 10:
            pp -= 10
        sp = score[player]
        sp += pp
        if sp >= 21:
            ret = (0, 1) if player == 1 else (1, 0)

            count.map[(pos, score, die, player)] = ret
            return ret
        else:
            new_pos = (pos[0], pp) if player == 1 else (pp, pos[1])
            new_score = (score[0], sp) if player == 1 else (sp, score[1])
            other = 1 - player

            ret = roll(new_pos, new_score, other)

            count.map[(pos, score, die, player)] = ret

            return ret
    count.map = {}

    pos = (7, 6)
    #pos = (4, 8)

    ret = roll(pos, (0, 0), 0)
    result = max(ret)
    print(result)
    assert(result == 912857726749764)


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
