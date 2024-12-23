from common import main

DAY = 4
YEAR = 2023
SAMPLE = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def parse(puzzle_input: str):
    splat = [line.split(": ") for line in puzzle_input.splitlines()]
    return [(int(s[0].split()[1]), *parse_card_nums(s[1])) for s in splat]


def parse_card_nums(card_nums: str):
    win_nums, your_nums = card_nums.split(" | ")
    return (
        set(int(n) for n in win_nums.split()),
        tuple(int(n) for n in your_nums.split()),
    )


def part1(parsed_input):
    return sum(
        2 ** (winners - 1)
        for _, win_nums, your_nums in parsed_input
        if (winners := sum(n in win_nums for n in your_nums)) > 0
    )


def part2(parsed_input):
    scores = [
        sum(n in win_nums for n in your_nums)
        for _, win_nums, your_nums in parsed_input
    ]

    cards = [1 for _ in scores]

    for idx, score in enumerate(scores):
        for j in range(idx + 1, idx + score + 1):
            cards[j] += cards[idx]

    return sum(cards)


if __name__ == "__main__":
    main(DAY, YEAR, SAMPLE, parse, part1, part2)
