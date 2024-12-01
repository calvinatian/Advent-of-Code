# from aocd import get_data
# from aocd import submit
# from aocd import lines  # like data.splitlines()
# from aocd import numbers  # uses regex pattern -?\d+ to extract integers from data

# data = get_data(day=3, year=2022)

import math
from pprint import pprint
from string import ascii_lowercase, ascii_uppercase
from collections import deque, defaultdict

def printgrid(grid):
    for row in grid:
        print("".join(row))
    print()

def p1(name):
    rlen = 1000
    clen = 1000
    # rlen = 20
    # clen = 20
    grid = [["." for _ in range(clen)] for _ in range(rlen)]
    with open(name, "r") as f:
        for line in f:
            prevx = -1
            prevy = -1
            line = line.strip()
            line = line.split(" -> ")
            for coord in line:
                coord = coord.split(",")
                x = int(coord[0])
                y = int(coord[1])
                grid[y][x] = "#"
                if prevx == x:
                    # draw col
                    for ny in range(min(y, prevy), max(y, prevy)):
                        # print(x, ny)
                        grid[ny][x] = "#"
                elif prevy == y:
                    # draw row
                    for nx in range(min(x, prevx), max(x, prevx)):
                        # print(nx, y)
                        grid[y][nx] = "#"
                prevx = x
                prevy = y
    # printgrid(grid)

    # simulate sand
    cont = True
    sand_units = 0
    while cont:
        sandx = 500
        # sandx = 7
        sandy = 0
        iteration = 0
        while sandy < len(grid) and sandx < len(grid[0]):
            if iteration > 450:
                cont = False
                break
            iteration += 1
            # move down
            if (0 <= sandy+1 < len(grid) and 0 <= sandx < len(grid[0])) and grid[sandy+1][sandx] == ".":
                sandy += 1
            # move left
            elif (0 <= sandy+1 < len(grid) and 0 <= sandx-1 < len(grid[0])) and grid[sandy+1][sandx-1] == ".":
                sandx -= 1
                sandy += 1
            # move right
            elif (0 <= sandy+1 < len(grid) and 0 <= sandx+1 < len(grid[0])) and grid[sandy+1][sandx+1] == ".":
                sandx += 1
                sandy += 1
            # stop
            else:
                grid[sandy][sandx] = "o"
                sand_units += 1
                break
        if not cont:
            break
        # if sandy >= len(grid) or sandx >= len(grid[0]):
        #     cont = False
    # printgrid(grid)
    return sand_units

def p2(name):
    rlen = 1000
    clen = 2000
    xoffset = 500
    # rlen = 30
    # clen = 30
    maxy = 0
    grid = [["." for _ in range(clen)] for _ in range(rlen)]
    with open(name, "r") as f:
        for line in f:
            prevx = -1
            prevy = -1
            line = line.strip()
            line = line.split(" -> ")
            for coord in line:
                coord = coord.split(",")
                x = int(coord[0]) + xoffset
                y = int(coord[1])
                maxy = max(maxy, y)
                grid[y][x] = "#"
                if prevx == x:
                    # draw col
                    for ny in range(min(y, prevy), max(y, prevy)):
                        # print(x, ny)
                        grid[ny][x] = "#"
                elif prevy == y:
                    # draw row
                    for nx in range(min(x, prevx), max(x, prevx)):
                        # print(nx, y)
                        grid[y][nx] = "#"
                prevx = x
                prevy = y
    # printgrid(grid)

    # add floor
    floory = maxy + 2
    for x in range(clen):
        grid[floory][x] = "#"

    # simulate sand
    sand_units = 0
    while grid[0][500 + xoffset] != "o":
    # while grid[0][17] != "o":
        sandx = 500 + xoffset
        # printgrid(grid)
        # sandx = 17
        sandy = 0
        while sandy < len(grid) and sandx < len(grid[0]):
            # move down
            if (0 <= sandy+1 < len(grid) and 0 <= sandx < len(grid[0])) and grid[sandy+1][sandx] == ".":
                sandy += 1
            # move left
            elif (0 <= sandy+1 < len(grid) and 0 <= sandx-1 < len(grid[0])) and grid[sandy+1][sandx-1] == ".":
                sandx -= 1
                sandy += 1
            # move right
            elif (0 <= sandy+1 < len(grid) and 0 <= sandx+1 < len(grid[0])) and grid[sandy+1][sandx+1] == ".":
                sandx += 1
                sandy += 1
            # stop
            else:
                grid[sandy][sandx] = "o"
                sand_units += 1
                break

        # if sandy >= len(grid) or sandx >= len(grid[0]):
        #     cont = False
    # printgrid(grid)
    return sand_units

# pprint(f'{p1("test")=}')
# pprint(f'{p1("input")=}')
# pprint(f'{p2("test")=}')
pprint(f'{p2("test2.txt")=}')
pprint(f'{p2("input")=}')

# if __name__ == "__main__":
#     def submit_answer(ans, part):
#         submit(ans, part=part)
#     # submit_answer(a, part="a")
#     # submit_answer(b, part="b")
#     pass
