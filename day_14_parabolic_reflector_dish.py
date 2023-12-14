def part_1(data):
    answer = 0
    for column in zip(*data):
        next_position = len(column)
        for i, c in enumerate(column):
            if c == "O":
                answer += next_position
                next_position -= 1
            if c == "#":
                next_position = len(column) - 1 - i
    return answer


def part_2(data):
    cycles = dict()
    maps = dict()
    for cycle in range(1000000000):
        for _ in range(4):
            data = ["".join(line) for line in zip(*reversed(data))]
            for i, line in enumerate(data):
                next_position = 0
                new_line = ""
                for j, c in enumerate(reversed(line)):
                    if c == "O":
                        new_line += "O"
                        next_position += 1
                    elif c == "#":
                        new_line += "." * (j - next_position)
                        new_line += "#"
                        next_position = j + 1
                new_line += "." * (len(line) - next_position)
                data[i] = "".join(reversed(new_line))
        key = "\n".join(data)
        if key in cycles:
            start = cycles[key]
            period = cycle - cycles[key]
            answer_cycle = ((999999999 - start) % period) + start
            return sum(sum(len(column) - i for i, c in enumerate(column) if c == "O")
                       for column in zip(*maps[answer_cycle].splitlines()))
        cycles[key] = cycle
        maps[cycle] = key


if __name__ == "__main__":
    with open("day_14_input.txt", "r") as f:
        inp = f.read().splitlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
