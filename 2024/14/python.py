import argparse
import re
from pprint import pprint
from collections import defaultdict
from itertools import permutations
import math

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

def parse(text):
    robots = defaultdict(list)
    for line in text:
        line = line.strip()
        matches = re.search(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
        px = int(matches.group(1))
        py = int(matches.group(2))
        vx = int(matches.group(3))
        vy = int(matches.group(4))
        # print(px, py, vx, vy)
        robots[vx, vy].append((px, py))
    return robots

def visualize(locations, max_x, max_y):
    grid = []
    for r in range(max_y):
        row = []
        # if r == max_y // 2:
        #     grid.append([" " for _ in range(max_x)])
        #     continue
        for c in range(max_x):
            # if c == max_x // 2:
            #     row.append(" ")
            #     continue
            if (c, r) in locations:
                row.append(str(locations[c, r]))
            else:
                row.append(".")
        grid.append(row)

    for row in grid:
        print("".join(row))
    # pprint(grid)

def safety(locations, max_x, max_y):
    lx = range(0, max_x // 2)
    rx = range(max_x // 2 + 1, max_x)

    ty = range(0, max_y // 2)
    by = range(max_y // 2 + 1, max_y)

    print(lx, rx, ty, by)

    quads = [0, 0, 0, 0]
    for coord, count in locations.items():
        x, y = coord
        if x in lx and y in ty:
            # print(x, y, "1", count)
            quads[0] += count
        elif x in rx and y in ty:
            # print(x, y, "2", count)
            quads[1] += count
        elif x in lx and y in by:
            # print(x, y, "3", count)
            quads[2] += count
        elif x in rx and y in by:
            # print(x, y, "4", count)
            quads[3] += count
    return quads

def p1(text, is_test):
    # print(text)
    ans = 0
    if is_test:
        max_x = 11 # 0 1 2 3 4, 6 7 8 9 10
        max_y = 7  # 0 1 2, 4 5 6
    else:
        max_x = 101
        max_y = 103

    robots = parse(text)
    count = defaultdict(int)
    
    # do 100 seconds
    for vx, vy in robots.keys():
        for px, py in robots[vx, vy]:
            for _ in range(100):
                px += vx
                px %= max_x
                py += vy
                py %= max_y
            count[px, py] += 1
    # print(count)
    quads = safety(count, max_x, max_y)
    # print(quads)
    ans = math.prod(quads)
    # visualize(count, max_x, max_y)



    return ans


def p2(text, is_test):
    # print(text)
    ans = 0
    if is_test:
        max_x = 11 # 0 1 2 3 4, 6 7 8 9 10
        max_y = 7  # 0 1 2, 4 5 6
    else:
        max_x = 101
        max_y = 103

    robots = parse(text)
    count = defaultdict(int)

    for vx, vy in robots.keys():
        for px, py in robots[vx, vy]:
            count[px, py] += 1

    overlapping = True
    seconds = 0
    while overlapping:
        seconds += 1
        if seconds < 5:
        # if seconds % 1000 == 0:
            pprint(count)
            print(seconds)
            visualize(count, max_x, max_y)
        # else:
        #     break

        for vx, vy in robots.keys():
            new_pos = []
            for px, py in robots[vx, vy].copy():
                count[px, py] -= 1
                px += vx
                px %= max_x
                py += vy
                py %= max_y
                count[px, py] += 1
                new_pos.append((px, py))
            robots[vx, vy] = new_pos
        if all(c <= 1 for c in count.values()):
            overlapping = False

    # print(count)
    # quads = safety(count, max_x, max_y)
    # print(quads)
    # ans = math.prod(quads)
    visualize(count, max_x, max_y)

    return seconds



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--test", help="run test file", action="store_true")
    args = parser.parse_args()
    filename = "input"
    if args.test:
        filename = "test"
    text = open_file(filename)
    print(f"Part 1: {p1(text, args.test)}")
    print(f"Part 2: {p2(text, args.test)}")
