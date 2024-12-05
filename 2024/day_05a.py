from collections import defaultdict
from day_05inp import INPUT

RULES, PAGES = INPUT.split("\n\n")

rules = defaultdict(set)

for rule in RULES.split("\n"):
    before, after = map(int, rule.split("|"))
    rules[after].add(before)


total = 0
for pageset in PAGES.split("\n"):
    pages = list(map(int, pageset.split(",")))
    for i in range(len(pages)):
        before = pages[i]
        after = set(pages[i + 1 :])
        if rules[before].intersection(after):
            break  # rule violated
    else:
        midpage = pages[len(pages) // 2]
        total += midpage

print(total)
