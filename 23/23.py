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


def do(depth):

    with open('input') as file:
        area = file.read().splitlines()

        if depth == 4:
            area.insert(3, "  #D#C#B#A#")
            area.insert(4, "  #D#B#A#C#")

        arena = []
        arena.append(list('#' * 13))
        arena.append(list('#...........#'))
        arena.append(list('###.#.#.#.###'))
        arena.append(list('###.#.#.#.###'))
        if depth == 4:
            arena.append(list('###.#.#.#.###'))
            arena.append(list('###.#.#.#.###'))
        arena.append(list('  #########'))

        scores = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
        rooms = {'A': 3, 'B': 5, 'C': 7, 'D': 9}

        def room(state, type):
            x = rooms[type]
            res = [None] * depth
            for a in state:
                if a[0] == x:
                    for d in range(depth):
                        if a[1] == d + 2:
                            res[d] = a

            #validate_room(state, res)

            return res

        def print_area(state):
            lines = copy.deepcopy(arena)
            for a in state:
                lines[a[1]][a[0]] = a[2]

            for line in lines:
                print(''.join(line))

        def occupied(state, x, y):
            return any((x, y) == a[:2] for a in state)

        def can_move_out_of_room(state, a):
            # On top with wrong type or,
            # On top with correct type, but wrong type below
            x, y, type = a
            #assert(x == rooms[type])

            if occupied(state, x, y - 1):  # Not on top
                return False

            # On top

            if x != rooms[type]:  # Wrong room
                if not occupied(state, x, y - 1):
                    return True

            # Correct room, on top

            r = room(state, type)
            idx = r.index(a)

            for i in range(idx + 1, len(r)):
                rr = r[i]

                if rooms[rr[2]] != x: # wrong type
                    return True
            return False

        def can_move_into_room(state, type):
            r = room(state, type)
            last_free = 0
            for i in range(len(r)):
                rr = r[i]
                if rr is None:
                    last_free = i
                else:
                    if rr[2] != type:
                        return None

            return last_free

        def find(state, x, y, type, offset):
            assert(y == 1)
            ret = []
            steps = offset
            for i in range(x + 1, 12):
                steps += 1
                if occupied(state, i, y):
                    break
                if i == rooms[type]:
                    slot = can_move_into_room(state, type)
                    if slot is not None:
                        return [((i, 2 + slot), steps + 1 + slot)]
                if i not in rooms.values() and offset > 0:
                    ret.append(((i, y), steps))
            steps = offset
            for i in range(x - 1, 0, -1):
                steps += 1
                if occupied(state, i, y):
                    break
                if i == rooms[type]:
                    slot = can_move_into_room(state, type)
                    if slot is not None:
                        return [((i, 2 + slot), steps + 1 + slot)]
                if i not in rooms.values() and offset > 0:
                    ret.append(((i, y), steps))
            return ret

        def move(state, a):
            x, y, type = a
            if y >= 2: # in room
                res = can_move_out_of_room(state, a)
                if res:
                    return find(state, x, 1, type, y - 1)

            if y == 1: #corridor
                return find(state, x, y, type, 0)

            return []

        visited = set()

        def dijkstra(src, dst):
            cost = {src: 0}
            pq = queue.PriorityQueue()
            pq.put((0, src))

            while not pq.empty():
                _, curr = pq.get()
                visited.add(curr)

                if curr == dst:
                    continue

                state = list(curr)

                for i in range(len(state)):
                    a = state[i]
                    type = a[2]
                    moves = move(state, a)
                    for (x, y), steps in moves:
                        score = steps * scores[type]
                        old = state[i]
                        state[i] = (x, y, a[2])
                        state_t = tuple(sorted(state))
                        state[i] = old
                        if state_t not in visited:
                            oc = cost.get(state_t, sys.maxsize)
                            nc = cost[curr] + score
                            if nc < oc:
                                pq.put((nc, state_t))
                                cost[state_t] = nc

            return cost[dst]

        amphi = []
        for y in range(2 + depth + 1):
            for x in range(11):
                if area[y][x].isalpha():
                    amphi.append((x, y, area[y][x]))

        #print(amphi)
        #print(room('A'))
        #print_area()

        dst2 = ((3, 2, 'A'), (5, 2, 'B'), (7, 2, 'C'), (9, 2, 'D'), (3, 3, 'A'), (5, 3, 'B'), (7, 3, 'C'), (9, 3, 'D'))
        dst4 = ((3, 2, 'A'), (5, 2, 'B'), (7, 2, 'C'), (9, 2, 'D'), (3, 3, 'A'), (5, 3, 'B'), (7, 3, 'C'), (9, 3, 'D'), (3, 4, 'A'), (5, 4, 'B'), (7, 4, 'C'), (9, 4, 'D'), (3, 5, 'A'), (5, 5, 'B'), (7, 5, 'C'), (9, 5, 'D'))

        return dijkstra(tuple(sorted(amphi)), tuple(sorted(dst4 if depth == 4 else dst2)))


def f01():
    result = do(2)
    print(result)
    assert(result == 15109)


def f02():
    result = do(4)
    print(result)
    assert(result == 53751)


def main():
    f01()
    f02()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
