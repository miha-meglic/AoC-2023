// Puzzle input should be piped in via stdin.
// 	Example: cat input.txt | dotnet run
// 	Example: aocd 11 2023 | dotnet run
//
// args[0]: Part number (1 or 2)
// 		By default, both parts will be run.

int? part = null;

if (args.Length > 0)
	part = int.Parse(args[0]);

List<List<string>> input = new List<List<string>>();

string? line;
while ((line = Console.ReadLine()) != null) {
	input.Add(line.ToCharArray().Select(c => c.ToString()).ToList());
}

switch (part) {
	case 1:
		Console.Write("Part 1: ");
		Part1(input);
		break;
	case 2:
		Console.Write("Part 2: ");
		Part2(input);
		break;
	default:
		Console.Write("Part 1: ");
		Part1(input);
		Console.Write("Part 2: ");
		Part2(input);
		break;
}

static void Part1(List<List<string>> input) {
	Console.WriteLine(CalculateExpandedDistanceSum(input, 2));
}

static void Part2(List<List<string>> input) {
	Console.WriteLine(CalculateExpandedDistanceSum(input, 1000000));
}

static List<List<string>> Transpose2DList(List<List<string>> input) {
	return input
		.SelectMany(inner => inner.Select((item, index) => new { item, index }))
		.GroupBy(i => i.index, i => i.item)
		.Select(g => g.ToList())
		.ToList();
}

static (List<int>, List<int>) CalculateExpandedIndexes(List<List<string>> input, int expansion) {
	expansion = expansion - 1;

	// Calculate vertical expansion
	List<int> yCorrected = new List<int>();
	if (input[0].Contains("#"))
		yCorrected.Add(0);
	else
		yCorrected.Add(expansion);

	for (int i = 1; i < input.Count; i++) {
		if (input[i].Contains("#")) {
			yCorrected.Add(yCorrected[i - 1] + 1);
		} else {
			yCorrected.Add(yCorrected[i - 1] + 1 + expansion);
		}
	}

	// Calculate horizontal expansion
	input = Transpose2DList(input);

	List<int> xCorrected = new List<int>();
	if (input[0].Contains("#"))
		xCorrected.Add(0);
	else
		xCorrected.Add(expansion);

	for (int i = 1; i < input.Count; i++) {
		if (input[i].Contains("#")) {
			xCorrected.Add(xCorrected[i - 1] + 1);
		} else {
			xCorrected.Add(xCorrected[i - 1] + 1 + expansion);
		}
	}

	return (xCorrected, yCorrected);
}

static int TaxicabDistance((int, int) a, (int, int) b) {
	return Math.Abs(a.Item1 - b.Item1) + Math.Abs(a.Item2 - b.Item2);
}

static long CalculateExpandedDistanceSum(List<List<string>> input, int expansion) {
	var (xExp, yExp) = CalculateExpandedIndexes(input, expansion);

	List<(int, int)> galaxies = new List<(int, int)>();

	for (int y = 0; y < input.Count; y++) {
		for (int x = 0; x < input[y].Count; x++) {
			if (input[y][x] == "#") {
				galaxies.Add((xExp[x], yExp[y]));
			}
		}
	}

	long distanceSum = 0;

	for (int i = 0; i < galaxies.Count; i++) {
		for (int j = i + 1; j < galaxies.Count; j++) {
			distanceSum += TaxicabDistance(galaxies[i], galaxies[j]);
		}
	}

	return distanceSum;
}
