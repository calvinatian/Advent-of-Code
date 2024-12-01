# from aocd import get_data
# from aocd import submit
# from aocd import lines  # like data.splitlines()
# from aocd import numbers  # uses regex pattern -?\d+ to extract integers from data

# data = get_data(day=3, year=2022)

from string import ascii_lowercase, ascii_uppercase
from collections import defaultdict, Counter, deque
from pprint import pprint
from copy import deepcopy
import re

class Monkey:
    def __init__(self, items, op, test, testt, testf):
        self.items = items
        self.op = op
        self.test = test
        self.testt = testt
        self.testf = testf
        self.inspections = 0

    def __repr__(self):
        return f"Inspections: {self.inspections}"
        return f"Monkey({self.items}, {self.op}, {self.test}, {self.testt}, {self.testf})"

def p1(name):
    ans = 0
    monkeys = {}
    with open(name, "r") as f:
        # 5 lines per monkey
        i = 0
        size = 3 if name == "test" else 7
        while i <= size:
            monkey = f.readline()
            monkey = i
            i += 1
            items = [x.strip(",") for x in f.readline().strip().split()[2:]]
            op = f.readline().strip().split()[-3:]
            test = f.readline().strip().split()[-1]
            testt = f.readline().strip()[-1]
            testf = f.readline().strip()[-1]
            blank = f.readline().strip()
            monkeys[monkey] = Monkey(items, op, test, testt, testf)
            # print(f"{monkey=}, {items=}, {op=}, {test=}, {testt=}, {testf=}")
        # for line in f:
        #     line = line.strip()
        #     if i % 5 == 0:
        #         monkeys[line] = []
        #     i += 1

    rounds = 0
    while rounds < 20:
        for i in monkeys:
            mon = monkeys[i]
            # j = 0
            while len(mon.items) > 0:
            # for i in range(len(mon.items)):
                worry = int(mon.items.pop(0))
                mon.inspections += 1
                # j += 1
                # monkey inspects
                if mon.op[1] == "*":
                    # mul
                    if mon.op[2] == "old":
                        worry *= worry
                    else:
                        worry *= int(mon.op[2])
                elif mon.op[1] == "+":
                    worry += int(mon.op[2])
                # worry // 3
                worry //= 3
                test = int(mon.test)
                if worry % test == 0:
                    # do testt
                    new_mon = int(mon.testt)
                else:
                    # do testf
                    new_mon = int(mon.testf)
                # throw item
                monkeys[new_mon].items.append(worry)
        rounds += 1

    return sorted(monkeys.items(), key=lambda x: x[1].inspections, reverse=True)

def printcrt(crt):
    
    c = deepcopy(crt)
    for _ in range(6):
        print("".join(c.pop(0)))


def p2(name):
    ans = 0
    monkeys = {}
    with open(name, "r") as f:
        # 5 lines per monkey
        i = 0
        size = 3 if name == "test" else 7
        while i <= size:
            monkey = f.readline()
            monkey = i
            i += 1
            items = [x.strip(",") for x in f.readline().strip().split()[2:]]
            op = f.readline().strip().split()[-3:]
            test = f.readline().strip().split()[-1]
            testt = f.readline().strip()[-1]
            testf = f.readline().strip()[-1]
            blank = f.readline().strip()
            monkeys[monkey] = Monkey(items, op, test, testt, testf)

    from functools import reduce
    from operator import mul
    lcm = reduce(mul, [int(monkeys[mon].test) for mon in monkeys], 1)  # prod of mods

    rounds = 0
    while rounds < 10000:
        for i in monkeys:
            mon = monkeys[i]
            # j = 0
            while len(mon.items) > 0:
            # for i in range(len(mon.items)):
                worry = int(mon.items.pop(0))
                mon.inspections += 1
                # j += 1
                # monkey inspects
                if mon.op[1] == "*":
                    # mul
                    if mon.op[2] == "old":
                        worry *= worry
                    else:
                        worry *= int(mon.op[2])
                elif mon.op[1] == "+":
                    worry += int(mon.op[2])
                # worry // 3
                # worry //= 3\
                worry %= lcm
                test = int(mon.test)
                if worry % test == 0:
                    # do testt
                    new_mon = int(mon.testt)
                else:
                    # do testf
                    new_mon = int(mon.testf)
                # throw item
                monkeys[new_mon].items.append(worry)
        rounds += 1

    return sorted(monkeys.items(), key=lambda x: x[1].inspections, reverse=True)

pprint(p1("test"))
pprint(p1("input"))
pprint(p2("test"))
pprint(p2("input"))

# if __name__ == "__main__":
#     def submit_answer(ans, part):
#         submit(ans, part=part)
#     # submit_answer(a, part="a")
#     # submit_answer(b, part="b")
#     pass
