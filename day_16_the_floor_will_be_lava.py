def part_1(data):
    return get_energised_cells(-1, 0, 1, 0, data)


def part_2(data):
    h, w = len(data), len(data[0]) 
    return max([get_energised_cells(-1, y, 1, 0, data) for y in range(h)]
               + [get_energised_cells(w, y, -1, 0, data) for y in range(h)]
               + [get_energised_cells(x, -1, 0, 1, data) for x in range(w)]
               + [get_energised_cells(x, h, 0, -1, data) for x in range(w)])


def get_energised_cells(x, y, dx, dy, data):
    h, w = len(data), len(data[0]) 
    beams = [((x, y), (dx, dy))]
    visited = set()
    while beams:
        (x, y), (dx, dy) = beams.pop()
        
        x += dx
        y += dy
        if x < 0 or y < 0 or x >= w or y >= h:
            continue
        if ((x, y), (dx, dy)) in visited:
            continue
        
        visited.add(((x, y), (dx, dy)))
         
        if data[y][x] == "-" and dy != 0:
            beams.append(((x, y), (-1, 0)))
            beams.append(((x, y), (1, 0)))
        elif data[y][x] == "|" and dx != 0:
            beams.append(((x, y), (0, -1)))
            beams.append(((x, y), (0, 1)))
        elif data[y][x] == "/":
            beams.append(((x, y), (-dy, -dx)))
        elif data[y][x] == "\\":
            beams.append(((x, y), (dy, dx)))
        else:
            beams.append(((x, y), (dx, dy)))
    
    return len(set(v[0] for v in visited))


if __name__ == "__main__":
    with open("day_16_input.txt", "r") as f:
        inp = f.read().splitlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
