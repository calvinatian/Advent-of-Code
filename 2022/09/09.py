# from aocd import get_data
# from aocd import submit
# from aocd import lines  # like data.splitlines()
# from aocd import numbers  # uses regex pattern -?\d+ to extract integers from data

# data = get_data(day=3, year=2022)

from string import ascii_lowercase, ascii_uppercase

def p1(name):
    with open(name, "r") as f:
        visited = set()
        visited.add((0, 0))
        hx, hy = 0, 0
        tx, ty = 0, 0
        for line in f:
            line = line.strip()
            direction, distance = line.split()
            distance = int(distance)
            for _ in range(distance):
                if direction == "U":
                    hy += 1
                elif direction == "D":
                    hy -= 1
                elif direction == "L":
                    hx -= 1
                elif direction == "R":
                    hx += 1
                if abs(hx - tx) + (abs(hy - ty)) > 2:
                    # move tx, ty
                    tx += 1 if hx > tx else -1
                    ty += 1 if hy > ty else -1
                elif abs(hx - tx) > 1:
                    tx += 1 if hx > tx else -1
                elif abs(hy - ty) > 1:
                    ty += 1 if hy > ty else -1
                # print((hx, hy), (tx, ty))
                visited.add((tx, ty))
        # print(visited)
        # print(sorted(visited))
        return len(visited)

def p2(name):
    with open(name, "r") as f:
        visited = set()
        visited.add((0, 0))
        # hx, hy = 0, 0
        # tx, ty = 0, 0
        knots = [[0, 0] for _ in range(10)]
        for line in f:
            line = line.strip()
            direction, distance = line.split()
            distance = int(distance)
            for _ in range(distance):
                for i, knot in enumerate(knots):
                    if i == 0:
                        hx, hy = knot
                        if direction == "U":
                            hy += 1
                        elif direction == "D":
                            hy -= 1
                        elif direction == "L":
                            hx -= 1
                        elif direction == "R":
                            hx += 1
                        knots[i] = [hx, hy]
                    else:
                        hx, hy = knots[i - 1]
                        tx, ty = knot
                        if abs(hx - tx) + (abs(hy - ty)) > 2:
                            # move tx, ty
                            tx += 1 if hx > tx else -1
                            ty += 1 if hy > ty else -1
                        elif abs(hx - tx) > 1:
                            tx += 1 if hx > tx else -1
                        elif abs(hy - ty) > 1:
                            ty += 1 if hy > ty else -1
                        knots[i] = [tx, ty]
                        # print((hx, hy), (tx, ty))
                    if i == 9:
                        visited.add((tx, ty))
        # print(visited)
        # print(sorted(visited))
        return len(visited)

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
