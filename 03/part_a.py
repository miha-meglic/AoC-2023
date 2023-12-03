import aocd
import re

data = aocd.get_data(day=3, year=2023)

lines = data.splitlines()

prev_line_symbols = []
line_symbols = []
next_line_symbols = [m.start(0) for m in re.finditer(r'[^\w.]', lines[0])]

total = 0

for i, line in enumerate(lines):
	prev_line_symbols = line_symbols
	line_symbols = next_line_symbols
	next_line_symbols = [m.start(0) for m in re.finditer(r'[^\w.]', lines[i + 1])] if i + 1 < len(lines) else []

	nums = [int(s) for s in re.findall(r'\d+', line)]
	nums_ranges = [range(m.start(0)-1, m.end(0)+1) for m in re.finditer(r'\d+', line)]

	for j, num in enumerate(nums):
		valid = False
		for k in nums_ranges[j]:
			if k in prev_line_symbols or k in line_symbols or k in next_line_symbols:
				valid = True
				break

		if valid:
			total += num

print(total)
