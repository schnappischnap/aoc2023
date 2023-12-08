import itertools
import math
import re


def part_1(data):
    instructions, network = data.split("\n\n")
    nodes = dict()
    for line in network.splitlines():
        current, left, right = re.findall("(\w+)", line)
        nodes[current] = (left, right)
    
    current = "AAA"
    for i, instruction in enumerate(itertools.cycle(instructions)):
        current = nodes[current][0 if instruction == "L" else 1]
        if current == "ZZZ":
            return i


def part_2(data):
    instructions, network = data.split("\n\n")
    nodes = dict()
    for line in network.splitlines():
        current, left, right = re.findall("(\w+)", line)
        nodes[current] = (left, right)
    
    def solve(current):
        for i, instruction in enumerate(itertools.cycle(instructions)):
            current = nodes[current][0 if instruction == "L" else 1]
            if current.endswith("Z"):
                return i+1
    
    return math.lcm(*(solve(node) for node in nodes.keys() if node.endswith("A")))


if __name__ == "__main__":
    with open("day_08_input.txt", "r") as f:
        inp = f.read()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
