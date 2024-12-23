from day_23inp import INPUT
from collections import defaultdict
from itertools import combinations

connections = defaultdict(set)
for edge in INPUT.split("\n"):
    n1, n2 = edge.split("-")
    connections[n1].add(n2)
    connections[n2].add(n1)

rings = set()
for n, neighbors in connections.items():
    for n1, n2 in combinations(neighbors, r=2):
        if n2 in connections[n1]:
            if n.startswith("t") or n1.startswith("t") or n2.startswith("t"):
                rings.add(tuple(sorted([n, n1, n2])))

print(len(rings))
