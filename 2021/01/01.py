# Part 1: 1121
# Part 2: 1065
from collections import deque

class Name:
    def __init__(self, path):
        self._data = []
        with open(path, "r") as f:
            # print(f.readlines())
            self.data = [int(x.strip()) for x in f.readlines()]

    def part1(self):
        prev = None
        ans = 0
        for i in self.data:
            if prev and i > prev:
                ans += 1
            prev = i
        return ans

    def part2(self):
        A = deque(self.data[0:3])
        B = deque(self.data[1:3])
        ans = 0
        for i in self.data[3:]:
            B.append(i)
            if sum(B) > sum(A):
                ans += 1
                # print(sum(B))
            A = B.copy()
            B.popleft()
        return ans



if __name__ == "__main__":
    # path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\01\test.txt"
    path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\01\input.txt"
    test = Name(path)
    
    part1 = test.part1()
    print(part1)
    part2 = test.part2()
    print(part2)
