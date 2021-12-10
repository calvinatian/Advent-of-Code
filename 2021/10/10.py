# Part 1: 
# Part 2: 

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
                self.data.append([x for x in line])
                print(line)
        print(self.data)


    def part1(self):
        d = self.data.copy()
        match = {
            "(": ")",
            "[": "]",
            "{": "}",
            "<": ">",
        }
        s = []
        illegal = []
        for l in d:
            for c in l:
                if c in match:
                    s.append(c)
                elif c in match.values():
                    if match[s[-1]] != c:
                        illegal.append(c)
                        break
                    else:
                        s.pop()
        score = {
            ")": 3,
            "]": 57,
            "}": 1197,
            ">": 25137,
        }
        ans = 0
        print(illegal)
        for i in illegal:
            ans += score[i]
        return ans

    def part2(self):
        d = self.data.copy()
        match = {
            "(": ")",
            "[": "]",
            "{": "}",
            "<": ">",
        }
        rem = []
        for l in d:
            s = []
            illegal = False
            for c in l:
                if c in match:
                    s.append(c)
                elif c in match.values():
                    if match[s[-1]] != c:
                        illegal = True
                        break
                    else:
                        s.pop()
            if not illegal:
                rem.append(s)
        score = {
            ")": 1,
            "]": 2,
            "}": 3,
            ">": 4,
        }
        scores = []
        print(len(rem))
        for l in rem:
            ans = 0
            l = l[::-1]
            print(l)
            for c in l:
                ans *= 5
                ans += score[match[c]]
            scores.append(ans)

        scores.sort()
        print(scores)
        print("DAWIH")
        return scores[len(scores)//2]

 

if __name__ == "__main__":
    path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\10\test.txt"
    path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\10\input.txt"
    test = Name(path)

    part1 = test.part1()
    print(part1)
    part2 = test.part2()
    print(part2)
