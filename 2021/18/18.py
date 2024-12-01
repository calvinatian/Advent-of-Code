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
            # for line in f:
            #     line = line.strip()
            #     self.data.append(SnailNum(eval(line)))
                # [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
            # self.print(self.data)


    def print(self, d):
        for l in d:
            print(l)
        print("\n")

    def part1(self):
        d = deepcopy(self.data)
        n = SnailNum([[[[[9,8],1],2],3],4])
        print(n)
        n._reduce()
        print(n)
        
    def part2(self):
        d = deepcopy(self.data)
    
        return

class Node():
    def __init__(self, data, left, right):
        # print(pair, type(pair))

        self.data = data
        self.left = left
        self.right = right
        # if type(pair[0]) == list:
        #     self.left = Node(pair[0])
        # else:
        #     self.left = int(pair[0])
        # if type(pair[1]) == list:
        #     self.right = Node(pair[1])
        # else:
        #     self.right = int(pair[1])

    def __iter__(self):
        def recur(node):
            if not node: return

            if type(node) == int:
                yield node
            else:
                recur(node.left)
                recur(node.right)
        recur(self)

    def __str__(self):
        l = []
        for i in self:
            l.append(i)
        return l

class SnailNum():

    def __init__(self, lst):
        self.num = Node(lst)
        print(self.num)

    def __add__(self, other):
        self.num = [self.num, other.num]

    def _reduce(self):
        # nested inside 4 -> explode left
        # num > 10: split
        def explode_pair(pair, nest_count):
            if nest_count >= 4:
                return (pair[0], pair[1])
            # if type(pair[0]) == list:
            #     pair[0], pair[1] += explode_pair(pair[0], nest_count)

        nested = self.num
        nest_count = 0
        prev = None
        # while True:
        #     if nest_count >= 4:
        #         break
        #     if type(nested[0]) == list:
        #         prev, nested = nested, nested[0]
        #         nest_count += 1
        #     else:
        #         break
        print(prev, nest_count)

    def __str__(self):
        return str(self.num)


if __name__ == "__main__":
    path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\18\input.txt"
    path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\18\test.txt"
    test = Name(path)

    part1 = test.part1()
    print(part1)
    part2 = test.part2()
    print(part2)
