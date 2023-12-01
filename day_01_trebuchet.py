import re


def part_1(data):
    digits = [[c for c in line if c.isdigit()] for line in data]
    return sum(int(d[0] + d[-1]) for d in digits)


def part_2(data):
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    values = {v: str(i) for i, v in enumerate(numbers, start=1)}
    pattern = re.compile(f"(?=(\d|{'|'.join(s for s in numbers)}))")
    digits = [pattern.findall(line) for line in data]
    return sum(int(values.get(d[0], d[0]) + values.get(d[-1], d[-1])) for d in digits)


if __name__ == "__main__":
    with open("day_01_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
