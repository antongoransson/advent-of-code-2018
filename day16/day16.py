def addr(regs, a, b, c):
    regs[c] = regs[a] + regs[b]
    return regs


def addi(regs, a, b, c):
    regs[c] = regs[a] + b
    return regs


def mulr(regs, a, b, c):
    regs[c] = regs[a] * regs[b]
    return regs


def muli(regs, a, b, c):
    regs[c] = regs[a] * b
    return regs


def banr(regs, a, b, c):
    regs[c] = regs[a] & regs[b]
    return regs


def bani(regs, a, b, c):
    regs[c] = regs[a] & b
    return regs


def borr(regs, a, b, c):
    regs[c] = regs[a] | regs[b]
    return regs


def bori(regs, a, b, c):
    regs[c] = regs[a] | b
    return regs


def setr(regs, a, b, c):
    regs[c] = regs[a]
    return regs


def seti(regs, a, b, c):
    regs[c] = a
    return regs


def gtir(regs, a, b, c):
    regs[c] = int(a > regs[b])
    return regs


def gtri(regs, a, b, c):
    regs[c] = int(regs[a] > b)
    return regs


def gtrr(regs, a, b, c):
    regs[c] = int(regs[a] > regs[b])
    return regs


def eqir(regs, a, b, c):
    regs[c] = int(a == regs[b])
    return regs


def eqri(regs, a, b, c):
    regs[c] = int(regs[a] == b)
    return regs


def eqrr(regs, a, b, c):
    regs[c] = int(regs[a] == regs[b])
    return regs


opcodes = {
    0: addr,
    1: addi,
    2: mulr,
    3: muli,
    4: banr,
    5: bani,
    6: borr,
    7: bori,
    8: setr,
    9: seti,
    10: gtir,
    11: gtri,
    12: gtrr,
    13: eqir,
    14: eqri,
    15: eqrr
}


def solve_part_1(samples):
    tot = 0
    instructions = {}
    while len(instructions) < 15:
        for sample in samples:
            before, instruction, after = sample
            possible_instructions = []
            correct = []
            for i in range(16):
                a = opcodes[i](before[:], *instruction[1:])
                if instruction[0] not in instructions and i not in instructions.values():
                    if a == after:
                        possible_instructions.append(i)
                if a == after:
                    correct.append(i)
            if len(correct) >= 3:
                tot += 1
            if len(possible_instructions) == 1:
                instructions[instruction[0]] = possible_instructions[0]
    return tot, instructions


def solve_part_2(test_program, instructions):
    regs = [0] * 4
    for command in test_program:
        opcodes[instructions[command[0]]](regs, *command[1:])
    return regs


def main():
    samples = []
    with open('input.txt') as f:
        part1, part2 = f.read().split('\n\n\n')
        for x in part1.split('\n\n'):
            before, instruction, after = x.split('\n')
            samples.append(
                (before[8:][1:-1].split(','), instruction.split(' '), after[8:][1:-1].split(',')))
        test_program = [list(map(int, s.split(' ')))
                        for s in part2.split('\n') if s]
    samples = [(list(map(int, s[0])), list(map(int, s[1])),
                list(map(int, s[2]))) for s in samples]
    sol1, instructions = solve_part_1(samples)
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2(test_program, instructions)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
