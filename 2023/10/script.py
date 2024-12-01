import sys
import re
from enum import Enum
from pprint import pprint
from copy import deepcopy

if len(sys.argv) > 1:
    FILENAME = "test"
else:
    FILENAME = "input"

def adjacent(data, current):
    adjacent = []
    current_node = data[current[0]][current[1]][0]
    # returns list of adjacent nodes
    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        # up, down, left, right
        x, y = current
        x += i
        y += j

        # out of bounds
        # print(x, y, i ,j, len(data[0]))

        if x < 0 or y < 0:
            continue
        if x >= len(data) or y >= len(data[0]):
            continue

        node = data[x][y][0]
        match (i, j):
            case (-1, 0):
                # up
                if current_node == "|" or current_node == "S" or current_node == "J" or current_node == "L":
                    if node == "|" or node == "F" or node == "7":
                        # valid
                        if (x, y) not in adjacent:
                            adjacent.append((x, y))
                # if current_node == "J" or current_node == "L":
                #     if node == "|"
            case (1, 0):
                # down
                if current_node == "|" or current_node == "S" or current_node == "F" or current_node == "7":
                    if node == "|" or node == "J" or node == "L":
                        # valid
                        if (x, y) not in adjacent:
                            adjacent.append((x, y))
            case (0, -1):
                # left
                if current_node == "-" or current_node == "S" or current_node == "J" or current_node == "7":
                    if node == "-" or node == "L" or node == "F":
                        # valid
                        if (x, y) not in adjacent:
                            adjacent.append((x, y))
            case (0, 1):
                # right
                if current_node == "-" or current_node == "S" or current_node == "L" or current_node == "F":
                    if node == "-" or node == "J" or node == "7":
                        # valid
                        if (x, y) not in adjacent:
                            adjacent.append((x, y))
    return adjacent

def part1():
    data = []

    with open(FILENAME) as f:
        for line in f:
            line = line.strip()
            data.append([[x, 0] for x in line])

    # pprint(data)
    
    # find S
    start = None
    for i in range(len(data)):
        for j in range(len(data[0])):
            # print(len(data), len(data[0]) , i, j)
            if data[i][j][0] == "S":
                start = (i, j)
                
    connections = { # ((from), (to)) (row, col)
        "J": ((0, -1), (-1, 0)),
        "7": ((0, -1), (1, 0)),
        "L": ((0, 1), (-1, 0)),
        "F": ((0, 1), (1, 0)),

        "|": ((0, -1), (0, 1)),
        "-": ((-1, 0), (1, 0)),
    }
    
    print(start)

    # find 2 adjacent pipes to S
    left, right = adjacent(data, start)
    data[left[0]][left[1]][1] = 1
    data[right[0]][right[1]][1] = 1
    left_data = deepcopy(data)
    right_data = deepcopy(data)

    print(left, right)
    # follow path, counting distance from s
    # while left != right:
    for _ in range(10000):
        # update left
        # find adjacent to left
        adjacent_cell_coords = adjacent(data, left)
        current = left_data[left[0]][left[1]]

        # print(f"currently at {left} {current}, adjacent to {adjacent_cell_coords}")
        if len(adjacent_cell_coords) == 1:
            adj = adjacent_cell_coords[0]
        else:
            # check adjs[0] for 0
            next_cell = left_data[adjacent_cell_coords[0][0]][adjacent_cell_coords[0][1]]
            if next_cell[1] == 0:
                adj = adjacent_cell_coords[0]
            else:
                adj = adjacent_cell_coords[1]

        left_node = left_data[adj[0]][adj[1]]
        if left_node[1] != 0:
            left_node[1] = min(left_data[left[0]][left[1]][1] + 1, left_node[1])
        else:
            left_node[1] = left_data[left[0]][left[1]][1] + 1
        left = adj
        
        # if left == right:
        #     break
        
        # update right
        adjacent_cell_coords = adjacent(data, right)
        current = right_data[right[0]][right[1]]

        # print(f"currently at {right} {current}, adjacent to {adjacent_cell_coords}")
        if len(adjacent_cell_coords) == 1:
            adj = adjacent_cell_coords[0]
        else:
            # check adjs[0] for 0
            next_cell = right_data[adjacent_cell_coords[0][0]][adjacent_cell_coords[0][1]]
            if next_cell[1] == 0:
                adj = adjacent_cell_coords[0]
            else:
                adj = adjacent_cell_coords[1]

        right_node = right_data[adj[0]][adj[1]]
        if right_node[1] != 0:
            right_node[1] = min(right_data[right[0]][right[1]][1] + 1, right_node[1])
        else:
            right_node[1] = right_data[right[0]][right[1]][1] + 1
        right = adj


    # find max distance
    m = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            # if data[i][j][1] > m:
            a = min(left_data[i][j][1], right_data[i][j][1])
            m = max(a, m)
    # pprint(left_data)
    # pprint(right_data)
    return m

# print(part1())

def find_main_loop():
    """returns grid with tiles on main loop marked as True"""
    data = []

    with open(FILENAME) as f:
        for line in f:
            line = line.strip()
            data.append([[x, False] for x in line])

    # find S
    start = None
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j][0] == "S":
                start = (i, j)
                data[i][j][1] = True

    print(start)
    # data[start[0]][start[1]][1] = True
    current = adjacent(data, start)[0]
    # follow path, marking pipes from s
    # while True:
    for _ in range(200000):
        data[current[0]][current[1]][1] = True
        adjacent_cell_coords = adjacent(data, current)
        for adj in adjacent_cell_coords:
            if data[adj[0]][adj[1]][1] == True:
                continue
            else:
                current = adj
                break

    return data

def print_grid(data, compressed=False):
    for i in range(len(data)):
        if compressed:
            step = 2
        else:
            step = 1
        for j in range(0, len(data[0]), step):
            node = data[i][j]
            if node[0] == ".":
                if node[1]:
                    print("O", end="")
                else:
                    print("I", end="")
            else:
                print(node[0], end="")
        print()

def part2():
    data = []

    mapping = {
        "|": "|.",
        "-": "--",
        "L": "L-",
        "J": "J.",
        "7": "7.",
        "F": "F-",
        ".": "..",
        "S": "F-",  # hard code, look at input S
    }

    with open(FILENAME) as f:
        for line in f:
            line = line.strip()
            new_line = []
            for x in line:
                new_line += [[y, False] for y in mapping[x]]
            # data.append([[mapping] for x in line])
            data.append(new_line)

    # print_grid(data)
    # flood fill from edges
    main_loop = find_main_loop()
    print_grid(main_loop)

    # replace everything not on main loop with .
    for i in range(len(data)):
        for j in range(0, len(data[0]), 2):
            if main_loop[i][j//2][1] == False:
                data[i][j][0] = "."
                data[i][j + 1][0] = "."

    for i in range(len(data)):
        for j in (0, len(data[0]) - 1):
            # do dfs and set nodes to true
            stack = [(i, j)]
            while stack:
                current = stack.pop()
                data[current[0]][current[1]][1] = True
                for r, c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if current[0] + r < 0 or current[1] + c < 0:
                        continue
                    if current[0] + r >= len(data) or current[1] + c >= len(data[0]):
                        continue
                    if data[current[0] + r][current[1] + c][1]:
                        continue
                    if data[current[0] + r][current[1] + c][0] == ".":
                        stack.append((current[0] + r, current[1] + c))
    
    for i in (0, len(data) - 1):
        for j in range(len(data[0])):
            # do dfs and set nodes to true
            if data[i][j][0] != ".":
                continue
            stack = [(i, j)]
            while stack:
                current = stack.pop()
                data[current[0]][current[1]][1] = True
                for r, c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if current[0] + r < 0 or current[1] + c < 0:
                        continue
                    if current[0] + r >= len(data) or current[1] + c >= len(data[0]):
                        continue
                    if data[current[0] + r][current[1] + c][1]:
                        continue
                    if data[current[0] + r][current[1] + c][0] == ".":
                        stack.append((current[0] + r, current[1] + c))

    total_tiles = 0
    total_marked_tiles = 0
    for i in range(len(data)):
        for j in range(0, len(data[0]), 2):
            # if data[i][j][0] + data[i][j + 1] == "..":
            if data[i][j][0] == ".":
                total_tiles += 1
                # if main_loop[i][j//2][1] == False:  # not on main loop
                if data[i][j][1]:
                    total_marked_tiles += 1

    # print_grid(data)
    print_grid(data, True)
    print(total_tiles, total_marked_tiles)
    return total_tiles - total_marked_tiles

print(part2())
