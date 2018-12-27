import regex as re
from itertools import chain


class Group:
    def __init__(self, army_name, n_units, hp, ap, dmg_type, initiative, weaknesses, immunities):
        self.army_name = army_name
        self.hp = int(hp)
        self.ap = int(ap)
        self.n_units = int(n_units)
        self.dmg_type = dmg_type
        self.initiative = int(initiative)
        self.weaknesses = weaknesses
        self.immunities = immunities
        self.target = None
        self.dead = False

    def __str__(self):
        return f'Army: {self.army_name}, HP: {self.hp}, AP: {self.ap}, Units: {self.n_units}, Dmg: {self.dmg_type}, Initative: {self.initiative}, Weaknesses: {self.weaknesses}, Immune: {self.immunities}, Targets: {1 if self.target else 0}'

    def copy(self, boost=0):
        return Group(self.army_name, self.n_units, self.hp, self.ap + boost, self.dmg_type, self.initiative, self.weaknesses, self.immunities)

    def ep(self):
        return self.ap * self.n_units

    def tot_hp(self):
        return self.hp * self.n_units

    def attack(self):
        if self.target:
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
            enemy_groups = [e for e in groups if e.army_name != g.army_name]
            if not enemy_groups:
                return sum([group.n_units for group in groups]), g.army_name
            friendly_groups = [f for f in groups if f.army_name == g.army_name]
            friendly_targets = [f.target for f in friendly_groups]
            possible_targets = [
                e for e in enemy_groups if e not in friendly_targets]
            g.set_target(possible_targets)
        groups.sort(key=lambda x: x.initiative, reverse=True)
        for g in groups:
            if g.dead:
                continue
            g.attack()
        groups = [g for g in groups if not g.dead]


def solve_part_1(groups):
    g = [group.copy() for group in groups]
    n_units, _ = fight(g)
    return n_units


def solve_part_2(groups):
    g = [group.copy() for group in groups]
    n_units, team = fight(g)
    boost = 52
    while team == 'Infection':
        g = [group.copy(boost * int(group.army_name != 'Infection'))
             for group in groups]
        n_units, team = fight(g)
        boost += 1
    return n_units, team


def main():
    groups = []
    with open('input.txt') as f:
        current_army = ''
        for line in f:
            l = line.strip()
            if not l:
                continue
            if l[-1] == ':':
                current_army = l[:-1]
            else:
                n_units, hp, ap, initiative = re.findall(r'-?\d+', l)
                s = re.search(r'\(.*\)', l)
                weaknesses = []
                immunities = []
                if s:
                    weaknesses = re.findall(
                        r'weak to (\w*)(, \w*)?', s.group(0))
                    immunities = re.findall(
                        r'immune to (\w*)(, \w*)?', s.group(0))
                    if weaknesses:
                        weaknesses = [w.replace(', ', '')
                                      for w in weaknesses[0] if w]
                    if immunities:
                        immunities = [w.replace(', ', '')
                                      for w in immunities[0] if w]
                dmg_type = re.findall(r'\d+ (\w+) damage', l)[0]
                groups.append(Group(current_army, n_units, hp, ap,
                                    dmg_type, initiative, weaknesses, immunities))
    sol1 = solve_part_1(groups)
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2(groups)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
