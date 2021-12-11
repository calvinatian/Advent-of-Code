# Part 1: 1627
# Part 2: 328

# from copy import deepcopy
# from math import e
# from collections import deque
# from collections import Counter
# from math import prod

class Name:
    def __init__(self, path):
        with open(path, "r") as f:
            self.data = []
            for line in f:
                line = line.strip()
                self.data.append([int(x) for x in line])
                print(line)
        # print(self.data)
        self.rlen = len(self.data)
        self.clen = len(self.data[0])

    def print(self, d):
        for l in d:
            print(l)
        print("")

    def part1(self):
        d = self.data.copy()
        flashes = 0
        days = 100
        for _ in range(days):
            reset = set()
            seeds = []
            for r in range(self.rlen):
                for c in range(self.clen):
                    if d[r][c] >= 9:
                        seeds.append((r, c))
                        reset.add((r,c))
                    d[r][c] += 1
            # self.print(d)
            while seeds:
                # print(reset, seeds)
                r, c = seeds.pop()
                reset.add((r,c))
                flashes += 1
                for ar, ac in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    ar = ar + r
                    ac = ac + c
                    if (ar, ac) not in reset and (0 <= ar < self.rlen) and (0 <= ac < self.clen):
                        if (d[ar][ac] >= 9):
                            seeds.append((ar, ac))
                            reset.add((ar, ac))
                        else:
                            d[ar][ac] += 1
            for r, c in reset:
                d[r][c] = 0
        #     self.print(d)
        # self.print(d)
        return flashes

    def part2(self):
        d = self.data.copy()
        flashes = 0
        day = 0
        while True:
            reset = set()
            seeds = []
            for r in range(self.rlen):
                for c in range(self.clen):
                    if d[r][c] >= 9:
                        seeds.append((r, c))
                        reset.add((r,c))
                    d[r][c] += 1
            # self.print(d)
            while seeds:
                # print(reset, seeds)
                r, c = seeds.pop()
                reset.add((r,c))
                flashes += 1
                for ar, ac in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    ar = ar + r
                    ac = ac + c
                    if (ar, ac) not in reset and (0 <= ar < self.rlen) and (0 <= ac < self.clen):
                        if (d[ar][ac] >= 9):
                            seeds.append((ar, ac))
                            reset.add((ar, ac))
                        else:
                            d[ar][ac] += 1
            for r, c in reset:
                d[r][c] = 0
            if len(reset) == self.rlen * self.clen:
                return day 
            day += 1

 

if __name__ == "__main__":
    path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\11\test.txt"
    path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\11\input.txt"
    test = Name(path)

    part1 = test.part1()
    print(part1)
    part2 = test.part2()
    print(part2)
