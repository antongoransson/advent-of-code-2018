def solve_part_1(string):
    s = list(string)
    i = 0
    while i < (len(s) - 1):
        if ord(s[i]) == ord(s[i + 1]) - 32 or ord(s[i]) - 32 == ord(s[i + 1]):
            s = s[0:i] + s[i + 2:]
            i -= 1 if i > 0 else 0
        else:
            i += 1
    return len(s)


def solve_part_2(string):
    best = 10000
    for char in "abcdefghijklmnopqrstuvwxyz":
        to_replace = [char, char.capitalize()]
        s = [c for c in list(string) if c not in to_replace]
        l = solve_part_1(s)
        if l < best:
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
