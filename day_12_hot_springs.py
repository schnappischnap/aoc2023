import functools


def part_1(data):
    total = 0
    for line in data:
        left, right = line.split()
        counts = tuple(int(i) for i in right.split(","))
        total += count_combinations(left, counts)
    return total


def part_2(data):
    total = 0
    for line in data:
        left, right = line.split()
        springs = "?".join([left] * 5)
        counts = tuple(int(i) for i in right.split(",")) * 5
        total += count_combinations(springs, counts)
    return total


@functools.lru_cache
def count_combinations(springs, counts):
    if not springs:
        return 1 if not counts else 0
    match springs[0]:
        case ".":
            return count_combinations(springs.strip("."), counts)
        case "?":
            return count_combinations(springs.replace("?", "#", 1), counts)\
                   + count_combinations(springs.replace("?", ".", 1), counts)
        case "#":
            if not counts:
                return 0
            if len(springs) < counts[0]:
                return 0
            if any(c == "." for c in springs[:counts[0]]):
                return 0
            if len(counts) > 1:
                if len(springs) < counts[0] + 1 or springs[counts[0]] == "#":
                    return 0
                return count_combinations(springs[counts[0] + 1:], counts[1:])
            return count_combinations(springs[counts[0]:], counts[1:])


if __name__ == "__main__":
    with open("day_12_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
