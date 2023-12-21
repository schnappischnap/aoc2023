def part_1(data):
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == "S":
                start = (x, y)
    size = len(data)
    queue = set([start])
    for _ in range(64):
        new_queue = set()
        for (x, y) in queue:
            for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= nx < size and 0 <= ny < size and data[ny][nx] != "#":
                    new_queue.add((nx, ny))
        queue = new_queue
        
    return len(queue)


def part_2(data):
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == "S":
                start = (x, y)
    size = len(data)  # = len(data[0])

    def bfs(step_target):
        queue = set([start])
        for _ in range(step_target):
            new_queue = set()
            for (x, y) in queue:
                for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if data[ny % size][nx % size] != "#":
                        new_queue.add((nx, ny))
            queue = new_queue
        return len(queue)

    values = [bfs(size//2 + size * i) for i in range(3)]
    a0 = values[0]
    a1 = values[1] - values[0]
    a2 = values[2] - values[1]
    b = 26501365 // size
    return a0 + a1 * b + (a2-a1) * (b * (b-1)//2)


if __name__ == "__main__":
    with open("day_21_input.txt", "r") as f:
        inp = f.read().splitlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
