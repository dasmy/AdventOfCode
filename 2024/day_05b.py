from collections import defaultdict
from functools import cmp_to_key
from day_05inp import INPUT

RULES, PAGES = INPUT.split("\n\n")

rules = defaultdict(set)

for rule in RULES.split("\n"):
    before, after = map(int, rule.split("|"))
    rules[after].add(before)


def compare(left, right):
    if right in rules.get(left, set()):
        return +1  # left after right
    elif left in rules.get(right, set()):
        return -1  # right after left
    else:
        return 0


total = 0
for pageset in PAGES.split("\n"):
    pages = list(map(int, pageset.split(",")))
    sorted_pages = sorted(pages, key=cmp_to_key(compare))

    if sorted_pages != pages:
        midpage = sorted_pages[len(sorted_pages) // 2]
        total += midpage

print(total)
