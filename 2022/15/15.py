# from aocd import get_data
# from aocd import submit
# from aocd import lines  # like data.splitlines()
# from aocd import numbers  # uses regex pattern -?\d+ to extract integers from data

# data = get_data(day=3, year=2022)

import math
from pprint import pprint
from string import ascii_lowercase, ascii_uppercase
from collections import deque, defaultdict
import re

def mergeIntervals(intervals):
    intervals.sort()
    n_intervals = []
    for l,r in intervals:
        if len(n_intervals)==0 or l>n_intervals[-1][1]:
            n_intervals.append((l,r))
            continue
        r = max(r,n_intervals[-1][1])
        ll,rr = n_intervals.pop()
        n_intervals.append((ll,r))
    return n_intervals
# def mergeIntervals(intervals):
#     # Sort the array on the basis of start values of intervals.
#     intervals.sort()
#     stack = []
#     # insert first interval into stack
#     stack.append(intervals[0])
#     for i in intervals[1:]:
#         # Check for overlapping interval,
#         # if interval overlap
#         if stack[-1][0] <= i[0] <= stack[-1][-1]:
#             stack[-1][-1] = max(stack[-1][-1], i[-1])
#         else:
#             stack.append(i)
#     # print("The Merged Intervals are :", end=" ")
#     # for i in range(len(stack)):
#     #     print(stack[i], end=" ")
#     # print()
#     return stack

def p1(name):
    data = []
    with open(name, "r") as f:
        for line in f:
            nums = [int(x.group()) for x in re.finditer(r"-?\d+", line)]
            sensor_x, sensor_y, beacon_x, beacon_y = nums
            x_diff = abs(sensor_x - beacon_x)
            y_diff = abs(sensor_y - beacon_y)
            data.append((sensor_x, sensor_y, beacon_x, beacon_y, x_diff, y_diff))

    loc = 10
    loc = 2000000
    x_intervals = []
    for sensor_x, sensor_y, beacon_x, beacon_y, x_diff, y_diff in data:
        total_diff = x_diff + y_diff
        if sensor_y - total_diff <= loc <= sensor_y + total_diff:
            # x_range = x_diff - abs(loc - sensor_y) + 1
            x_range = total_diff - abs(loc - sensor_y)
            if x_range < 0:
                continue
            x_bounds = [sensor_x - x_range, sensor_x + x_range]
            x_intervals.append(x_bounds)

    # print(x_intervals)
    if not x_intervals:
        return 0
    merged = mergeIntervals(x_intervals)
    ans = 0
    for x1, x2 in merged:
        ans += x2 - x1
    return ans

def p2(name):
    data = []
    with open(name, "r") as f:
        for line in f:
            nums = [int(x.group()) for x in re.finditer(r"-?\d+", line)]
            sensor_x, sensor_y, beacon_x, beacon_y = nums
            x_diff = abs(sensor_x - beacon_x)
            y_diff = abs(sensor_y - beacon_y)
            data.append((sensor_x, sensor_y, beacon_x, beacon_y, x_diff, y_diff))

    # print(data)
    # loc = 10
    # loc = 2000000
    min_x, min_y = 0, 0
    max_x, max_y = 20, 20
    max_x, max_y = 4000000, 4000000
    all_x_intervals = []
    for y in range(min_y, max_y + 1):
        x_intervals = []
        loc = y
        for sensor_x, sensor_y, beacon_x, beacon_y, x_diff, y_diff in data:
            total_diff = x_diff + y_diff
            y_dist = abs(y - sensor_y)
            if y_dist > total_diff:
                continue

            x_range = total_diff - y_dist
            x_bounds = [sensor_x - x_range, sensor_x + x_range]
            x_intervals.append(x_bounds)
        if not x_intervals:
            continue

        merged = mergeIntervals(x_intervals)
        if len(merged) >= 2:
            # print(y, merged, sorted(x_intervals))
            print(y, merged)
            return (4000000 * (merged[0][1] + 1)) + y
        all_x_intervals.append(merged)
    # print(all_x_intervals)

    # for i, x_intervals in enumerate(all_x_intervals):
    #     # if len(x_intervals) == 2:
    #     #     if abs(x_intervals[0][1] - x_intervals[1][0]) == 2:
    #     #         return (4000000 * (x_intervals[0][1] + 1)) + i
    #     print(i, x_intervals)
    # print(x_intervals)
    # if not x_intervals:
    #     return 0
    # ans = 0
    # for x1, x2 in merged:
    #     ans += x2 - x1
    # return ans

pprint(f'{p1("test")=}')
pprint(f'{p1("input")=}')
# pprint(f'{p2("test")=}')
pprint(f'{p2("input")=}')

# if __name__ == "__main__":
#     def submit_answer(ans, part):
#         submit(ans, part=part)
#     # submit_answer(a, part="a")
#     # submit_answer(b, part="b")
#     pass
