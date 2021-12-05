# Part 1: 6007
# Part 2: 19349

from copy import deepcopy

class Name:
    def __init__(self, path):
        self.data = []
        self.xmax = 0
        self.ymax = 0
        with open(path, "r") as f:
            for line in f:
                l = line.strip().split(' -> ')
                x1,y1 = l[0].split(',')
                x2,y2 = l[1].split(',')
                x1 = int(x1)
                x2 = int(x2)
                y1 = int(y1)
                y2 = int(y2)
                self.xmax = max(self.xmax, x1, x2)
                self.ymax = max(self.ymax, y1, y2)
                self.data.append((x1,y1,x2,y2))
        self.board = [[0] * (self.xmax + 1) for row in range(self.ymax + 1)]
        # print(self.data)
        # print(self.xmax, self.ymax)
        # print(self.board)

    def part1(self):
        for data in self.data:
            x1, y1, x2, y2 = data
            if x1 == x2 or y1 == y2:
                # print(x1, y1, x2, y2)
                # print(min(y1, y2), max(y1, y2))
                # print(min(x1, x2), max(x1, x2))
                for r in range(min(y1, y2), max(y1, y2) + 1):
                    for c in range(min(x1, x2), max(x1, x2) + 1):
                        # print(r, c)
                        self.board[r][c] += 1
                        # print(self.board)
        ans = 0
        # for line in self.board:
        #     ans = max(max(line), ans)
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                if self.board[r][c] >= 2: ans += 1
        # print(self.board)
        return ans

    def part2(self):
        for data in self.data:
            x1, y1, x2, y2 = data

            if x1 == x2 or y1 == y2:
                # print(x1, y1, x2, y2)
                # print(min(y1, y2), max(y1, y2))
                # print(min(x1, x2), max(x1, x2))
                for r in range(min(y1, y2), max(y1, y2) + 1):
                    for c in range(min(x1, x2), max(x1, x2) + 1):
                        # print(r, c)
                        self.board[r][c] += 1
                        # print(self.board)
            else:
                # print(x1, y1, x2, y2)
                r = y1
                c = x1
                for _ in range(max(x2, x1) - min(x2, x1) + 1):
                    # print(r, c)
                    self.board[r][c] += 1
                    r += 1 if y1 < y2 else -1
                    c += 1 if x1 < x2 else -1
                    
        ans = 0
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                if self.board[r][c] >= 2: ans += 1
        # print(self.board)
        return ans


if __name__ == "__main__":
    path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\05\test.txt"
    path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\05\input.txt"
    test = Name(path)

    # part1 = test.part1()
    # print(part1)
    part2 = test.part2()
    print(part2)
