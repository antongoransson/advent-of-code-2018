import networkx as nx
dirs = {
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0)
}


def solve_part_1(regex):
    graph = create_graph(regex)
    lengths = nx.algorithms.shortest_path_length(graph, (0, 0))
    return max(lengths.values())


def solve_part_2(regex):
    graph = create_graph(regex)
    lengths = nx.algorithms.shortest_path_length(graph, (0, 0))
    return len([p for p in lengths.values() if p >= 1000])


def create_graph(regex):
    graph = nx.Graph()
    stack = []
    x, y = 0, 0
    for c in regex[1:-1]:
        if c is '|':
            x, y = stack[-1]
        elif c is '(':
            stack.append((x, y))
        elif c is ')':
            x, y = stack.pop()
        else:
            dx, dy = dirs[c]
            new_p = (x + dx, y + dy)
            graph.add_edge((x, y), new_p)
            x, y = new_p
    return graph


def main():
    with open('input.txt') as f:
        regex = f.readline().strip()
    sol1 = solve_part_1(regex)
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2(regex)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
