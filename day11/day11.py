
def calc_power(x, y, serial_number):
    rack_id = x + 1 + 10
    p = (y + 1) * rack_id
    p += serial_number
    p *= rack_id
    p = (p // 100) % 10
    p -= 5
    return p

# https://en.wikipedia.org/wiki/Summed-area_table


def preprocess(grid, size):
    sum_grid = [[0]*size for i in range(size)]
    for i in range(size):
        sum_grid[0][i] = grid[0][i]
    for i in range(1, size):
        for j in range(size):
            sum_grid[i][j] = grid[i][j] + sum_grid[i - 1][j]
    for i in range(size):
        for j in range(1, size):
            sum_grid[i][j] += sum_grid[i][j-1]
    return sum_grid


def solve_part_1(sum_grid, size):
    sq = 3
    current_power = None
    for y in range(size - sq):
        for x in range(size - sq):
            power = sum_grid[y][x] + sum_grid[y + sq][x + sq] - \
                sum_grid[y][x + sq] - sum_grid[y + sq][x]
            if current_power is None or power > current_power:
                max_x_y = (x + 2, y + 2)
                current_power = power
    return ', '.join(map(str, max_x_y))


def solve_part_2(sum_grid, size):
    current_power = None
    for sq in range(1, 300):
        for y in range(size - sq):
            for x in range(size - sq):
                power = sum_grid[y][x] + sum_grid[y + sq - 1][x + sq - 1] - \
                    sum_grid[y][x + sq - 1] - sum_grid[y + sq - 1][x]
                if current_power is None or power > current_power:
                    max_x_y = (x + 2, y + 2)
                    current_size = sq
                    current_power = power
    return ', '.join(map(str, (*max_x_y, current_size)))


def main():
    serial_number = 2866
    size = 300
    grid = [[0]*size for i in range(size)]
    for y in range(size):
        for x in range(size):
            grid[y][x] = calc_power(x, y, serial_number)
    sum_grid = preprocess(grid, size)
    sol1 = solve_part_1(sum_grid, size)
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2(sum_grid, size)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
