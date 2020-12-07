# Part 1: 185
# Part 2: 89084

import re

class Luggage:
    def __init__(self, path: str):
        with open(path, "r") as f:
            self._rules = f.read()

    def parent_bag(self, search_color):
        """
        returns a set of all bag colors that could contain the input search bag
        """
        return self.parent_bag_helper(search_color, self._rules, set())

    def parent_bag_helper(self, search_color, rules, found_colors):
        """
        finds immediate parent bags of search_color and recursively searches those parents
        """
        parents = re.findall(f"(.*) bag.*contain.*{search_color} bag", rules)
        # base case, no bag color contains input color
        if len(parents) == 0:
            return
        else:
            for color in parents:
                found_colors.add(color)
                self.parent_bag_helper(color, rules, found_colors)
        return found_colors

    def child_bag(self, search_color):
        return sum(self.child_bag_helper(search_color, self._rules, [], 1))

    def child_bag_helper(self, search_color: str, rules: str, number_of_bags: list, parent_amount: int):
        # base case, bag has no children
        if re.search(f"{search_color} bags contain no other bags", rules):
            return
        else:
            children = re.search(f"{search_color} bags contain (.*).", rules).group(1)
            children = re.split(", ", children)

            for child in children:
                child = re.search(f"(\d*) (.*) bag", child)
                child_color = child.group(2)
                child_amount = int(child.group(1))

                number_of_bags.append(parent_amount * child_amount)
                self.child_bag_helper(child_color, rules, number_of_bags, parent_amount * child_amount)

        return number_of_bags

if __name__ == "__main__":
    path = r"2020\day7\input.txt"
    test = Luggage(path)
    part1 = test.parent_bag("shiny gold")
    print(len(part1))
    part2 = test.child_bag("shiny gold")
    print(part2)
