# Part 1: 6911
# Part 2: 3473

class Customs():
    def __init__(self, path):
        with open(path, "r") as f:
            self._data = [] # list of lists of form answers (letters a-z)
            _data = []
            family_members = 0
            for line in f:
                if line == "\n":
                    self._data.append((_data, family_members))
                    _data = []
                    family_members = 0
                else:
                    _data += list(line.strip())
                    family_members += 1

    def part1(self):
        count = 0
        for i in self._data:
            answers = set(i[0])
            count += len(answers)
        return count
    
    def part2(self):
        count = 0
        for i in self._data:
            family_members = i[1]
            storage = {}
            for j in i[0]:
                try:
                    storage[j] += 1
                except KeyError:
                    storage[j] = 1
            for k in storage:
                if storage[k] == family_members:
                    count += 1
        return count

if __name__ == "__main__":
    test = Customs(r"2020\day6\input.txt")
    print(test.part1())
    print(test.part2())
