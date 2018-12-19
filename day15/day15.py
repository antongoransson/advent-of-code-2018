def solve_part_1():
    pass


def solve_part_2():
    pass


def main():
    with open('example2.txt') as f:
        lines = [[c for c in line.strip()] for line in f]
        print(lines)
    sol1 = solve_part_1(int(score))
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2(score)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
