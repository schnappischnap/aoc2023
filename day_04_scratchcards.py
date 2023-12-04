from collections import defaultdict
import re


def part_1(data):
    scores = defaultdict(int)
    for line in data:
        numbers = re.findall(r"(\d+)", line)
        scores[line] = int(2 ** (sum(i in numbers[1:11] for i in numbers[11:]) - 1))
    return sum(scores.values())


def part_2(data):
    scratchcards = defaultdict(lambda: 1, ({i : 1 for i in range(len(data))}))
    for i, line in enumerate(data):
        numbers = re.findall(r"(\d+)", line)
        for k in range(sum(j in numbers[1:11] for j in numbers[11:])):
            scratchcards[i+k+1] += scratchcards[i]
    return sum(scratchcards.values())


if __name__ == "__main__":
    with open("day_04_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
