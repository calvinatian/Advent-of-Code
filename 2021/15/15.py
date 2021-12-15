# Part 1: 487
# Part 2: 2821

from copy import deepcopy
from math import log
# from collections import deque
# from collections import defaultdict
from math import inf
import heapq

class Name:
    def __init__(self, path):
        with open(path, "r") as f:
            self.data = []
            for line in f:
                line = line.strip()
                self.data.append([int(x) for x in line])
        self.print(self.data)
        n = (len(self.data) * len(self.data[0]) * 25)
        print(n * log(n, 2))

    def print(self, d):
        for l in d:
            print(l)
        print("\n")

    def part1(self):
        # d = deepcopy(self.data)
        # rlen = len(d)
        # clen = len(d[0])
        # costs = [[inf] * clen for r in range(rlen)]

        # end = (rlen - 1, clen - 1)
        # visited = set()

        # l = set()
        # for r in range(rlen):
        #     for c in range(clen):
        #         l.add((r, c))

        # costs[0][0] = 0
        # consider = set()
        # consider.add((0, 0))
        # while l:
        #     lowest = inf
        #     for r, c in consider:
        #         if (r, c) not in visited and (r, c) in l:
        #             if costs[r][c] < lowest:
        #                 nr, nc = r, c
        #                 lowest = costs[r][c]
        #     l.remove((nr, nc))
        #     visited.add((nr, nc))
        #     consider.remove((nr, nc))
        #     for ar, ac in [[nr + 1, nc], [nr - 1, nc], [nr, nc + 1], [nr, nc - 1]]:
        #         if 0 <= ar < rlen and 0 <= ac < clen:
        #             costs[ar][ac] = min(costs[ar][ac], costs[nr][nc] + d[ar][ac])
        #             consider.add((ar, ac))

        # r, c = end
        # self.print(costs)
        # return costs[r][c]
        d = deepcopy(self.data)
        rlen = len(d)
        clen = len(d[0])
        costs = [[inf] * clen for r in range(rlen)]
        costs[0][0] = 0

        end = (rlen - 1, clen - 1)
        visited = set()

        l = []
        heapq.heappush(l, (0, 0, 0))

        while l:
            lowest, nr, nc = heapq.heappop(l)
            # if nr, nc not in visited:
            visited.add((nr, nc))

            for ar, ac in [[nr + 1, nc], [nr - 1, nc], [nr, nc + 1], [nr, nc - 1]]:
                if 0 <= ar < rlen and 0 <= ac < clen:
                    costs[ar][ac] = min(costs[ar][ac], costs[nr][nc] + d[ar][ac])
                    if (costs[ar][ac], ar, ac) not in l and (ar, ac) not in visited:
                        heapq.heappush(l, (costs[ar][ac], ar, ac))

        r, c = end
        self.print(costs)
        return costs[r][c]

    def part2(self):
        # create new matrix
        d = deepcopy(self.data)
        rlen = len(d)
        clen = len(d[0])
        nd = [[0] * (clen * 5) for r in range(rlen * 5)]
        print(len(nd), len(nd[0]))
        for r in range(rlen):
            for c in range(clen):
                nd[r][c] = d[r][c]
        nrlen = len(nd)
        nclen = len(nd[0])
        for nr in range(nrlen):
            for nc in range(nclen):
                mult = (nr // rlen) + (nc // clen)
                r, c = nr % rlen, nc % clen
                v = d[r][c] + mult
                if v > 9:
                    v = (v % 10) + 1
                nd[nr][nc] = v
        self.print(nd)


        d = deepcopy(nd)
        rlen = len(d)
        clen = len(d[0])
        costs = [[inf] * clen for r in range(rlen)]
        costs[0][0] = 0

        end = (rlen - 1, clen - 1)
        visited = set()

        l = []
        heapq.heappush(l, (0, 0, 0))

        while l:
            lowest, nr, nc = heapq.heappop(l)
            visited.add((nr, nc))

            for ar, ac in [[nr + 1, nc], [nr - 1, nc], [nr, nc + 1], [nr, nc - 1]]:
                if 0 <= ar < rlen and 0 <= ac < clen:
                    costs[ar][ac] = min(costs[ar][ac], costs[nr][nc] + d[ar][ac])
                    if (costs[ar][ac], ar, ac) not in l and (ar, ac) not in visited:
                        heapq.heappush(l, (costs[ar][ac], ar, ac))

        r, c = end
        self.print(costs)
        return costs[r][c]



if __name__ == "__main__":
    path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\15\test.txt"
    path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\15\input.txt"
    test = Name(path)

    part1 = test.part1()
    print(part1)
    part2 = test.part2()
    print(part2)
