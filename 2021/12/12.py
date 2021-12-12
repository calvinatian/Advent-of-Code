# Part 1: 4186
# Part 2: 92111

# from copy import deepcopy
# from math import e
# from collections import deque
from collections import defaultdict
# from math import prod

class Name:
    def __init__(self, path):
        with open(path, "r") as f:
            self.data = []
            for line in f:
                line = line.strip()
                self.data.append(line.split("-"))
                # print(line)
        print(self.data)
        self.paths = []

    def print(self, d):
        for l in d:
            print(l)
        print("")

    def part1(self):
        d = self.data.copy()
        big = defaultdict(set)
        small = defaultdict(set)
        for a, b in d:
            if a.lower() == a: # small
                small[a].add(b)
            else:
                big[a].add(b)
            if b.lower() == b: # small
                small[b].add(a)
            else:
                big[b].add(a)
        all = big | small
        print(big, small, all)

        ans = 0
        paths = []
        for a in all["start"]:
            dfs = [(a, set(), ["start"])]
            # used = set()
            # m = set()
            # p = []
            while dfs:
                # print(dfs)
                l, used, p = dfs.pop()
                p.append(l)
                if l.lower() == l: used.add(l)
                for c in all[l]:
                    if c in used or c == "start":
                        continue
                    if c == "end":
                        # print(c, dfs)
                        pc = p.copy()
                        pc.append("end")
                        paths.append(pc)
                        ans += 1
                    else:
                        dfs.append((c, used.copy(), p.copy()))
        # self.print(paths)
        return ans
        # self.search(all, [], "start", set())
        # print(self.paths)


    def part2(self):
        d = self.data.copy()
        big = defaultdict(set)
        small = defaultdict(set)
        for a, b in d:
            if a.lower() == a: # small
                small[a].add(b)
            else:
                big[a].add(b)
            if b.lower() == b: # small
                small[b].add(a)
            else:
                big[b].add(a)
        all = big | small
        print(big, small, all)

        ans = 0
        paths = []
        for a in all["start"]:
            dfs = [(a, set(), ["start"], False)]
            # used = set()
            # m = set()
            # p = []
            while dfs:
                # print(dfs)
                l, used, p, twice = dfs.pop()
                p.append(l)
                if l.lower() == l: used.add(l)
                for c in all[l]:
                    if c == "start":
                        continue
                    if c == "end":
                        # print(c, dfs)
                        pc = p.copy()
                        pc.append("end")
                        paths.append(pc)
                        ans += 1
                    else:
                        if c in used:
                            if not twice:
                                dfs.append((c, used.copy(), p.copy(), True))
                        else:
                            dfs.append((c, used.copy(), p.copy(), twice))
        return ans


if __name__ == "__main__":
    path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\12\test.txt"
    path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\12\input.txt"
    test = Name(path)

    part1 = test.part1()
    print(part1)
    part2 = test.part2()
    print(part2)
