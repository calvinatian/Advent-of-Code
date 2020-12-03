# Part 1: 927684
# Part 2: 292093004

class Report():
    def __init__(self, path):
        """
        path should be absolute path to file

        file should contain a list of integers seperated by new lines
        """
        self._sum = 2020
        with open(path, "r") as f:
            self._data = [int(x) for x in list(f)]

    def __len__(self):
        """
        number of integers in data list
        """
        return len(self._data)
    def __repr__(self):
        return self._data
    def __iter__(self):
        for i in range(len(self)):
            yield self._data[i]

    def repair_two(self):
        """
        return the multiplication of the two numbers that add up to 2020
        """
        for i in range(0, len(self)):
            for j in range(i + 1, len(self)):
                if self._data[i] + self._data[j] == self._sum:
                    return self._data[i] * self._data[j]

    def repair_three(self):
        """
        return the multiplication of the three numbers that add up to 2020
        """
        for i in range(0, len(self)):
            for j in range(i + 1, len(self)):
                for k in range(j + 1, len(self)): 
                    if self._data[i] + self._data[j] + self._data[k] == self._sum:
                        return self._data[i] * self._data[j] * self._data[k]


if __name__ == "__main__":
    report = Report(r"2020\day1\input.txt")
    print(report.repair_two())
    print(report.repair_three())
