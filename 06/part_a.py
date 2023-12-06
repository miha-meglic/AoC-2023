import aocd
import re

data = aocd.get_data(day=6, year=2023)

lines = data.splitlines()

time_list = [int(t) for t in re.split(r"\s+", lines[0])[1:]]
distance_list = [int(d) for d in re.split(r"\s+", lines[1])[1:]]

td = list(zip(time_list, distance_list))

total = 1

for time, record_distance in td:
    ways = 0
    for i in range(time + 1):
        distance = (time - i) * i
        if distance > record_distance:
            ways += 1

    total *= ways

print(total)
