from collections import deque
from itertools import count
from math import lcm
from day_20 import INPUT
from typing import Dict


class Module:
    def __init__(self, name, output):
        self.name = name
        self.output = output.split(', ')

    def __call__(self, source, pulse):
        raise NotImplemented


class Broadcaster(Module):
    def __call__(self, source, pulse):
        return [(self.name, o, pulse) for o in self.output]


class FlipFlop(Module):
    def __init__(self, name, output):
        super().__init__(name, output)
        self.state = False

    def __call__(self, source, pulse):
        if pulse:
            return []
        else:
            self.state = not self.state
            return [(self.name, o, self.state) for o in self.output]


class Conjunction(Module):
    def __init__(self, name, output):
        super().__init__(name, output)
        self.input_states = None

    def set_inputs(self, inputs):
        assert self.input_states is None
        self.input_states = dict((inp, False) for inp in inputs)

    def __call__(self, source, pulse):
        assert source in self.input_states
        self.input_states[source] = pulse

        out = not all(s for s in self.input_states.values())
        return [(self.name, o, out) for o in self.output]


def day_20b(inp):
    modules: Dict[str, Module] = {}
    flipflops = {}

    for line in inp.split('\n'):
        module, output = line.split(' -> ')
        if module == 'broadcaster':
            m = Broadcaster(module, output)
        elif module[0] == '%':
            m = FlipFlop(module[1:], output)
        elif module[0] == '&':
            m = Conjunction(module[1:], output)
            flipflops[m.name] = []

        modules[m.name] = m

    for name, module in modules.items():
        for o in module.output:
            if o in flipflops:
                flipflops[o].append(name)

    for name, inputs in flipflops.items():
        modules[name].set_inputs(inputs)

    # &ns &vd &bh &dl lead to &zh -> rx
    # thus, the all must get low input at the same button press instance
    # to turn the input of &zh high and thus rx low
    # --> assume things are cyclic and compute the lcm in the end
    first_low = {
        'ns': None,
        'vd': None,
        'bh': None,
        'dl': None,
    }

    for i in count(start=1):
        todo = deque([('start', 'broadcaster', False), ])
        while todo:
            source, target, pulse = todo.popleft()

            if target in first_low and not pulse:
                if first_low[target] is None:
                    first_low[target] = i
                    print(first_low)

                if all(f is not None for f in first_low.values()):
                    return lcm(*first_low.values())

            if target == 'rx' and not pulse:
                return i
            else:
                try:
                    new_pulses = modules[target](source, pulse)
                    todo.extend(new_pulses)
                except KeyError:
                    pass
                    # print(f'Dangling node {target} from {source} with pulse {pulse} on button presse {i}')

    return 0


print(day_20b(INPUT))
