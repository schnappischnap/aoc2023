from collections import defaultdict
import math
import re


def part_1(data):
    pattern = re.compile(r"(\d+) (\w+)")
    maximum = {"red": 12, "green": 13, "blue": 14}
    return sum(i for i, line in enumerate(data, start=1)
               if not any(int(count) > maximum[colour] for count, colour in pattern.findall(line)))


def part_2(data):
    pattern = re.compile(r"(\d+) (\w+)")
    power_sum = 0
    for line in data:
        maximum = defaultdict(int)
        for count, colour in pattern.findall(line):
            maximum[colour] = max(int(count), maximum[colour])
        power_sum += math.prod(maximum.values())
    return power_sum


if __name__ == "__main__":
    with open("day_02_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
