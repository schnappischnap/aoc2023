def part_1(data):
    corners = [(0, 0)]
    for line in data:
        direction, length, _ = line.split()
        if direction == "R":
            corners.append((corners[-1][0] + int(length), corners[-1][1]))
        elif direction == "L":
            corners.append((corners[-1][0] - int(length), corners[-1][1]))
        elif direction == "D":
            corners.append((corners[-1][0], corners[-1][1] + int(length)))
        else:
            corners.append((corners[-1][0], corners[-1][1] - int(length)))

    area = sum(x1 * y2 - y1 * x2 for (x1, y1), (x2, y2) in zip(corners, corners[1:])) // 2  # Shoelace formula
    perimeter = sum(abs((x2 - x1) + (y2 - y1)) for (x1, y1), (x2, y2) in zip(corners, corners[1:]))
    return area + (perimeter // 2) + 1  # Pick's formula


def part_2(data):
    corners = [(0, 0)]
    for line in data:
        code = line.strip()[-7:-1]
        length = int(code[:5], 16)
        direction = int(code[-1])
        if direction == 0:
            corners.append((corners[-1][0] + length, corners[-1][1]))
        elif direction == 1:
            corners.append((corners[-1][0], corners[-1][1] + length))
        elif direction == 2:
            corners.append((corners[-1][0] - length, corners[-1][1]))
        else:
            corners.append((corners[-1][0], corners[-1][1] - length))

    area = sum(x1 * y2 - y1 * x2 for (x1, y1), (x2, y2) in zip(corners, corners[1:])) // 2  # Shoelace formula
    perimeter = sum(abs((x2 - x1) + (y2 - y1)) for (x1, y1), (x2, y2) in zip(corners, corners[1:]))
    return area + (perimeter // 2) + 1  # Pick's formula    


if __name__ == "__main__":
    with open("day_18_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
