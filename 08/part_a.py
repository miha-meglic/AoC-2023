import aocd
import re

data = aocd.get_data(day=8, year=2023)
data = data.splitlines()

mapping = {
    m.group(1): (m.group(2), m.group(3))
    for m in [re.match(r"(\w+) = \((\w+), (\w+)\)", line) for line in data[2:]]
}

loc = "AAA"
jumps = 0

while loc != "ZZZ":
    for move in data[0]:
        loc = mapping[loc][1 if move == "R" else 0]
        jumps += 1

        if loc == "ZZZ":
            break

print(jumps)
