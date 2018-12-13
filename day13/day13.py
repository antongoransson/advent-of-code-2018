turns = {
    'LEFT': 'STRAIGHT',
    'STRAIGHT': 'RIGHT',
    'RIGHT': 'LEFT'
}

directions = {
    ('^', 'LEFT'): {'new_direction': '<', 'pos_diff': (0, -1)},
    ('^', 'STRAIGHT'): {'new_direction': '^', 'pos_diff': (-1, 0)},
    ('^', 'RIGHT'): {'new_direction': '>', 'pos_diff': (0, 1)},
    ('v', 'LEFT'):  {'new_direction': '>', 'pos_diff': (0, 1)},
    ('v', 'STRAIGHT'):  {'new_direction': 'v', 'pos_diff': (1, 0)},
    ('v', 'RIGHT'): {'new_direction': '<', 'pos_diff': (0, -1)},
    ('<', 'LEFT'): {'new_direction': 'v', 'pos_diff': (1, 0)},
    ('<', 'STRAIGHT'): {'new_direction': '<', 'pos_diff': (0, -1)},
    ('<', 'RIGHT'): {'new_direction': '^', 'pos_diff': (-1, 0)},
    ('>', 'LEFT'): {'new_direction': '^', 'pos_diff': (-1, 0)},
    ('>', 'STRAIGHT'): {'new_direction': '>', 'pos_diff': (0, 1)},
    ('>', 'RIGHT'): {'new_direction': 'v', 'pos_diff': (1, 0)}
}

turn_events = {
    ('^', '/'): {'new_direction': '>', 'pos_diff': (0, 1)},
    ('^', '\\'): {'new_direction': '<', 'pos_diff': (0, -1)},
    ('v', '/'): {'new_direction': '<', 'pos_diff': (0, -1)},
    ('v', '\\'): {'new_direction': '>', 'pos_diff': (0, 1)},
    ('<', '/'): {'new_direction': 'v', 'pos_diff': (1, 0)},
    ('<', '\\'): {'new_direction': '^', 'pos_diff': (-1, 0)},
    ('>', '/'): {'new_direction': '^', 'pos_diff': (-1, 0)},
    ('>', '\\'): {'new_direction': 'v', 'pos_diff': (1, 0)},
    ('^', '|'): {'new_direction': '^', 'pos_diff': (-1, 0)},
    ('v', '|'): {'new_direction': 'v', 'pos_diff': (1, 0)},
    ('>', '-'): {'new_direction': '>', 'pos_diff': (0, 1)},
    ('<', '-'): {'new_direction': '<', 'pos_diff': (0, -1)},
}


def solve_part_1(cart_map, carts):
    while True:
        carts.sort(key=lambda x: x['pos'])
        for i, cart in enumerate(carts):
            pos = cart['pos']
            path = cart_map[pos]
            direction = cart['direction']
            turn = cart['next_turn']
            if path is '+':
                event = directions[(direction, turn)]
                turn = turns[turn]
            else:
                event = turn_events[(direction, path)]
            direction = event['new_direction']
            new_pos = event['pos_diff']
            pos = (pos[0] + new_pos[0], pos[1] + new_pos[1])
            carts[i] = {'next_turn': turn, 'pos': pos, 'direction': direction}
            current_locs = []
            for c in carts:
                if c['pos'] in current_locs:
                    return c['pos'][1], c['pos'][0]
                current_locs.append(c['pos'])


def solve_part_2(cart_map, carts):
    while True:
        carts.sort(key=lambda x: x['pos'])
        dead = []
        current_locs = []
        for i, cart in enumerate(carts):
            pos = cart['pos']
            if pos in current_locs:
                dead.append(pos)
                continue
            path = cart_map[pos]
            direction = cart['direction']
            turn = cart['next_turn']
            if path is '+':
                event = directions[(direction, turn)]
                turn = turns[turn]
            else:
                event = turn_events[(direction, path)]
            direction = event['new_direction']
            new_pos = event['pos_diff']
            pos = (pos[0] + new_pos[0], pos[1] + new_pos[1])
            carts[i] = {'next_turn': turn, 'pos': pos, 'direction': direction}
            if pos in current_locs:
                dead.append(carts[i]['pos'])
            else:
                current_locs.append(carts[i]['pos'])
        carts = [cart for cart in carts if cart['pos'] not in dead]
        if len(carts) is 1:
            return carts[0]['pos'][1], carts[0]['pos'][0]


def main():
    cart_map = {}
    carts = []
    m = []
    with open('input.txt') as f:
        for i, line in enumerate(f.readlines()):
            s = list(line)
            m.append(line.replace('\n', '').replace('^', '|').replace(
                'v', '|').replace('<', '-').replace('>', '-'))
            for j, c in enumerate(s):
                if c in ['>', '<']:
                    cart_map[(i, j)] = '-'
                    carts.append({
                        'pos': (i, j), 'direction': c, 'next_turn': 'LEFT'})
                elif c in ['^', 'v']:
                    cart_map[(i, j)] = '|'
                    carts.append({
                        'pos': (i, j), 'direction': c, 'next_turn': 'LEFT'})
                else:
                    cart_map[(i, j)] = c
    sol1 = solve_part_1(cart_map, [c for c in carts])
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2(cart_map, [c for c in carts])
    print('Part 2: {}'.format(sol2))
    # for r in m:
    #     print(r)


if __name__ == "__main__":
    main()
