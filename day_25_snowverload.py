import math
import networkx as nx
import re


def part_1(data):
    G = nx.Graph()
    for line in data:
        node, *others = re.findall(r"\w+", line)
        G.add_edges_from((node, other) for other in others)
    G.remove_edges_from(nx.minimum_edge_cut(G))
    return math.prod(len(c) for c in nx.connected_components(G))


if __name__ == "__main__":
    with open("day_25_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
