import regex as re


def create_soil(clay, spring):
    min_x = min(clay, key=lambda x: x[0])[0] - 1
    max_x = max(clay, key=lambda x: x[0])[0]
    max_y = max(clay, key=lambda x: x[1])[1]
    m = [['.' for _ in range(0, max_x - min_x + 2)] for _ in range(max_y + 5)]
    m[spring[1]][spring[0] - min_x] = '+'
    for x, y in clay:
        m[y][x - min_x] = '#'
    return m, min_x, max_y, max_x


def caged(m, a, b):
    y = a
    x = b
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


def settle(m, a, b):
    y = a
    x = b
    if m[y][x - 1] is '#' and m[y][x] is '|':
        while m[y][x] is '|' and m[y + 1][x] in '#~':
            m[y][x] = '~'
            x += 1
    if m[y][x + 1] is '#' and m[y][x] is '|':
        while m[y][x] is '|' and m[y + 1][x] in '#~':
            m[y][x] = '~'
            x -= 1


def flow(m, y, x, max_y):
    if y + 1 < max_y:
        if m[y + 1][x] in '.|':
            m[y + 1][x] = '|'
            flow(m, y + 1, x, max_y)
            # if m[y + 1][x] in '#':
        else:
            if m[y][x + 1] in '.|':
                m[y][x + 1] = '|'
                flow(m, y, x + 1, max_y)
            if m[y][x - 1] in '.':
                m[y][x - 1] = '|'
                flow(m, y, x - 1, max_y)
        if caged(m, y, x):
            settle(m, y, x)


def solve_part_1(m, y, x, max_y):
    i = 0
    t = 0
    while i < 1000:
        flow(m, y, x, max_y)
        i += 1
        # for row in m:
        #     print(''.join(row))

    for row in m:
        t += row.count('~') + row.count('|')
        print(''.join(row))
    return t


def solve_part_2(lines):
    pass


def main():
    clay = []
    with open('example.txt') as f:
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
    grid, min_x, max_y, max_x = create_soil(clay, spring)
    sol1 = solve_part_1(grid, 0, 500 - min_x, max_y+1)
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2([])
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
