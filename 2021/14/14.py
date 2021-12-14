# Part 1: 2988
# Part 2: 3572761917024

from copy import deepcopy
# from math import e
from collections import Counter
from collections import defaultdict
# from math import prod

class Name:
    def __init__(self, path):
        with open(path, "r") as f:
            self.data = {}
            self.initial = ""
            PT = False
            for line in f:
                line = line.strip()
                if line == "":
                    PT = True
                    continue
                if PT:
                    poly = line.split(" -> ")
                    p = poly[0]
                    i = poly[1]
                    self.data[p] = i
                else:
                    self.initial = line
        print(self.data)

    def print(self, d):
        for l in d:
            print(l)
        print("")

    def part1(self):
        d = self.data.copy()
        str = self.initial
        DAYS = 10
        for _ in range(DAYS):
            # print(str)
            # print(len(str))
            pairs = []
            for c in range(len(str) - 1):
                pairs.append(str[c:c+2])
            # print(pairs)

            nstr = []
            inserted = False
            for pair in pairs:
                a, b = pair
                if not inserted:
                    nstr.append(a)
                # pair = "".join(pair)
                if pair in d:
                    nstr.append(d[pair])
                    inserted = True
                else:
                    inserted = False
                nstr.append(b)
            str = "".join(nstr)

        count = Counter(str)
        return max(count.values()) - min(count.values())

    def part2(self):
        d = self.data.copy()
        str = self.initial
        DAYS = 40
        pairs = defaultdict(int)
        for c in range(len(str) - 1):
            pairs[(str[c:c+2])] += 1
        for day in range(DAYS):
            # print(str)
            # print(day, len(str))
            # print(pairs)
            npairs = deepcopy(pairs)
            for pair in pairs:
                if pair in d and pairs[pair] > 0:
                    a, b = pair
                    c = d[pair]
                    npairs[f"{a}{c}"] += pairs[pair]
                    npairs[f"{c}{b}"] += pairs[pair]
                    npairs[pair] -= pairs[pair]
            pairs = deepcopy(npairs)
            print(sum(pairs.values()))

        lets = defaultdict(int)
        for pair in pairs:
            a, b = pair
            lets[a] += pairs[pair]
            lets[b] += pairs[pair]
        print(lets)
        return (max(lets.values())+1)//2 - (min(lets.values())+1)//2

if __name__ == "__main__":
    path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\14\input.txt"
    path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\14\test.txt"
    test = Name(path)

    part1 = test.part1()
    print(part1)
    part2 = test.part2()
    print(part2)
