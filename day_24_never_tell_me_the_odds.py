import re
import z3


def part_1(data):
    lines = [tuple(int(i) for i in re.findall(r"-?\d+", line)) for line in data]
    count = 0
    for i, (x0, y0, _, dx0, dy0, _) in enumerate(lines):
        for (x1, y1, _, dx1, dy1, _) in lines[i+1:]:
            a = dy0 / dx0
            b = dy1 / dx1
            if a == b: continue
            c = y0 - a * x0
            d = y1 - b * x1
            x = (d - c) / (a - b)
            y = a * ((d - c) / (a - b)) + c
            if (200000000000000 <= x <= 400000000000000 and 
                200000000000000 <= y <= 400000000000000 and
                (x - x0) / dx0 > 0 and (x - x1) / dx1 > 0):
                count += 1

    return count


def part_2(data):
    lines = [tuple(int(i) for i in re.findall(r"-?\d+", line)) for line in data]
    pxr, pyr, pzr, vxr, vyr, vzr = z3.Reals("pxr pyr pzr vxr vyr vzr")
    solver = z3.Solver()
    for k, (px, py, pz, vx, vy, vz) in enumerate(lines[:3]):
        tK = z3.Real(f"t{k}")
        solver.add(tK > 0)
        solver.add(pxr + tK * vxr == px + tK * vx)
        solver.add(pyr + tK * vyr == py + tK * vy)
        solver.add(pzr + tK * vzr == pz + tK * vz)
    solver.check()
    return sum(solver.model()[var].as_long() for var in [pxr, pyr, pzr])
    


if __name__ == "__main__":
    with open("day_24_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
