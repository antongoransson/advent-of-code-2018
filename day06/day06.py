MAX_DIST = 10000


def dist(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


def solve_part_1(c, max_y, max_x, min_x, min_y):
    m = [[-1 for i in range(min_x, max_x + 1)]
         for j in range(min_y, max_y + 1)]
    counts = {k: 0 for k, _ in c}
    for i in range(max_y - min_y):
        for j in range(max_x - min_x):
            min_dist = 100000000000
            close_coords = []
            for k, coord in c:
                d = dist((j, i), coord)
                if d < min_dist:
                    min_dist = d
                    close_coords = [k]
                elif d == min_dist:
                    close_coords.append(k)
            if len(close_coords) == 1:
                k = close_coords[0]
                m[i][j] = k
                counts[k] += 1
    inf_areas = set()
    for i in range(max_x - min_x + 1):
        inf_areas.update([m[0][i], m[max_y-min_y][i]])
    for i in range(max_y - min_y + 1):
        inf_areas.update([m[i][0], m[i][max_x-min_x]])
    best = max([v for k, v in counts.items() if k not in inf_areas])
    return best


def solve_part_2(c, max_y, max_x, min_x, min_y):
    a = 0
    for i in range(max_y):
        for j in range(max_x):
            s = sum([dist((j, i), coord) for k, coord in c])
            if s < MAX_DIST:
                a += 1
    return a


def main():
    with open('input.txt') as f:
        coords = [list(map(int, line.strip().split(','))) for line in f]
        ys = [c[0] for c in coords]
        xs = [c[1] for c in coords]
        min_y = min(ys)
        max_y = max(ys)
        min_x = min(xs)
        max_x = max(xs)
    c = list(zip([i + 1 for i in range(len(coords))], coords))
    sol1 = solve_part_1(c, max_y, max_x, min_x, min_y)
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2(c, max_y, max_x, min_x, min_y)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
