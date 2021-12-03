# Part 1: 741950
# Part 2: 903810

class Name:
    def __init__(self, path):
        self._data = []
        with open(path, "r") as f:
            # print(f.readlines())
            self.data = [x.strip() for x in f.readlines()]

    def part1(self):
        ans = 0
        gamma = []
        epsilon = []
        for i in range(len(self.data[0])):
            ones = 0
            zeroes = 0
            for n in self.data:
                if n[i] == "1":
                    ones += 1
                else:
                    zeroes += 1
            gamma.append("1" if ones > zeroes else "0")
            epsilon.append("1" if ones < zeroes else "0")


        gamma = int("".join(gamma), 2)
        epsilon = int("".join(epsilon), 2)
        # epsilon = ~gamma
        return gamma * epsilon

    def part2(self):
        oxygen = []
        carbon = []

        ones = 0
        zeroes = 0
        for n in self.data:
            if n[0] == "1":
                ones += 1
            else:
                zeroes += 1
        if ones >= zeroes:
            oxygen = [x for x in self.data if x[0] == "1"]
            carbon = [x for x in self.data if x[0] == "0"]
        else:
            oxygen = [x for x in self.data if x[0] == "0"]
            carbon = [x for x in self.data if x[0] == "1"]

        print(oxygen)
        for i in range(1, len(self.data[0])):
            if len(oxygen) == 1:
                break
            ones = 0
            zeroes = 0
            for n in oxygen:
                if n[i] == "1":
                    ones += 1
                else:
                    zeroes += 1
            if ones >= zeroes:
                oxygen = [x for x in oxygen if x[i] == "1"]
            else:
                oxygen = [x for x in oxygen if x[i] == "0"]
        for i in range(1, len(self.data[0])):
            if len(carbon) == 1:
                break
            ones = 0
            zeroes = 0
            for n in carbon:
                if n[i] == "1":
                    ones += 1
                else:
                    zeroes += 1
            if ones >= zeroes:
                carbon = [x for x in carbon if x[i] == "0"]
            else:
                carbon = [x for x in carbon if x[i] == "1"]


        return int(oxygen[0], 2) * int(carbon[0], 2)



if __name__ == "__main__":
    # path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\03\test.txt"
    path = r"E:\Cloud\Dropbox\Development\Python\Advent of Code\2021\03\input.txt"
    test = Name(path)
    
    # part1 = test.part1()
    # print(part1)
    part2 = test.part2()
    print(part2)
