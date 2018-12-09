from collections import deque
from itertools import cycle


def solve_part_1(n_players, n_marbles):
    board = deque([0])
    player_scores = {i: 0 for i in range(n_players)}
    for next_marble, player in zip([i + 1 for i in range(n_marbles + 1)], cycle([i for i in range(n_players)])):
        if next_marble % 23 == 0:
            board.rotate(7)
            player_scores[player] += next_marble + board.popleft()
        else:
            board.rotate(-2)
            board.appendleft(next_marble)
    best_player = max(player_scores, key=player_scores.get)
    return (best_player, player_scores[best_player])


def main():
    with open('input.txt') as f:
        i = f.read().split()
        n_players, n_marbles = int(i[0]), int(i[6])
    # n_players, n_marbles = 9, 25  # ans == 32
    # n_players, n_marbles = 10, 1618  # ans == 8317
    # n_players, n_marbles = 13, 7999  # ans == 146373
    sol1 = solve_part_1(n_players, n_marbles)
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_1(n_players, n_marbles * 100)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
