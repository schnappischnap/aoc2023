from collections import defaultdict


def part_1(data):
    slopes = {">": (1, 0), "<": (-1, 0), "v": (0, 1), "^": (0, -1)}
    w, h = len(data[0]), len(data)

    def dfs(start, target):
        stack = [(start[0], start[1], set(), 0)]
        paths = []
        while stack:
            x, y, visited, steps = stack.pop()
            if delta := slopes.get(data[y][x], False):
                nx, ny = (x + delta[0], y + delta[1])
                if (nx, ny) not in visited:
                    if (nx, ny) == target:
                        paths.append(steps + 1)
                    stack.append((nx, ny, visited | {(nx, ny)}, steps + 1))
            else:
                for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                    if 0 <= nx < w and 0 <= ny < h and data[y][x] != "#" and (nx, ny) not in visited:
                        if delta := slopes.get(data[ny][nx], False) and (x - nx, y - ny) == delta:
                            continue
                        if (nx, ny) == target:
                            paths.append(steps + 1)
                        stack.append((nx, ny, visited | {(nx, ny)}, steps + 1))
        return paths
    
    return max(path for path in dfs((data[0].index("."), 0), (data[-1].index("."), len(data) - 1)))


def part_2(data):
    w, h = len(data[0]), len(data)

    graph = defaultdict(list)
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == "#": continue
            for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0 <= nx < w and 0 <= ny < h and data[ny][nx] != "#":
                    graph[(x, y)].append((nx, ny, 1))

    while True:
        for (x0, y0), edges in graph.items():
            if len(edges) == 2:
                (x1, y1, l1), (x2, y2, l2) = edges
                graph[(x1, y1)].remove((x0, y0, l1))
                graph[(x2, y2)].remove((x0, y0, l2))
                graph[(x1, y1)].append((x2, y2, l1 + l2))
                graph[(x2, y2)].append((x1, y1, l1 + l2))
                del graph[(x0, y0)]
                break
        else:
            break

    def dfs(start, target):
        stack = [(start[0], start[1], set(), 0)]
        paths = []
        while stack:
            x, y, visited, steps = stack.pop()
            for nx, ny, length in graph[(x, y)]:
                if (nx, ny) not in visited:
                    if (nx, ny) == target:
                        paths.append(steps + length)
                    stack.append((nx, ny, visited | {(nx, ny)}, steps + length))
        return paths
    
    return max(path for path in dfs((data[0].index("."), 0), (data[-1].index("."), len(data) - 1)))


if __name__ == "__main__":
    with open("day_23_input.txt", "r") as f:
        inp = f.read().splitlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
