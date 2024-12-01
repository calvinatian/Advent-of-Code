# from aocd import get_data
# from aocd import submit
# from aocd import lines  # like data.splitlines()
# from aocd import numbers  # uses regex pattern -?\d+ to extract integers from data

# data = get_data(day=3, year=2022)

from string import ascii_lowercase, ascii_uppercase

def p1(name):
    with open(name, "r") as f:
        ans = 0
        for line in f:
            line = line.strip()
            l = len(line)
            a, b = line[:l // 2], line[(l // 2):]
            # print(a, b)
            for char in a:
                if char in b:
                    if char in ascii_lowercase:
                        v = ord(char) - ord("a") + 1
                        ans += v
                    elif char in ascii_uppercase:
                        v = ord(char) - ord("A") + 1 + 26
                        ans += v
                    print(char.__repr__(), ans, v)
                    break
        return ans
def p2(name):
    with open(name, "r") as f:
        ans = 0
        group = []
        for line in f:
            line = line.strip()
            group.append(line)
            if len(group) != 3:
                continue
            for char in group[0]:
                if char in group[1] and char in group[2]:
                    if char in ascii_lowercase:
                        v = ord(char) - ord("a") + 1
                        ans += v
                    elif char in ascii_uppercase:
                        v = ord(char) - ord("A") + 1 + 26
                        ans += v
                    print(char.__repr__(), ans, v)
                    break
            group = []
        return ans

# print(p1("test"))
# print(p1("input"))
print(p2("test"))
print(p2("input"))

# if __name__ == "__main__":
#     def submit_answer(ans, part):
#         submit(ans, part=part)
#     # submit_answer(a, part="a")
#     # submit_answer(b, part="b")
#     pass
