import aocd
import re

data = aocd.get_data(day=4, year=2023)

total = 0

for line in data.splitlines():
	[winning, hand] = re.fullmatch(r'Card\s*[0-9]+:\s+((?:\s*[0-9]+)*)\s+\|\s+((?:\s*[0-9]+)*)', line).groups()
	winning = re.split(r'\s+', winning.strip())
	hand = re.split(r'\s+', hand.strip())

	winning_hand = [x for x in hand if x in winning]
	match_count = len(winning_hand)

	total += 2**(match_count - 1) if match_count > 0 else 0

print(total)
