from collections import Counter
from itertools import combinations


def solve_part_1(box_ids):
    n_two = 0
    n_three = 0
    for b_id in box_ids:
        c = Counter(b_id)
        for v in c.values():
            if v == 2:
                n_two += 1
            elif v == 3:
                n_three += 1
    return n_two * n_three


def solve_part_2(box_ids):
    for box_id1, box_id2 in combinations(box_ids, 2):
        for i in range(len(box_ids)):
            box_seq1 = box_id1[0:i] + box_id1[i + 1:]
            box_seq2 = box_id2[0:i] + box_id2[i + 1:]
            if box_seq1 == box_seq2:
                return box_seq1


def main():
    with open('input.txt') as f:
        box_ids = [b_id.strip() for b_id in f]
    sol1 = solve_part_1(box_ids)
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2(box_ids)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
