
def solve_part_1(instructions):

    pass


def solve_part_2(instructions):
    pass


def main():
    with open('input.txt') as f:
        instructions = [line for line in f]
    sol1 = solve_part_1(instructions)
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2(instructions)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
