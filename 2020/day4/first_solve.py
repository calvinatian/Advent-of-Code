# Part 1: 196
# Part 2: 114

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
            # print(passport)
            fields = self._fields.copy()
            _passport = []
            for field in passport:
                # print(field)
                _field = field.split(":")
                # print(_field)
                _passport.append(_field[0])
        
            # print(_passport, fields)
            if len(_passport) == len(fields):
                # print(_passport)
                valid += 1
            elif len(_passport) == len(fields) - 1:
                # check if only missing field is cid
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
                    # print(field)
                    if field[0] == "byr":
                        # print(int(field[1]))
                        if not 1920 <= int(field[1]) <= 2002:
                            # print("FALSE", field[1])
                            valid = False
                            break
                        # print(field[1])
                    elif field[0] == "iyr":
                        if not 2010 <= int(field[1]) <= 2020:
                            valid = False
                            break
                        # print(field[1])
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
                        # print(unit)
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
                        # print(field[1])

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
                        # print(field[1])

                    elif field[0] == "ecl":
                        colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                        if field[1] not in colors:
                            # print(field[1])
                            valid = False
                            break
                        # print(field[1])

                    elif field[0] == "pid":
                        nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                        if len(field[1]) == 9:
                            # print(field[1])
                            for char in field[1]:
                                if char not in nums:
                                    valid = False
                                    break
                        else:
                            valid = False
                            break
                        # print(field[1])

                    elif field[0] == "cid":
                        pass
                    # else:
                    #     valid = False
                    #     break

                if valid:
                    # print(passport)
                    valid_passports += 1

        return valid_passports

    # def check_new(self):
    #     # use regex
    #     with open(self._path, "r") as f:
    #         for line in f:
    #             pass



    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    # hgt (Height) - a number followed by either cm or in:
    #     If cm, the number must be at least 150 and at most 193.
    #     If in, the number must be at least 59 and at most 76.
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    # cid (Country ID) - ignored, missing or not.

    # byr (Birth Year)
    # iyr (Issue Year)
    # eyr (Expiration Year)
    # hgt (Height)
    # hcl (Hair Color)
    # ecl (Eye Color)
    # pid (Passport ID)
    # cid (Country ID)

if __name__ == "__main__":
    p = Passport(r"2020\day4\input.txt")
    print(len(p))
    # print(p)
    # for i in p:
    #     print(i)
    # p.check()
    print(p.check_new()) # <116
