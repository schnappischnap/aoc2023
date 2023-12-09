def part_1(data):
    def solve(values):
        new_values = [b - a for a, b in zip(values, values[1:])]
        if all(v == 0 for v in new_values):
            return values[-1]
        return values[-1] + solve(new_values)
    
    return sum(solve([int(i) for i in history.split()]) for history in data)


def part_2(data):
    def solve(values):
        new_values = [b - a for a, b in zip(values, values[1:])]
        if all(v == 0 for v in new_values):
            return values[0]
        return values[0] - solve(new_values)
    
    return sum(solve([int(i) for i in history.split()]) for history in data)


if __name__ == "__main__":
    with open("day_09_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
