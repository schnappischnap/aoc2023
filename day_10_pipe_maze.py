def part_1(data):
    deltas = {"|": {(0, -1): (0, -1), (0, 1): (0, 1)},
              "-": {(1, 0): (1, 0), (-1, 0): (-1, 0)},
              "7": {(1, 0): (0, 1), (0, -1): (-1, 0)},
              "L": {(0, 1): (1, 0), (-1, 0): (0, -1)},
              "F": {(-1, 0): (0, 1), (0, -1): (1, 0)},
              "J": {(0, 1): (-1, 0), (1, 0): (0, -1)}}

    start = (-1, -1)
    for i, line in enumerate(data):
        if "S" in line:
            start = (line.index("S"), i)
            break

    dx, dy = 0, 1
    x, y = start[0] + dx, start[1] + dy

    steps = 1
    while (x, y) != start:
        pipe = data[y][x]
        dx, dy = deltas[pipe][(dx, dy)]
        x += dx
        y += dy
        steps += 1

    return steps // 2


def part_2(data):
    deltas = {"|": {(0, -1): (0, -1), (0, 1): (0, 1)},
              "-": {(1, 0): (1, 0), (-1, 0): (-1, 0)},
              "7": {(1, 0): (0, 1), (0, -1): (-1, 0)},
              "L": {(0, 1): (1, 0), (-1, 0): (0, -1)},
              "F": {(-1, 0): (0, 1), (0, -1): (1, 0)},
              "J": {(0, 1): (-1, 0), (1, 0): (0, -1)}}

    start = (-1, -1)
    for i, line in enumerate(data):
        if "S" in line:
            start = (line.index("S"), i)
            break

    dx, dy = 0, 1
    x, y = start[0] + dx, start[1] + dy

    pipe = set([(x, y)])
    while (x, y) != start:
        pipe_section = data[y][x]
        dx, dy = deltas[pipe_section][(dx, dy)]
        x += dx
        y += dy
        pipe.add((x, y))

    count = 0
    for y, line in enumerate(data):
        norths = 0
        for x, pipe_section in enumerate(line):
            if (x, y) in pipe:
                if data[y][x] in "S|LJ":
                    norths += 1
                continue
            count += norths % 2 == 1

    return count


if __name__ == "__main__":
    with open("day_10_input.txt", "r") as f:
        inp = f.read().splitlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
