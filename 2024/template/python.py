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


def p1(text):
    print(text)
    ans = 0
    for line in text:
        line = line.strip()

    return ans


def p2(text):
    print(text)
    ans = 0

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
