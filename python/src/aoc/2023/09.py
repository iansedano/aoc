from common import main

DAY = 9
YEAR = 2023
SAMPLE = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


def parse(puzzle_input):
    return [
        tuple(int(i) for i in line.split())
        for line in puzzle_input.splitlines()
    ]


def part1(parsed_input):
    return sum(get_next_oasis_value(seq) for seq in parsed_input)


def part2(parsed_input):
    return sum(get_next_oasis_value(seq, reverse=True) for seq in parsed_input)


def get_next_oasis_value(sequence, reverse=False):
    diffs = [sequence[::-1]] if reverse else [sequence]

    while not all(i == 0 for i in diffs[-1]):
        diffs.append(get_differences(diffs[-1]))

    return sum(element[-1] for element in reversed(diffs))


def get_differences(sequence):
    return [b - a for a, b in zip(sequence[:-1], sequence[1:])]


if __name__ == "__main__":
    main(DAY, YEAR, SAMPLE, parse, part1, part2)
