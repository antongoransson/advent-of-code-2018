
from collections import deque


class Unit:
    def __init__(self, hp, pos, ap, t):
        self.hp = hp
        self.pos = pos
        self.ap = ap
        self.is_elf = True
        self.type = t
        self.dead = False
        self.has_attacked = False
        self.killed_elf = False

    def __str__(self):
        return 'TYPE: {}, HP: {}, POS: {}'.format(self.type, self.hp, self.pos)

    def maybe_attack(self, grid, targets):
        values = [p for p in get_all_adjacent(grid, self.pos)]
        adjacent_targets = [t for t in targets if t.pos in values]
        if adjacent_targets:
            # DO ATTACK
            adjacent_targets.sort(
                key=lambda unit: (unit.hp, unit.pos))
            target = adjacent_targets[0]
            target.hp -= self.ap
            if target.hp <= 0:
                grid[target.pos[0]][target.pos[1]] = '.'
                target.dead = True
                if target.type == 'E':
                    self.killed_elf = True
            self.has_attacked = True
        else:
            self.has_attacked = False


def get_adjacent(grid, pos):
    adjacent = [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]),
                (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)]
    return[p for p in adjacent if grid[p[0]][p[1]] in '.']


def get_all_adjacent(grid, pos):
    adjacent = [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]),
                (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)]
    return[p for p in adjacent if grid[p[0]][p[1]] not in '#']


def get_neighbours(grid):
    n = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pos = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            pos = [p for p in pos if p[0] >= 0 and p[1] >=
                   0 and p[0] < len(grid) and p[1] < len(grid[i])]
            n[i, j] = pos
    return n


def bfs(graph, grid, start, goal):
    paths = []
    goals = get_adjacent(grid, goal)
    for p in get_adjacent(grid, start):
        found = False
        if p in goals:
            paths.append([p])
            continue
        # keep track of explored nodes
        explored = set()
        # keep track of all the paths to be checked
        queue = deque([[p]])
        # keeps looping until all possible paths have been checked
        while queue:
            if found:
                break
            path = queue.popleft()
            node = path[-1]
            if node not in explored:
                neighbours = graph[node]
                for neighbour in neighbours:
                    if grid[neighbour[0]][neighbour[1]] is '.':
                        new_path = list(path)
                        new_path.append(neighbour)
                        queue.append(new_path)
                        if neighbour in goals:
                            paths.append(new_path)
                            found = True
                explored.add(node)
    return paths


def simulate_game(grid, units, is_part2):
    graph = get_neighbours(grid)
    for i in range(100):
        units = [u for u in units if not u.dead]
        units.sort(key=lambda x: x.pos)
        for u in units:
            if u.dead:
                continue
            targets = [e for e in units if e.type !=
                       u.type and not e.dead]
            if not targets:
                return i * sum([unit.hp for unit in units if not unit.dead])
            u.maybe_attack(grid, targets)
            if is_part2 and u.killed_elf:
                return False
            if not u.has_attacked:
                paths = []
                for t in targets:
                    paths.extend(bfs(graph, grid, u.pos, t.pos))
                if paths:
                    paths.sort(key=lambda x: (len(x), x[-1], x[0]))
                    best_path = paths[0]
                    grid[u.pos[0]][u.pos[1]] = '.'
                    u.pos = best_path[0]
                    grid[u.pos[0]][u.pos[1]] = u.type
                    u.maybe_attack(grid, targets)
                    if is_part2 and u.killed_elf:
                        return False


def test():
    sol = [18740, 27730, 36334, 39514, 27755, 28944]
    for k in range(1, 7):
        units = set()
        with open('example{}.txt'.format(k)) as f:
            grid = [[c for c in line.strip()] for line in f]
            for i, row in enumerate(grid):
                for j, col in enumerate(grid[i]):
                    if col == 'E':
                        units.add(Unit(200, (i, j), 3, 'E'))
                    elif col == 'G':
                        units.add(Unit(200, (i, j), 3, 'G'))
        sol1 = simulate_game(grid, units, False)
        assert(sol1 == sol[k - 1])


def main():
    test()
    units = set()
    part2_units = set()
    with open('input.txt') as f:
        grid = [[c for c in line.strip()] for line in f]
        for i, _ in enumerate(grid):
            for j, col in enumerate(grid[i]):
                if col == 'E':
                    units.add(Unit(200, (i, j), 3, 'E'))
                    part2_units.add(Unit(200, (i, j), 20, 'E'))
                elif col == 'G':
                    units.add(Unit(200, (i, j), 3, 'G'))
                    part2_units.add(Unit(200, (i, j), 3, 'G'))
    sol1 = simulate_game([[c for c in row] for row in grid], units, False)
    print('Part 1: {}'.format(sol1))
    sol2 = simulate_game(grid, part2_units, True)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
