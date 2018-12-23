import z3
import regex as re


def dist(p, q):
    x1, y1, z1 = p
    x2, y2, z2 = q
    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)


def dist2(p, q):
    x1, y1, z1 = p
    x2, y2, z2 = q
    return abs_z3(x1 - x2) + abs_z3(y1 - y2) + abs_z3(z1 - z2)


def abs_z3(x):
    return z3.If(x >= 0, x, -x)


def solve_part_1(nanobots):
    nanobots.sort(key=lambda x: x['r'])
    strongest = nanobots[-1]
    return len([1 for bot in nanobots if dist(bot['pos'], strongest['pos']) <= strongest['r']])


def solve_part_2(nanobots):
    s = z3.Optimize()
    x = z3.Int('x')
    y = z3.Int('y')
    z = z3.Int('z')
    d = z3.Int('d')
    dists = [z3.Int(i) for i in range(len(nanobots))]
    for i, bot in enumerate(nanobots):
        dists[i] = z3.If(dist2(bot['pos'], (x, y, z)) <= bot['r'], 1, 0)
    s.maximize(z3.Sum(*dists))
    s.add(d == dist2((x, y, z), (0, 0, 0)))
    s.minimize(d)
    s.check()
    return s.model()[d]


def main():
    with open('input.txt') as f:
        nanobots = [re.findall(r'-?\d+', line) for line in f]
        nanobots = [{'pos': (int(x), int(y), int(z)), 'r': int(r)}
                    for x, y, z, r in nanobots]
    sol1 = solve_part_1(nanobots)
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2(nanobots)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
