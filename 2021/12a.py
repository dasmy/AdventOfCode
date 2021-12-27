from collections import defaultdict


def find_paths(input):
    map = defaultdict(set)

    for edge in input.split('\n'):
        edge = edge.strip()
        if len(edge) != 0:
            n1, n2 = edge.split('-')
            for s, t in ((n1, n2), (n2, n1)):
                if t != 'start' and s != 'end':
                    map[s].add(t)

    def traverse(next, visited, route):
        this_route = route[:] + [next, ]

        if next == 'end':
            yield ','.join(this_route)

        this_visited = visited.union([next, ]) if next.islower() else visited

        for next_candidate in map[next].difference(visited):
            yield from traverse(next_candidate, this_visited, this_route)

    routes = [route for route in traverse(next='start', visited=set(), route=list())]
    print(f'Number of routes: {len(routes)}')


find_paths(
'''start-A
start-b
A-c
A-b
b-d
A-end
b-end
''')

find_paths(
'''dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc'''
)

find_paths(
'''fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW'''
)

find_paths(
'''QF-bw
end-ne
po-ju
QF-lo
po-start
XL-ne
bw-US
ne-lo
nu-ne
bw-po
QF-ne
ne-ju
start-lo
lo-XL
QF-ju
end-ju
XL-end
bw-ju
nu-start
lo-nu
nu-XL
xb-XL
XL-po'''
)
