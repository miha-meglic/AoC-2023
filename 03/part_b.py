import aocd
import re

data = aocd.get_data(day=3, year=2023)

lines = data.splitlines()

prev_line_nums = []
line_nums = []
next_line_nums = [(int(m.group(0)), range(m.start(0), m.end(0))) for m in re.finditer(r'\d+', lines[0])]

total = 0

for i, line in enumerate(lines):
	prev_line_nums = line_nums
	line_nums = next_line_nums
	next_line_nums = [(int(m.group(0)), range(m.start(0), m.end(0))) for m in re.finditer(r'\d+', lines[i + 1])] if i + 1 < len(lines) else []

	star_ranges = [range(m.start(0)-1, m.end(0)+1) for m in re.finditer(r'\*', line)]
	nums = prev_line_nums + line_nums + next_line_nums

	for s_range in star_ranges:
		count = 0
		temp_mul = 1
		
		for num in nums:
			for j in s_range:
				if j in num[1]:
					count += 1
					temp_mul *= num[0]
					break
		
		if count == 2:
			total += temp_mul

print(total)
