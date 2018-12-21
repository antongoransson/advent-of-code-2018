import matplotlib.pyplot as plt


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
        if regs[ip] == 28:
            regs[0] = regs[3]
        opcodes[c_i[0]](regs, *c_i[1:])
        regs[ip] += 1
    return regs[0]


def solve_part_2():
    seen = set()
    prev_v = -1
    d = 0
    while True:
        c = (d | 65536)
        d = 5557974
        while True:
            d += (c & 255)
            d &= 16777215
            d *= 65899
            d &= 16777215
        # if regs[ip] == 28:
            if 256 > c:
                if d not in seen:
                    seen.add(d)
                    prev_v = d
                    break
                else:
                    return prev_v
            else:
                c //= 256


def main():
    with open('input.txt') as f:
        with open('input.txt') as f:
            ip = int(f.readline().strip()[-1])
            lines = [line.strip().split(' ') for line in f]
            instructions = [[i[0], int(i[1]), int(
                i[2]), int(i[3])] for i in lines]
    sol1 = solve_part_1(ip, instructions)
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2()
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
