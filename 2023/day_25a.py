import networkx as nx
import random
from day_25 import INPUT_TEST, INPUT


def day_02a(inp):
    G = nx.Graph()
    nodes = set()
    for line in inp.split('\n'):
        start, targets = line.split(': ')
        nodes.add(start)
        for target in targets.split(' '):
            G.add_edge(start, target, capacity=1.0)
            nodes.add(target)

    nodes = list(nodes)

    cut_value = None
    while cut_value != 3:
        n1, n2 = random.sample(nodes, k=2)

        cut_value, partition = nx.minimum_cut(G, n1, n2)

    reachable, non_reachable = partition

    return len(reachable) * len(non_reachable)


print(day_02a(INPUT_TEST))
print(day_02a(INPUT))
