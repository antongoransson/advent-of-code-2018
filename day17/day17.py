import regex as re
import sys

sys.setrecursionlimit(10000)


def create_soil(clay, spring):
    min_x = min(clay, key=lambda x: x[0])[0]
    min_y = min(clay, key=lambda x: x[1])[1]
    max_x = max(clay, key=lambda x: x[0])[0] + 50
    max_y = max(clay, key=lambda x: x[1])[1]
    m = [['.' for _ in range(0, max_x)] for _ in range(max_y + 2)]
    m[spring[1]][spring[0]] = '+'
    for x, y in clay:
        m[y][x] = '#'
    return m, max_y, min_y


def caged(m, y, x):
    if m[y][x - 1] in '#' and m[y][x] not in '~':
        while m[y + 1][x] in '#~' and m[y][x] not in '#.':
            x += 1
        if m[y][x] is '#' and m[y + 1][x] in '#~':
            return True
    elif m[y][x + 1] in '#' and m[y][x] not in '~':
        while m[y + 1][x] in '#~' and m[y][x] not in '#.':
            x -= 1
        if m[y][x] is '#' and m[y + 1][x] in '#~':
            return True
    return False


def settle(m, y, x):
    if m[y][x - 1] is '#' and m[y][x] is '|':
        while m[y][x] is '|' and m[y + 1][x] in '#~':
            m[y][x] = '~'
            x += 1
    if m[y][x + 1] is '#' and m[y][x] is '|':
        while m[y][x] is '|' and m[y + 1][x] in '#~':
            m[y][x] = '~'
            x -= 1


def flow_left(m, y, x, max_y):
    while m[y][x - 1] in '.' and m[y + 1][x] not in '.':
        m[y][x - 1] = '|'
        x -= 1
    if caged(m, y, x):
        settle(m, y, x)
        while m[y - 1][x] not in '|':
            x += 1
        flow(m, y - 1, x, max_y)
    # else:
    else:
        flow(m, y, x, max_y)


def flow_right(m, y, x, max_y):
    while m[y][x + 1] in '.|' and m[y + 1][x] not in '.|':
        m[y][x + 1] = '|'
        x += 1
    if caged(m, y, x):
        settle(m, y, x)
        while m[y - 1][x] not in '|':
            x -= 1
        flow(m, y - 1, x, max_y)
    else:
        flow(m, y, x, max_y)


def flow(m, y, x, max_y):
    if caged(m, y, x):
        settle(m, y, x)
    elif y + 1 < max_y:
        while y + 1 < max_y and m[y + 1][x] in '.|':
            m[y + 1][x] = '|'
            y += 1
            if caged(m, y, x):
                settle(m, y, x)
                while m[y][x] not in '|':
                    y -= 1
        if caged(m, y, x):
            settle(m, y, x)
            y -= 1
        if m[y][x + 1] in '.|':
            flow_right(m, y, x, max_y)
        if m[y][x - 1] in '.':
            flow_left(m, y, x, max_y)
        if caged(m, y, x):
            settle(m, y, x)


def solve_part_1(m, y, x, max_y, min_y):
    flow(m, y, x, max_y)
    return sum(row.count('~') + row.count('|') for row in m[min_y:])


def solve_part_2(m, y, x, max_y, min_y):
    flow(m, y, x, max_y)
    return sum(row.count('~')for row in m[min_y:])


def main():
    clay = []
    with open('input.txt') as f:
        for line in f:
            x = re.search(r'x=\d+(\.\.\d+)?', line).group().split('=')[1]
            y = re.search(r'y=\d+(\.\.\d+)?', line).group().split('=')[1]
            if '..' in x:
                start, end = map(int, x.split('..'))
                clay.extend([(x_i, int(y))
                             for x_i in range(start, end + 1)])
            elif '..' in y:
                start, end = map(int, y.split('..'))
                clay.extend([(int(x), y_i)
                             for y_i in range(start, end + 1)])
    spring = (500, 0)
    grid, max_y, min_y = create_soil(clay, spring)
    sol1 = solve_part_1(grid, 0, 500, max_y+1, min_y)
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2(grid, 0, 500, max_y+1, min_y)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
