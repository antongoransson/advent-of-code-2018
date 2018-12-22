import time


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
    'addr': addr,
    'addi': addi,
    'mulr': mulr,
    'muli': muli,
    'banr': banr,
    'bani': bani,
    'borr': borr,
    'bori': bori,
    'setr': setr,
    'seti': seti,
    'gtir': gtir,
    'gtri': gtri,
    'gtrr': gtrr,
    'eqir': eqir,
    'eqri': eqri,
    'eqrr': eqrr
}


def solve_part_1(ip, instructions):
    regs = [0] * 6
    while regs[ip] < len(instructions):
        c_i = instructions[regs[ip]]
        opcodes[c_i[0]](regs, *c_i[1:])
        regs[ip] += 1
    return regs[0]


def solve_part_2(ip, instructions):
    regs = [0] * 6
    regs[0] = 1
    while regs[ip] < len(instructions):
        if regs[ip] == 2 and regs[3] != 0:
            if regs[5] % regs[3] == 0:
                regs[0] += regs[3]
            regs[2] = 1
            regs[1] = regs[5]
            regs[ip] = 12
        c_i = instructions[regs[ip]]
        opcodes[c_i[0]](regs, *c_i[1:])
        regs[ip] += 1
    return regs[0]


def main():
    with open('input.txt') as f:
        ip = int(f.readline().strip()[-1])
        lines = [line.strip().split(' ') for line in f]
        instructions = [[i[0], int(i[1]), int(i[2]), int(i[3])] for i in lines]
    sol1 = solve_part_1(ip, instructions)
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2(ip, instructions)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
