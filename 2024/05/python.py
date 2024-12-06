import argparse
import re
from pprint import pprint
from collections import defaultdict
from itertools import permutations

def open_file(filename):
    with open(filename) as f:
        return f.readlines()
    
def valid(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])

def recur(grid, r, c, seen):
    if (r, c) in seen:
        return
    if (r < len(grid) or c < len(grid[0])):
        return


def p1(text):
    ans = 0
    process_pages = False
    pages = []
    rules = defaultdict(list)
    for line in text:
        line = line.strip()
        if not line:
            process_pages = True
            continue
        if process_pages:
            pages.append([int(x) for x in line.split(",")])
        else:
            before, after = [int(x) for x in line.split("|")]
            rules[before].append(after)
    # pprint(rules)
    # print(pages)

    for line in pages:
        valid = True
        seq = []
        for page in line:
            # check if everything in seq so far doesnt contain current page as a before rule
            for prev in seq:
                if prev in rules[page]:
                    valid = False
                    break
            if not valid:
                break
            seq.append(page)

        if valid:
            ans += seq[len(seq)//2]



    return ans


def p2(text):
    ans = 0
    process_pages = False
    pages = []
    rules = defaultdict(list)
    for line in text:
        line = line.strip()
        if not line:
            process_pages = True
            continue
        if process_pages:
            pages.append([int(x) for x in line.split(",")])
        else:
            before, after = [int(x) for x in line.split("|")]
            rules[before].append(after)
    pprint(rules)
    print(pages)

    def isValid(line, rules):
        valid = True
        seq = []
        for page in line:
            # check if everything in seq so far doesnt contain current page as a before rule
            for prev in seq:
                if prev in rules[page]:
                    valid = False
                    break
            if not valid:
                break
            seq.append(page)

        if valid:
            # invalid_lines.append(seq)
            return True
        return False

    invalid_lines = []
    for line in pages:
        if not isValid(line, rules):
            invalid_lines.append(line)

    print(invalid_lines)

    def valid_page(page, rules, seq, to_check):
        # for prev in seq:
        #     if page in rules[prev]:
        #         return False

        for next in to_check:
            if page in rules[next]:
                return False
        return True

    def get_next_valid_page(rules, seq, to_check):
        for p in to_check:
            if valid_page(p, rules, seq, to_check):
                print(seq, p, to_check)
                return p
        raise Exception(f"cant find next page\n{rules=}\n{seq=}\n{to_check=}")


    valid = []
    for line in invalid_lines:
        seq = []
        length = len(line)
        while len(seq) != length:
            # get number not dependent on anything else
            page = get_next_valid_page(rules, seq, line)
            seq.append(page)
            print(line, page)
            line.remove(page)

        valid.append(seq)
        ans += seq[len(seq)//2]

    print(valid)
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
