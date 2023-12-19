import re
from day_19 import INPUT_TEST, INPUT


class PartInterval:
    def __init__(self, other: 'PartInterval' = None, modified_ranges: dict = None):
        self.ranges = {
            'x': (1, 4001),
            'm': (1, 4001),
            'a': (1, 4001),
            's': (1, 4001),
        }

        if other is not None:
            self.ranges.update(other.ranges)

        if modified_ranges is not None:
            self.ranges.update(modified_ranges)

    def split(self, attr, comp, value):
        oldrange = self.ranges[attr]
        if comp == '<':
            if oldrange[1] <= value:
                return self, None
            elif oldrange[0] > value:
                return None, self
            else:
                return \
                    PartInterval(other=self, modified_ranges={attr: (oldrange[0], value)}), \
                    PartInterval(other=self, modified_ranges={attr: (value, oldrange[1])})
        elif comp == '>':
            if oldrange[0] > value:
                return self, None
            elif oldrange[1] <= value:
                return None, self
            else:
                return \
                    PartInterval(other=self, modified_ranges={attr: (value+1, oldrange[1])}), \
                    PartInterval(other=self, modified_ranges={attr: (oldrange[0], value+1)})
        else:
            assert False

    def __repr__(self):
        return str(self.ranges)

    def count(self):
        total = 1
        for rmin, rmax in self.ranges.values():
            assert rmax > rmin
            total *= rmax - rmin

        return total


class Rule:
    _NAME_PATTERN = re.compile(r'([a-z]+){([^}]+)}')
    _RULE_PATTERN = re.compile(r'([xmas]+)([<>=])(\d+):([ARa-z]+)')

    def __init__(self, s):
        m = self._NAME_PATTERN.match(s)
        assert m is not None
        self.name = m.group(1)
        self.decisions = []
        rules = m.group(2)
        for r in rules.split(','):
            m = self._RULE_PATTERN.match(r)
            if m is not None:
                self.decisions.append((
                    {
                        'attr': m.group(1),
                        'comp': m.group(2),
                        'value': int(m.group(3)),
                    }, m.group(4)))
            else:
                self.decisions.append(r)

    def apply(self, part: PartInterval):
        out = []

        for d in self.decisions:
            if part is not None:
                if isinstance(d, tuple):
                    p_true, p_false = part.split(**d[0])
                    if p_true is not None:
                        out.append((d[1], p_true))
                    part = p_false
                else:
                    out.append((d, part))

        return out


def day_19b(inp):
    rules = {}
    for line in inp.split('\n'):
        if not line:
            break
        else:
            rule = Rule(line)
            rules[rule.name] = rule

    parts = [('in', PartInterval())]
    accepted_parts = []
    while parts:
        print(parts)
        new_parts = []
        for rule, part in parts:
            if rule == 'A':
                accepted_parts.append(part)
            elif rule == 'R':
                pass
            else:
                new_parts.extend(rules[rule].apply(part))

        parts = new_parts

    return sum(p.count() for p in accepted_parts)


print(day_19b(INPUT_TEST))
print(day_19b(INPUT))
