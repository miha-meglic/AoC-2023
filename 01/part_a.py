import aocd
import re

data = aocd.get_data(day=1, year=2023)

total = 0

for line in data.splitlines():
	digits = re.findall(r'\d', line)
	value = int(digits[0] + digits[-1])
	total += value

print(total)
