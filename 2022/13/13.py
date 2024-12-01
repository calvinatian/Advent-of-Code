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
        i = 1
        pairs = []
        for line in f:
            line = line.strip()
            if line == "":
                # do checking
                # print(pairs)
                p2 = pairs.pop()
                p1 = pairs.pop()
                def check(p1, p2):
                    # if not p1:
                    #     return True
                    # print(p1, p2)

                    if type(p1) == int and type(p2) == int:
                        return p1 - p2

                    elif type(p1) == list and type(p2) == list:
                        # if len(p2) < len(p1):
                        #     return len(p1) - len(p2)
                        for i in range(min(len(p1), len(p2))):
                            v = check(p1[i], p2[i])
                            if v == 0:
                                continue
                            return v
                        return len(p1) - len(p2)

                    elif type(p1) == int and type(p2) == list:
                        return check([p1], p2)
                    else:
                        return check(p1, [p2])
                        # p1 = 
                        # for i in range(len(p1)):
                        #     if not check(p1, p2[i]):
                        #         return False
                if check(p1, p2) < 0:
                    # print(i)
                    ans += i
                i += 1
                pairs = []
                continue
            # print(line)
            pairs.append(eval(line))

    # print(i)
    return ans

def p2(name):
    ans = 0
    with open(name, "r") as f:
        i = 1
        pairs = []
        for line in f:
            line = line.strip()
            if line == "":
                continue
            pairs.append(eval(line))

        pairs.append([[2]])
        pairs.append([[6]])

        def check(p1, p2):
            # if not p1:
            #     return True
            # print(p1, p2)

            if type(p1) == int and type(p2) == int:
                return p1 - p2

            elif type(p1) == list and type(p2) == list:
                # if len(p2) < len(p1):
                #     return len(p1) - len(p2)
                for i in range(min(len(p1), len(p2))):
                    v = check(p1[i], p2[i])
                    if v == 0:
                        continue
                    return v
                return len(p1) - len(p2)

            elif type(p1) == int and type(p2) == list:
                return check([p1], p2)
            else:
                return check(p1, [p2])

        from functools import cmp_to_key
        s = sorted(pairs, key=cmp_to_key(lambda x, y: check(x, y)))


    pprint(s)
    return (s.index([[2]]) + 1) * (s.index([[6]]) + 1)

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
