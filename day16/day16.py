opcodes = {
    0: lambda regs, a, b, c: addr(regs, a, b, c),
    1: lambda regs, a, b, c: addi(regs, a, b, c),
    2: lambda regs, a, b, c: mulr(regs, a, b, c),
    3: lambda regs, a, b, c: muli(regs, a, b, c),
    4: lambda regs, a, b, c: banr(regs, a, b, c),
    5: lambda regs, a, b, c: bani(regs, a, b, c),
    6: lambda regs, a, b, c: borr(regs, a, b, c),
    7: lambda regs, a, b, c: bori(regs, a, b, c),
    8: lambda regs, a, b, c: setr(regs, a, b, c),
    9: lambda regs, a, b, c: seti(regs, a, b, c),
    10: lambda regs, a, b, c: gtir(regs, a, b, c),
    11: lambda regs, a, b, c: gtri(regs, a, b, c),
    12: lambda regs, a, b, c: gtrr(regs, a, b, c),
    13: lambda regs, a, b, c: eqir(regs, a, b, c),
    14: lambda regs, a, b, c: eqri(regs, a, b, c),
    15: lambda regs, a, b, c: eqrr(regs, a, b, c)
}


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


def solve_part_1(samples):
    tot = 0
    instructions = {}

    # while len(instructions) < 15:
    for sample in samples:
        before, instruction, after = sample
        before = list(before)
        after = list(after)
        instruction = list(instruction)
        correct = []
        for i in range(16):
            regs = before[:]
            # if instruction[0] not in instructions:
            a = opcodes[i](regs, instruction[1],
                           instruction[2], instruction[3])
            if a == after:
                correct.append(i)
        if len(correct) >= 3:
            tot += 1
        elif len(correct) == 1:
            instructions[instruction[0]] = correct[0]
    return tot, instructions


def solve_part_2(score):
    pass


def main():
    samples = []
    with open('input.txt') as f:
        part1, part2 = f.read().split('\n\n\n')
        for x in part1.split('\n\n'):
            # print(x, '\n')
            before, instruction, after = x.split('\n')
            samples.append(
                (map(int, before.split(': ')[1][1:-1].split(',')), map(int, instruction.split(' ')), map(int, after.split(':  ')[1][1:-1].split(','))))
    sol1 = solve_part_1(samples)
    print('Part 1: {}'.format(sol1))
    # sol2 = solve_part_2(score)
    # print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
