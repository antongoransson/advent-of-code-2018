import regex as re


def dist(p, q):
    x1, y1, z1 = p
    x2, y2, z2 = q
    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)


def solve_part_1(nanobots):
    nanobots.sort(key=lambda x: x['r'])
    strongest = nanobots[-1]
    return len([1 for bot in nanobots if dist(bot['pos'], strongest['pos']) <= strongest['r']])


def solve_part_2(depth, target):
    pass


def main():
    with open('input.txt') as f:
        nanobots = [re.findall(r'-?\d+', line) for line in f]
        nanobots = [{'pos': (int(x), int(y), int(z)), 'r': int(r)}
                    for x, y, z, r in nanobots]
    sol1 = solve_part_1(nanobots)
    print('Part 1: {}'.format(sol1))
    # sol2 = solve_part_2(nanobots)
    # print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
