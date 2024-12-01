# from aocd import get_data
# from aocd import submit
# from aocd import lines  # like data.splitlines()
# from aocd import numbers  # uses regex pattern -?\d+ to extract integers from data

# data = get_data(day=3, year=2022)

from string import ascii_lowercase, ascii_uppercase

def p1(name):
    with open(name, "r") as f:
        # instructions = f.readline()
        init_size = 8
        init_size = 3
        stacks = [
            ["V", "J", "B", "D"],
            ["F", "D", "R", "W", "B", "V", "P"],
            ["Q", "W", "C", "D", "L", "F", "G", "R"],
            ["B", "D", "N", "L", "M", "P", "J", "W"],
            ["Q", "S", "C", "P", "B", "N", "H"],
            ["G", "N", "S", "B", "D", "R"],
            ["H", "S", "F", "Q", "M", "P", "B", "Z"],
            ["F", "L", "W"],
            ["R", "M", "F", "V", "S",]
        ]
        for i in range(len(stacks)):
            stacks[i] = stacks[i][::-1]

        # stacks = [
        #     ["Z", "N"],
        #     ["M", "C", "D"],
        #     ["P"]
        # ]

        skip = 10
        # skip = 5
        while skip > 0:
            f.readline()
            skip -= 1

        for line in f:
            line = line.strip()
            # print(line)
            ins = [int(x) for i, x in enumerate(line.split(" ")) if i % 2 == 1]
            amt = ins[0]
            s1 = ins[1] - 1
            s2 = ins[2] - 1
            # print(amt, s1, s2)
            # print(stacks)
            # print(stacks[s1], len(stacks[s1]))
            while amt > 0:
                stacks[s2].append(stacks[s1].pop())
                amt -= 1

        return "".join([x[-1] if x else "" for x in stacks])

def p2(name):
    with open(name, "r") as f:
        # instructions = f.readline()
        init_size = 8
        init_size = 3
        stacks = [
            ["V", "J", "B", "D"],
            ["F", "D", "R", "W", "B", "V", "P"],
            ["Q", "W", "C", "D", "L", "F", "G", "R"],
            ["B", "D", "N", "L", "M", "P", "J", "W"],
            ["Q", "S", "C", "P", "B", "N", "H"],
            ["G", "N", "S", "B", "D", "R"],
            ["H", "S", "F", "Q", "M", "P", "B", "Z"],
            ["F", "L", "W"],
            ["R", "M", "F", "V", "S",]
        ]
        for i in range(len(stacks)):
            stacks[i] = stacks[i][::-1]

        # stacks = [
        #     ["Z", "N"],
        #     ["M", "C", "D"],
        #     ["P"]
        # ]

        skip = 5 if len(stacks) == 3 else 10
        while skip > 0:
            f.readline()
            skip -= 1

        for line in f:
            line = line.strip()
            print(line)
            ins = [int(x) for i, x in enumerate(line.split(" ")) if i % 2 == 1]
            amt = ins[0]
            s1 = ins[1] - 1
            s2 = ins[2] - 1
            print(amt, s1, s2)
            print(stacks)
            print(stacks[s1], len(stacks[s1]))
            stacks[s2].extend(stacks[s1][len(stacks[s1]) - amt:])
            stacks[s1] = stacks[s1][:len(stacks[s1]) - amt]
            # while amt > 0:
            #     stacks[s2].append(stacks[s1].pop())
            #     amt -= 1
        print(stacks)
        return "".join([x[-1] if x else "" for x in stacks])

# print(p1("test"))
# print(p1("input"))
# print(p2("test"))
print(p2("input"))

# if __name__ == "__main__":
#     def submit_answer(ans, part):
#         submit(ans, part=part)
#     # submit_answer(a, part="a")
#     # submit_answer(b, part="b")
#     pass
