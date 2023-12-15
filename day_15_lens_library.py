from collections import defaultdict


def part_1(data):
    return sum(calculate_hash(step) for step in data.split(","))


def part_2(data):
    boxes = defaultdict(list)
    for step in data.split(","):
        if step.endswith("-"):
            label = step[:-1]
            box = calculate_hash(label)
            boxes[box] = [(a, b) for a, b in boxes[box] if a != label]
        else:
            label, lens = step.split("=")
            box = calculate_hash(label)
            for i, (a, _) in enumerate(boxes[box]):
                if a == label:
                    boxes[box][i] = (label, int(lens))
                    break
            else:
                boxes[box].append((label, int(lens)))
    
    return sum(sum((box+1) * (i+1) * lens for i, (_, lens) in enumerate(lenses)) 
               for box, lenses in boxes.items())


def calculate_hash(string):
    value = 0
    for c in string:
        value = (value + ord(c)) * 17 % 256
    return value


if __name__ == "__main__":
    with open("day_15_input.txt", "r") as f:
        inp = f.read()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
