import sys
import re
from enum import Enum
from pprint import pprint
from collections import deque, defaultdict, Counter

if len(sys.argv) > 1:
    FILENAME = "input"
else:
    FILENAME = "test"

def part1():
    data = []

    with open(FILENAME) as f:
        for line in f:
