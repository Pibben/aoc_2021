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


def play(board, num):
    if num in board:
        idx = board.index(num)
        board[idx] = None

        # Check rows
        for row in range(5):
            found = True
            for col in range(5):
                if board[row * 5 + col] is not None:
                    found = False
                    break
            if found:
                return True

        # Check cols
        for col in range(5):
            found = True
            for row in range(5):
                if board[row * 5 + col] is not None:
                    found = False
                    break
            if found:
                return True

    return False


def get_score(board):
    return sum(int(a) for a in board if a is not None)


def f01():
    with open('input') as file:
        groups = file.read().split('\n\n')
        rand = toInt(groups[0].split(','))
        boards = [toInt(b.split()) for b in groups[1:]]

        for r in rand:
            for bi in range(len(boards)):
                b = boards[bi]
                if play(b, r):
                    result = r * get_score(b)
                    assert(result == 67716)
                    print(result)
                    return


def f02():
    with open('input') as file:
        groups = file.read().split('\n\n')
        rand = toInt(groups[0].split(','))
        boards = [toInt(b.split()) for b in groups[1:]]

        board_done = [False] * len(boards)
        for r in rand:
            for bi in range(len(boards)):
                if board_done[bi]:
                    continue
                b = boards[bi]
                if play(b, r):
                    board_done[bi] = True
                    if all(board_done):
                        result = r * get_score(b)
                        assert(result == 1830)
                        print(result)
                        return


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
