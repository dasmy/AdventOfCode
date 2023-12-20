from collections import deque
from day_20 import INPUT_TEST, INPUT_TEST_2, INPUT
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


def day_20a(inp):
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

    num_pulses = {True: 0, False: 0}
    for _ in range(1000):
        todo = deque([('start', 'broadcaster', False), ])
        num_pulses[False] += 1
        while todo:
            source, target, pulse = todo.popleft()
            try:
                new_pulses = modules[target](source, pulse)
                for p in new_pulses:
                    num_pulses[p[2]] += 1
                todo.extend(new_pulses)
            except KeyError:
                print(f'Dangling node {target}')

    return num_pulses, num_pulses[True] * num_pulses[False]


print(day_20a(INPUT_TEST))
print(day_20a(INPUT_TEST_2))
print(day_20a(INPUT))
