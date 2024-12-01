# Part 1: 
# Part 2: 

from copy import deepcopy
from math import log
# from collections import deque
# from collections import defaultdict
from math import inf
import heapq
import re

class Name:
    def __init__(self, path):
        # target area: x=20..30, y=-10..-5
        with open(path, "r") as f:
            self.data = []
            for line in f:
                line = line.strip().split("target area: ")[1]
                xrange, yrange = line.split(", ")
                xmin, xmax = xrange.split("..")
                ymin, ymax = yrange.split("..")
                xmin = xmin.split("=")[1]
                ymin = ymin.split("=")[1]
                xmin, xmax, ymin, ymax = int(xmin), int(xmax), int(ymin), int(ymax)
                print(xmin, xmax, ymin, ymax)
            self.xmin, self.xmax, self.ymin, self.ymax = xmin, xmax, ymin, ymax


    def print(self, d):
        for l in d:
            print(l)
        print("\n")

    def part1(self):
        d = deepcopy(self.data)
        # xpos, ypos = 0, 0
        # xv, yv = 17, -4
        # valid = False
        # while not (self.xmin <= xpos <= self.xmax and self.ymin <= ypos <= self.ymax):
        #     print(xv, yv, (xpos, ypos))
        #     xpos += xv
        #     ypos += yv
        #     if xv != 0:
        #         if xv > 0:
        #             xv -= 1
        #         else:
        #             xv += 1
        #     yv -= 1
        #     if self.xmin <= xpos <= self.xmax and self.ymin <= ypos <= self.ymax:
        #         valid = True
        #         break
        #     if xv == 0:
        #         if not (self.xmin <= xpos <= self.xmax):
        #             break
        # n * n+1 // 2 = x
        # 2x = n^2+n
        # n^2 +n -2x = 0
        # 25 + 5 -15
        tnums = {}
        tnumrange = 30
        for i in range(-tnumrange, tnumrange + 1):
            tn = (i * (i + 1)) // 2
            if i >= 0:
                tnums[tn] = i
            else:
                tnums[-tn] = i
        print(tnums)
        for xpos in range(self.xmin, self.xmax + 1):
            if xpos in tnums:
                xv = tnums[xpos]
                break
            # for yv in range(self.ymax, self.ymin - 1, -1):
            #     if xv in tnums and yv in tnums:
            #         break
        yheight = 0
        for y
        return (xpos, ypos, valid)
    def part2(self):
        d = deepcopy(self.data)
    
        return



if __name__ == "__main__":
    path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\17\input.txt"
    path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\17\test.txt"
    test = Name(path)

    part1 = test.part1()
    print(part1)
    part2 = test.part2()
    print(part2)
