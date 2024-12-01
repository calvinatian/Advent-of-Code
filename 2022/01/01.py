from aocd import get_data
from aocd import submit
# from aocd import lines  # like data.splitlines()
# from aocd import numbers  # uses regex pattern -?\d+ to extract integers from data

data = get_data(day=1, year=2022)

with open("input.in", "r") as f:
    data = f.readlines()
elves = []
total = 0
i = 0
for line in data:
    line = line.strip()
    # print(line)
    if line == "":
        elves.append((total, i))
        i += 1
        total = 0
    else:
        total += int(line)
elves.append((total, i))
elves.sort()
# print(elves)

a = elves[-1][0]
print(a)

b = sum([x[0] for x in elves[-1:-4:-1]])
print(b)
def submit_answer(ans, part):
    submit(ans, part=part)

if __name__ == "__main__":
    # submit_answer(a, part="a")
    # submit_answer(b, part="b")
    pass
