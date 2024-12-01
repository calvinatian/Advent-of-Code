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
            data = line.strip()
        stream = [x for x in data[:4]]
        print(stream)
        for i, char in enumerate(data[4:]):
            if char in stream or len(set(stream)) != 4:
                stream.pop(0)
                stream.append(char)
            else:
                return i + 4
        return ans

def p2(name):
    with open(name, "r") as f:
        ans = 0
        for line in f:
            data = line.strip()
        stream = [x for x in data[:14]]
        for i, char in enumerate(data[14:]):
            # print(stream)
            if len(set(stream)) == 14:
                return i + 14

            stream.pop(0)
            stream.append(char)

        return i

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
