import networkx as nx


def create_cave(depth, size_y, size_x, target):
    cave = [[0 for _ in range(size_x)] for _ in range(size_y)]
    erosion = [[0 for _ in range(size_x)] for _ in range(size_y)]
    erosion[0][0] = depth % 20183
    x_t, y_t = target
    for y in range(1, len(cave)):
        cave[y][0] = y * 48271
        erosion[y][0] = (cave[y][0] + depth) % 20183
    for x in range(1, len(cave[0])):
        cave[0][x] = x * 16807
        erosion[0][x] = (cave[0][x] + depth) % 20183
    for y in range(1, len(cave)):
        for x in range(1, len(cave[y])):
            if y == y_t and x == x_t:
                erosion[y][x] = depth % 20183
                continue
            cave[y][x] = erosion[y-1][x] * erosion[y][x-1]
            erosion[y][x] = (cave[y][x] + depth) % 20183

    for y, _ in enumerate(erosion):
        for x, _ in enumerate(erosion[y]):
            t = erosion[y][x] % 3
            erosion[y][x] = {
                0: '.',
                1: '=',
                2: '|'
            }[t]
    erosion[y_t][x_t] = '.'
    return erosion


cost = {
    '.': 0,
    '=': 1,
    '|': 2
}

tools = {
    'torch': 0,
    'climbing_gear': 1,
    'neither': 2
}

region_tools = {
    '.': (tools['torch'], tools['climbing_gear']),
    '=': (tools['neither'], tools['climbing_gear']),
    '|': (tools['torch'], tools['neither']),
}


def solve_part_1(depth, target):
    x_t, y_t = target
    cave = create_cave(depth, y_t + 30, x_t + 30, target)
    risk = 0
    for y in range(y_t + 1):
        for x in range(x_t + 1):
            risk += cost[cave[y][x]]
    return risk


def solve_part_2(depth, target):
    x_t, y_t = target
    cave = create_cave(depth, y_t + 30, x_t + 30, target)
    graph = create_graph(cave)
    return nx.algorithms.dijkstra_path_length(
        graph, ((0, 0), tools['torch']), ((y_t, x_t), tools['torch']), weight='weight')


def create_graph(cave):
    graph = nx.Graph()
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for y in range(len(cave)):
        for x in range(len(cave[y])):
            region = cave[y][x]
            r_tools = region_tools[region]
            graph.add_edge(((y, x), r_tools[0]),
                           ((y, x), r_tools[1]), weight=7)
            for d_y, d_x in dirs:
                pt_n = (y + d_y, x + d_x)
                if 0 <= pt_n[0] < len(cave) and 0 <= pt_n[1] < len(cave[0]):
                    region_nb = cave[pt_n[0]][pt_n[1]]
                    for tool in tools.values():
                        if tool in region_tools[region] and tool in region_tools[region_nb]:
                            graph.add_edge(
                                ((y, x), tool), (pt_n, tool), weight=1)
    return graph


def main():
    with open('input.txt') as f:
        depth = int(f.readline().strip()[6:])
        target = [int(a) for a in f.readline().strip()[7:].split(',')]
    sol1 = solve_part_1(depth, target)
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2(depth, target)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
