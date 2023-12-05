from collections import defaultdict
from day_05 import INPUT_TEST, INPUT


class Rule:
    def __init__(self, destination, source, len):
        self.destination = destination
        self.source = source
        self.len = len
        self.destination_end = self.destination + self.len
        self.source_end = self.source + self.len
        self.delta = self.destination - self.source

    def _apply(self, source):
        return (source - self.source) + self.destination

    def apply(self, sources):
        leftover_sources = []
        mapped_destinations = []

        for source in sources:
            input_start = source[0]
            input_end = source[1]

            if input_start < self.source:
                if input_end <= self.source:
                    #  i----i S----S
                    leftover_sources.append(source)
                elif input_end <= self.source_end:
                    #  i---S===i---S
                    leftover_sources.append((input_start, self.source))
                    mapped_destinations.append((self._apply(self.source), self._apply(input_end)))
                    pass
                else:
                    #  i---S===S---i
                    leftover_sources.append((input_start, self.source))
                    mapped_destinations.append((self._apply(self.source), self._apply(self.source_end)))
                    leftover_sources.append((self.source_end, input_end))
            elif input_start < self.source_end:
                if input_end <= self.source_end:
                    #  S---i===i---S
                    mapped_destinations.append((self._apply(input_start), self._apply(input_end)))
                else:
                    #  S---i===S---i
                    mapped_destinations.append((self._apply(input_start), self._apply(self.source_end)))
                    leftover_sources.append((self.source_end, input_end))
            else:
                #  S----S i----i
                leftover_sources.append(source)

        print(leftover_sources, mapped_destinations)
        return leftover_sources, mapped_destinations

    @classmethod
    def from_line(cls, line):
        values = line.split(' ')
        return cls(int(values[0]), int(values[1]), int(values[2]))


def day_05b(inp):
    lines = inp.split('\n')

    idx = 0
    assert lines[idx].startswith('seeds: ')
    seed_intervals = [int(s) for s in lines[idx][7:].split(' ')]

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
            maps[current_map].append(Rule.from_line(lines[idx]))

    seeds = []
    for seed_idx in range(len(seed_intervals) // 2):
        seed_start = seed_intervals[2*seed_idx]
        seed_len = seed_intervals[2*seed_idx+1]
        seeds.append((seed_start, seed_start + seed_len))

    destination = seeds
    source = seeds
    for map in MAPS:
        source = destination
        destination = []

        for rule in maps[map]:
            source, d = rule.apply(source)
            destination.extend(d)

        # transfer all unmapped as identity map
        destination.extend(source)

    return min(d[0] for d in destination)


print(day_05b(INPUT_TEST))
print(day_05b(INPUT))
