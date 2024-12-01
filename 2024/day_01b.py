from day_01inp import INPUT

from collections import Counter

list1 = []
list2 = []

for row in INPUT.split("\n"):
    a, b = row.split()
    list1.append(int(a))
    list2.append(int(b))

c = Counter(list2)

total = 0
for a in list1:
    total += a * c[a]

print(total)
