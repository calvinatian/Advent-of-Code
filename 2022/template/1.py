# from aocd import get_data
# from aocd import submit
# from aocd import lines  # like data.splitlines()
# from aocd import numbers  # uses regex pattern -?\d+ to extract integers from data

# data = get_data(day=3, year=2022)

import math
from pprint import pprint
from string import ascii_lowercase, ascii_uppercase
from collections import deque, defaultdict

def p1(name):
    ans = 0
    with open(name, "r") as f:
        for line in f:
            line = line.strip()
    return ans

def p2(name):
    ans = 0
    with open(name, "r") as f:
        for line in f:
            line = line.strip()
    return ans

pprint(f'{p1("test")=}')
pprint(f'{p1("input")=}')
pprint(f'{p2("test")=}')
pprint(f'{p2("input")=}')

# if __name__ == "__main__":
#     def submit_answer(ans, part):
#         submit(ans, part=part)
#     # submit_answer(a, part="a")
#     # submit_answer(b, part="b")
#     pass
