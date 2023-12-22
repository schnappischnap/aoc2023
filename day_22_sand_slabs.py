from collections import defaultdict
import re


def part_1(data):
    bricks = []
    for line in data:
        values = tuple(int(i) for i in re.findall(r"\d+", line))
        bricks.append((values[0:3], values[3:6]))
    
    do_not_disintegrate = set()
    highest = defaultdict(lambda: (0, None))  # z coordinate, brick
    for brick in sorted(bricks, key=lambda b: b[0][2]):
        max_height = 0
        supported_by = set()
        (x0, y0, z0), (x1, y1, z1) = brick
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                z, supporting_brick = highest[(x, y)]
                if z > max_height:
                    max_height = z
                    supported_by = {supporting_brick}
                elif z == max_height:
                    supported_by.add(supporting_brick)
        if len(supported_by) == 1:
            do_not_disintegrate.update(supported_by)
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                highest[(x, y)] = (max_height + (z1 - z0) + 1, brick)
    
    return len(bricks) - len(do_not_disintegrate) + 1


def part_2(data):
    bricks = []
    for line in data:
        values = tuple(int(i) for i in re.findall(r"\d+", line))
        bricks.append((values[0:3], values[3:6]))
    
    graph = defaultdict(list)
    highest = defaultdict(lambda: (0, None))  # z coordinate, brick
    for brick in sorted(bricks, key=lambda b: b[0][2]):
        max_height = 0
        supported_by = set()
        (x0, y0, z0), (x1, y1, z1) = brick
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                z, supporting_brick = highest[(x, y)]
                if z > max_height:
                    max_height = z
                    supported_by = {supporting_brick}
                elif z == max_height:
                    supported_by.add(supporting_brick)
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                highest[(x, y)] = (max_height + (z1 - z0) + 1, brick)
        for supporting_brick in supported_by:
            if supporting_brick:
                graph[supporting_brick].append(brick)

    def count_falls(start):
        supports_count = defaultdict(int)
        for brick in graph:
            for other in graph[brick]:
                supports_count[other] += 1
        count = 0
        queue = [start]
        while queue:
            brick = queue.pop()
            for other in graph[brick]:
                supports_count[other] -= 1
                if supports_count[other] == 0:
                    queue.append(other)
                    count += 1
        return count
    
    return(sum(count_falls(brick) for brick in bricks))


if __name__ == "__main__":
    with open("day_22_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
