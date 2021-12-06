# Part 1: 353079
# Part 2: 1605400130036

from copy import deepcopy
from math import e
from collections import deque
from collections import Counter

class Name:
    def __init__(self, path):
        with open(path, "r") as f:
            self.data = [int(x) for x in f.read().strip().split(',')]
        # print(self.data)
        # print(self.xmax, self.ymax)
        # print(self.board)

    def part1(self):
        day = 0
        a = self.data.copy()
        b = []
        while day < 80:
            for c in a:
                c -= 1
                if c < 0:
                    b.append(6)
                    b.append(8)
                else:
                    b.append(c)
            day += 1
            a = b.copy()
            b = []
        return len(a)

    def part2(self):
        # a = deque(self.data.copy().sort())
        # a = {i: 0 for i in range(1, 257)}
        # (a[x] += self.data.count(x) for x in sorted(self.data))
        # {x: self.data.count(x) for x in sorted(self.data)}
        TOTAL_DAYS = 255
        a = Counter(self.data)
        print(a)
        # total_fish = len(self.data)
        total_fish = len(self.data)
        for i in range(1, TOTAL_DAYS + 1):
            c = a.get(i, 0)
            if c != 0:
                print(i, c, total_fish, a.get(17,0), a.get(9,0), a.get(10,0))
                # new_fish = ((256 - i) // 7) * c
                # total_fish += new_fish
                total_fish += c
                a[i + 9] += c
                a[i + 7] += c
                # for j in range(i, TOTAL_DAYS + 1, 7):
                #     a[j + 8] += c
                #     a[j + 7] += c
        return total_fish

        # tf = 0
        # day = 0
        # while a:
        #     c = a.popleft()
        #     tf += (256 - c) // 7


        # return total_fish * e ** (71//8)


if __name__ == "__main__":
    path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\06\test.txt"
    path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\06\input.txt"
    test = Name(path)

    part1 = test.part1()
    print(part1)
    part2 = test.part2()
    print(part2)
    print(353079)
    print(26984457539)
