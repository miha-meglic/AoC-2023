import re

total = 0

with open("input.txt", "r") as f:
	for line in f:
		digits = re.findall(r'\d', line)
		value = int(digits[0] + digits[-1])
		total += value

print(total)
