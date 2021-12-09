# Part 1: 562
# Part 2: 1076922

from copy import deepcopy
# from math import e
from collections import deque
from collections import Counter
from math import prod

class Name:
    def __init__(self, path):
        with open(path, "r") as f:
            self.data = []
            for line in f:
                line = line.strip()
                self.data.append([int(x) for x in line])
                # print(line)
        # print(self.data)


    def part1(self):
        d = self.data.copy()
        rlen = len(d)
        clen = len(d[0])
        ans = 0
        for r in range(rlen):
            for c in range(clen):
                is_low = True
                for ar, ac in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ar = r + ar
                    ac = c + ac
                    if (0 <= ar < rlen) and (0 <= ac < clen) and (d[r][c] >= d[ar][ac]):
                        is_low = False
                        break
                if is_low:
                    ans += 1 + d[r][c]
                    # print(d[r][c], ans)
        return ans

    def part2(self):
        d = self.data.copy()
        rlen = len(d)
        clen = len(d[0])
        checked = set()
        ans = []
        for r in range(rlen):
            for c in range(clen):
                if d[r][c] != 9 and (r, c) not in checked:
                    s = [(r, c)]
                    size = 0
                    island = set()
                    while s:
                        nr, nc = s.pop()
                        if (nr, nc) not in checked: size += 1
                        checked.add((nr, nc))
                        island.add((nr, nc))
                        for ar, ac in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            ar = nr + ar
                            ac = nc + ac
                            # print(d[ar][ac])
                            if (ar, ac) not in checked and (0 <= ar < rlen) and (0 <= ac < clen) and (d[ar][ac] != 9):
                                s.append((ar, ac))
                    ans.append(size)
                # else:
                checked.add((r, c))
        ans.sort()
        return prod(ans[-1:-4:-1])

 

if __name__ == "__main__":
    path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\09\test.txt"
    path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\09\input.txt"
    test = Name(path)

    part1 = test.part1()
    print(part1)
    part2 = test.part2()
    print(part2)
