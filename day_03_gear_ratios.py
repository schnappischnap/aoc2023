from collections import defaultdict
import math
import re


def part_1(data):
    parts = {(x, y) for y in range(len(data)) 
                    for x in range(len(data[y])) 
                    if data[y][x] not in "0123456789.\n"}
    part_sum = 0
    for y, line in enumerate(data):
        for re_match in re.finditer(r"(\d+)", line):
            neighbours = [(x + dx, y + dy) for dx in (-1, 0, 1)
                                           for dy in (-1, 0, 1)
                                           for x in range(*re_match.span())]
            if any(neighbour in parts for neighbour in neighbours):
                part_sum += int(re_match.group())
    return part_sum


def part_2(data):
    gears = {(x, y) for y in range(len(data)) 
                    for x in range(len(data[y])) 
                    if data[y][x] == "*"}
    gear_values = defaultdict(list)
    for y, line in enumerate(data):
        for re_match in re.finditer(r"(\d+)", line):
            neighbours = {(x + dx, y + dy) for dx in (-1, 0, 1)
                                           for dy in (-1, 0, 1)
                                           for x in range(*re_match.span())}
            for gear in neighbours & gears:
                gear_values[gear].append(int(re_match.group()))
    return sum(math.prod(v) for v in gear_values.values() if len(v) == 2)


if __name__ == "__main__":
    with open("day_03_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
