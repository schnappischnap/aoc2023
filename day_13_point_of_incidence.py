def part_1(data):
    answer = 0
    for pattern in data.split("\n\n"):
        pattern = pattern.splitlines()
        for j in [100, 1]:
            for i in range(1, len(pattern)):
                a, b = pattern[:i], pattern[i:]
                if all(c == d for c, d in zip(reversed(a), b)):
                    answer += j * i
            pattern = list(zip(*pattern))
    return answer


def part_2(data):
    answer = 0
    for pattern in data.split("\n\n"):
        pattern = pattern.splitlines()
        for j in [100, 1]:
            for i in range(1, len(pattern)):
                a, b = pattern[:i], pattern[i:]
                if sum(sum(e != f for e, f in zip(c, d)) for c, d in zip(reversed(a), b)) == 1:
                    answer += j * i
            pattern = list(zip(*pattern))
    return answer


if __name__ == "__main__":
    with open("day_13_input.txt", "r") as f:
        inp = f.read()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
