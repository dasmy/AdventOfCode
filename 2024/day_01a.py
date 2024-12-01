from day_01inp import INPUT

list1 = []
list2 = []

for row in INPUT.split("\n"):
    a, b = row.split()
    list1.append(int(a))
    list2.append(int(b))

total = 0
for a, b in zip(sorted(list1), sorted(list2)):
    total += abs(a - b)

print(total)
