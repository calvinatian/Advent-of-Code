import argparse
import re
from pprint import pprint
from collections import defaultdict
from itertools import permutations
from copy import copy

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

map = defaultdict(int)
# count = defaultdict(int)
# next = defaultdict(int)

def blink2(t1):
    t2 = defaultdict(int)
    # for n in nums:
    for n in [x for x in t1.keys()]:
        length =  len(str(n))
        if n == 0:
            c = t1[n]
            t2[1] += c
            # t2[0] = 0
            # print(f"if c: {c}")

        elif length % 2 == 0:
            if n in map:
                l, r = map[n]
            else:
                l = int(str(n)[length//2:])
                r = int(str(n)[:length//2])
                map[n] = (l, r)

            c = t1[n]
            # t2[n] = 0
            t2[l] += c
            t2[r] += c
            # print(f"elif c: {c}")

        else:
            c = t1[n]
            # print(f"else c: {c}")
            t2[n * 2024] += c
            # t2[n] = 0
        # print(c)

    # t1, t2 = t2, defaultdict(int)
    # print(t1)
    return t2


def p1(text):
    # print(text)
    ans = 0
    nums = []
    for line in text:
        line = line.strip()
        nums += [int(x) for x in line.split(" ")]
    
    print(nums)
    BLINKS = 75
    for _ in range(BLINKS):
        nums = blink(nums)
        print(f"iter: {_}")
    print(nums)

    # n = blink(nums)
    # print(n)

    return len(nums)


def p2(text):
    # print(text)
    nums = []
    for line in text:
        line = line.strip()
        nums += [int(x) for x in line.split(" ")]
    
    print(nums)
    t1 = defaultdict(int)
    for n in nums:
        t1[n] += 1

    print(t1)
    BLINKS = 75
    for _ in range(BLINKS):
        t1 = blink2(t1)
        # print(f"iter: {_}")
        print(t1)

    # n = blink(nums)
    # print(n)

    return sum(t1.values())



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--test", help="run test file", action="store_true")
    args = parser.parse_args()
    filename = "input"
    if args.test:
        filename = "test"
    text = open_file(filename)
    # print(f"Part 1: {p1(text)}")
    print(f"Part 2: {p2(text)}")
