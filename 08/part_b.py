import aocd
import re
from math import lcm


def get_steps(loc: str, moves: str, mapping: dict[str, tuple[str, str]]) -> int:
    """Returns the number of steps it takes to get from loc to a location ending in 'Z' for a "ghost"."""
    steps = 0
    while loc[2] != "Z":
        for move in moves:
            loc = mapping[loc][1 if move == "R" else 0]
            steps += 1

            if loc[2] == "Z":
                break
    return steps


data = aocd.get_data(day=8, year=2023)
data = data.splitlines()

mapping = {
    m.group(1): (m.group(2), m.group(3))
    for m in [re.match(r"(\w+) = \((\w+), (\w+)\)", line) for line in data[2:]]
}

# Get all locations that end with 'A'
locs = list(filter(lambda x: x[2] == "A", mapping.keys()))

# Calculate the number of steps it takes to get from each location to a location ending in 'Z'
jumps = [get_steps(loc, data[0], mapping) for loc in locs]

# Find the least common multiple of all the jumps
# AKA the number of steps it takes for all the ghosts to reach a location ending in 'Z' at the same time
print(lcm(*jumps))
