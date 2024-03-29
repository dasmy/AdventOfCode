input = '''Valve HM has flow rate=0; tunnels lead to valves LS, YS
Valve IY has flow rate=15; tunnels lead to valves YI, MU, KN, QS, QM
Valve VI has flow rate=22; tunnels lead to valves LE, SE, RB, JR
Valve SE has flow rate=0; tunnels lead to valves VI, AZ
Valve QU has flow rate=0; tunnels lead to valves YC, QK
Valve RB has flow rate=0; tunnels lead to valves AN, VI
Valve PU has flow rate=0; tunnels lead to valves JR, IM
Valve OA has flow rate=0; tunnels lead to valves KZ, FR
Valve AQ has flow rate=23; tunnels lead to valves FA, QM, GE
Valve QS has flow rate=0; tunnels lead to valves IM, IY
Valve HC has flow rate=24; tunnel leads to valve XH
Valve QI has flow rate=0; tunnels lead to valves KQ, LS
Valve FA has flow rate=0; tunnels lead to valves HA, AQ
Valve BA has flow rate=0; tunnels lead to valves KZ, ME
Valve DH has flow rate=0; tunnels lead to valves LT, HA
Valve TE has flow rate=0; tunnels lead to valves AA, ZJ
Valve AA has flow rate=0; tunnels lead to valves YS, XT, TE, GY, FS
Valve YC has flow rate=9; tunnels lead to valves DV, XH, DJ, QU
Valve KN has flow rate=0; tunnels lead to valves IY, AZ
Valve GS has flow rate=0; tunnels lead to valves FS, KZ
Valve DJ has flow rate=0; tunnels lead to valves YC, UV
Valve GY has flow rate=0; tunnels lead to valves QK, AA
Valve ZJ has flow rate=6; tunnels lead to valves RC, HS, UV, ME, TE
Valve RC has flow rate=0; tunnels lead to valves BY, ZJ
Valve QK has flow rate=10; tunnels lead to valves QU, XX, HS, RM, GY
Valve AN has flow rate=0; tunnels lead to valves HA, RB
Valve XT has flow rate=0; tunnels lead to valves AA, KQ
Valve LT has flow rate=0; tunnels lead to valves IM, DH
Valve YI has flow rate=0; tunnels lead to valves LE, IY
Valve BK has flow rate=0; tunnels lead to valves LS, RM
Valve LE has flow rate=0; tunnels lead to valves VI, YI
Valve IM has flow rate=19; tunnels lead to valves PU, EC, QS, LT
Valve SK has flow rate=0; tunnels lead to valves RF, AZ
Valve RM has flow rate=0; tunnels lead to valves QK, BK
Valve YM has flow rate=0; tunnels lead to valves LS, KZ
Valve DV has flow rate=0; tunnels lead to valves YC, AI
Valve QM has flow rate=0; tunnels lead to valves IY, AQ
Valve KZ has flow rate=5; tunnels lead to valves BA, GS, YM, OA, XX
Valve FS has flow rate=0; tunnels lead to valves GS, AA
Valve UV has flow rate=0; tunnels lead to valves DJ, ZJ
Valve AZ has flow rate=20; tunnels lead to valves SE, KN, SK, MS
Valve BY has flow rate=0; tunnels lead to valves RC, LS
Valve OY has flow rate=0; tunnels lead to valves KQ, EI
Valve XX has flow rate=0; tunnels lead to valves KZ, QK
Valve ME has flow rate=0; tunnels lead to valves BA, ZJ
Valve YS has flow rate=0; tunnels lead to valves AA, HM
Valve MS has flow rate=0; tunnels lead to valves AZ, HA
Valve HS has flow rate=0; tunnels lead to valves QK, ZJ
Valve LS has flow rate=3; tunnels lead to valves BK, HM, QI, BY, YM
Valve KQ has flow rate=17; tunnels lead to valves OY, XT, QI
Valve MU has flow rate=0; tunnels lead to valves IY, HA
Valve EC has flow rate=0; tunnels lead to valves IM, GE
Valve XH has flow rate=0; tunnels lead to valves HC, YC
Valve JR has flow rate=0; tunnels lead to valves PU, VI
Valve EI has flow rate=0; tunnels lead to valves OY, RF
Valve AI has flow rate=25; tunnel leads to valve DV
Valve GE has flow rate=0; tunnels lead to valves AQ, EC
Valve RF has flow rate=18; tunnels lead to valves EI, FR, SK
Valve FR has flow rate=0; tunnels lead to valves OA, RF
Valve HA has flow rate=12; tunnels lead to valves AN, FA, MU, MS, DH'''

import re
from functools import cache

available_time = 30


class Valve:
    def __init__(self, line):
        m = re.match(r'Valve ([A-Z][A-Z]) has flow rate=([0-9]*); (?:tunnel leads to valve|tunnels lead to valves) ([A-Z, ]*)', line)
        valve = m.group(1)
        assert valve not in valves
        rate = int(m.group(2))
        tunnels = m.group(3).split(', ')

        self.name = valve
        self.rate = rate
        self.tunnels = tunnels
        self.open = False

    def __str__(self) -> str:
        return f'{self.name}: {"open" if self.open else "closed"}, rate = {self.rate}, tunnels: {self.tunnels}'

    def __repr__(self) -> str:
        return str(self)


valves = {}
for line in input.split('\n'):
    valve = Valve(line)
    valves[valve.name] = valve


@cache
def explore_tunnels(time, pos, opened):
    if time == available_time:
        return 0
    else:
        return max(traverse(time + 1, tunnel, opened) for tunnel in valves[pos].tunnels)


@cache
def traverse(time, pos, opened):
    if time == available_time:
        return 0
    else:
        best = explore_tunnels(time, pos, opened)

        if valves[pos].rate > 0 and pos not in opened:
            remaining_time = available_time - time - 1
            released = remaining_time * valves[pos].rate + explore_tunnels(time + 1, pos, opened + (pos, ))
            best = max(best, released)

        return best


released = traverse(0, 'AA', tuple())
print(released)
