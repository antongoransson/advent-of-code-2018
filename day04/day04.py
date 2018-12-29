from collections import defaultdict
from datetime import datetime
import regex as re


def solve_part_1(schedule):
    sleeping_time = defaultdict(int)
    minutes_slept = defaultdict(lambda: defaultdict(int))
    guard_id = 0
    for i in range(len(schedule)):
        time, event = schedule[i]
        if 'falls asleep' in event:
            wakeup_time = schedule[i + 1][0]
            for j in range(time.minute, wakeup_time.minute):
                sleeping_time[guard_id] += 1
                minutes_slept[guard_id][j] += 1
        elif 'begins shift' in event:
            guard_id = int(re.findall(r'\d+', event)[0])
    g_id = max(sleeping_time, key=sleeping_time.get)
    m = max(minutes_slept[g_id], key=minutes_slept[g_id].get)
    return g_id * m, minutes_slept


def solve_part_2(minutes_slept):
    max_guard = 0
    current_max_minute = 0
    current_max_value = 0
    for guard_id, minutes in minutes_slept.items():
        max_minute = max(minutes, key=minutes.get)
        time = minutes[max_minute]
        if time > current_max_value:
            max_guard = guard_id
            current_max_minute = max_minute
            current_max_value = time
    return max_guard * current_max_minute


def main():
    with open('input.txt') as f:
        schedule = [
            (list(map(int, re.findall(r'\d+', c))), c.strip().split(']')[1]) for c in f]
    sorted_schedule = sorted([(datetime(date[0], date[1], date[2], date[3], date[4]), guard_id)
                              for date, guard_id in schedule])
    sol1, minutes_slept = solve_part_1(sorted_schedule)
    print('Part 1: {}'.format(sol1))
    sol2 = solve_part_2(minutes_slept)
    print('Part 2: {}'.format(sol2))


if __name__ == "__main__":
    main()
