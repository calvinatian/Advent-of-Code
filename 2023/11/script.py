import sys
import re
from enum import Enum
from pprint import pprint
from collections import deque, defaultdict, Counter

if len(sys.argv) > 1:
    FILENAME = "input"
else:
    FILENAME = "test"


EXPANSION_RATE = 1000000-1
# EXPANSION_RATE = 100-1

def transpose(data):
    return [*zip(*data)]

def expand_universe(data):
    empty_rows = [i for i, line in enumerate(data) if all([x == "." for x in line])]
    empty_cols = [i for i, line in enumerate(transpose(data)) if all([x == "." for x in line])]
    print(empty_rows, empty_cols)

    row_expanded = []
    for i, line in enumerate(data):
        row_expanded.append(line)
        if i in empty_rows:
            for _ in range(EXPANSION_RATE):
                row_expanded.append(["." for _ in line])
    col_expanded = []
    for i, line in enumerate(transpose(row_expanded)):
        col_expanded.append(line)
        if i in empty_cols:
            for _ in range(EXPANSION_RATE):
                col_expanded.append(["." for _ in line])

    return transpose(col_expanded)


def part1():
    data = []

    with open(FILENAME) as f:
        for line in f:
            data.append(list(line.strip()))

    data = expand_universe(data)
    # pprint(data)
    galaxies = set()
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char == "#":
                galaxies.add((i, j))
    print(galaxies)

    # find distance to closest galaxy
    all_distances = {}
    ans = 0
    for galaxy in galaxies:
        distances = {}
        q = deque()
        q.append((galaxy[0], galaxy[1], 0))
        visited = set()
        while q:
            # print(f"{galaxy=} {q=} {visited=}")
            x, y, d = q.popleft()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            if (x, y) in galaxies and (x, y) != galaxy:
                distances[(x, y)] = d
            # else:
            for r, c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= x + r < len(data) and 0 <= y + c < len(data[0]):
                    # if (x + r, y + c) not in visited:
                    q.append((x + r, y + c, d+1))
        print(f"{galaxy=} {distances=} {len(distances)=}")
        ans += sum(distances.values())
        all_distances[galaxy] = distances
    print(f"{len(all_distances.values())=}")
    return ans // 2

# print("part1")
# print(part1())

def part2():
    data = []

    with open(FILENAME) as f:
        for line in f:
            data.append(list(line.strip()))

    # data = expand_universe(data)
    # pprint(data)
    galaxies = set()
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char == "#":
                galaxies.add((i, j))
    print(galaxies)

    # find distance to closest galaxy
    all_distances = {}
    ans = 0
    empty_rows = [i for i, line in enumerate(data) if all([x == "." for x in line])]
    empty_cols = [i for i, line in enumerate(transpose(data)) if all([x == "." for x in line])]
    for galaxy in galaxies:
        distances = defaultdict(lambda: float("inf"))
        q = deque()
        q.append((galaxy[0], galaxy[1], 0))
        visited = set()
        while q:
            # print(f"{galaxy=} {q=} {visited=}")
            x, y, d = q.popleft()
            if (x, y) in visited and (x, y) not in galaxies:
                continue
            visited.add((x, y))
            if (x, y) in galaxies and (x, y) != galaxy:
                distances[(x, y)] = min(distances[(x, y)], d)
            # else:
            for r, c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= x + r < len(data) and 0 <= y + c < len(data[0]):
                    nd = d
                    if (x+r) in empty_rows:
                        nd += EXPANSION_RATE
                    if (y+c) in empty_cols:
                        nd += EXPANSION_RATE
                    q.append((x + r, y + c, nd+1))
        # print(f"{galaxy=} {distances.items()=} {len(distances)=}")
        print(f"done gal: {galaxy} | more to go: {len(galaxies) - len(all_distances.values())}")
        ans += sum(distances.values())
        all_distances[galaxy] = distances
    print(f"{len(all_distances.values())=}")
    return ans // 2


print(part2())
