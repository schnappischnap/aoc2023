from heapq import heappush, heappop
import math


def part_1(data):
    h, w = len(data), len(data[0])
    start = ((0, 0), (1, 0), 0)  # ((x, y), (dx, dy), straight line count)
    distances = {start: 0}
    queue = [(0, start)]
    visited = set()

    while queue:
        _, node = heappop(queue)
        if node[0] == (w-1, h-1):
            return distances[node]
        visited.add(node)
        (x, y), (dx, dy), count = node

        for new_node in neighbours(x, y, dx, dy, count):
            nx, ny = new_node[0]
            if 0 <= nx < w and 0 <= ny < h and new_node not in visited:
                new_distance = distances[node] + int(data[ny][nx])
                if new_distance < distances.get(new_node, math.inf):
                    distances[new_node] = new_distance
                    heappush(queue, (new_distance, new_node))


def part_2(data):
    h, w = len(data), len(data[0])
    start = ((0, 0), (1, 0), 0)  # ((x, y), (dx, dy), straight line count)
    distances = {start: 0}
    queue = [(0, start)]
    visited = set()

    while queue:
        _, node = heappop(queue)
        if node[0] == (w-1, h-1) and node[2] >= 4:
            return distances[node]
        visited.add(node)
        (x, y), (dx, dy), count = node

        for new_node in neighbours(x, y, dx, dy, count, True):
            nx, ny = new_node[0]
            if 0 <= nx < w and 0 <= ny < h and new_node not in visited:
                new_distance = distances[node] + int(data[ny][nx])
                if new_distance < distances.get(new_node, math.inf):
                    distances[new_node] = new_distance
                    heappush(queue, (new_distance, new_node))


def neighbours(x, y, dx, dy, count, ultra=False):
    if not ultra or count >= 4:
        yield ((x - dy, y + dx), (-dy, dx), 1)
        yield ((x + dy, y - dx), (dy, -dx), 1)
    if count < (10 if ultra else 3):
        yield ((x + dx, y + dy), (dx, dy), count+1)


if __name__ == "__main__":
    with open("day_17_input.txt", "r") as f:
        inp = f.read().splitlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
