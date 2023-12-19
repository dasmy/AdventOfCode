import re
from day_19 import INPUT_TEST, INPUT


class Part:
    _PATTERN = re.compile(r'{([xmas])=(\d+),([xmas])=(\d+),([xmas])=(\d+),([xmas])=(\d+)}')

    def __init__(self, s):
        self.rating = 0
        m = self._PATTERN.match(s)
        assert m is not None
        g = iter(m.groups())
        for name in g:
            value = int(next(g))
            setattr(self, name, value)
            self.rating += value


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
                attr = m.group(1)
                comp = m.group(2)
                val = int(m.group(3))
                dest = m.group(4)
                if comp == '<':
                    func = lambda p, a=attr, v=val: getattr(p, a) < v
                elif comp == '>':
                    func = lambda p, a=attr, v=val: getattr(p, a) > v
                else:
                    assert False

                self.decisions.append((func, dest))
            else:
                self.decisions.append((lambda p: True, r))

    def apply(self, part):
        for d in self.decisions:
            if d[0](part):
                return d[1]
        assert False


def day_19a(inp):
    rules = {}
    parts = None
    for line in inp.split('\n'):
        if not line:
            parts = []
        elif parts is not None:
            parts.append(Part(line))
        else:
            rule = Rule(line)
            rules[rule.name] = rule

    total = 0
    for part in parts:
        rule = 'in'
        while rule not in 'AR':
            rule = rules[rule].apply(part)
        if rule == 'A':
            total += part.rating

    return total


print(day_19a(INPUT_TEST))
print(day_19a(INPUT))
