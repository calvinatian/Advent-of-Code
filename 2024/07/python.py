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

def try_op(remaining, running_sum, target):
    if len(remaining) == 0:
        return running_sum == target
    if running_sum > target:
        return False

    return try_op(remaining[1:], running_sum + remaining[0], target) + try_op(remaining[1:], running_sum * remaining[0], target)


def try_op2(remaining, running_sum, target):
    if len(remaining) == 0:
        return running_sum == target
    if running_sum > target:
        return False

    add = int(running_sum) + int(remaining[0])
    mul = int(running_sum) * int(remaining[0])
    concat = int(str(running_sum) + str(remaining[0]))

    return try_op2(remaining[1:], add, target) + try_op2(remaining[1:], mul, target) + try_op2(remaining[1:], concat, target)


def p1(text):
    # print(text)
    ans = 0

    nums = []
    for line in text:
        line = line.strip()
        n = []
        a, rest = line.split(": ")
        n.append(int(a))
        for num in rest.split(" "):
            n.append(int(num))
        nums.append(n)
    # print(nums)

    for n in nums:
        res, rest = n[0], n[1:]
        if try_op(rest, 0, res):
            ans += res


    return ans


def p2(text):
    print(text)
    ans = 0

    nums = []
    for line in text:
        line = line.strip()
        n = []
        a, rest = line.split(": ")
        n.append(int(a))
        for num in rest.split(" "):
            n.append(num)
        nums.append(n)
    print(nums)

    for n in nums:
        res, rest = n[0], n[1:]
        if try_op2(rest, 0, res):
            ans += res


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
