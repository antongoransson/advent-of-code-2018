
from collections import Counter
from itertools import combinations


def solve_part_1(box_ids):
    n_two = 0
    n_three = 0
    for b_id in box_ids:
        c = Counter(b_id)
        if 2 in c.values():
            n_two += 1
        if 3 in c.values():
            n_three += 1
    return n_two * n_three


def solve_part_2(box_ids):
    for box_id1, box_id2 in combinations(box_ids, 2):
        b2_seqs = [box_id2[0:i] + box_id2[i + 1:] for i in range(len(box_ids))]
        for b1_seq in [box_id1[0:i] + box_id1[i + 1:] for i in range(len(box_ids))]:
            if b1_seq in b2_seqs:
                return b1_seq


def main():
    with open('input.txt') as f:
        box_ids = [b_id.strip() for b_id in f]
    sol1 = solve_part_1(box_ids)
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2(box_ids)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
