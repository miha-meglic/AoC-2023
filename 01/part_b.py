# You need to explicitly install the regex module with pip
# This adds the `overlapped` flag to the findall method
import regex as re

digit_map = {
	'one': '1',
	'two': '2',
	'three': '3',
	'four': '4',
	'five': '5',
	'six': '6',
	'seven': '7',
	'eight': '8',
	'nine': '9'
}

total = 0

with open("input.txt", "r") as f:
	for line in f:
		digits = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)
		digits = list(map(lambda x: digit_map[x] if len(x) > 1 else x, digits))
		value = int(digits[0] + digits[-1])
		total += value

print(total) 
