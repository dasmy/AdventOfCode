input = '''Monkey 0:
  Starting items: 83, 62, 93
  Operation: new = old * 17
  Test: divisible by 2
    If true: throw to monkey 1
    If false: throw to monkey 6

Monkey 1:
  Starting items: 90, 55
  Operation: new = old + 1
  Test: divisible by 17
    If true: throw to monkey 6
    If false: throw to monkey 3

Monkey 2:
  Starting items: 91, 78, 80, 97, 79, 88
  Operation: new = old + 3
  Test: divisible by 19
    If true: throw to monkey 7
    If false: throw to monkey 5

Monkey 3:
  Starting items: 64, 80, 83, 89, 59
  Operation: new = old + 5
  Test: divisible by 3
    If true: throw to monkey 7
    If false: throw to monkey 2

Monkey 4:
  Starting items: 98, 92, 99, 51
  Operation: new = old * old
  Test: divisible by 5
    If true: throw to monkey 0
    If false: throw to monkey 1

Monkey 5:
  Starting items: 68, 57, 95, 85, 98, 75, 98, 75
  Operation: new = old + 2
  Test: divisible by 13
    If true: throw to monkey 4
    If false: throw to monkey 0

Monkey 6:
  Starting items: 74
  Operation: new = old + 4
  Test: divisible by 7
    If true: throw to monkey 3
    If false: throw to monkey 2

Monkey 7:
  Starting items: 68, 64, 60, 68, 87, 80, 82
  Operation: new = old * 19
  Test: divisible by 11
    If true: throw to monkey 4
    If false: throw to monkey 5'''

import re


monkeys = list()
for line in input.split('\n\n'):
    monkey_data = line.split('\n')

    for data in monkey_data:
        m = re.match(r'Monkey ([0-9]+):', data)
        if m is not None:
            monkey_id = int(m.group(1).strip())
            assert monkey_id == len(monkeys)
            monkeys.append({'id': monkey_id, 'inspected': 0})
            continue

        m = re.match(r'  Starting items: ([0-9, ]+)', data)
        if m is not None:
            monkeys[-1]['items'] = [int(i.strip()) for i in m.group(1).split(',')]
            continue

        m = re.match(r'  Operation: new = old ([+*]) ([0-9]+|old)', data)
        if m is not None:
            monkeys[-1]['operation'] = m.group(1).strip()
            try:
                monkeys[-1]['operand'] = int(m.group(2).strip())
            except ValueError:
                monkeys[-1]['operand'] = m.group(2)
            continue

        m = re.match(r'  Test: divisible by ([0-9, ]+)', data)
        if m is not None:
            monkeys[-1]['test'] = int(m.group(1).strip())
            continue

        m = re.match(r'    If (true|false): throw to monkey ([0-9, ]+)', data)
        if m is not None:
            monkeys[-1][m.group(1)] = int(m.group(2).strip())
            continue

        raise ValueError(f'Unexpected monkey data "{data}"')

for turn in range(20):
    print(f'Turn {turn}...')
    for monkey in monkeys:
        print(f'Monkey {monkey["id"]}:')
        for item in monkey['items']:
            monkey['inspected'] += 1

            operand = item if monkey["operand"] == 'old' else monkey["operand"]
            if monkey['operation'] == '*':
                item *= operand
                print(f'    Worry level is multiplied by {operand} to {item}.')
            elif monkey['operation'] == '+':
                item += operand
                print(f'    Worry level increases by {operand} to {item}.')
            else:
                raise ValueError(f'Unsupported operationd {monkey["operation"]}')

            item //= 3
            print(f'    Monkey gets bored with item. Worry level is divided by 3 to {item}.')

            if item % monkey['test'] == 0:
                print(f'    Current worry level is divisible by {monkey["test"]}.')
                target = monkey['true']
            else:
                print(f'    Current worry level is not divisible by {monkey["test"]}.')
                target = monkey['false']

            assert target != monkey['id']
            monkeys[target]['items'].append(item)
            print(f'    Item with worry level {item} is thrown to monkey {target}.')

        monkey['items'] = []

for monkey in monkeys:
    print(f'Monkey {monkey["id"]} ispected items {monkey["inspected"]} times.')

inspections = [monkey["inspected"] for monkey in monkeys]
inspections.sort(reverse=True)
print(inspections[0] * inspections[1])
