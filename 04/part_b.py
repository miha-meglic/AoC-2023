import aocd
import re

data = aocd.get_data(day=4, year=2023)

matches = dict()
copies = dict()

for i, line in enumerate(data.splitlines()):
	[winning, hand] = re.fullmatch(r'Card\s*[0-9]+:\s+((?:\s*[0-9]+)*)\s+\|\s+((?:\s*[0-9]+)*)', line).groups()
	winning = re.split(r'\s+', winning.strip())
	hand = re.split(r'\s+', hand.strip())

	winning_hand = [x for x in hand if x in winning]
	matches[i] = len(winning_hand)
	copies[i] = 1

for i in range(len(matches)):
	for j in range(i + 1, i + 1 + matches[i]):
		copies[j] += copies[i]

print(sum(copies.values()))
