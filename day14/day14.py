def arr_to_str(a):
    return ''.join(map(str, a))


def solve_part_1(score):
    elf1 = 0
    elf2 = 1
    recipes = [3, 7]
    for _ in range(score + 10):
        new_recipe = recipes[elf1] + recipes[elf2]
        if new_recipe >= 10:
            recipes.append(new_recipe // 10)
        recipes.append(new_recipe % 10)
        elf1 = (1 + recipes[elf1] + elf1) % len(recipes)
        elf2 = (1 + recipes[elf2] + elf2) % len(recipes)
    return arr_to_str(recipes[-10:])


def solve_part_2(score):
    elf1 = 0
    elf2 = 1
    l = len(score)
    recipes = [3, 7]
    while True:
        new_recipe = recipes[elf1] + recipes[elf2]
        if new_recipe >= 10:
            recipes.append(new_recipe // 10)
            if arr_to_str(recipes[-l:]) == score:
                return len(recipes[:-l])
        recipes.append(new_recipe % 10)
        if arr_to_str(recipes[-l:]) == score:
            return len(recipes[:-l])
        elf1 = (1 + recipes[elf1] + elf1) % len(recipes)
        elf2 = (1 + recipes[elf2] + elf2) % len(recipes)


def main():
    with open('input.txt') as f:
        score = f.read()
    sol1 = solve_part_1(int(score))
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2(score)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
