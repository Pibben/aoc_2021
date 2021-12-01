import numpy as np


def main():
    with open('input.txt') as file:
        values = file.readlines()
        values = [int(l) for l in values]
        diff = np.diff(values)
        num = sum(1 for e in diff if e > 0)
        print(num)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
