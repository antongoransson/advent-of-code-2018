def solve_part_1(n_players, n_marbles):
    board = [0]
    player_scores = {i: 0 for i in range(n_players)}
    next_marble = 1
    current_index = 0
    while True:
        for p in range(n_players):
            if next_marble > n_marbles:
                best_player = max(player_scores, key=player_scores.get)
                return (best_player, player_scores[best_player])

            if len(board) == 1:
                current_index = 1
                board.insert(current_index, next_marble)
            elif next_marble % 23 == 0:
                player_scores[p] += next_marble
                index = (current_index - 7) % len(board)
                player_scores[p] += board.pop(index)
                current_index = index
            else:
                current_index = (current_index + 2) % len(board)
                board.insert(current_index, next_marble)
            next_marble += 1


def solve_part_2(nodes):
    pass


def main():
    with open('input.txt') as f:
        i = f.read().split()
        n_players, n_marbles = int(i[0]), int(i[6])
    # nodes = list(map(int, "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2".split()))
    # n_players, n_marbles = 9, 25  # ans == 32
    # n_players, n_marbles = 10, 1618  # ans == 8317
    # n_players, n_marbles = 13, 7999  # ans == 146373

    sol1 = solve_part_1(n_players, n_marbles)
    print('Part 1: {}'.format(sol1))
    # sol2 = solve_part_1(n_players, n_marbles * 100)
    # print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
