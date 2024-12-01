FILENAME = "input"

def part1():
    data = []
    with open(FILENAME) as f:
        for line in f:
            line = line.strip()
            numbers = line.split(": ")[1]
            winning, have = numbers.split(" | ")
            winning = winning.split(" ")
            have = have.split(" ")

            data.append((set(winning), have))
    
    ans = 0
    for winning, have in data:
        points = 0
        for card in have:
            if card == "":
                continue
            if card in winning:
                print(card)
                if points == 0:
                    points = 1
                else:
                    points *= 2
        ans += points
        print(points)
        print(winning, have)

    return ans
# print(part1())

def part2():
    data = []
    with open(FILENAME) as f:
        for line in f:
            line = line.strip()
            numbers = line.split(": ")[1]
            winning, have = numbers.split(" | ")
            winning = winning.split(" ")
            have = have.split(" ")

            data.append((set(winning), have))
    
    matches = {}
    for i, (winning, have) in enumerate(data):
        matching = 0
        for card in have:
            if card == "":
                continue
            if card in winning:
                matching += 1
        matches[i] = matching
    print(matches)

    copies = {i: 1 for i in range(len(data))}
    print(copies)
    for k, v in matches.items():
        print(k, v)
        for i in range(matches[k]):
            copies[k + i + 1] += copies[k]
    print(matches)
    print(copies)
    return sum(copies.values())

    # ans = len(data)
    # scratchcards = [i for i in range(len(data))]
    # matches = {}
    # while scratchcards:
    #     card_index = scratchcards.pop(0)

    #     if card_index in matches:
    #         ans += matches[card_index]

    #         for j in range(matches[card_index]):
    #             if card_index + j + 1 not in matches:
    #                 scratchcards.append(card_index + j + 1)
    #             else:
    #                 ans += matches[card_index + j + 1]
    #         continue

    #     winning, have = data[card_index]

    #     matching = 0
    #     for card in have:
    #         if card == "":
    #             continue
    #         if card in winning:
    #             matching += 1

    #     ans += matching
    #     matches[card_index] = matching
    #     for j in range(matching):
    #         scratchcards.append(card_index + j + 1)
    #     # print(matching)
    #     # print(winning, have)
    #     # print(len(scratchcards))
    #     print(ans)

    # print(matches)
    # return ans
print(part2())
