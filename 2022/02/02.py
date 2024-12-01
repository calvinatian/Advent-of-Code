from aocd import get_data
from aocd import submit
# from aocd import lines  # like data.splitlines()
# from aocd import numbers  # uses regex pattern -?\d+ to extract integers from data

data = get_data(day=2, year=2022)

with open("input.in", "r") as f:
    data = f.readlines()

elves = []
total = 0
i = 0

tie = ["AX", "BY", "CZ"]
win = ["CX", "AY", "BZ"]
lose = ["AY", "BZ", "CX"]
total = 0
for line in data:
    line = line.strip()
    # print(line.split())
    a, b = line.split()
    combo = f"{a}{b}"
    points = "-XYZ".index(b)
    total += points
    # print(combo)
 
    if combo in win:
        total += 6
    elif combo in tie:
        total += 3
    else:
        total += 0

print(total)
# print(elves)

"lose draw win"
a = "ABC"
b = "XYZ"
# lose + 2
# tie = same
# win + 1

total = 0
for line in data:
    line = line.strip()
    # print(line.split())
    x, y = line.split()
    combo = f"{x}{y}"
    # total += points
    # print(combo)

    v = a.index(x)
    # points = b.index((v + 2) % 3) + 1
    # print(v)
    if y == "X":
        total += ((v + 2) % 3) + 1
        total += 0
        print("lose", v, total)
    elif y == "Y":
        total += (v) + 1
        total += 3
        print("draw", v, total)
    else:
        total += ((v + 1) % 3) + 1
        total += 6
        print("wom", v, total)
    # print(total)

print(total)

if __name__ == "__main__":
    def submit_answer(ans, part):
        submit(ans, part=part)
    # submit_answer(a, part="a")
    # submit_answer(b, part="b")
    pass
