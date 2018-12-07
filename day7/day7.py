from collections import defaultdict

N_WORKERS = 6


def get_available(d):
    return [C for C, v in d.items() if len(v) == 0]


def create_dict(instructions):
    d = defaultdict(set)
    for fst, snd in instructions:
        d[snd].add(fst)
        d[fst].union(set())
    return d


def solve_part_1(instructions):
    d = create_dict(instructions)
    next_instruction = sorted(get_available(d))
    order = []
    while next_instruction:
        next_instruction = next_instruction[0]
        d.pop(next_instruction, None)
        for v in d.values():
            if next_instruction in v:
                v.remove(next_instruction)
        order.append(next_instruction)
        next_instruction = sorted(get_available(d))
    return ''.join(order)


def solve_part_2(instructions):
    d = create_dict(instructions)
    jobs = defaultdict(lambda: defaultdict(int))
    next_instructions = sorted(get_available(d))
    seconds = 10000
    for i in range(seconds):
        for instruction in next_instructions:
            for worker in range(N_WORKERS):
                if not jobs[worker] and instruction in d:
                    jobs[worker][instruction] = ord(instruction) - 4
                    d.pop(instruction, None)
        for worker in jobs:
            if jobs[worker]:
                c = next(iter(jobs[worker].keys()))
                jobs[worker][c] -= 1
                if jobs[worker][c] == 0:
                    jobs[worker].pop(c, None)
                    for v in d.values():
                        if c in v:
                            v.remove(c)
        next_instructions = sorted(get_available(d))
        if not d and not sum([1 if jobs[worker] else 0 for worker in jobs]):
            return i + 1


def main():
    with open('input.txt') as f:
        instructions = [(line[5], line[36]) for line in f]
    sol1 = solve_part_1(instructions)
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2(instructions)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
