
from collections import Counter
from itertools import combinations
from collections import Counter
from datetime import datetime
size = 1200


def solve_part_1(claims):
    pass


def solve_part_2(claims, square):
    pass


def main():
    with open('input.txt') as f:
        claims = [c.strip().split() for c in f]
    sol1, square = solve_part_1(claims)
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2(claims, square)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
