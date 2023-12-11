import aocd
from functools import reduce


def calc_next_value(history: list[int]) -> int:
    diffs = [history]
    while reduce(lambda a, b: abs(a) + abs(b), diffs[-1]) > 0:
        diffs.append([y - x for x, y in zip(diffs[-1][:-1], diffs[-1][1:])])

    diffs[-1].append(0)
    for i in range(len(diffs) - 2, -1, -1):
        diffs[i].append(diffs[i][-1] + diffs[i + 1][-1])

    return diffs[0][-1]


data = aocd.get_data(day=9, year=2023)
total = 0

for line in data.splitlines():
    history = [int(x) for x in line.split(" ")]
    total += calc_next_value(history)

print(total)
