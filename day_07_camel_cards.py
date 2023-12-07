from collections import Counter
import functools


def part_1(data):
    def compare(hand1, hand2):
        card_scores = {c: i for i, c in enumerate("23456789TJQKA")}
        counts1 = [v for _, v in Counter(hand1).most_common()]
        counts2 = [v for _, v in Counter(hand2).most_common()]
        if counts1 == counts2:
            for a, b in zip(hand1, hand2):
                if a != b:
                    return 1 if card_scores[a] > card_scores[b] else -1
        return 1 if counts1 > counts2 else -1
    
    cards = [line.strip().split() for line in data]
    cards.sort(key=functools.cmp_to_key(lambda a, b: compare(a[0], b[0])))
    return sum(i * int(bid) for i, (_, bid) in enumerate(cards, start=1))


def part_2(data):
    def compare(hand1, hand2):
        card_scores = {c: i for i, c in enumerate("J23456789TQKA")}
        counter1 = Counter(hand1)
        counter2 = Counter(hand2)
        if "J" in hand1 and len(counter1) > 1:
            counter1 = Counter(hand1.replace("J", Counter(hand1.replace("J", "")).most_common()[0][0]))
        if "J" in hand2 and len(counter2) > 1:
            counter2 = Counter(hand2.replace("J", Counter(hand2.replace("J", "")).most_common()[0][0]))
        counts1 = [v for _, v in counter1.most_common()]
        counts2 = [v for _, v in counter2.most_common()]
        if counts1 == counts2:
            for a, b in zip(hand1, hand2):
                if a != b:
                    return 1 if card_scores[a] > card_scores[b] else -1
        return 1 if counts1 > counts2 else -1

    cards = [line.strip().split() for line in data]
    cards.sort(key=functools.cmp_to_key(lambda a, b: compare(a[0], b[0])))
    return sum(i * int(bid) for i, (_, bid) in enumerate(cards, start=1))


if __name__ == "__main__":
    with open("day_07_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
