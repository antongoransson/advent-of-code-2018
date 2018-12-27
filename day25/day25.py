import regex as re
from collections import deque, defaultdict


def dist(p, q):
    return sum(abs(x - y) for x, y in zip(p, q))


def solve_part_1(points):
    d = defaultdict(set)
    for p1 in points:
        for p2 in points:
            if dist(p1, p2) <= 3:
                d[p1].add(p2)

    c = set()
    n = 0
    for p in points:
        if p in c:
            continue
        n += 1
        q = deque([p])
        while q:
            v = q.popleft()
            if v in c:
                continue
            c.add(v)
            for y in d[v]:
                q.append(y)
    return n


def main():
    points = []
    with open('input.txt') as f:
        for line in f:
            x, y, z, v = map(int, re.findall(r'-?\d+', line))
            points.append((x, y, z, v))
    sol1 = solve_part_1(points)
    print('Part 1: {}'.format(sol1))


if __name__ == "__main__":
    main()
