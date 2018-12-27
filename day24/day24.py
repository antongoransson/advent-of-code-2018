import regex as re
from itertools import chain


class Group:
    def __init__(self, army, n_units, hp, ap, dmg_type, initiative, weaknesses, immunities):
        self.army = army
        self.hp = int(hp)
        self.ap = int(ap)
        self.n_units = int(n_units)
        self.dmg_type = dmg_type
        self.initiative = int(initiative)
        self.weaknesses = weaknesses
        self.immunities = immunities
        self.target = None
        self.dead = False

    def copy(self, boost=0):
        return Group(self.army, self.n_units, self.hp, self.ap + boost, self.dmg_type, self.initiative, self.weaknesses, self.immunities)

    def ep(self):
        return self.ap * self.n_units

    def attack(self):
        t = self.target
        dmg = self.effective_damage(t) // t.hp
        t.n_units -= dmg
        if t.n_units <= 0:
            t.dead = True
        self.target = None

    def set_target(self, possible_targets):
        if possible_targets:
            possible_targets.sort(key=lambda x: (
                self.effective_damage(x), x.ep(), x.initiative), reverse=True)
            t = possible_targets[0]
            if self.effective_damage(t) > 0:
                self.target = t
                return
        self.target = None

    def effective_damage(self, enemy):
        if self.dmg_type in enemy.immunities:
            return 0
        if self.dmg_type in enemy.weaknesses:
            return self.ep() * 2
        return self.ep()


def fight(groups):
    while True:
        groups.sort(key=lambda x: (x.ep(), x.initiative), reverse=True)
        for g in groups:
            enemy_groups = [e for e in groups if e.army != g.army]
            if not enemy_groups:
                return sum([group.n_units for group in groups]), g.army
            curr_targets = [f.target for f in groups if f.army == g.army]
            g.set_target([e for e in enemy_groups if e not in curr_targets])
        groups.sort(key=lambda x: x.initiative, reverse=True)
        n_attacks = 0
        for g in groups:
            if g.dead or not g.target:
                continue
            g.attack()
            n_attacks += 1
        if n_attacks == 0:
            return None, None
        groups = [g for g in groups if not g.dead]


def solve_part_1(groups):
    g = [group.copy() for group in groups]
    n_units, _ = fight(g)
    return n_units


def solve_part_2(groups):
    g = [group.copy() for group in groups]
    n_units, team = fight(g)
    boost = 0
    while team != 'Immune System':
        g = [group.copy(boost * int(group.army == 'Immune System'))
             for group in groups]
        n_units, team = fight(g)
        boost += 1
    return n_units


def main():
    groups = []
    with open('input.txt') as f:
        lines = [line.strip() for line in f if line.strip()]
    current_army = ''
    for l in lines:
        if l[-1] == ':':
            current_army = l[:-1]
            continue
        n_units, hp, ap, initiative = re.findall(r'-?\d+', l)
        s = re.search(r'\(.*\)', l)
        w, i = [], []
        if s:
            w = re.findall(
                r'weak to (\w*)(, \w*)?', s.group(0))
            i = re.findall(
                r'immune to (\w*)(, \w*)?', s.group(0))
            if w:
                w = [s.replace(', ', '') for s in w[0] if w]
            if i:
                i = [w.replace(', ', '') for w in i[0] if w]
        dmg_type = re.findall(r'\d+ (\w+) damage', l)[0]
        g = Group(current_army, n_units, hp, ap, dmg_type, initiative, w, i)
        groups.append(g)
    sol1 = solve_part_1(groups)
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2(groups)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
