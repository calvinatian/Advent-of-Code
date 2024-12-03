import argparse
import re

def open_file(filename):
    with open(filename) as f:
        return f.readlines()


def p1(text):
    ans = 0
    for line in text:
        matches = re.findall(r"mul\((\d+),(\d+)\)", line)
        for x, y in matches:
            ans += int(x) * int(y)

    return ans


def p2(text):
    ans = 0
    go = True
    for line in text:
        matches = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", line)
        for a, b, do, dont in matches:
            if do:
                go = True
            if dont:
                go = False
            if a and b and go:
                ans += int(a) * int(b)

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
