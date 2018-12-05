from itertools import cycle


def solve_part_1(frequencies):
    return sum(frequencies)


def solve_part_2(frequencies):
    current_freq = 0
    unique_freq = set([current_freq])
    for freq in cycle(frequencies):
        current_freq += freq
        if current_freq in unique_freq:
            return current_freq
        unique_freq.add(current_freq)


def main():
    with open('input.txt') as f:
        frequencies = [int(freq) for freq in f]
    sol1 = solve_part_1(frequencies)
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2(frequencies)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
