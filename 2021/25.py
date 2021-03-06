import numpy as np
from itertools import count


def print_field(f):
    cucumber = ['.', '>', 'v']
    for r in f:
        print(''.join(cucumber[c] for c in r))


def simulate(input):
    field = []
    cucumber = {'.': 0, '>': 1, 'v': 2}
    for line in input.split('\n'):
        field.append([cucumber[c] for c in line])

    field = np.asarray(field)
    c_east = field == 1
    c_south = field == 2

    def move(c, axis, other):
        # move forward where possible
        moved = np.logical_and(np.roll(c, 1, axis), np.logical_not(np.logical_or(c, other)))
        # erase all that have been moved from their old position
        c = np.logical_and(c, np.logical_not(np.roll(moved, -1, axis)))
        # return those who moved and those who did not move
        return np.logical_or(c, moved)

    for step in count(1):
        print(step)
        print_field(field)
        assert not np.any(np.logical_and(c_east, c_south))
        c_east = move(c_east, 1, c_south)
        c_south = move(c_south, 0, c_east)

        field_new = 1*c_east + 2*c_south
        if np.all(field_new == field):
            break

        field = field_new

    print(f'Static after {step} steps')


simulate(
    '''v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>'''
)

simulate(
    '''v>.v.>.v..>...v..v>>>.v..>.>>vvv.v>..v.v...>v...v.v>>.>.v.>.>.vv.>v..>vv>.v>>>>.>...>.>>v..v>>vvv.v......v..>v..>>>.vv.vv..>.v.v>v>>.>v.v>v
>...>v.>.>..v>v.v>v..vvv..>>>vv>>..vv.v>>.vvv>v..vv.>>.>>.>>.....>.vv..v>vv.v>.>>.....vv.v>.v.>v.....>.>.v>.v..>>.>......v>.v.v>.v>v.vvv..v
vvv..vvvv>>>..v>>>>..>.v.>>v.v>>>..>>...>vv.>.vv..>....>>v.>..vvv>v.v.>...>>.>>...vvv..>>vv.v>>.>..>>v..>v>>>v.>>...v.v>...vvv..>..v.>..>..
v...vvv..>.........vv..>>>>>>..>v.v.v...v..>..>.v...>.vv.>v...vvv.>.vvv....v.v....v>v>>vvv....>.vv.v..vvvvv..v......v.>vv>v>...vv.v..>>..>v
.vvv.v..>.>.v>v....>v.v.>>.vv..v.>.>.v.....v>..v...v...>>>.>....v.........vv.vv..>v>..>v.>>..vv.........>.>.vvvv...>...>v>..>vv.v...v.v...v
>>..v.v>>..>v.v...>.v..v.v..>v.>.>.>>.v.>v>>..>.>v.>v.v>.>vv>v.v>>>.>vvv>v>.>v..>..v..>.vv.v.v..>>.>>..v.v>.v.>.v....>vv.>v....vvv.>.v.v>>.
>>>>>v>>.v.vv>..v.>.v.>vvv.>v>..v.....vv..v>........v..>v>v.vv..>>>v.>>v..>v.>vv.v..>>>v..v>v>...>>..v>>..v>.vv>.vvvv.....v>.vv....>v.v..v.
v>.v.v...v.>vv.....vv.>.>..>..v.>v..>...>>.v.>...>.v.v>v.v.....>.>>v>>v.>v>.>..vv>..>.v.>v.......vv.>.>v..>>.>>.v..vvv>v..>v.v..v..v.>v.v>v
.....vv>>>..>..>..v.v..v>.>.>..>>....vv.v.v..>.vv>>vv.v...>.>.>>v>.>.>v.v..>.>.>.v.>.>>v.>.>.>vv..>...>v>.v>.>>....v.>.vvv>v>..>>>.........
vvvvv.......v.....>v.>.....>v>.>>...vv>....v.....v>.v..v>..>....>v.....v.v.>.>v>>.>.v.v...>.>>>..>v....>>vv...>.>v.v>v>.>.v..vvv>......vvvv
...>>v>...v...>.>.v.>..>.v.v.v.v...v.>.v>.v>....v>.v>>>..>>...>>...v..vv.......v>..>>v.v>.>.v.vv..>.>v>>.>vv...vv.>v.>v.vvv.>vv..>v>>....v.
v.....>....v>v>v.v.v..vv..v>.>....v>.vv..>..v.v>v>...>vv.>>.v.v>>v..v>.v...>.v..>>..>v>>vvvvv.v.>vvv.>>....v>>>v...v.......v...vvv...vv>..>
.....>.v.vv>v.>.v>...>.>v...>v.>.....>.v........>..v>v..v>>vv..>.....>>..>vv...v>v...v>..vv...>>..>>>..>.v>v>v>>.vv..v..>>vv.v>vv.v>>..v>>v
..v....vvv.>>.vv.....v...vv>.>>vv>.vv..>>>>.v...>.v..>v.>>>>....>>v.vv>v......>v.v>..v>..v.vv....>>v..v..>.>>...v.>..>vv.v....>v....vv..>.>
>..>v>..>>>.vv..>>>...>.>v>>vv.>v.v...>.>.v>..>....v..>>v>vv..v..v...>..v.vv>v.vvv>>vvv.......v.>>..>>.>>>>v>>>>v....v.>v..>..v.>.v>..v...v
v.v...>..v..v.vv.>>v.>.v.>>.v..>...vv..v>.>.>>v.v>>>>v.>vv..>.v..>>...>vv..v.v.>........v>.>.>>vvv..>vv>vv>..v.v>.v>...v.v.....v>>.>.>v>>..
.>vv.v>......>.vv..vv....v.>v>v.>v>.v...>.>v..v..>v.v..>...>>.v>.vv..>.......>v..>.v.>vv...>v...v>..vv.>.>>.v.....vv>v.>v.>..>.>.>vv>.>vv.v
.>v.v.>..v>.>>.v>>.>v.vv..v......vvv>>v..>..v..vv>..>vvvv..v>...>.v..v..>.vvv..>.v.>.>>.>vv.v.vvv....>.vv.....vv.>>>..vv....>vvv.>..v..>vv.
...>>.v>>v>.>vv..>....v...>>...v>..v..v..vvv..v.>>>v.>..>>v>>>.>>...v.>..v>..>.v.v>>vv..v.vvv>>........>..vv..vv.>v.v..v.>>..>>..>v>...v..>
>.>.v..vvv...>.>>>>.>v.vv>>.v.>vv.>>..>...v..>...>...>>.>v..>v.>.v>.v.....v>..v..>.>.>>v>...v.v>..v.v.vv.>>v..v.>>.v..v>v...>>v.>v.>..>....
>.v.vv.v.vv...>..>v>>..v>.v.>.>v.>..>>.>vv>...>>.v..>v>..>v...vv....>..>v>v>.v>..>>..v.>>>.v.>>>>.v..>v....vv>....>>..vv..>vvv>v.>>>.>...>v
.vv...v.>.vv.>..>>..>>>v.v>......v.......v.v>>..v>.>......v.v..>vvvv>>..>..>..>..vv.>vv.....v...vv>v.>v.>...v>v...v.vv>..vv>>>vv>..v.v>.>.v
.>..>.>...>.>.v....>>..v>.>>.>....v>>>v.>v>.>>v.v.v..v...>.>....>vv.v...v....>..>vv....v...>.>......v>.>>v.v>v.>>v...v..>v.>..>..v.>.vv...>
>>.>>>v....v..v..>...v..>................>.v..v>v.vv.>vvv.>..v..>v>>v.v......>v....>>>...>v>.....v>>......vv.....v..>v.v.v>>...v.v....v...v
..>..vv>>.v>v..>.v..v..v....v>.v.v>.>>.>>..>v>..>.v..>....>..>v.>>v.vv..>...>.v>..>>.vv>vvv>...vvv>.....>.v>v>..>>vv>.....>vv...vvv.>.v>>.>
v.v.v....>>v.>>v>vvvv...v>>v.>..>.....>v>.>..>>>v.vv..>..>...>..>>>.vv.....>...>vvv>>.>>....v.>v>v>...>..vv>.>v.>.>..v>..>.v..>..>..>vv....
>.vv..v>...vv>vv.....v..v>....>vv.v>>.>..v>.>>>>vv>>vv.....>....v..>>v>.v......>..>v.v>.v.vv>...>v.......>.>.v.vv>>..v..vvv..v>...v>>....v.
.>>.>.v.v.v.>>..vvv.v.>>v..vv....v.v.v.>..>v.>>....>......>>..>.v.v>..v..v..>.>>.>..v>.>v....v.>v>v.v.>.>>vv.v>v>v.....>>v>.v>...>...v.>.v.
v>..v>...>..>....v.v.>>......>...>>.v>v..>...>.v....>.>..>.vvv.>.v..>>.>>.>>...vvv.v.>.>...>.>...v.v.>>>v.>.>.v...>>v>>>..v>.>.>>....>>>.vv
v..>.v..>v>.>.>>.v.>..>...v.>.v>vv..>>.vv...>>>>>..>.v.>.>>...>..v.>vv..>v..v>..>vv>..>>>..v>.>v...>v..v>>v>>.v..>>..v...>..>>.vv..vv>..vv.
...vv..>v.>v..>..v.>.>>>.>>..>.v..>.>...>.>.vvv>>.>vv>v..>>.>>.v>>.>>v>.>.>>>v..>..>>>....v.v.vvv>.>>.....>...>....vv.>vvv.v..>.>>.>.......
.>>..vvvv..vv>>>vv>.v.>vv...>>.v..v......>v.vv>>v>>v....v>>.v>>v.v.vvv>vv.v>.>.v..>.>>v>>>.v.>v....>.v.>v.vv....>>..>>v.v.v>v.v.v.v.>...>>.
>>..>>v.v.>>vv>>>.>>...>v>v.v..v>>>v.>vv.>.vv..v>..>vvvv>>.>..v.v>>.vvv.>>..v>>>..v>>...>>>.>v>.>>>...>v.v.vv.>.vv.vv>.vv.>..vv>v.>vv>.v...
v>>..>.v>..v.v..>.vv.>v..v...>v>v...vvvv.v>.v..v..v>..v>>.>.v.vv.....vv..v>.....>>.>.v.vv>.v...v.v.v.v>>...vvv>v..vv>>.....>.>..>..>v.v>>..
.>>.....v>>..v>v...v.>.v.>.v>>>>>>>v..>.>..vv.......>>.v>vv..>v.v>.>v>>v>.v..>..>...>vvvv...>.v.vv>..vv........>....v.v..vvv...v...v..vv..>
..v...vv>v.>v>..>>v...v>v>v...v>v>>>v....v..>v.v..v....v..>..>>..>..>.>.vv.>>>v..vv.vv..>.v..v.>>.v...v>....>..v.>...vvvvvvv.>>>v.vv.....>>
..>.v>..v.v.vvv.v.v>.v..>.vv>.>.>v>.vv.>v>....vvv.vv.v....v..>....>>vv..>..v.v...v...v>v..>..>.>....>>>>>>>>.>.vv.v.v>vv>.v>...>.>.>>.....>
.>....>...vv>>v.v.v>>..vv.......v>>..v..vv>.>>v>v....v>.v.>..v..>..>>v.v...>>>....>>v.vv.>..>>...>>>...v.>v..v..v...>....>>>>vvv......v....
..>.v.>..>>v.vvvv.>>.>.>>.>>v>.v.vv>v.>v.vv.v..v.>.>>.>v>..v...>.>...v>vv.>.>>>.v.>>v>...>v..vv>.v.vv..v.>>v>..v>..v.>>>v.>.v....>v..v>....
v..>.>>>vv.>>vv..>v>..>...>v..vv..v>>..>v>..v.>.........>.v.>..v..v>>..v>>>.>..v....v.>>v......>>..v.>.>>.>v>>>.>>vvvv>.>v.>.>.v>.>..>>v.>>
..v..>.v..>>>..v>v.>..>>vv>..vv..vv.>v>..v.v.vv.>>....>..vv.>..>.>.>...>vvv>..v....>.v.>vv>.>.v.v>..>>..v.>.v>...v>vv>>.>>.>.>....>...v>.>.
vv.>..v.v...v.vv>v.....v>.>v...v..vv>...>>>....>>>.....>..v.>.v>>.>....>v>....vv>.>.vv>..>.....v.v..>.....vv.v.>v.v.vvv.>v>...>v.....>v..vv
v.v>>.>.>...>>>...v>v.v.vv>.v...vv.>.>.....>..>>.>.>vv..v>>.>v.....>..v......>v>.v.>.v>v..>v.v..>..v.>>..v.>v.>vv>....v.>....v..>..vv.....>
v>v.>.......>.>>>...>.>......vvv...>..>..v>>>vv.>..>>v>.>>.>v>v>vvvv.v>.>.>v>.>vv.....>........>.v.>..>>.>.v...vvv.>>.>v.>....>.v.>.......>
>>...>vv>>>v.>>...v>.v>...>v....>>>>..>....>>..>>>>.v>.>...vvv>.....>>...v..v..>>>v.>vv>.v.>>v>vvvv.>.>vv..>.>vv.>v.>..>..v>vv.>.vv.....v..
v..>....>..>..>>v...>.>...v>v..v..v.>>....>>vvv..>.v..v>...>..>....v>v......>.v>v.vv..>.v...>v>>.v.>.>.v.vv>>v>>......v>.v.>...........v>..
v>.vv.>....>>..>.>>.vv..>....v>vvv>...>.>..>>.v>....>.v..>...v>>.v..>v.v.v.v>>.vvv.v.>v>>.>..v>v..>v......v...>.>>>>>v>v>.>..>v.>v>v>vv>...
..v.v.>v.>..>>..vv....vv.>.>..>...>v>>v.>.v>.v.>.>..>>......vv.>......v>..>v>.>.v.>>.....>v...>>>vv>.v>..vv.>.v.>.v..>..>.....vv.v>vvv>....
>.v.v..>>>>v>...v....>.>v>..>........>..v>>>.vv....>v>vv>>>>..v...v.v.>>v>v..v...vv.v.>v.v.>..>>...>.vvv..>....>...>v>v>.v.v.vv.v>v.v.v...v
..vv>.>.>...>v..v.>>>>.>.......>>v..>.......>>.v..v>.v...>.....v>v.v...>vv.>.v.>..vv>..v.vv..>>.....v.v....>..>>.v.>>>>.vvv.v>>>.>v.>>..>>.
>.>v.v>>.vv>v..v...>>..v.>v..v....>..v.>>v...v>.v>.....>......>.vvvv.v>>..>>...>...>>v>vv..v>v>.v>.....vv.....v...v>.>..v.>vvv>>vv>..v>.>..
v..>.vv.v..>>.>.v..>v.v.>v>>..>.>vvv..>.vv.vvvv>>v>>vv>.>>.>v.>.v.>>......>v>.>v.>v.>..>..>.v>.......>v.v..>.>v>...v..>...v.>...v>>v>.v>.vv
>.>>.v>.>v>.v..>>.vvv...>.>v>vv...v.v>vv>vv.>....v...>..v..>>.v..v......>vv>.>v>..v.>.>...>.>.vv...>>....>...v.v....vv..v..>>>>>.>.>..>v>..
.>.vvv>.>.>>v>v..>.v.>.v.....v..>..>v.......v.v>.>..>vv.v...>.>>.>.v>>.....v.>>vvv.v>.v.>>>.>.>>.>>.>>vv......vv.>vv..v.>>.v>...>.>.v>>v.vv
.>........>vv.v>v.v.>.v.>v.v>....v..v.>.....>v...v.vvv..>...>v>..>.vv.vvv...v.v.v>vvv.vvv>vvv..v.vv..>..v.v>...v....vv>.....v>..>>.v>......
v>v.v.v.>.>v>>v>..vv..>.vv......v..v...v..>.>>.v.>...>.......v...>..v.>.vv>.>>..>...vv.>v....>.vvv...>>.v...vvvv>.>..>>...>>>...v.>......vv
>.v.>..>v>vv..vv..>>..vvv.>...v..v.>.>vv.v.v.>.v.vvv.>.>>..v....>..v>v>..vv...v>>v..v>v.>>v>v..>.>.>.vvv.>....>v.v..>v...v..>.vv....vv>>.v>
v.>>...v>.v..v.>..>v.>..>.>...v..v.>>>...vv>>>>>.v.>.v>..v..>.vvv.v...>.>>v..>v...v.v.....>.vv>>.>..v.v..>.>.v>>v>>.>vv.>>...vv>>..v>>v>>v>
>v.>...v..>........v..>vvv..vv...>..v.vvv.v.>..>>v.>.v.v.>..>..>.vvv.v>v....>>>>.v>.v>vv..v..v.v.v.>>>>.........v..v.>v.vv>vv.v.vv....v>.vv
........>.>..v....v.>.v...vvv.v.v.>v..>>...v......>...v>......>v.>.>v..v.>>vv>.vv.>>.v>...>>.>>v.>..v>...v....>vv>.vv>..vvv.v>>.vv..v.v.v>>
>>.>..>vv.v.v>>v..>>....>..>.>...v.v.>..v>.....>...>.v.v>....>vv...v....>..v.>v....>.v.v.....vv>>vv>..v>.v.>..>>>>.v>.v....>>..>.v....v...v
....vvvvv.>.>>....v..>..v>....>...v.v>.>v..>.v.v...vv...v.>>.....vv.v>>.>>>>..vv>.v.>.>..>v..>.>...vv.vv.v..>..v.>v.>>v>..v.>.>.vv>..v..v..
..v...v..vv....vvvvvvv.v>.v>.v>>..v...v..v>vv.vv.v...>>v.>>v.v...v.>>v.>.v>.v>.v..>vv....v>.>.>...v>>..v.>>..v.v>>..>>>.vv.>vvv.>.v>...>>>.
.>v>v.>..>v>....>v>.v...vv...vvvv>v..v>.v..>.vvvv.>>.v>.v>.v.>>.v>.>>>>v..v....>>..>.>>>.>.vv.>..>.>.vv>.vv..vv..v.>>v>v..>>v>>>.v..v..v.v>
vv...>vv>....>>...v..v.v.vv...>.>v.>...v.vv.....v.>v.v.vv.v.>>>..v..>v>>>vvv....v.v.v.v.>vv.>...>........v.>..>vv.>.v.v>v>.vv>vv.>>vvv>v...
v.>.>.>>.>.v..>>>v.>v>.v..>v...v.>.>.v.v.>>>vv>...>.>.v..>..vv>vvv..>..v.>>.v...v.>>...>v>.v.>..>.v...v...>.>>v.>>....v.v.>>>>...v..v..>..>
vvv.>v..>v..v>.>>vv..v..v.>..>.>v>v.v.>..>.vvv..>>.>v..v.vv.>v.vv.>vv......v...v.>.>>>>v>...>.v.v.>>.>v..>..>...v.v.v.>.>v..v.>...vv...>.v>
>v.........v....>>>.>...>.>vv>..>.v.>>vv>...v.>v.>...>..v.>v.>.>v>.....>>>.>...>.v>....>v>>v>>.v.vv.v.>v..v.>>>v>v.v>..>>v>.>v>vv.v.vv....v
v.>.>v..v.vv..>>...>..v...v>..vv.>.>>>>..v>>vv>....>..>v>v>>..v.>.>>.v.>v.v...v>.>.>>vvv>>.>.>>v....>v...>v>...>>..>.v.v...v>>v.vv..v...v.>
.v.vv>v.>...>v>.v.>.>..>.v......vvv.....>.vv>>>..v...v.v.>....vv.v.v.vvvv.vv..>>..>..>....>.vv>>.>.>>.vvv.vvv.>..>>>..v.v....v..........vv>
..v.v.>..>...>...v....v.>>>...>>...v.v>.vvvv.>v.>..v>.>>...vv.>....vv...>>.>..>vv>v>.>.>..v>.vv.>>v.>>vv>..>..v>v>...v>.>>v.v..>>vv.>....>>
>.v>.....vvv..>>>>v.v...>.v.>....>.>v>>.>>..>.>vv>.....v>v.v...v.v>.>..v>...>vv>..v>>..>..>>>.v.>>>....v>v..>vv..v.v..>v>v>.>.v...>v.v..v..
....>v>>>v>>..v.>v>..v>.........v>>>>..>.>.>.>.v.>.>v..v..>..v.>......>v.v.v>v.vv....v...>........v>...v.>>...>.>v.>.vv...>.v.>>v...>.>.>vv
>...v.vv>.>..v.>>..v.>v.v>....>....>.>>.vvv..>.>..v>.>.>...vv>....v.vvv.>...v..>.v..>....>..v.>v.>.>....v.vvv>.v>v......v..>vvv..vv.vv>vv..
.....>vv>v....vvv..v>v>.v..v..>...>..v>>>......v..v.>vvv.>v.vv>.v....>.>v>..>v..>v......vv.>.>>>.vvvv...>...>>v....>..>>.>.v>v>.>.v..>.v.>v
...........v>>.>vv..v......>vvv>.v.>.>..>.v..v.v....>v>.>.>>..v..>vvv..v.vv..>v.vv.>v.v..vvv>.>..vv.vv.v>v.>>.v..>....>v..>v.....>.>.>vv.>>
v.>.v.v.v...vv...v....v....v.>v>v.>...>v.vv>v..>v..>>...vv>...vv.v.....v>.....>...>>...v.v>.>v>v........>...v.v..vvv...>.v....>vvv.>....>..
v..v.vv>.vv.v...>>...>..>vv>v>>..>v.>...v.>v..>.v....vvv...vv..>vv.v...vv>v.>>..>.>>>>v>>v>.>vv>v>.>.>...>v>.vv.>..v>.vv.v....>.....v.v....
..v......v>vv...v>.vv...vvv>>.v>>>>>v...vv...>v.>>.>..vv>vv.v....v>vv...>...vv....>>.vv......v>..>.v.>..>vv.vvv>vv..>v.>..v.>vvvv>...v>vv..
...v.v.>>....>...vv>.v.....v>...v.......>>.>...v.v>vvv..>..>.>..vvvv..>...>..v..>vvv.......>vvv>>..v....v..v>>>>.v>....>>vv..>....v.v..v>..
.>v>.>..vvv.>>>>...>>.>..>>.vv>..v....>..>......>.vv>..>vv>.>v>v>.v>v....>v.>.>.>vv.>v.v.>>v...v.>.v...>>.....v>.vv>v.v.>vv.>.>.>....>>v>.v
vv...v..v.....v..>>v....v.vv..v>.>....>>vv>.>.>..>.v....v>>v......>.v>>>>.>>.>>>.>..>.>.v>.>...>>.vv.v.vvvvv.v.>v>>v.v>.v.......>.>>..>.>>>
>.v.>...>..v..v..>.>v...v.>v.>.>....>.v>>v.vv>v.....vvv>v...vv.vv>..vv.v>...>vv>>>>.v..v..>v.v..>v..v>v.....vv.>..v....v...v>....v>>.v..v.>
v>.>.>v>.>>..>v>.>.>>..v......>.>>..>.>..>.v....>...vv>>...v.>.>.v>.vvv.v>vv>.>v>>.>v.vvv>v.vvv>..vv..>.>..v.....v>.....>>....>>vv...v.v>>>
.v...>..v...>v...>...>.>.>.>>>>..v.>.vv..>..v>>..>..>v...>...v.v.vv.v..vv..v>....>.>..>>.v..>...>v>v>.>.>v.>.v>..>...>..v.v>...>...vvv..>>.
>>>..v>>vv.>v..v.>.v>.v>.>v>>.v>>v>v>>.v..>.v>..v>..>..v.>v..v.>.vv>.........vvv...>>.....v>..>>.>v.>.>...vv>..v.v>>..v...>v....v....vv>..>
>v....>>....v..v..>..>vv............>>...vv.>.v>..v>...v>.>v>>..>.....>>.v>..v..vvv>...vv>....>>vv..v.vv>....>.v..v..>.vvv..v...>>v.>.>v.>.
>...v>.v.v..>...>.>>.>..>..>..v.v..>>>.v>>vv.>...v>>.v.>vv....v..vvvvv...>vv....>.>.v...>>.>.>vv...>>v..>vvvv>.v>>...vv>.>v.>>vv...>....v>.
...........v..vv...>v..>.>>..v.....v.>...vvv.>.v.....>>>.v>..>..>..v.vv>v..>v>>..>.....>vv>v>.>v.>...v.>v.vvv....>v>...>...>..>.>>..>...>.>
.>...>....v....v.v>.>>.>.v>>.>>v..>v.>>>>.v.>.v..v>..v>>v...v.vvvvvv..vvv.>..vv.v...>..>>..>v.>>...v>vv>v.>.>.>>v.vv.v......v>v.v..v>vv>.>v
.v>vv>>v..v.>>..v.....>v.v>vvv.....>.......v>..v>v.vvv>...>..>...>.>.>.>v>.>..v...>v..v...v..v.v..v.v>......v.>...>.>vvv>>>.v.v.>.>.>..v>..
..v>v.v>>>..>vv..>.v.v.>v>...v.v.vv.v..v..v>.v.....>...>..>>>v...v>>.v>......v>>>v>>...v>.v>>.....v.v..vvv.>>.v>..>..>vvv.>vv..>.>......v..
.>..v>.v..>v...v..>>..v..>.>.....>...vv..v.v..>>v...v>.>v....vvv...>.>.vvv>vvv..vvv..v>vvv>v>.>..>v>>.>>>.v..>......>v>......>.>v.>.v>>>..>
v.>>>...>..vv.>..>vv.v.v..>>.>.v..v..v..>>vv....v...v.v>...vv>.>.>.>>vv.vv.>..>vv.>v.>>>.v.v.>....>v>v....>>>v..v>.>.>>....v.>.>>>.v..vv>v.
>vv.>>>........v>>v...>..>..>.............v..>>..vvv..>..>..v.>>v.>>v>..v>>>....v>.>v>>....v...>..>>v..>v>>..>>....vv.vv>v........>.>v>.vv>
v.....v.v.v..>...>>>..>>v...v..>v.v..v....vv..>>..>>vv....vv.>>>vvv>......>...v>v.v..v>.>...v>>.>.>v....>.>v...v.v>..>.>...>>>.>.v>.>...v..
.>.>.v.>vv...>v>>v.....v>..>..v>>>.v>>..vvvv.....>.v>.vv..>..>v..v>>..>v>...v.>.>v..>v.v.v.v>>v.>.>>.vvv..>>>vv...v>>v>...vvv.>vv..vvv..>.v
...>.>......v..v.v...v>.v>>v..>.v..v>.>.v.>>>..>.>v........v.v.v..>>..v.v.>...v.>....v...v.>vv>.>.v.>v...>vv>....vv.v..>v.v.>v>.>....>..v>>
......>...v...v.vvv....v>..>>.v...vv.v>>..v.>>>v.>>v.v>..vv.>v.v....>.>v.v..v>.>.>v.>..vv........>..v..v.vv...>v>.....>.>>.vv..v..>v.v>>v..
v.vv...>.....>.>.>>v.>..>v...>.v.>>vv.vv.v.v...>>>...v>>.v..>.>>>...>>>vv>........>v...>v>vv>.>v.>v>>v...>.>>.>>.vv>>.>>v>.>>>>v..v.v.vv.v.
v...>>.v.vv.vv>..>.v.v>...>v.v>v.v.v>>v.v>v.>...v..vv.....vv..>v>>>...v...>.v.>>>>.v>v>>>>>>...>....>.v..>v.>.v....>>.vvv..>.>vv......>>...
.>v..v....>>>>vv>vv..>v.v.>.v>.>..>.v.v..>..v>...vv..v.>>.v....vvv>v>v>>>..v..>>>>vv.>.v>..vvv.>.>>....vv...>..>>v>vv>.>...v.>.>v..vv...>..
....>....>>..v...>>>.v.>.vv.vv.>>>>>....v..v..vv>>..>...v>...v>..>.v...v....v>.vv....v...>...v.....v..>.v...>..>..>vv.>v.v>...>.v.v>.v..v>>
..>...v...v.>vv........>v.>..>>.>.v.v>..>v....v.>.>vv.>.v>.>v...>....>.v..>..>vv.v>v....vv>>>..v.......v.>vv>>v..v.>>.v.....>>>...>..v...>>
>.v..>v...>........>v..v.v..vv>v>.>>..>>..>v>v..vvv.v....v.v...>>>..v..>..>>.>>v.>..>..>vv.....>..>>..>........>v.vv>......vv......v.vvvv>.
.>..v..>..>v.v..v.v..v.>>v..>>.v>>.>v.v>>..v>vv>.vv>>.>>>>>>.vv>v..>.v.>...>>>.v>v>v..vv.>v..........v..>.>.>v....vv>...v..>..>...v...vv..v
v.vv..v.....vv....>>v.>v.vv>...>.>v.v...>.>.....v>.vv...>..vv.v..>v........>>vv.>vvv.>...>..>..v.>..v.>vv>..v.>.>v.>.>.v>.>.>.>.>vv>v.v>.>.
.vvv.>>>.>.vv.vv..>.>..>..v.....>.v>......v.>vv.>.v>..>.>.v>.vvv.v>.v..>..>v..>.v..>v..>..>vv.>v>>v>.v...>.v..v>>vv.>.>.>vv....>.v.>....vv.
>>>v..v.>.v..vv>..v...>..v.vv>.>.v>...>..vv>.>..v..>...>.>vvvvv..v..vv...v.>.v....v>>>.vv.>..>.............>>..v>.>>>.v>v..>.>>.>v>>v..>.>>
>.>.....v>v.vvv.vv......vv.>..v>..>vvvvv.....vv..v.>v>.v>vv...>..>>v...>v.>>.v>..>>vv.....>>>vvv>.>...>.>..>.>..>>>>.>>.vvvv..>>.>..>..v..v
.v>v...>vvvv.v>..v.vv>v..v...v..>.>...v>...>.>>.>..v..v..>v..v...>.vvv.vv.>>.v>vv.v....>>.>.>.>..vvv.>v.v.>v>.>>..>v>vvv>.>>>v>v..vvvvv.>.v
...>>>v>>>..v>...>>..>.>.vvv>vvvv>v..>>...>>..vvvv..v.>>.....>>..>>.>v.>v...v.v..>.v>..v>v>.>.v.v..v.v....>...v..v..v>..v.v.v...>v.v..>v...
.v.>>>..>v>>>>...>.vv......>>.v.v......v..v>.>...vvv>vv>v>v.....v>.......>>>>.v>..>..v..v>>>..>.vvv>v>>.>>.>...>vvvv>v.>...v.>v>..vv..v>vvv
.>.>..>.....v..v.>..v>..v..v>vv>..........>v.v...v>>.>v.v.vvv>v.vv>>vv....v...>v...vv>.>>>>>vvv>..>...>>>.v>>....vv.>.....>>..>v..v>vv..>.>
>>v>v..>...vv...v>.>.>>....>.>>vv..>.....>.v.vv..v..>.>v.v...v.>.v.>>....>...>v.>v>>...>..>v.>.>.vvv.>v.>>>vv>vv.vv>...v>.>......v.v.>>....
.>v..>>...v>>.>..v>...v.>..>>>.v.v..v>..>.v..v....v>>vv>.>>>.>..>..v..>.v.v.>v.>v>>..>.v...v.v>>...vv..v..vv.>>>>v..>...vv>>>>>v..v.vvvv>>.
>.....v.v>....vv.>.v>.>>>>...>v..>.v....>>>.....>...>>>>.vvv>.>v>...>v.>..v>v.>vv...>>....vvv..v........>....>...v>..v>v>v..>v..v..>.>.>>>v
.vv>.vv..>>>vv>.vv.v..>.>v.v>v.>vv..vv.v..v.vv.>v>>>....v.....>v.v.>.>v..v..v....v.v.v..v.vv>>>v.>>..>v...>...v..>...>>>.>.>v..v..>.....>v>
..>.vv.>.>v....v.v..>v.>..>.>.>>..vvv>......>v>>>.>.v.v.v...>v.v>........>>>..>......v.v>>....>>.>v..v..>.>v..vv>>.>.v.>..v..v..>v..>v....>
v>vv..vvv.>.vvv..>.>..>.v.v.v.>..>v..vvv>.>>.v>v>vv..v.v>.v.>>>v>.>..v>>....v...vv>.v..>.v>>...>>....v.v....v.>v...>..v..>>.....>>v..v.>>v.
.v>.........>.v>>v..v>.....vv>vv.....>.v>.>>..>..v>.vvvv...>..>.v>.v...v......v>v..>.v>.v>v>vv....>v.....>>v..v>..v.>...v>...v..>.vv>v>v>>v
..>v.v>..v.>...vv>>.>..vv>>>>.>.v.>.>....>..vv.v.>.v..>.>.....>>v.....vv.>.>.v..v>.>>.v.>.>....v.>>.v.v.vv>v.v.>>v>v>>..v>.>..v.v>.>>.v....
...vv>.v.....>vv............v....vvvv...>>v.v.v..>v.vv.vvv>>v.v...>v.>.>.>.v.>.v.>.>v>..>.v>v>v.>>...v>>>>v.v.>..v..v.>.>..v>......v>vvv>vv
..>.v.v...>..>vv>>>..v.vv>...>....v>.>>.>>...v>...v..v>>vvv......>.>.....>.>.>>.v.v>v.....>>v>v>>vv.v.v>.>v..v>v>.....v.>..vv>>....>>vv...v
>..>vv>>v>.>v....>v.>...v...vvv..v.v>.>.>>vv...v..>.....>....vv..>.vvv.>.vv>...v>.>...>..>>>.v>....>>v.v.>vv..>.>>v.....v.vvvv>.>>vv.>v...v
.....vv.>v.>..>>..........vv>>.>.>..>.>..>>......>..>...v.v>vv>.v..>>v>vv.vvv.v...v.>vv>...vv.>v.>.v.v...>vv.v>...>..v>...vv.vvvv.>...>v.v>
.>v>>.vv.v.v....>>>>..>>v>>.>>.>v.>>.>..v>.>..>..v.v..>v.......v>.>..v.v...v.vv.>..v...v.v>v>>v.v>.>..v..v.>v.v.v>v..>.>...>.>.>...>.>.vv..
.v>v...>....vv>>.....>.vv........>.v.vv..>.>>...>.>vv...v>.>..vvv..>>vv.>>...>.v>v>..>>vv...v..v.>>.>vv..v..v>>.>.>v>>...v>>vv.>>..........
.v...>.v>>vv>>v...>v...v...v>>.>v>>v.>>..>>vv>.....v.vvv.>v.....>..v.v.v.>..v>..v....>>..vvv..>v...>>.>v.v.v>..vv.vv.>.v.v.>..>.v.v>v>vv>..
.>..>v>>>.>...>>v..vv.v>v>.v>vvv.>..v.>>.vv>.v>...v.>>>..vv.v.......>>.>v...>.....>>.>v>v.>..>.>.>.>..vv.>v.>..vvvv....>.v....>>.v.>.vvv...
>v..>.v..>>..v..vv....v...>vvv>>....>.>..vv.>..vv...>...>v>>.>.>..>v>....>>>..v.>>.>..v..>v..>.vv...v.>.>..v...>...>..>.....v....v..>.v.v.>
>v>v......v>..v>..>.v>...v.....>.>v.>>....>v>>.>>vv..>vv.v.v....>v.v>v..>v>..v>v>>.>..vv.....vv..v.v.v....>v..v>vv.....>.>>.v..v>>...>..vv>
...vv>vv..>..>v.vvvvvvv.>.>..>.v.vv>>v.vv...>>.....v.>>.v...>.>....v.>.>>.>v>.>.>..>>...>vvv..>..>.....>..>.>..v>v.>.v>v>>....v>....>>..v.>
>v..>...vv.vv>>>v...vvv.>..>.............v>vv.v.vv.vv.>>.v>>...vv>...v>.>..v.v...v>v.....>vv.>vv>..>.>v.v>..>..>....vv>.......v>>vv.>>>>..>
>v..>vvv.v.>v>.....>..v>v..>.>>>.>.v..>.v.>...v.v....v>.v.v>.v.......vv.>..>..>v.>.>.v.v>v..v>..>vv.>>.vv>>.v..v>.>.>.>.>v...>.>v...vv..v>.
..v..v>v>>vv.v.v.v.>v.>>v.vv........>v.>.v...>.>v.>>.>v.vvvvv>.>.>>...>.>..>>...v.vv..v..v...>>v>>.>>.>.vv>.v...>.>.v..>...v.>>..>>.v>>>v.v
>vv..>..v...>.vv..>........>..vvv....>v..vv>..v.v.>>v>>.>>.vv.v...v>.v>>>...>.vv.v.v>..v...>.vv>..v.v>..>>.>v>.....>>.>..v>vv..v.v>vv......'''
)
