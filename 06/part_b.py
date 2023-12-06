import aocd
import re

data = aocd.get_data(day=6, year=2023)

lines = data.splitlines()

time = int(''.join(re.split(r"\s+", lines[0])[1:]))
record_distance = int(''.join(re.split(r"\s+", lines[1])[1:]))

# Iterative search for the bottom bound
min_time = 0
for i in range(time + 1):
    distance = (time - i) * i
    if distance > record_distance:
        min_time = i
        break

# Binary search for the top bound
bot = min_time
top = time + 1
while top - bot > 1:
	mid = (top + bot) // 2
	if (time - mid) * mid > record_distance:
		bot = mid
	else:
		top = mid
max_time = bot

print(max_time - min_time + 1)
