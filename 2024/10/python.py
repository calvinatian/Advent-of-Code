import argparse
import re
from pprint import pprint
from collections import defaultdict
from itertools import permutations

def open_file(filename):
    with open(filename) as f:
        return f.readlines()
    
def valid(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])

def recur(grid, r, c, seen):
    if (r, c) in seen:
        return
    if (r < len(grid) or c < len(grid[0])):
        return

def travel(grid, r, c, prev, seen):
    if not valid(grid, r, c) or (r, c) in seen:
        return 0


    if prev == "8" and grid[r][c] == "9" and (r, c) not in seen:
        seen.add((r, c))
        return 1

    current = grid[r][c]
    if current != str(int(prev) + 1):
        return 0

    total = 0
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr = r + dr
        nc = c + dc
        score = travel(grid, nr, nc, current, seen)
        # seen.update(updated_seen)
        # print(score)
        total += score
    return total


def p1(text):
    # print(text)
    ans = 0
    grid = []
    for line in text:
        line = line.strip()
        row = [c for c in line]
        grid.append(row)

    # pprint(grid)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "0":
                ans += travel(grid, r, c, "-1", set())

    return ans

def travel2(grid, r, c, prev, seen):
    if not valid(grid, r, c) or (r, c) in seen:
        return 0


    if prev == "8" and grid[r][c] == "9" and (r, c) not in seen:
        seen.add((r, c))
        return 1

    current = grid[r][c]
    if current != str(int(prev) + 1):
        return 0

    total = 0
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr = r + dr
        nc = c + dc
        score = travel2(grid, nr, nc, current, seen.copy())
        # seen.update(updated_seen)
        # print(score)
        total += score
    return total

def p2(text):
    # print(text)
    ans = 0
    grid = []
    for line in text:
        line = line.strip()
        row = [c for c in line]
        grid.append(row)

    # pprint(grid)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "0":
                ans += travel2(grid, r, c, "-1", set())

    return ans



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--test", help="run test file", action="store_true")
    args = parser.parse_args()
    filename = "input"
    if args.test:
        filename = "test"
    text = open_file(filename)
    print(f"Part 1: {p1(text)}")
    print(f"Part 2: {p2(text)}")
