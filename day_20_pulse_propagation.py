import math


def part_1(data):
    connections = dict()
    states = dict()
    for line in data:
        module, links = line.split(" -> ")
        module_name = "broadcaster" if module == "broadcaster" else module[1:]
        if module.startswith("%"):
            states[module[1:]] = False
        elif module.startswith("&"):
            states[module[1:]] = dict()
        connections[module_name] = list(links.split(", "))

    for module, links in connections.items():
        for link in links:
            if isinstance(states.get(link, None), dict):
                states[link][module] = False
    
    pulses = [0, 0]
    for _ in range(1000):
        queue = [("broadcaster", "button", False)]
        while queue:
            module, source, high_pulse = queue.pop(0)
            pulses[high_pulse] += 1
            if module == "broadcaster":
                queue += [(m, module, False) for m in connections[module]]
            elif isinstance(states.get(module, None), bool) and not high_pulse:
                states[module] = not states[module]
                queue += [(m, module, states[module]) for m in connections[module]]
            elif isinstance(states.get(module, None), dict):
                states[module][source] = high_pulse
                all_high = all(v == True for v in states[module].values())
                queue += [(m, module, not all_high) for m in connections[module]]

    return pulses[0] * pulses[1]


def part_2(data):
    connections = dict()
    states = dict()
    for line in data:
        module, links = line.split(" -> ")
        module_name = "broadcaster" if module == "broadcaster" else module[1:]
        if module.startswith("%"):
            states[module[1:]] = False
        elif module.startswith("&"):
            states[module[1:]] = dict()
        connections[module_name] = list(links.split(", "))

    for module, links in connections.items():
        for link in links:
            if isinstance(states.get(link, None), dict):
                states[link][module] = False
    
    sub_cycles = {m: None for m in states["gf"]}
    for i in range(1, 100000000000000):
        queue = [("broadcaster", "button", False)]
        while queue:
            module, source, high_pulse = queue.pop(0)
            
            if module == "broadcaster":
                queue += [(m, module, False) for m in connections[module]]
            elif isinstance(states.get(module, None), bool) and not high_pulse:
                states[module] = not states[module]
                queue += [(m, module, states[module]) for m in connections[module]]
            elif isinstance(states.get(module, None), dict):
                states[module][source] = high_pulse
                all_high = all(v == True for v in states[module].values())
                queue += [(m, module, not all_high) for m in connections[module]]
            
                if module in states["gf"] and not all_high:
                    sub_cycles[module] = i
                    if all(m != None for m in sub_cycles.values()):
                        return math.lcm(*sub_cycles.values())


if __name__ == "__main__":
    with open("day_20_input.txt", "r") as f:
        inp = f.read().splitlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
