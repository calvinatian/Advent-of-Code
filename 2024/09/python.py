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

def res(result):
    return "".join([str(x) for x in result])

def p1(text):
    ans = 0
    # counts = []
    # blanks = []
    disk = []
    for line in text:
        line = line.strip()
        # print(f"debug: line_length: {len(line)}, expected largest num: {len(line) // 2}")
        b = False
        num = 0
        for c in line:
            if b:
                disk.append((int(c), "blank"))
            else:
                disk.append((int(c), num))
                num += 1
            b = not b

    # print(disk)
    result = []
    index = 0
    back_index = len(disk) - 1
    # print(disk)
    done = False
    while index < len(disk):
        count, num = disk[index]
        if index == 3:
            set_break = 0
        # print(f"intermediate befor {index=}\t{back_index=}\t{res(result)=}\t{disk=}")
        if num == "blank" and index <= back_index:
            # fill in blank spots
            while count > 0 and index <= back_index:
                # get num to fill
                end_count, end_num = disk[back_index]
                while end_num == "blank" and back_index >= 0:
                    end_count, end_num = disk[back_index]
                    back_index -= 1
                
                if back_index < 0:
                    # print("ADWAIUHDAI")
                    done = True

                to_fill = min(count, end_count)
                result.extend([end_num for _ in range(to_fill)])
                count -= to_fill
                end_count -= to_fill

                # if count < 0 or end_count < 0:
                #     raise Exception(f"err: {count} {end_count, end_num}")
                disk[back_index] = (end_count, end_num)
                if end_count == 0:
                    back_index -= 1
                    # disk.append((end_count, end_num))

            # if index < len(disk):
            disk[index] = (0, "blank")
        # else:
        elif index <= back_index:
            result.extend([num for _ in range(count)])
            disk[index] = (0, num)
        # print(f"intermediate after {index=}\t{back_index=}\t{res(result)=}\t{disk=}")

        index += 1


    # print(disk)
    # print(result)
    # print("".join([str(x) for x in result]))

    # calculate checksum
    for i, n in enumerate(result):
        ans += i * n

    return ans


def p1_(text):
    ans = 0
    counts = []
    blanks = []
    for line in text:
        line = line.strip()
        b = False
        num = 0
        for c in line:
            if b:
                blanks.append(int(c))
            else:
                counts.append((int(c), num))
                num += 1
            b = not b

    print(counts, blanks)

    blank_index = 0
    transformed_blanks = []
    count_index = len(counts) - 1
    while count_index > 0:
        count, num = counts[count_index]
        while count > 0:
            blank_count = blanks[blank_index]
            if blank_count == 0:
                break
            to_remove = min(count, blank_count)
            count -= to_remove
            blanks[blank_index] -= to_remove
            if blanks[blank_index] == 0:
                blank_index += 1

            transformed_blanks.append((to_remove, num))

        counts[count_index] = (count, num)
        transformed_blanks.append("sep")
        count_index -= 1

    print(transformed_blanks)
    print(counts, blanks)

    # make result
    result = []
    count_index = 0
    transformed_index = 0
    while count_index < len(counts) and transformed_index < len(transformed_blanks):
        count, num = counts[count_index]
        result.extend([num for _ in range(count)])

        while transformed_blanks[transformed_index] != "sep":
            count, num = transformed_blanks[transformed_index]
            result.extend([num for _ in range(count)])
            transformed_index += 1

        transformed_index += 1
        count_index += 1
    # get remaining
    while count_index < len(counts):
        count, num = counts[count_index]
        result.extend([num for _ in range(count)])
        count_index += 1

    while transformed_index < len(transformed_blanks):
        if transformed_blanks[transformed_index] != "sep":
            count, num = transformed_blanks[transformed_index]
            result.extend([num for _ in range(count)])
        transformed_index += 1

    print(result)

    # calculate checksum
    for i, n in enumerate(result):
        ans += i * n

    return ans

def make_result(nums, blanks):
    result = []
    for i in range(len(blanks)):
        c, n = nums[i]
        result.extend([n for _ in range(c)])
        for c, n in blanks[i][1:]:
            result.extend([n for _ in range(c)])
        result.extend(["." for _ in range(blanks[i][0][0])])
    
    c, n = nums[-1]
    result.extend([n for _ in range(c)])
    return result


def p2(text):
    ans = 0
    # counts = []
    # blanks = []
    disk = []
    nums = []
    blanks = []
    for line in text:
        line = line.strip()
        print(f"debug: line_length: {len(line)}, expected largest num: {len(line) // 2}")
        b = False
        num = 0
        for c in line:
            if b:
                blanks.append([(int(c), ".")])
            else:
                nums.append((int(c), num))
                num += 1
            b = not b

    print(nums)
    print(blanks)
    result = []


    print(result)
    # print("".join([str(x) for x in result]))
    nums_index = len(nums) - 1
    while nums_index >= 0:
        count, num = nums[nums_index]

        for blank_index in range(len(blanks)):
            blank_count, _ = blanks[blank_index][0]
            if count <= blank_count and blank_index < nums_index:
                blank_count -= count
                blanks[blank_index].append((count, num))
                blanks[blank_index][0] = (blank_count, ".")
                # nums.pop(nums_index)
                nums[nums_index] = (count, ".")
                break

        nums_index -= 1

    print(nums)
    print(blanks)
    result = make_result(nums, blanks)
    print("".join(str(x) for x in result))

    # calculate checksum
    for i, n in enumerate(result):
        # print(f"{i=} {n=} {type(i)=} {type(n)=}")
        if n != ".":
            ans += i * n

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
