import numpy as np


def f02():
    with open('input') as file:
        values = file.readlines()
        aim = 0
        depth = 0
        pos = 0
        for value in values:
            cmd, amt = value.split()
            amt = int(amt)
            if cmd == 'up':
                aim -= amt
            if cmd == 'down':
                aim += amt
            if cmd == 'forward':
                pos += amt
                depth += aim * amt

        print(pos * depth)


def f01():
    with open('input') as file:
        values = file.readlines()
        aim = 0
        pos = 0
        for value in values:
            cmd, amt = value.split()
            amt = int(amt)
            if cmd == 'up':
                aim -= amt
            if cmd == 'down':
                aim += amt
            if cmd == 'forward':
                pos += amt

        print(pos * aim)

def main():
    f01()
    f02()

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
