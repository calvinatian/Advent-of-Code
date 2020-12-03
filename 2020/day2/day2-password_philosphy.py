# Part 1: 638
# Part 2: 699

class Password():
    def __init__(self, path):
        """
        path should be absolute path to file

        file should contain a range of numbers, a letter, and a string seperated by new lines
        """
        self._data = []
        with open(path, "r") as f:
            for line in f:
                # make each line in the file a list of the password paramaters
                self._data.append(line.strip().split(" "))

    def __len__(self):
        return len(self._data)
    def __repr__(self):
        return self._data
    def __iter__(self):
        for i in range(len(self)):
            yield self._data[i]

    def checker(self):
        """
        range of numbers represents minimum number of times a letter has to appear

        return number of valid passwords
        """
        valid = 0
        for pass_ in self._data:
            num = pass_[0].split("-")
            min_, max_ = int(num[0]), int(num[1])
            letter = pass_[1].strip(":")
            password = pass_[2]
            counter = 0
            for l in password:
                if l == letter:
                    counter += 1
            if min_ <= counter <= max_:
                valid += 1
        return valid

    def checker_new(self):
        """
        range of numbers represent the positions where the letter has to appear (only once out of the two positions)

        return number of valid passwords
        """
        valid = 0
        for pass_ in self._data:
            num = pass_[0].split("-") # split the range
            first, second = int(num[0]) - 1, int(num[1]) - 1 # first num is first position, second num is second position
            letter = pass_[1].strip(":")
            password = list(pass_[2])
            counter = 0
            if (password[first] == letter) ^ (password[second] == letter): # XOR the two positions
                valid += 1
        return valid


if __name__ == "__main__":
    password = Password(r"2020\day2\input.txt")
    print(password.checker())
    print(password.checker_new())
