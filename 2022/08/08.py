# from aocd import get_data
# from aocd import submit
# from aocd import lines  # like data.splitlines()
# from aocd import numbers  # uses regex pattern -?\d+ to extract integers from data

# data = get_data(day=3, year=2022)

from string import ascii_lowercase, ascii_uppercase
from pprint import pprint

def p1(name):
    matrix = []
    checked = set()
    with open(name, "r") as f:
        for line in f:
            line = line.strip()
            matrix.append([int(x) for x in line])

    # print(matrix[0][:1])
    ans = 0
    for r in range(1, len(matrix) - 1):
        for c in range(1, len(matrix[0]) - 1):
            # check left and right no max higher
            val = matrix[r][c]
            # print(matrix[r][:c], matrix[r][c+1:])
            if val > max(matrix[r][:c] + [0]) or val > max(matrix[r][c+1:] + [0]):
                checked.add((r, c))
                ans += 1

    # pprint(matrix)
    # print(checked)
    matrix = [*zip(*matrix)]
    for r in range(1, len(matrix) - 1):
        for c in range(1, len(matrix[0]) - 1):
            # check left and right no max higher
            val = matrix[r][c]
            if (c, r) not in checked and (val > max(matrix[r][:c]) or val > max(matrix[r][c+1:])):
                ans += 1
                # print((r, c))
                # print
                # pprint(matrix)
    # print(checked)
    rlen = len(matrix[0])
    clen = len(matrix)
    return ans + rlen * 2 + clen * 2 - 4

from collections import defaultdict
def p2(name):
    matrix = []
    checked = set()
    with open(name, "r") as f:
        for line in f:
            line = line.strip()
            matrix.append([int(x) for x in line])

    # print(matrix[0][:1])
    ans = 0
    scores = defaultdict(lambda: 1)
    for r in range(1, len(matrix) - 1):
        for c in range(1, len(matrix[0]) - 1):
            # check left and right no max higher
            val = matrix[r][c]
            # print(matrix[r][:c], matrix[r][c+1:])
            tcount = 0
            for lc in range(c - 1, -1, -1):
                if matrix[r][lc] >= val:
                    tcount += 1
                    break
                else:
                    tcount += 1
            # if r == 3 and c == 2: print(tcount)
            scores[(r, c)] *= tcount
            tcount = 0
            for rc in range(c + 1, len(matrix[0])):
                if matrix[r][rc] >= val:
                    tcount += 1
                    break
                else:
                    tcount += 1
            # if r == 3 and c == 2: print(tcount)

            scores[(r, c)] *= tcount

    flipped = [*zip(*matrix)]
    for r in range(1, len(flipped) - 1):
        for c in range(1, len(flipped[0]) - 1):
            # check left and right no max higher
            val = flipped[r][c]
            # print(flipped[r][:c], flipped[r][c+1:])
            tcount = 0
            for lc in range(c - 1, -1, -1):
                if flipped[r][lc] >= val:
                    tcount += 1
                    break
                else:
                    tcount += 1
            # if r == 3 and c == 2: print(tcount)

            scores[(c, r)] *= tcount
            tcount = 0
            for rc in range(c + 1, len(flipped[0])):
                if flipped[r][rc] >= val:
                    tcount += 1
                    break
                else:
                    tcount += 1
            # if r == 3 and c == 2: print(tcount)

            scores[(c, r)] *= tcount
    # print(checked)
    # print(scores)
    # pprint(matrix)
    return max(scores.values())

print(p1("test"))
print(p1("input"))
print(p2("test"))
print(p2("input"))

# if __name__ == "__main__":
#     def submit_answer(ans, part):
#         submit(ans, part=part)
#     # submit_answer(a, part="a")
#     # submit_answer(b, part="b")
#     pass
