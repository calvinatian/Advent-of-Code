import argparse
import re
from pprint import pprint

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
    ans = 0
    grid = []
    for line in text:
        line = line.strip()
        row = []
        for c in line:
            row.append(c)
        grid.append(row)

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "X":
                # check hor
                hor = True
                for i in range(1, 4):
                    nr = r + i
                    if not valid(grid, nr, c):
                        hor = False
                if hor and grid[r+1][c] == "M" and grid[r+2][c] == "A" and grid[r+3][c] == "S":
                        ans += 1

                # check vertical
                hor = True
                for i in range(1, 4):
                    nc = c + i
                    if not valid(grid, r, nc):
                        hor = False
                if hor and grid[r][c+1] == "M" and grid[r][c+2] == "A" and grid[r][c+3] == "S":
                        ans += 1

                # check diagonal dr
                hor = True
                for i in range(1, 4):
                    nc = c + i
                    nr = r + i
                    if not valid(grid, nr, nc):
                        hor = False
                if hor and grid[r+1][c+1] == "M" and grid[r+2][c+2] == "A" and grid[r+3][c+3] == "S":
                        ans += 1

                # check diagonal dl
                hor = True
                for i in range(1, 4):
                    nc = c - i
                    nr = r + i
                    if not valid(grid, nr, nc):
                        hor = False
                if hor and grid[r+1][c-1] == "M" and grid[r+2][c-2] == "A" and grid[r+3][c-3] == "S":
                        ans += 1

                # check diagonal ur
                hor = True
                for i in range(1, 4):
                    nc = c + i
                    nr = r - i
                    if not valid(grid, nr, nc):
                        hor = False
                if hor and grid[r-1][c+1] == "M" and grid[r-2][c+2] == "A" and grid[r-3][c+3] == "S":
                        ans += 1

                # check backwards
                hor = True
                for i in range(1, 4):
                    nr = r - i
                    if not valid(grid, nr, c):
                        hor = False
                if hor and grid[r-1][c] == "M" and grid[r-2][c] == "A" and grid[r-3][c] == "S":
                        ans += 1

                # check vertical
                hor = True
                for i in range(1, 4):
                    nc = c - i
                    if not valid(grid, r, nc):
                        hor = False
                if hor and grid[r][c-1] == "M" and grid[r][c-2] == "A" and grid[r][c-3] == "S":
                        ans += 1

                # check diagonal ul
                hor = True
                for i in range(1, 4):
                    nc = c - i
                    nr = r - i
                    if not valid(grid, nr, nc):
                        hor = False
                if hor and grid[r-1][c-1] == "M" and grid[r-2][c-2] == "A" and grid[r-3][c-3] == "S":
                        ans += 1

    return ans


def p2(text):
    # print(text)
    ans = 0
    """
    S S
     A
    M M
    """
    grid = []
    for line in text:
        line = line.strip()
        row = []
        for c in line:
            row.append(c)
        grid.append(row)

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "A":
                # check s top
                hor = True
                for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    nr = r + dr
                    nc = c + dc
                    if not valid(grid, nr, nc):
                        hor = False

                if hor:
                    dr = grid[r+1][c+1]  # down_right
                    dl = grid[r+1][c-1]  # down_left
                    ur = grid[r-1][c+1]  # up_right
                    ul = grid[r-1][c-1]  # up_left
                    if ul == ur == "S" and dr == dl == "M":
                        ans += 1
                    elif ul == dl == "S" and dr == ur == "M":
                        ans += 1
                    elif ul == ur == "M" and dr == dl == "S":
                        ans += 1
                    elif ul == dl == "M" and dr == ur == "S":
                        ans += 1

                    # elif ul == dr == "S" and ur == dl == "M":
                    #      ans += 1
                    # elif ul == dr == "M" and ur == dl == "S":
                    #      ans += 1

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
