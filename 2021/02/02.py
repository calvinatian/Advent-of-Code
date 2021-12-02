# Part 1: 
# Part 2: 

class Name:
    def __init__(self, path):
        self._data = []
        with open(path, "r") as f:
            # print(f.readlines())
            self.data = [x.strip() for x in f.readlines()]

    def part1(self):
        ans = 0
        hor = 0
        ver = 0
        # print(self.data)
        for d in self.data:
            # print(d)
            a = d.split(' ')
            b = int(a[1])
            if a[0] == "forward":
                hor += b
            elif a[0] == "up":
                ver -= b
            else:
                ver += b

        return hor * ver

    def part2(self):
        ans = 0
        hor = 0
        ver = 0
        aim = 0
        depth = 0
        # print(self.data)
        for d in self.data:
            # print(d)
            a = d.split(' ')
            b = int(a[1])
            if a[0] == "forward":
                hor += b
                if aim:
                    depth += (b * aim)
            elif a[0] == "down":
                aim += b
            elif a[0] == "up":
                aim -= b

        print(depth, aim, hor)
        return hor * depth



if __name__ == "__main__":
    # path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\02\test.txt"
    path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\02\input.txt"
    test = Name(path)
    
    part1 = test.part1()
    print(part1)
    part2 = test.part2()
    print(part2)
