import networkx as nx


def solve_part_1(depth, target):
    pass


def solve_part_2(depth, target):
    pass


def main():
    with open('input.txt') as f:
        depth = int(f.readline().strip()[6:])
        target = [int(a) for a in f.readline().strip()[7:].split(',')]
    sol1 = solve_part_1(depth, target)
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2(depth, target)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
