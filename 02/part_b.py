import aocd

data = aocd.get_data(day=2, year=2023)

game_power_sum = 0

for line in data.splitlines():
	[_, game_data] = line.split(':')
	turns = game_data.split(';')

	min_required = {
		"red": 0,
		"green": 0,
		"blue": 0
	}

	for turn in turns:
		cubes = turn.split(',')
		for cube in cubes:
			[_, count, color] = cube.split(' ')
			if int(count) > min_required[color]:
				min_required[color] = int(count)

	game_power = min_required["red"] * min_required["green"] * min_required["blue"]
	game_power_sum += game_power

print(game_power_sum)
