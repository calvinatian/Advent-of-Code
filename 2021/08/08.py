# Part 1: 495
# Part 2: 1055164

from copy import deepcopy
# from math import e
from collections import deque
from collections import Counter
from math import inf

class Name:
    def __init__(self, path):
        with open(path, "r") as f:
            self.data = []
            for line in f:
                line = line.strip()
                info, output = line.split(" | ")
                info = info.split(" ")
                output = output.split(" ")
                self.data.append(tuple([info, output]))
        # print(self.data)


    def part1(self):
        d = self.data.copy()
        easy = (2, 3, 4, 7)
        signals = {
            2: 1,
            3: 7,
            4: 4,
            5: [2, 3, 5],
            6: [0, 6, 9],
            7: 8,
        }
        ans = 0
        for info, o in d:
            part = {}
            # parse input
            for s in o:
                # print(s)
                if len(s) in easy:
                    part[s] = signals[len(s)]
                    ans += 1

            # parse output
        return ans

    def part2(self):
        # line = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"

        # a -> d -> g -> b -> f -> c -> e
        d = deepcopy(self.data)
        ans = 0
        for info, o in d:
            info = sorted(info, key=lambda x: len(x))
            # info = ['cg', 'gcb', 'gfac', 'bdaec', 'gdafb', 'bgcad', 'fgaebd', 'agbcfd', 'gdcbef', 'cdgabef']
            # o = ["cg", "cg", "fdcagb", "cbg"]
            # print(info)
            # 1, 7, 4, (2, 3, 5), (0, 6, 9), 8
            # 0  1  2   3  4  5    6  7  8   9
            one = info[0]
            seven = info[1]
            four = info[2]
            eight = info[9]

            letters = {}
            for c in seven:
                if c not in one:
                    letters["a"] = c
                    break
            four = [x for x in four if x not in one] # b, d

            five_digits = [info[3], info[4], info[5]]
            # 3
            for s in five_digits:
                if all((x in s) for x in one):
                    three = s
                    five_digits.remove(s)
                    break
            for c in three:
                # print(three, four)
                # print(f"HERE {three, four, seven, letters['a']}")
                if c not in seven and c in four:
                    letters["d"] = c
                elif c not in seven and c not in four and c != letters["a"]:
                    letters["g"] = c
            # 4
            for c in four:
                if c not in three:
                    letters["b"] = c
                    break
            # 5
            for s in five_digits:
                free_spot = True
                l = None
                correct = True
                for c in s:
                    if c not in letters.values():
                        if free_spot:
                            free_spot = False
                            l = c
                        else:
                            correct = False
                # print(s, letters.values(), correct, )
                if correct and not free_spot:
                    five = s
                    letters["f"] = l
                    five_digits.remove(s)
                    break

            six_digits = [info[6], info[7], info[8]]
            # 9
            for s in six_digits:
                free_spot = True
                l = None
                correct = True
                for c in s:
                    # print("HDHAOW", letters.values(), letters, s)
                    if c not in letters.values():
                        if free_spot:
                            free_spot = False
                            l = c
                        else:
                            correct = False
                if correct and not free_spot and all((x in s) for x in one):
                    nine = s
                    letters["c"] = l
                    six_digits.remove(s)
                    break
            for c in eight:
                # print(letters.values(), len(letters))
                if c not in letters.values():
                    letters["e"] = c
                    break
            # print(letters, ans)

            convert = {
                "abcefg": 0,
                "cf": 1,
                "acdeg": 2,
                "acdfg": 3,
                "bcdf": 4,
                "abdfg": 5,
                "abdefg": 6,
                "acf": 7,
                "abcdefg": 8,
                "abcdfg": 9
            }

            letters = {v: k for k, v in letters.items()}
            # print(letters)

            num = []
            for s in o:
                let = []
                # print(s)
                for c in s:
                    let.append(letters[c])
                # print(let)
                num.append(str(convert["".join(sorted(let))]))
            num = int("".join(num))
            print(num)
            ans += num
        return ans

    def part202(self):
        d = self.data.copy()
        easy = (2, 3, 4, 7)
        signals = {
            2: 1,
            3: 7,
            4: 4,
            5: [2, 3, 5],
            6: [0, 6, 9],
            7: 8,
        }
        #  0000
        # 5    1
        # 5    1
        #  6666
        # 4    2
        # 4    2
        #  3333
        nmap = {}
        nmap[(0, 1, 2, 3, 4, 5)] = 0
        nmap[(1, 2)] = 1
        nmap[(0, 1, 3, 5, 6)] = 2
        nmap[(0, 1, 2, 3, 6)] = 3
        nmap[(1, 2, 5, 6)] = 4
        nmap[(0, 2, 3, 5, 6)] = 5
        nmap[(0, 2, 3, 4, 5, 6)] = 6
        nmap[(0, 1, 2)] = 7
        nmap[(0, 1, 2, 3, 4, 5, 6)] = 8
        nmap[(0, 1, 2, 3, 5, 6)] = 9
        print(len(nmap))

        kmap = {v: k for k, v in nmap.items()}
        print(kmap)

        ans = 0
        for info, o in d:
            let_to_num = {l: None for l in "abcdefg"}
            # parse input
            info = sorted(info, key=lambda x: len(x))
            print(info)
            for s in info:
                # print(s)
                if len(s) in easy:
                    # 1, 7, 4, (2, 3, 5), (0, 6, 9), 8

                    # n = signals[len(s)]
                    # vals = kmap[n]
                    known = set()
                    let_to_num[s[0]] = set(*kmap[0])
                    set.add(*kmap[0])
                    for x in kmap[7]:
                        if x not in let_to_num[s[0]]:
                            let_to_num[s[1]] = x
                            set.add(x)
                    for x in kmap[4]:
                        if x not in let_to_num[s[0]] and x != let_to_num[s[1]]:
                            let_to_num[s[2]] = x
                            set.add(x)
                    # try to find 3
                    for c in [s[3], s[4], s[5]]:
                    # try to find 9
                    # find unique 8 part
                    # 
                        ""
                    let_to_num[s[1]] = set(*vals)
                    let_to_num[s[1]] = set(*vals)
                    let_to_num[s[1]] = set(*vals)
                    let_to_num[s[1]] = set(*vals)

            # parse output
            output = []
            for s in o:
                if len(s) in easy:
                    output.append(str(signals[len(s)]))
                else:
                    nums = tuple(sorted([let_to_num[x] for x in s]))
                    print(nums, s, let_to_num, ans)
                    output.append(str(nmap[nums]))
            ans += int("".join(output))

        return ans



if __name__ == "__main__":
    path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\08\test.txt"
    path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\08\input.txt"
    test = Name(path)

    # part1 = test.part1()
    # print(part1)
    part2 = test.part2()
    print(part2)
