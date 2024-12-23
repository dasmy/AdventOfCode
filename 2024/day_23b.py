from day_23inp import INPUT
from collections import defaultdict
from itertools import combinations
from functools import cache

connections = defaultdict(set)
for edge in INPUT.split("\n"):
    n1, n2 = edge.split("-")
    connections[n1].add(n2)
    connections[n2].add(n1)


@cache
def is_clique(c):
    for n1, n2 in combinations(c, r=2):
        if n2 not in connections[n1]:
            return False
    return True


max_clique = tuple([None])
for n, neighbors in connections.items():
    print(n)
    try:
        for r in reversed(range(len(max_clique), len(neighbors))):
            for c in combinations(neighbors, r=r):
                c = tuple(sorted([*c, n]))
                if is_clique(c):
                    assert len(c) > len(max_clique)
                    max_clique = c
                    print(len(c), c)
                    # continue with next n
                    raise StopIteration
    except StopIteration:
        pass

print(f"\nLargest Clique: {len(max_clique)}\n{','.join(max_clique)}")
