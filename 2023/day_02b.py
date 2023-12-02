from day_02 import EVIDEMCE, INPUT_TEST, INPUT


class Game:
    def __init__(self, game):
        game_id, draws = game.split(':')
        self.id = int(game_id[5:])
        self.max = {'red': 0, 'green': 0, 'blue': 0}
        for draw in draws.split(';'):
            for cubes in draw.split(','):
                for key, c in self.max.items():
                    if cubes.endswith(key):
                        count = int(cubes[:-len(key)-1])
                        self.max[key] = max(c, count)
                        break
                else:
                    raise ValueError(cubes)

    def power(self):
        p = 1
        for v in self.max.values():
            p *= v
        return p

    def __str__(self):
        values = ', '.join(f'{v} {k}' for (k, v) in self.max.items())
        return f'--> Game {self.id}: {values}'


def day_02a(inp):
    total = 0
    for g in inp.split('\n'):
        game = Game(g)
        total += game.power()

    return total


print(day_02a(INPUT_TEST))
print(day_02a(INPUT))
