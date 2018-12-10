from collections import deque
from itertools import cycle


def solve_part_1(input):
    pass


def solve_part_2(input):
    pass


def main():
    with open('example.txt') as f:
        i = f.read().split()
        n_players, n_marbles = int(i[0]), int(i[6])
    # n_players, n_marbles = 9, 25  # ans == 32
    # n_players, n_marbles = 10, 1618  # ans == 8317
    # n_players, n_marbles = 13, 7999  # ans == 146373
    sol1 = solve_part_1(n_players, n_marbles)
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_1(n_players, n_marbles * 100)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
