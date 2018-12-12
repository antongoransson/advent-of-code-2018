# import sys
# sys.setrecursionlimit(10000)


def solve_part_1(nodes):
    if not nodes:
        return 0
    n_children, n_metadata = [nodes.pop(0) for _ in range(2)]
    v = 0
    if n_children != 0:
        v = sum([solve_part_1(nodes) for _ in range(n_children)])
    return sum([nodes.pop(0) for i in range(n_metadata)]) + v


def solve_part_2(nodes):
    if not nodes:
        return 0
    n_children, n_metadata = [nodes.pop(0) for _ in range(2)]
    if n_children == 0:
        return sum([nodes.pop(0) for _ in range(n_metadata)])
    child_values = {i + 1: solve_part_2(nodes) for i in range(n_children)}
    s = sum([child_values[nodes[i]]
             for i in range(n_metadata) if nodes[i] in child_values])
    del nodes[0:n_metadata]
    return s


def main():
    with open('input.txt') as f:
        nodes = list(map(int, f.read().split()))
    # nodes = list(map(int, "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2".split()))
    sol1 = solve_part_1([n for n in nodes])
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2(nodes)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
