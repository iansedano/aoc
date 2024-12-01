from collections import Counter
from textwrap import dedent

from aocd import get_data

DAY = 1
YEAR = 2024
SAMPLE = dedent(
    """
    3   4
    4   3
    2   5
    1   3
    3   9
    3   3
    """.strip()
)


def parse(puzzle_input):
    left, right = [], []
    for line in puzzle_input.split("\n"):
        left_item, right_item = (int(i) for i in line.split())
        left.append(left_item)
        right.append(right_item)

    return left, right


def part_1(parsed_input):
    left, right = parsed_input
    return sum(abs(i - j) for i, j in zip(sorted(left), sorted(right)))


def part_2(parsed_input):
    left, right = parsed_input
    counter_right = Counter(right)
    return sum(counter_right[item] * item for item in left)


if __name__ == "__main__":
    data = get_data(day=DAY, year=YEAR).strip()
    parsed = parse(data)
    print(f"Part 1: {part_1(parsed)}")
    print(f"Part 2: {part_2(parsed)}")
