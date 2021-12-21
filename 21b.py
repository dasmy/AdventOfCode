from itertools import product
from collections import defaultdict

# pre-tabulate the possible sums with three dice rolls and their multiplicity
MOVES = defaultdict(int)
for roll in product([1, 2, 3], repeat=3):
    MOVES[sum(roll)] += 1


def turn(pos1, pos2, score1=0, score2=0):
    if not hasattr(turn, 'cache'):
        turn.cache = {}

    try:
        return turn.cache[(pos1, pos2, score1, score2)]
    except KeyError:
        win1, win2 = 0, 0

        for move, count in MOVES.items():
            p1 = (pos1 - 1 + move) % 10 + 1
            s1 = score1 + p1
            if s1 >= 21:
                win1 += count
            else:
                w2, w1 = turn(pos2, p1, score2, s1)
                win1 += count*w1
                win2 += count*w2

        turn.cache[(pos1, pos2, score1, score2)] = (win1, win2)
        return win1, win2


def play(p1, p2):
    print(turn(p1, p2))


play(4, 8)
play(5, 8)
