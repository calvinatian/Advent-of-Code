import sys
import re
from enum import Enum
from pprint import pprint

if len(sys.argv) > 1:
    FILENAME = "input"
else:
    FILENAME = "test"

def part1():
    data = []

    with open(FILENAME) as f:
        for line in f:
            line = line.strip()
            data.append([int(x) for x in line.split(" ")])
    print(data)


    ans = 0
    for line in data:
        to_process = [line.copy()]
        differences = [line.copy()]

        while len(to_process) > 0:
            current = to_process.pop(0)
            # calc differences between i and i+1 for all i
            new_differences = []
            for i in range(len(current)-1):
                new_differences.append((current[i+1]-current[i]))
            differences.append(new_differences)
            if new_differences != [] and not all(v == 0 for v in new_differences):
                to_process.append(new_differences)
        

        # for difference in differences:
        #     if all(v == 0 for v in difference):
        #         differences.remove(difference)
        pprint(differences)

        for i in range(len(differences) - 1, -1, -1):
            if i == len(differences) - 1:
                differences[i].append(differences[i][-1])
            elif i+1 >= 0:
                differences[i].append(differences[i][-1] + differences[i+1][-1])

        ans += differences[0][-1]

    return ans

# print(part1())

def part1():
    data = []

    with open(FILENAME) as f:
        for line in f:
            line = line.strip()
            data.append([int(x) for x in line.split(" ")])
    print(data)


    ans = 0
    for line in data:
        to_process = [line.copy()]
        differences = [line.copy()]

        while len(to_process) > 0:
            current = to_process.pop(0)
            # calc differences between i and i+1 for all i
            new_differences = []
            for i in range(len(current)-1):
                new_differences.append((current[i+1]-current[i]))
            differences.append(new_differences)
            if new_differences != [] and not all(v == 0 for v in new_differences):
                to_process.append(new_differences)
        

        # for difference in differences:
        #     if all(v == 0 for v in difference):
        #         differences.remove(difference)
        pprint(differences)

        for i in range(len(differences) - 1, -1, -1):
            if i == len(differences) - 1:
                differences[i].insert(0, differences[i][0])
            elif i+1 >= 0:
                print(differences[i+1][0], differences[i][0])
                differences[i].insert(0, differences[i][0] - differences[i+1][0])

        ans += differences[0][0]
        pprint(differences)

    return ans

print(part1())
