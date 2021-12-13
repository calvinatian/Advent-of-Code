# Part 1: 664
# Part 2: EFJKZLBL

# from copy import deepcopy
# from math import e
# from collections import deque
from collections import defaultdict
# from math import prod

class Name:
    def __init__(self, path):
        with open(path, "r") as f:
            self.cord = []
            self.fold = []
            rmax = 0
            cmax = 0
            is_instruction = False
            for line in f:
                line = line.strip()
                if line == "":
                    is_instruction = True
                    continue
                if is_instruction:
                    l = line.split("=")
                    dir = l[0][-1]
                    val = int(l[1])
                    self.fold.append((dir,val))
                else:
                    l = line.split(",")
                    x = int(l[0])
                    y = int(l[1])
                    rmax = max(rmax, y)
                    cmax = max(cmax, x)
                    self.cord.append((x, y))
                # print(line)
        self.data = []
        for r in range(rmax + 1):
            self.data.append(["." for c in range(cmax + 1)])
            # for c in range(cmax):
        for x, y in self.cord:
            # print(x, y)
            self.data[y][x] = "#"

        # print(rmax, cmax, self.fold)
        # self.print(self.data)
        # self.paths = []
        self.rmax = rmax

    def print(self, d):
        for l in d:
            print(l)
        print("")

    def part1(self):
        d = self.data.copy()
        v = self.fold.copy()[0]
        dir = v[0]
        loc = v[1]
        # print(dir, loc)
        if dir == "y": # ver down->up
            for r in range(loc + 1, len(d)):
                ar = loc - abs(r - loc)
                # print(r, ar)
                for c in range(len(d[0])):
                    d[ar][c] = "#" if "#" in [d[r][c], d[ar][c]] else "."
            for r in range(loc + 1, len(d)):
                d.pop()

        else: # hor left->right
            nd = [["."] * loc for r in range(len(d))]
            # self.print(nd)
            for r in range(len(d)):
                for c in range(loc + 1, len(d[0])):
                    ac = loc - abs(c - loc)
                    # print(r, c, ac)
                    d[r][ac] = "#" if "#" in [d[r][c], d[r][ac]] else "."
            for r in range(len(nd)):
                for c in range(len(nd[0])):
                    nd[r][c] = d[r][c]
            d = nd
        
        # self.print(d)
        ans = 0
        # return sum(map(sum, d))
        for r in range(len(d)):
            for c in range(len(d[0])):
                if d[r][c] == "#":
                    ans += 1
        return ans



    def part2(self):

        d = self.data.copy()
        f = self.fold.copy()
        # print(dir, loc)
        for v in f:
            dir = v[0]
            loc = v[1]
            if dir == "y": # ver down->up
                for r in range(loc + 1, len(d)):
                    ar = loc - abs(r - loc)
                    # print(r, ar)
                    for c in range(len(d[0])):
                        d[ar][c] = "#" if "#" in [d[r][c], d[ar][c]] else "."
                for r in range(loc + 1, len(d)):
                    d.pop()

            else: # hor left->right
                nd = [["."] * loc for r in range(len(d))]
                # self.print(nd)
                for r in range(len(d)):
                    for c in range(loc + 1, len(d[0])):
                        ac = loc - abs(c - loc)
                        # print(r, c, ac)
                        d[r][ac] = "#" if "#" in [d[r][c], d[r][ac]] else "."
                for r in range(len(nd)):
                    for c in range(len(nd[0])):
                        nd[r][c] = d[r][c]
                d = nd

            # self.print(d)

        ans = 0
        # return sum(map(sum, d))
        for r in range(len(d)):
            for c in range(len(d[0])):
                if d[r][c] == "#":
                    ans += 1
        self.print(d)
        return ans


if __name__ == "__main__":
    path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\13\test.txt"
    path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\13\input.txt"
    test = Name(path)

    part1 = test.part1()
    print(part1)
    part2 = test.part2()
    print(part2)
