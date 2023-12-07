import math
from collections import Counter

from common import main

DAY = 7
YEAR = 2023
SAMPLE = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


def parse(puzzle_input):
    step = [
        (
            (h := hand.split())[0],
            int(h[1]),
        )  # QQQJA 483 -> ((12, 12, 12, 11, 10), 483)
        for hand in puzzle_input.splitlines()
    ]

    return (
        [(parse_cards_jack(s[0]), s[1]) for s in step],
        [(parse_cards_joker(s[0]), s[1]) for s in step],
    )


def parse_cards_jack(hand):
    FACES = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}

    return tuple(
        int(char) if char not in FACES else FACES[char] for char in hand
    )


def parse_cards_joker(hand):
    FACES = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10}

    return tuple(
        int(char) if char not in FACES else FACES[char] for char in hand
    )


def part1(parsed_input):
    hands, _ = parsed_input
    hands = sorted(hands, key=lambda h: h[0], reverse=True)
    hands = sorted(hands, key=sort_hand_types, reverse=True)

    return sum(i * h[1] for i, h in enumerate(reversed(hands), 1))


def part2(parsed_input):
    _, hands = parsed_input
    hands = sorted(hands, key=lambda h: h[0], reverse=True)
    hands = sorted(hands, key=sort_hand_types_wildcard, reverse=True)

    return sum(i * h[1] for i, h in enumerate(reversed(hands), 1))


def sort_hand_types(hand):
    h, bid = hand
    h_c = Counter(h)
    counts = sorted(h_c.values(), reverse=True)
    if counts[0] == 5:  # five of kind
        return 7
    if counts[0] == 4:  # four of kind
        return 6
    if counts[0] == 3 and counts[1] == 2:  # full house
        return 5
    if counts[0] == 3:  # three of kind
        return 4
    if counts[0] == 2 and counts[1] == 2:  # two pair
        return 3
    if counts[0] == 2:  # pair
        return 2
    return 1


def sort_hand_types_wildcard(hand):
    h, bid = hand
    h_c = Counter(h)
    wildcards = h_c[1]
    h_c = Counter(filter(lambda c: c != 1, h))
    counts = sorted(h_c.values(), reverse=True)
    if wildcards == 5:  # 5 of kind
        return 7
    if counts[0] + wildcards == 5:  # 5 of kind
        return 7
    if counts[0] + wildcards == 4:  # 4 of kind
        return 6
    if counts[0] + counts[1] + wildcards == 5:  # full house
        return 5
    if counts[0] + wildcards == 3:  # three of kind
        return 4
    if counts[0] + counts[1] + wildcards == 4:  # two pair
        return 3
    if counts[0] + wildcards == 2:  # pair
        return 2
    return 1


if __name__ == "__main__":
    main(DAY, YEAR, SAMPLE, parse, part1, part2)
