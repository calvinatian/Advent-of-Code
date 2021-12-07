# Part 1: 354129
# Part 2: 98905973

from copy import deepcopy
from math import e
from collections import deque
from collections import Counter
from math import inf

class Name:
    def __init__(self, path):
        with open(path, "r") as f:
            self.data = [int(x) for x in f.read().strip().split(',')]
        print(self.data)

    def part1(self):
        d = self.data.copy()
        dis = inf
        for i in range(min(d), max(d) + 1):
            td = 0
            for pos in d:
                td += abs(pos - i)
            dis = min(dis, td)
        return dis

    def part2(self):
        d = self.data.copy()
        dis = inf
        for i in range(min(d), max(d) + 1):
            td = 0
            for pos in d:
                n = abs(pos - i)
                td +=  (n * (n + 1)) // 2 
            dis = min(dis, td)
        return dis



if __name__ == "__main__":
    path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\07\test.txt"
    path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\07\input.txt"
    test = Name(path)

    part1 = test.part1()
    print(part1)
    part2 = test.part2()
    print(part2)
