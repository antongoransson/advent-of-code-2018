
from collections import Counter
from itertools import combinations
from collections import Counter

size = 1200

def solve_part_1(claims):
    square = [[0 for i in range(size)] for j in range(size)]
    for claim in claims:
        claim_id = claim[0][1:]
        left_margin, top_margin = map(int, claim[2][:-1].split(','))
        width, height = map(int, claim[3].split('x'))
        for i in range(top_margin, top_margin + height):
            for j in range(left_margin, left_margin + width):
                if square[i][j] == 0:
                    square[i][j] = claim_id
                else:
                    square[i][j] = 'X'
    s = [Counter(row).get('X', 0) for row in square]
    return sum(s), square


def solve_part_2(claims, square):
    for claim in claims:
        claim_id = claim[0][1:]
        left_margin, top_margin = map(int, claim[2][:-1].split(','))
        width, height = map(int, claim[3].split('x'))
        ok = True
        for i in range(top_margin, top_margin + height):
            for j in range(left_margin, left_margin + width):
                if square[i][j] == 'X':
                    ok = False
        if ok:
            return claim_id


def main():
    with open('input.txt') as f:
        claims = [c.strip().split() for c in f]
    sol1, square = solve_part_1(claims)
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2(claims, square)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
