import argparse
import re
from pprint import pprint
from collections import defaultdict
from itertools import permutations
from copy import deepcopy

def open_file(filename):
    with open(filename) as f:
        return f.readlines()

def recur(grid, r, c, seen):
    if (r, c) in seen:
        return
    if (r < len(grid) or c < len(grid[0])):
        return

def find_start(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "^":
                return (r, c)

def in_bounds(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])

def not_obstacle(grid, r, c):
    return grid[r][c] != "#"

def visualize(grid, visited):
    grid = deepcopy(grid)
    for r, c in visited:
        grid[r][c] = "x"
    pprint(grid)


def p1(text):
    # print(text)
    ans = 0
    grid = []
    for line in text:
        line = line.strip()
        grid.append([c for c in line])
    
    pos_r, pos_c = find_start(grid)
    dir = 3
    visited = set()
    while in_bounds(grid, pos_r, pos_c):
        visited.add((pos_r, pos_c))
        match dir:
            case 0:  # right
                nc = pos_c + 1
                if not in_bounds(grid, pos_r, nc):
                    break
                if not_obstacle(grid, pos_r, nc):
                    pos_c = nc
                else:
                    dir += 1
                    dir %= 4
            case 1:  # down
                nr = pos_r + 1
                if not in_bounds(grid, nr, pos_c):
                    break
                if not_obstacle(grid, nr, pos_c):
                    pos_r = nr
                else:
                    dir += 1
                    dir %= 4
            case 2:  # left
                nc = pos_c - 1
                if not in_bounds(grid, pos_r, nc):
                    break
                if not_obstacle(grid, pos_r, nc):
                    pos_c = nc
                else:
                    dir += 1
                    dir %= 4
            case 3:  # up
                nr = pos_r - 1
                if not in_bounds(grid, nr, pos_c):
                    break
                if not_obstacle(grid, nr, pos_c):
                    pos_r = nr
                else:
                    dir += 1
                    dir %= 4
            

    # pprint(grid)
    # visualize(grid, visited)
    return len(visited)


def is_loop(grid, pos_r, pos_c):
    start_r = pos_r
    start_c = pos_c
    dir = 3
    visited = set()
    while in_bounds(grid, pos_r, pos_c):
        if (pos_r, pos_c, dir) in visited:
            print((pos_r, pos_c, dir))
            return True

        visited.add((pos_r, pos_c, dir))
        match dir:
            case 0:  # right
                nc = pos_c + 1
                if not in_bounds(grid, pos_r, nc):
                    break
                if not_obstacle(grid, pos_r, nc):
                    pos_c = nc
                else:
                    dir += 1
                    dir %= 4
            case 1:  # down
                nr = pos_r + 1
                if not in_bounds(grid, nr, pos_c):
                    break
                if not_obstacle(grid, nr, pos_c):
                    pos_r = nr
                else:
                    dir += 1
                    dir %= 4
            case 2:  # left
                nc = pos_c - 1
                if not in_bounds(grid, pos_r, nc):
                    break
                if not_obstacle(grid, pos_r, nc):
                    pos_c = nc
                else:
                    dir += 1
                    dir %= 4
            case 3:  # up
                nr = pos_r - 1
                if not in_bounds(grid, nr, pos_c):
                    break
                if not_obstacle(grid, nr, pos_c):
                    pos_r = nr
                else:
                    dir += 1
                    dir %= 4

        # if pos_r == start_r and pos_c == start_c and dir == 3:
        #     return True

    return False

def p2(text):
    print(text)
    ans = 0
    grid = []
    for line in text:
        line = line.strip()
        grid.append([c for c in line])
    
    start_r, start_c = find_start(grid)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            new_grid = deepcopy(grid)
            if grid[r][c] == ".":
                new_grid[r][c] = "#"
                # visualize(new_grid, set())
                if is_loop(new_grid, start_r, start_c):
                    ans += 1


    # pprint(grid)
    # visualize(grid, visited)
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
