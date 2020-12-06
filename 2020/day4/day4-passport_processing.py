# Part 1: 196
# Part 2: 114
# Very messy, should redo using regex

import re
class Passport():
    def __init__(self, path):
        self._data = [] # list of lists, each list is a passport
        self._fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
        self._path = path
        with open(path, "r") as f:
            _passport = [] # temporary passport
            for line in f:
                if line == "\n":
                    self._data.append(_passport)
                    _passport = []
                else:
                    # remove newline characters, split at spacess
                    line = line.strip().split(" ")
                    _passport +=  line

    def __len__(self):
        """
        return number of passports
        """
        return len(self._data)
    def __repr__(self):
        return str(self._data)
    def __iter__(self):
        for i in self._data:
            yield i

    def check(self):
        valid = 0
        for passport in self:
            fields = self._fields.copy()
            _passport = []
            for field in passport:
                _field = field.split(":")
                _passport.append(_field[0])
        
            if len(_passport) == len(fields):
                valid += 1
            elif len(_passport) == len(fields) - 1:
                cid = False
                for i in _passport:
                    if i == "cid":
                        cid = True
                if cid == False:
                    valid += 1

        return valid

    def check_new(self):
        valid_passports = 0

        for passport in self:
            if len(passport) == len(self._fields):
                valid = True
            elif len(passport) == len(self._fields) - 1:
                cid = False
                for i in passport:
                    i = i.split(":")
                    if i[0] == "cid":
                        cid = True
                if cid == False:
                    valid = True
                else:
                    valid = False
            else:
                valid = False

            if valid:
                for field in passport:
                    field = field.split(":")
                    if field[0] == "byr":
                        if not 1920 <= int(field[1]) <= 2002:
                            valid = False
                            break
                    elif field[0] == "iyr":
                        if not 2010 <= int(field[1]) <= 2020:
                            valid = False
                            break
                    elif field[0] == "eyr":
                        if not 2020 <= int(field[1]) <= 2030:
                            valid = False
                            break
                    elif field[0] == "hgt":
                        unit = ""
                        num = ""
                        nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                        for char in field[1]:
                            if char in nums:
                                num += char
                            else:
                                unit += char
                        if unit != "cm" and unit != "in":
                            valid = False
                            break
                        elif unit == "cm":
                            if not 150 <= int(num) <= 193:
                                valid = False
                                break
                        elif unit == "in":
                            if not 59 <= int(num) <= 76:
                                valid = False
                                break

                    elif field[0] == "hcl":
                        if len(field[1]) != 7:
                            valid = False
                            break
                        else:
                            for i, char in enumerate(field[1]):
                                if i == 0:
                                    if char != "#":
                                        valid = False
                                        break
                                elif i <= 6:
                                    chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
                                    if char not in chars:
                                        valid = False
                                        break
                                elif i > 6:
                                    valid = False
                                    break

                    elif field[0] == "ecl":
                        colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                        if field[1] not in colors:
                            valid = False
                            break

                    elif field[0] == "pid":
                        nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                        if len(field[1]) == 9:
                            for char in field[1]:
                                if char not in nums:
                                    valid = False
                                    break
                        else:
                            valid = False
                            break

                    elif field[0] == "cid":
                        pass

                if valid:
                    valid_passports += 1

        return valid_passports

if __name__ == "__main__":
    p = Passport(r"2020\day4\input.txt")
    print(p.check())
    print(p.check_new())
