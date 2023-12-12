import aocd
from enum import Enum


class Direction(Enum):
    NORTH = (-1, 0)
    SOUTH = (1, 0)
    EAST = (0, 1)
    WEST = (0, -1)


def get_available_directions(pipe: str) -> tuple[Direction, Direction]:
    if pipe == "|":
        return (Direction.NORTH, Direction.SOUTH)
    elif pipe == "-":
        return (Direction.EAST, Direction.WEST)
    elif pipe == "L":
        return (Direction.NORTH, Direction.EAST)
    elif pipe == "J":
        return (Direction.NORTH, Direction.WEST)
    elif pipe == "7":
        return (Direction.SOUTH, Direction.WEST)
    elif pipe == "F":
        return (Direction.SOUTH, Direction.EAST)


def move(pos: tuple[int, int], direction: Direction) -> tuple[int, int]:
    return (pos[0] + direction.value[0], pos[1] + direction.value[1])

def choose_direction(pos: tuple[int, int], prev_pos: tuple[int, int], directions: list[Direction]) -> Direction:
     for direction in directions:
        if move(pos, direction) != prev_pos:
            return direction

def at_pos(pos: tuple[int, int], data: list[str]) -> str:
    return data[pos[0]][pos[1]]


data = aocd.get_data(day=10, year=2023)
data = data.splitlines()

# Find the starting point
pos = (0, 0)
for x, line in enumerate(data):
	for y, char in enumerate(line):
		if char == "S":
			pos = (x, y)
			break

# Find the available directions
avail_dirs = []

if Direction.SOUTH in get_available_directions(at_pos(move(pos, Direction.NORTH), data)):
    avail_dirs.append(Direction.NORTH)
if Direction.WEST in get_available_directions(at_pos(move(pos, Direction.EAST), data)):
    avail_dirs.append(Direction.EAST)
if Direction.NORTH in get_available_directions(at_pos(move(pos, Direction.SOUTH), data)):
    avail_dirs.append(Direction.SOUTH)
if Direction.EAST in get_available_directions(at_pos(move(pos, Direction.WEST), data)):
    avail_dirs.append(Direction.WEST)

# Move to the first pipe
prev_pos = pos
pos = move(pos, avail_dirs[0])
dist = 1

# Move through the loop
while at_pos(pos, data) != 'S':
    ndir = choose_direction(pos, prev_pos, get_available_directions(at_pos(pos, data)))
    prev_pos = pos
    pos = move(pos, ndir)
    dist += 1

# Print the distance of the farthest pipe from the starting point
print(dist/2)
