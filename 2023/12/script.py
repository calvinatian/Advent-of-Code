import sys
import re
from enum import Enum
from pprint import pprint
from collections import deque, defaultdict, Counter

if len(sys.argv) > 1:
    FILENAME = "input"
else:
    FILENAME = "test"

def is_valid(springs, damage):
    re_pattern = f"{}"
    for s in springs:

def part1():
    data = []

    with open(FILENAME) as f:
        for line in f:
            springs, damage = line.strip().split(" ")
            damage = [int(x) for x in damage.split(",")]
            data.append((springs, damage))
    pprint(data)

print(part1())
