# from aocd import get_data
# from aocd import submit
# from aocd import lines  # like data.splitlines()
# from aocd import numbers  # uses regex pattern -?\d+ to extract integers from data

# data = get_data(day=3, year=2022)

from string import ascii_lowercase, ascii_uppercase
# from float import inf
import math
from pprint import pprint
from collections import deque

def p1(name):
    matrix = []
    with open(name, "r") as f:
        for line in f:
            line = line.strip()
            matrix.append([x for x in line])
    print(len(matrix), len(matrix[0]))

    # find E
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == "E":
                end = (r, c)
                break

    # find S
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == "S":
                start = (r, c)
                break

    # find path from S to E
    # path_len = 0
    # checked = {}
    checked = set()
    matrix[end[0]][end[1]] = "z"
    matrix[start[0]][start[1]] = "a"

    # to_check = [(0, 0, 0)]
    to_check = deque()
    # to_check.append((0, 0, 0))
    to_check.append((start[0], start[1], 0))
    while to_check:
        # pos = to_check.pop(0)
        pos = to_check.popleft()
        r, c, length = pos

        if (r, c) == end:
            return length
        if (r, c) in checked:
            continue
        checked.add((r, c))

        # for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
        for nr, nc in [(r, c+1), (r+1, c), (r, c-1), (r-1, c)]:

            if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]):
                # if ord(matrix[nr][nc]) <= ord(matrix[r][c]) + 1:
                if ord(matrix[nr][nc]) - ord(matrix[r][c]) <= 1:
                    # if (nr, nc) not in checked:
                    # checked.add((nr, nc))
                        # checked[(nr, nc)] = length + 1
                        # checked[(nr, nc)] = length + 1checked[(r, c)] + 1
                    to_check.append((nr, nc, length + 1))
                    # else:
                    #     checked[(nr, nc)] = min(checked[(nr, nc)], checked[(r, c)] + 1)
                    #     to_check.append((nr, nc))

    # pprint(checked)
    print(end)
    # print(max(checked.values()))
    # return checked[(end[0], end[1])]

def p2(name):
    matrix = []
    with open(name, "r") as f:
        for line in f:
            line = line.strip()
            matrix.append([x for x in line])
    print(len(matrix), len(matrix[0]))

    # find E
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == "E":
                end = (r, c)
                break

    # find S's
    starts = []
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == "S" or matrix[r][c] == "a":
                starts.append((r, c))
                matrix[r][c] = "a"
                # break

    # find path from S to E
    checked = set()
    matrix[end[0]][end[1]] = "z"
    # matrix[start[0]][start[1]] = "a"

    to_check = deque()
    # to_check.append((start[0], start[1], 0))
    for start in starts:
        to_check.append((start[0], start[1], 0))
    while to_check:
        # pos = to_check.pop(0)
        pos = to_check.popleft()
        r, c, length = pos

        if (r, c) == end:
            return length
        if (r, c) in checked:
            continue
        checked.add((r, c))

        for nr, nc in [(r, c+1), (r+1, c), (r, c-1), (r-1, c)]:
            if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]):
                if ord(matrix[nr][nc]) - ord(matrix[r][c]) <= 1:

                    to_check.append((nr, nc, length + 1))


    # pprint(checked)
    print(end)
    # print(max(checked.values()))
    # return checked[(end[0], end[1])]

print(p1("test"))
print(p1("input"))
print(p2("test"))
print(p2("input"))

# if __name__ == "__main__":
#     def submit_answer(ans, part):
#         submit(ans, part=part)
#     # submit_answer(a, part="a")
#     # submit_answer(b, part="b")
#     pass
