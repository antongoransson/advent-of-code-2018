from itertools import cycle

N_GENERATIONS = 50000000000

def simulate_plants(initial_state, spread, n, init_offset = 0):
    curr_gen = list(initial_state)
    offset = init_offset
    for _ in range(n):
        l = len(curr_gen)
        hash_index_front = [i for i in range(4) if curr_gen[i] is '#']
        hash_index_back= [l - i - 1 for i in range(l - 3, l) if curr_gen[i] is '#']
        padding_front = '.' * (4 - hash_index_front[0] if hash_index_front else 4 ) 
        offset += len(padding_front) - 2
        padding_back =  '.' * (4 - hash_index_back[-1] if hash_index_back else 4)
        curr_gen = list(padding_front) + curr_gen + list(padding_back)
        next_gen = ['.'] * (len(curr_gen) - 4)
        for i in range(2, len(curr_gen) -2):
            row = ''.join(curr_gen[i - 2: i + 3])
            if row in spread:
                next_gen[i -2] = '#'
        curr_gen = next_gen
    return sum([i - offset for i in range(len(curr_gen)) if curr_gen[i] is '#' ]), curr_gen, offset


def solve_part_1(initial_state, spread):
    return simulate_plants(initial_state, spread, 20)[0]

def solve_part_2(initial_state, spread):
    curr_gen = list(initial_state)
    offset = 0
    prev_s = 0
    diff = -1
    for gen in range(10000):
        s, curr_gen, offset = simulate_plants(''.join(curr_gen), spread, 1, offset)
        if diff == s - prev_s:
            return s + (N_GENERATIONS - gen - 1 ) * diff
        diff = s - prev_s
        prev_s = s


def main():
    with open('input.txt') as f:
        initial_state = f.readline().strip().split(': ')[1]
        spread = [line.split(' => ')[0] for line in f if line.split(' => ')[1].strip() is '#']
    sol1 = solve_part_1(initial_state, spread)
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2(initial_state, spread)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()