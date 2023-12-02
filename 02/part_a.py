import aocd

limit = {
	"red": 12,
	"green": 13,
	"blue": 14
}

data = aocd.get_data(day=2, year=2023)

game_sum = 0

for line in data.splitlines():
	[game, game_data] = line.split(':')
	game = int(game[5:])
	turns = game_data.split(';')

	game_possible = True

	for turn in turns:
		cubes = turn.split(',')
		for cube in cubes:
			[_, count, color] = cube.split(' ')
			if int(count) > limit[color]:
				game_possible = False
				break
		else:
			continue
		break

	if game_possible:
		game_sum += game

print(game_sum)
