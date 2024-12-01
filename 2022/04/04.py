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
            p1, p2 = line.split(",")
            p1 = [int(x) for x in p1.split("-")]
            p2 = [int(x) for x in p2.split("-")]
            if (p1[0] <= p2[0] and p1[1] >= p2[1]) or (p2[0] <= p1[0] and p2[1] >= p1[1]):
                ans += 1
        return ans
def p2(name):
    with open(name, "r") as f:
        ans = 0
        for line in f:
            line = line.strip()
            p1, p2 = line.split(",")
            p1 = [int(x) for x in p1.split("-")]
            p2 = [int(x) for x in p2.split("-")]
            if (p1[1] >= p2[0] and p1[0] <= p2[0]) or (p2[1] >= p1[0] and p2[0] <= p1[0]):
                ans += 1
        return ans

print(p1("test"))
print(p1("input"))
print(p2("test"))
print(p2("input"))

# if __name__ == "__main__":
#     def submit_answer(ans, part):
#         submit(ans, part=part)
#     # submit_answer(a, part="a")
#     # submit_answer(b, part="b")
#     pass
