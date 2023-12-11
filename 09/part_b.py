import aocd
from functools import reduce


def calc_prev_value(history: list[int]) -> int:
    diffs = [history]
    while reduce(lambda a, b: abs(a) + abs(b), diffs[-1]) > 0:
        diffs.append([y - x for x, y in zip(diffs[-1][:-1], diffs[-1][1:])])

    diffs[-1].insert(0, 0)
    for i in range(len(diffs) - 2, -1, -1):
        diffs[i].insert(0, diffs[i][0] - diffs[i + 1][0])

    return diffs[0][0]


data = aocd.get_data(day=9, year=2023)
total = 0

for line in data.splitlines():
    history = [int(x) for x in line.split(" ")]
    total += calc_prev_value(history)

print(total)
