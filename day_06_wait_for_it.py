import math


def part_1(data):
    return math.prod(sum(i * (time - i) > distance for i in range(time))
                     for time, distance in zip((int(j) for j in data[0].split()[1:]),
                                               (int(j) for j in data[1].split()[1:])))


def part_2(data):
    time = int(data[0].replace(" ", "").split(":")[1])
    distance = int(data[1].replace(" ", "").split(":")[1])
    return sum(i * (time - i) > distance for i in range(time))


if __name__ == "__main__":
    with open("day_06_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
