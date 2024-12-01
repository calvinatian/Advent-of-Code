# from aocd import get_data
# from aocd import submit
# from aocd import lines  # like data.splitlines()
# from aocd import numbers  # uses regex pattern -?\d+ to extract integers from data

# data = get_data(day=3, year=2022)

import math
from pprint import pprint
from string import ascii_lowercase, ascii_uppercase
from collections import deque, defaultdict

def p1(name):
    # 7 units wide

    # ####

    # .#.
    # ###
    # .#.

    # ..#
    # ..#
    # ###

    # #
    # #
    # #
    # #

    # ##
    # ##

    rocks = [
        ["..####."],
        ["...#...",
         "..###..",
         "...#..."],
        ["....#..",
         "....#..",
         "..###.."],
        ["..#....",
         "..#....",
         "..#....",
         "..#...."],
        ["..##...",
         "..##..."]
    ]

    ans = 0
    direction = None
    with open(name, "r") as f:
        for line in f:
            line = line.strip()
            direction = line

    rocks_settled = 0
    i = 0
    direction_index = 0
    rock_index = 0
    # chamber 7 units wide
    chamber = ["......." for _ in range(3)]
    new_rock = True
    # do simulation
    while rocks_settled < 2022:
        # new rock
        if new_rock:
            rock = rocks[rock_index]
            new_rock = False
            rock_index += 1
            rock_index %= len(rocks)
            for layer in rock[::-1]:
                chamber.append(layer)
        # left edge 2 units away from wall
        # bottom edge 3 units away from bottom
        # push
        # fall down
        if i % 2 == 0:
            # push by jet
            if all(x[-1] == "." for x in rock):
                # shift
                if direction[direction_index] == ">":
                    # move left
                else:
                    # move right
            direction_index += 1
            direction_index %= len(direction)
        else:
            # push down
            
        i += 1
    return ans

def p2(name):
    ans = 0
    with open(name, "r") as f:
        for line in f:
            line = line.strip()
    return ans

pprint(f'{p1("test")=}')
pprint(f'{p1("input")=}')
pprint(f'{p2("test")=}')
pprint(f'{p2("input")=}')

# if __name__ == "__main__":
#     def submit_answer(ans, part):
#         submit(ans, part=part)
#     # submit_answer(a, part="a")
#     # submit_answer(b, part="b")
#     pass
