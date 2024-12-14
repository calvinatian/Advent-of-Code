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

# def recur(grid, r, c, seen):
#     if (r, c) in seen:
#         return
#     if (r < len(grid) or c < len(grid[0])):
#         return

def island_size(grid, r, c, let, area, seen):
    if not valid(grid, r, c):
        return area, seen
    
    if grid[r][c] != let or (r, c) in seen:
        return area, seen
    
    seen.add((r, c))
    area += 1
    for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        nr = dr + r
        nc = dc + c
        # print(nr, nc)
        new_area, connected = island_size(grid, nr, nc, let, area, seen)
        seen.update(connected)
        area = new_area
    return area, seen

def get_perimeter(visited):
    perim = 0
    for r, c in visited:
        for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            nr = dr + r
            nc = dc + c
            if (nr, nc) in visited:
                perim -= 1
        perim += 4
    return perim

# def get_sides(visited, grid):
#     sides = 0
#     removed = visited.copy()
#     for r, c in visited:
#         if (r, c) in removed:
#             sides += 4

#         # get connected pieces
#         # left
#         nr = r
#         while 0 <= nr:
#             nr -= 1
#             if (nr, c) in removed:
#                 removed.remove((nr, c))
#         # right
#         nr = r
#         while nr < len(grid):
#             nr += 1
#             if (nr, c) in removed:
#                 removed.remove((nr, c))
#         # up
#         nc = c
#         while 0 <= nc:
#             nc -= 1
#             if (r, nc) in removed:
#                 removed.remove((r, nc))
#         # down
#         nc = c
#         while nc < len(grid[0]):
#             nc += 1
#             if (r, nc) in removed:
#                 removed.remove((r, nc))

#     return sides

def p1(text):
    # print(text)
    ans = 0
    grid = []
    for line in text:
        line = line.strip()
        grid.append([x for x in line])

    # pprint(grid)
    seen = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) not in seen:
                area, connected = island_size(grid, r, c, grid[r][c], 0, set())
                seen.update(connected)
                perim = get_perimeter(connected)
                # print(grid[r][c], (r, c), area, perim, connected)
                ans += area * perim

    return ans


"""


EEEEE
EXXXX
EEEEE
EXXXX
EEEEE

  t
 l r
  d

tl, td, td, td, trd - 4   - 1t, 1d, 1r
lr                  - 2   
l, td, td, td, trd  - 4
lr,                 - 2
ld, td, td, td, trd - 4

4   2   2   2   3


tl, td, td, td, trd - 1t, 1d, 1r  , 1l?
lr                  - 1r
l, td, td, td, trd  - 1t, 1d, 1r
lr,                 - 1r
ld, td, td, td, trd - 1t, 1d, 1r

share with up?
  - dont count l r
share with left?
  - dont count t d

  
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA


t l , t   , t   , td  , td  , t  r  - 1t1l1d1r = 4
  l ,  _  ,    r,  _  ,  _  ,   lr  - 1l1r     = 2
  l ,  d  ,  d r, _   , _   .   lr  - 1d       = 1
  lr,  _  ,  _  , t l , t   ,    r  - 1r1t1l   = 3
  lr,  _  ,  _  ,   l ,  _  ,    r  -          = 0
 dl , td  , td  ,  d  ,  d  ,  d r  - 1d1t     = 2

 11?
"""
def list_xor(curr, top, left):
    res = []
    for c, t, l in zip(curr, top, left):
        if c == 1 and t == l == 0:
            res.append(1)
        else:
            res.append(0)
    return res

def get_sides(grid, connected, let):
    adj_map = defaultdict(list)
    ans = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) not in connected:
                continue
            
            # for each side, calculate what it's adj status is
            # top, down, left, right
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr = dr + r
                nc = dc + c
                if not valid(grid, nr, nc):  # out of bounds
                    adj_map[(r, c)].append(1)
                elif grid[nr][nc] != let:  # not same
                    adj_map[(r, c)].append(1)
                else:  # same let
                    adj_map[(r, c)].append(0)
                
            curr = adj_map[(r, c)]
            top  = [0, 0, 0, 0]
            left = [0, 0, 0, 0]
            if 0 <= r-1 and grid[r-1][c] == let:
                top  = adj_map[(r-1, c)]
            if 0 <= c-1 and grid[r][c-1] == let:
                left = adj_map[(r, c-1)]
            res = list_xor(curr, top, left)
            # print(f"{grid[r][c]=} ({r},{c}) {curr=} {top=} {left=} {res=}")
            ans += sum(res)
    return ans

def vis(grid):
    for line in grid:
        print("".join(line))

def p2(text):
    # print(text)
    ans = 0
    grid = []
    for line in text:
        line = line.strip()
        grid.append([x for x in line])

    # pprint(grid)
    vis(grid)
    seen = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) not in seen:
                area, connected = island_size(grid, r, c, grid[r][c], 0, set())
                seen.update(connected)
                sides = get_sides(grid, connected, grid[r][c])
                # print(grid[r][c], (r, c), area, sides, connected)
                ans += area * sides

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
