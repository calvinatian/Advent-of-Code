import argparse
import re
from pprint import pprint
from collections import defaultdict
from itertools import permutations, combinations

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


def p1(text):
    # print(text)
    ans = set()
    grid = []
    for line in text:
        line = line.strip()
        row = []
        for c in line:
            row.append(c)
        grid.append(row)

    pprint(grid)

    coords = defaultdict(list)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != ".":
                coords[grid[r][c]].append((r, c))

    # pprint(coords)
    for c, coords_list in coords.items():
        for perm in combinations(coords_list, 2):
            # print(perm)
            a, b = perm
            ax, ay = a
            bx, by = b

            dx = ax - bx
            dy = ay - by

            nax, nay = ax + dx, ay + dy
            nbx, nby = bx - dx, by - dy
            # print(ax, ay, bx, by, dx, dy)

            if valid(grid, nax, nay):
                ans.add((nax, nay))
                grid[nax][nay] = "#"
            if valid(grid, nbx, nby):
                ans.add((nbx, nby))
                grid[nbx][nby] = "#"
                # print((nax, nay), (nbx, nby))
    
    # pprint(grid)

    return len(ans)


def p2(text):
    # print(text)
    ans = set()
    grid = []
    for line in text:
        line = line.strip()
        row = []
        for c in line:
            row.append(c)
        grid.append(row)

    # pprint(grid)

    coords = defaultdict(list)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != ".":
                coords[grid[r][c]].append((r, c))

    # pprint(coords)
    for c, coords_list in coords.items():
        for perm in combinations(coords_list, 2):
            # print(perm)
            a, b = perm
            ax, ay = a
            bx, by = b

            dx = ax - bx
            dy = ay - by

            i = 0
            while True:
                nax, nay = ax + (i * dx), ay + (i * dy)
                nbx, nby = bx - (i * dx), by - (i * dy)
                # print(ax, ay, bx, by, dx, dy)

                av = valid(grid, nax, nay)
                if av:
                    ans.add((nax, nay))
                    grid[nax][nay] = "#"
                bv = valid(grid, nbx, nby)
                if bv:
                    ans.add((nbx, nby))
                    grid[nbx][nby] = "#"
                    # print((nax, nay), (nbx, nby))
                if not av and not bv:
                    break
                i += 1
    
    # pprint(grid)

    return len(ans)



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
