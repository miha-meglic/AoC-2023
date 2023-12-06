import aocd

def make_map(input: list[str]) -> dict[range, int]:
	"""Make a map of the input."""
	m = dict()
	for line in input:
		[dst, src, rng] = line.split(" ")
		dst, src, rng = int(dst), int(src), int(rng)

		diff = dst - src
		m[range(src, src+rng)] = diff
	return m

data = aocd.get_data(day=5, year=2023)

lines = data.splitlines()

seeds = [int(s) for s in lines[0].split(" ")[1:]]

i0 = 3
i1 = lines.index("", i0)

while True:
	mapping = make_map(lines[i0:i1])

	new_seeds = []
	processed = []
	for seed in seeds:
		for rng in mapping:
			if seed in rng:
				processed.append(seed)
				new_seeds.append(seed + mapping[rng])
				break
	
	not_mapped = [s for s in seeds if s not in processed]
	seeds = new_seeds + not_mapped

	i0 = i1 + 2
	if i0 >= len(lines):
		break
	try:
		i1 = lines.index("", i0)
	except ValueError:
		i1 = len(lines)

print(min(seeds))
