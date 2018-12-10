import regex as re
SIZE = 50


def get_maxes(d):
    max_y = max([y for x, y, _, _ in d.values()])
    min_y = min([y for x, y, _, _ in d.values()])
    max_x = max([x for x, y, _, _ in d.values()])
    min_x = min([x for x, y, _, _ in d.values()])
    return max_y, min_y, max_x, min_x


def solve_part_1(points):
    d = {i: p for i, p in enumerate(points)}
    s = 0
    while True:
        max_y, min_y, max_x, min_x = get_maxes(d)
        offset_x = abs(min_x)
        offset_y = abs(min_y)
        max_area = 600
        box = (max_x - min_x) * (max_y - min_y)
        if box < max_area:
            m = [['.' for i in range(max_x + offset_x + 1)]
                 for j in range(max_y + offset_y + 1)]
        for k, point in d.items():
            x, y, x_v, y_v = point
            new_x = x + x_v
            new_y = y + y_v
            d[k] = [new_x, new_y, x_v, y_v]
            if box < max_area:
                m[y - offset_y][x - offset_x] = '#'
        if box < max_area:
            print('Second: {}'.format(s))
            for row in m:
                if not all([x == '.' for x in row]):
                    print(''.join(row[:max_x - offset_x + 1]))
            return
        s += 1


def main():
    # with open('input.txt') as f:
    with open('input.txt') as f:
        points = [[int(s)
                   for s in re.findall(r'-?\d+', line)] for line in f]
    solve_part_1(points)


if __name__ == "__main__":
    main()
