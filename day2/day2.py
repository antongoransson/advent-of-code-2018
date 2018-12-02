
from collections import Counter


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
    for b_id1 in box_ids:
        for i in range(len(b_id1)):
            for b_id2 in box_ids:
                for j in range(len(b_id2)):
                    if b_id1 == b_id2:
                        continue
                    b1 = b_id1[0:i] + b_id1[i + 1:]
                    b2 = b_id2[0:j] + b_id2[j + 1:]
                    if b1 == b2:
                        return b1


def main():
    with open('input.txt') as f:
        box_ids = [b_id.strip() for b_id in f]
    sol1 = solve_part_1(box_ids)
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2(box_ids)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
