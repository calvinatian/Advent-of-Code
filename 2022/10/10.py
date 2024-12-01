# from aocd import get_data
# from aocd import submit
# from aocd import lines  # like data.splitlines()
# from aocd import numbers  # uses regex pattern -?\d+ to extract integers from data

# data = get_data(day=3, year=2022)

from string import ascii_lowercase, ascii_uppercase
from collections import defaultdict, Counter, deque
from pprint import pprint

def p1(name):
    with open(name, "r") as f:
        ins = []
        for i, line in enumerate(f):
            line = line.strip()
            ins.append(line)
            if "addx" in line:
                ins.append("noop")
    x = 1
    i = 1
    n = 0
    delay = [0, 0]
    ans = []
    while ins:
        op = ins.pop(0)
        # print(op)


        if i == 20 or (i + 20) % 40 == 0:
            ans.append(x * i)
            # print(i, x)

        if op == "noop":
            # do delay 1 cycle
            n = 0

        else:
            # print(op)
            op, n = op.split(" ")
            n = int(n)

        # print(i, x, n, end=" | ")

        delay = [delay[1], n]
        x += delay[0]
        # print(i, x, n, delay)
        # delay[0] = delay[1]
        # delay[1] = n

        i += 1
    print(ans)
    return sum(ans)

def printcrt(crt):
    from copy import deepcopy
    c = deepcopy(crt)
    for _ in range(6):
        print("".join(c.pop(0)))


def p2(name):
    with open(name, "r") as f:
        ins = []
        for i, line in enumerate(f):
            line = line.strip()
            ins.append(line)
            if "addx" in line:
                ins.append("noop")
    x = 1
    i = 1
    n = 0
    delay = [0, 0]
    ans = []
    crt = [["." for _ in range(40)] for _ in range(6)]
    # crt = ["#" * 40 for _ in range(6)]
    printcrt(crt)
    while ins:
        op = ins.pop(0)
        # print(op)

        if i == 20 or (i + 20) % 40 == 0:
            ans.append(x * i)
            # print(i, x)

        crtix = (i - 1) // 40
        crtiy = (i - 1) % 40
        print(i, x, crtix, crtiy)
        if x - 1 <= (crtiy) <= x + 1:
            crt[crtix][crtiy] = "#"
            # crt[crtix] = crt[crtix][:crtiy] + "." + crt[crtix][:crtiy + 1]

        if op == "noop":
            # do delay 1 cycle
            n = 0

        else:
            # print(op)
            op, n = op.split(" ")
            n = int(n)

        # print(i, x, n, end=" | ")

        delay = [delay[1], n]
        x += delay[0]

        i += 1
    # pprint(crt)
    printcrt(crt)
    print(ans)
    return sum(ans)

# print(p1("test"))
# print(p1("input"))
print(p2("test"))
print(p2("input"))

# if __name__ == "__main__":
#     def submit_answer(ans, part):
#         submit(ans, part=part)
#     # submit_answer(a, part="a")
#     # submit_answer(b, part="b")
#     pass
