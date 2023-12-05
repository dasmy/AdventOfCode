from collections import defaultdict
from day_05 import INPUT_TEST, INPUT

class Rule:
    def __init__(self, line):
        values = line.split(' ')
        self.destination = int(values[0])
        self.source = int(values[1])
        self.len = int(values[2])

    def applies(self, source):
        return self.source <= source < self.source + self.len

    def apply(self, source):
        return (source - self.source) + self.destination


def day_05a(inp):
    lines = inp.split('\n')

    idx = 0
    assert lines[idx].startswith('seeds: ')
    seeds = [int(s) for s in lines[idx][7:].split(' ')]

    MAPS = [
        'seed-to-soil map:',
        'soil-to-fertilizer map:',
        'fertilizer-to-water map:',
        'water-to-light map:',
        'light-to-temperature map:',
        'temperature-to-humidity map:',
        'humidity-to-location map:',
    ]

    maps = defaultdict(list)

    current_map = None
    for idx in range(1, len(lines)):
        if not lines[idx]:
            current_map = None
        elif lines[idx] in MAPS:
            current_map = lines[idx]
        else:
            maps[current_map].append(Rule(lines[idx]))

    lowest_location = 1e43
    for seed in seeds:
        source = seed
        for map in MAPS:
            for rule in maps[map]:
                if rule.applies(source):
                    destination = rule.apply(source)
                    break
            else:
                destination = source  # just to make that explicit here

            print(map, source, destination)
            source = destination

        lowest_location = min(lowest_location, source)
        print(source)

    return lowest_location


print(day_05a(INPUT_TEST))
print(day_05a(INPUT))
