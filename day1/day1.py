

def solve_part_1(frequencies):
    return sum(frequencies)


def solve_part_2(frequencies):
    i = 0
    current_freq = 0
    unique_freq = set()
    l = len(frequencies)
    while True:
        current_freq += frequencies[i]
        if current_freq in unique_freq:
            return current_freq
        unique_freq.add(current_freq)
        i = (i + 1) % l


def main():
    with open('input.txt') as f:
        frequencies = [int(freq.replace('+', '')) for freq in f]
    sol1 = solve_part_1(frequencies)
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2(frequencies)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
