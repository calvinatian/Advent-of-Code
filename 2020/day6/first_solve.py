# Part 1: 6911
# Part 2: 3473

path = r"2020\day6\input.txt"
# path = r"2020\day6\test.txt"
with open(path, "r") as f:
    data = []
    data_temp = []
    people = 0
    for line in f:
        # print(line)
        if line == "\n":
            data.append((data_temp, people))
            data_temp = []
            people = 0
            # print("d")
        else:
            data_temp += list(line.strip())
            people += 1
    # print(data)

count = 0
for i in data:
    answers = set(i[0])
    count += len(answers)

print(count)


count = 0

for i in data:
    # print(i)
    people = i[1]
    storage = {}
    for j in i[0]:
        # print(j)
        try:
            storage[j] += 1
        except KeyError:
            storage[j] = 1
    for k in storage:
        # print(storage[k], people, k)
        if storage[k] == people:
            count += 1

print(count)