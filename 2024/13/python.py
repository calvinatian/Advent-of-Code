import argparse
import re
from pprint import pprint
from collections import defaultdict
from itertools import permutations, batched
from functools import cache
import numpy as np
import math
import sympy as sp

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
    prizes = {}
    for lines in batched(text, 4):
        # print(lines)
        # A
        matches = re.search(r".?+(\d+).+?(\d+)", lines[0])
        ax = int(matches.group(1))
        ay = int(matches.group(2))

        matches = re.search(r".?+(\d+).+?(\d+)", lines[1])
        bx = int(matches.group(1))
        by = int(matches.group(2))

        matches = re.search(r".?+(\d+).+?(\d+)", lines[2])
        px = int(matches.group(1))
        py = int(matches.group(2))

        prizes[(px, py)] = ((ax, ay), (bx, by))
    # print(prizes)
    return prizes

@cache
def target(na, nb, px, py, tx, ty, ax, ay, bx, by):
    # print(na, nb, px, py, tx, ty)
    if na > 100 and nb > 100:
        return False, na, nb
    
    if px == tx and py == ty:
        return True, na, nb
    
    if px > tx or py > ty:
        return False, na, nb
    
    # if px < 100:
    #     print(px, py)

    # print(px, py, tx, ty)
    
    r1, a1, b1 = target(na + 1, nb, px + ax, py + ay, tx, ty, ax, ay, bx, by)
    # r2, a2, b2 = target(na + 1, nb, px + ax, py + ay, ax, ay, bx, by)
    r2, a2, b2 = target(na, nb + 1, px + bx, py + by, tx, ty, ax, ay, bx, by)
    # r4, a4, b4 = target(na, nb + 1, px + bx, py + by, ax, ay, bx, by)
    # print(px, py)
    # return True, na, nb
    # print(r1, r2, a1, a2, b1, b2, px)

    if r1 and r2:
        c1 = (a1 * 3) + b1
        c2 = (a2 * 3) + b2
        if c1 < c2:
            return True, a1, b1
        else:
            return True, a2, b2
    elif r1:
        return True, a1, b1
    elif r2:
        return True, a2, b2
    else:
        return False, na, nb


def p1(text):
    # print(text)
    # 0000000000000
    ans = 0
    prizes = parse(text)
    for prize, (a, b) in prizes.items():
        # print(prize, a, b, prize[0], prize[1], a[0], a[1], b[0], b[1])
        t, a, b = target(0, 0, 0, 0, prize[0], prize[1], a[0], a[1], b[0], b[1])
        if t:
            ans += (a * 3) + b
        # print(t, a, b)

        # break

    return ans


def parse2(text):
    prizes = {}
    for lines in batched(text, 4):
        # print(lines)
        # A
        matches = re.search(r".?+(\d+).+?(\d+)", lines[0])
        ax = int(matches.group(1))
        ay = int(matches.group(2))

        matches = re.search(r".?+(\d+).+?(\d+)", lines[1])
        bx = int(matches.group(1))
        by = int(matches.group(2))

        matches = re.search(r".?+(\d+).+?(\d+)", lines[2])
        px = int(matches.group(1))
        py = int(matches.group(2))

        prizes[(px+10000000000000, py+10000000000000)] = ((ax, ay), (bx, by))
    # print(prizes)
    return prizes


def lcm(x, y):
   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

@cache
def target2(tx, ty, ax, ay, bx, by):
    cx = lcm(ax, bx)
    cy = lcm(ay, by)
    print(cx, cy)


def p2(text):
    # print(text)
    ans = 0
    prizes = parse2(text)
    for prize, (a, b) in prizes.items():
        tx, ty = prize
        ax, ay = a
        bx, by = b

        A, B = sp.symbols('a, b')
        cx = sp.Eq(ax * A + bx * B, tx)
        cy = sp.Eq(ay * A + by * B, ty)
        res = sp.solve((cx, cy), (A, B))
        # print(res[A])
        # print(type(res[A]))
        if res[A].is_integer and res[B].is_integer:
            ans += res[A] * 3
            ans += res[B]



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
