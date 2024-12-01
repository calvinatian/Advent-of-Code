import argparse
from collections import Counter

def open_file(filename):
    with open(filename) as f:
        return f.readlines()

def p1(text):
    l, r = [], []
    for line in text:
        a, b = line.split()
        l.append(int(a))
        r.append(int(b))
    l.sort()
    r.sort()
    ans = 0
    for x, y in zip(l, r):
        ans += abs(abs(x) - abs(y))
    return ans

def p2(text):
    l, r = [], []
    for line in text:
        a, b = line.split()
        l.append(int(a))
        r.append(int(b))
    c = Counter(r)
    ans = 0
    for n in l:
        count = c.get(n, 0)
        ans += n * count
    return ans


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--test", help="run test file", action="store_true")
    args = parser.parse_args()
    filename = "input"
    if args.test:
        filename = "test"
    text = open_file(filename)
    print(f"Part 1: {p1(text)}")
    print(f"Part 2: {p2(text)}")
