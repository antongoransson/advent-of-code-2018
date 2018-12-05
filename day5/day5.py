def solve_part_1(string):
    stack = []
    for char in string:
        stack.append(char)
        if len(stack) > 1 and stack[-1] == stack[-2].swapcase():
            stack.pop()
            stack.pop()
    return len(stack)


def solve_part_2(string):
    best = None
    for char in 'abcdefghijklmnopqrstuvwxyz':
        to_replace = [char, char.capitalize()]
        s = [c for c in string if c not in to_replace]
        l = solve_part_1(s)
        if best is None or l < best:
            best = l
    return best


def main():
    with open('input.txt') as f:
        s = f.read()
    sol1 = solve_part_1(s)
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2(s)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
