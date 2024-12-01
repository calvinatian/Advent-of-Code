import re

from z3 import If, Int, Solver

with open("input") as f:
    ls = f.read().strip().split("\n")

ns = [list(map(int, re.findall("-?\d+", x))) for x in ls]


def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


beacons = set()
cants = set()
y = 2000000
for n in ns:
    p1 = (n[0], n[1])
    p2 = (n[2], n[3])
    beacons.add(p2)
    dist = manhattan(p1, p2)
    for x in range(n[0] - dist, n[0] + dist + 1):
        if manhattan(p1, (x, y)) <= dist:
            cants.add((x, y))

print(len(cants - beacons))


# Part 2
def z3abs(x):
    return If(x >= 0, x, -x)


s = Solver()
x = Int("x")
y = Int("y")
s.add(x >= 0)
s.add(x <= 4000000)
s.add(y >= 0)
s.add(y <= 4000000)
for n in ns:
    dist = manhattan((n[0], n[1]), (n[2], n[3]))
    s.add(z3abs(x - n[0]) + z3abs(y - n[1]) > dist)

s.check()
model = s.model()
print(model[x].as_long() * 4000000 + model[y].as_long())
