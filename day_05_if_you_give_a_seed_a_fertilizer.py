def part_1(data):
    seeds = [int(s) for s in data[0].split()[1:]]
    for chunk in data[1:]:
        converted = []
        for seed in seeds:
            for conversion in chunk.split("\n")[1:]:
                d_start, s_start, length = (int(s) for s in conversion.split())
                if s_start <= seed <= s_start + length:
                    converted.append(d_start + (seed - s_start))
                    break
            else:
                converted.append(seed)
        seeds = converted
    return min(seeds)


def part_2(data):
    seeds = [int(s) for s in data[0].split()[1:]]
    seed_ranges = [(seeds[i], seeds[i] + seeds[i+1] - 1) for i in range(0, len(seeds), 2)]
    for chunk in data[1:]:
        new_ranges = []
        for seed_range in seed_ranges:
            unprocessed = [seed_range]
            for conversion in chunk.split("\n")[1:]:
                new_unprocessed = []
                for (a, b) in unprocessed:
                    d_start, c, length = (int(s) for s in conversion.split())
                    d = c + length - 1
                    offset = d_start - c

                    to_process = []
                    extras = []
                    if a < c and d < b:
                        to_process = [(c, d)]
                        extras = [(a, c-1), (d+1, b)]
                    elif a < c <= b:
                        to_process = [(c, b)]
                        extras = [(a, c-1)]
                    elif a <= d < b:
                        to_process = [(a, d)]
                        extras = [(d+1, b)]
                    elif c <= a and b <= d:
                        to_process = [(a, b)]
                    else:
                        extras = [(a, b)]
                    
                    new_unprocessed += extras
                    new_ranges += [(a + offset, b + offset) for a, b in to_process]
                unprocessed = new_unprocessed
            new_ranges += unprocessed
        seed_ranges = new_ranges
    
    return min(x for x, _ in seed_ranges)


if __name__ == "__main__":
    with open("day_05_input.txt", "r") as f:
        inp = f.read().split("\n\n")
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))