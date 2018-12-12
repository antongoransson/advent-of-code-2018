from itertools import cycle

N_GENERATIONS = 20
def solve_part_1(initial_state, spread):
    curr_gen = initial_state
    next_gen = []
    for i in range(N_GENERATIONS):

def solve_part_2(frequencies):
   pass


def main():
    with open('input.txt') as f:
        initial_state = f.readline().strip().split(': ')[1]
        spread = [line.split(' => ')[0] for line in f if line.split(' => ')[1].strip() is '#']
    print(initial_state)
    print(spread)
    sol1 = solve_part_1(frequencies)
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2(frequencies)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()