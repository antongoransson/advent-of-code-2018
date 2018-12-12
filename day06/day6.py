SIZE = 400
MAX_DIST = 10000


def dist(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


def get_min(array):
    return min([v[1] for v in array])


def solve_part_1(c):
    m = [[0 for i in range(SIZE)] for j in range(SIZE)]
    counts = {k: 0 for k, _ in c}
    for i in range(SIZE):
        for j in range(SIZE):
            dists = [(k, dist((j, i), coord)) for k, coord in c]
            minimum = get_min(dists)
            close_coords = list(
                filter(lambda x: dist((j, i), x[1]) == minimum, c))
            if len(close_coords) > 1:
                m[i][j] = -1
            else:
                m[i][j] = close_coords[0][0]
        for k, _ in c:
            counts[k] += m[i].count(k)

    inf_areas = set()
    for i in range(SIZE):
        inf_areas.update([m[0][i], m[i][0], m[SIZE - 1][i], m[i][SIZE - 1]])
    best = max([v for k, v in counts.items() if k not in inf_areas])
    return best


def solve_part_2(c):
    a = 0
    for i in range(SIZE):
        for j in range(SIZE):
            s = sum([dist((j, i), coord) for k, coord in c])
            if s < MAX_DIST:
                a += 1
    return a


def main():
    with open('input.txt') as f:
        coords = [list(map(int, line.strip().split(','))) for line in f]
    c = list(zip([i + 1 for i in range(len(coords))], coords))
    sol1 = solve_part_1(c)
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2(c)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
