import itertools


def part_1(data):
    empty_rows = [i for i, line in enumerate(data) if all(c == "." for c in line.strip())]
    empty_cols = [i for i, line in enumerate(zip(*data)) if all(c == "." for c in line)]
    galaxies = [(x + sum(x > i for i in empty_cols), y + sum(y > j for j in empty_rows))
                for y, line in enumerate(data)
                for x, c in enumerate(line) if c == "#"]
    return sum(abs(a[0] - b[0]) + abs(a[1] - b[1]) for a, b in itertools.combinations(galaxies, 2))


def part_2(data):
    empty_rows = [i for i, line in enumerate(data) if all(c == "." for c in line.strip())]
    empty_cols = [i for i, line in enumerate(zip(*data)) if all(c == "." for c in line)]
    galaxies = [(x + 999999 * sum(x > i for i in empty_cols), y + 999999 * sum(y > j for j in empty_rows)) 
                for y, line in enumerate(data) 
                for x, c in enumerate(line) if c == "#"]
    return sum(abs(a[0] - b[0]) + abs(a[1] - b[1]) for a, b in itertools.combinations(galaxies, 2))


if __name__ == "__main__":
    with open("day_11_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
