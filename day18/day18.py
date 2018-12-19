import time
def neighbours(area, i, j):
    neighbours = ''
    for k in range(i - 1, i + 2):
        for l in range(j - 1, j + 2):
            if k >= 0 and k < len(area) and l >= 0 and l < len(area[k]) and (k != i or j != l):
                neighbours += area[k][l]
    return neighbours

def next_state(area):
    next_area = [[c for c in area[i]] for i in range(len(area))]
    for i, _ in enumerate(area):
        for j, _ in enumerate(area[i]):
            n = neighbours(area, i , j)
            if area[i][j] is '.':
                if n.count('|') >= 3:
                    next_area[i][j] = '|'
            elif area[i][j] is '#':
                if n.count('|') < 1 or n.count('#') < 1:
                    next_area[i][j] = '.'
            elif area[i][j] is '|':
                if n.count('#') >= 3:
                    next_area[i][j] = '#'
    return next_area

def solve_part_1(area):
    n_minutes = 10
    curr_minute = 0
    while curr_minute < n_minutes:
        curr_minute += 1
        area = next_state(area)
    tree_count= 0
    lumberyard_count = 0
    for row in area:
        tree_count += row.count('|')
        lumberyard_count += row.count('#')
    return tree_count * lumberyard_count

def solve_part_2(area):
    n_minutes = 1000000000
    curr_minute = 0
    repeating_values= {}
    while curr_minute < n_minutes:
        tree_count = 0
        lumberyard_count = 0
        area = next_state(area)
        for row in area:
            tree_count += row.count('|')
            lumberyard_count += row.count('#')
        tot = tree_count * lumberyard_count
        curr_minute += 1
        if tot in repeating_values and (n_minutes - curr_minute) % (curr_minute - repeating_values[tot]) == 0:
            return tot
        repeating_values[tot] = curr_minute


def main():
    with open('input.txt') as f:
        area = [[c for c in line.strip()] for line in f]
    sol1 = solve_part_1(area)
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2(area)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
