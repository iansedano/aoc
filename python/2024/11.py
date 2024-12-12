import functools
from collections import defaultdict
from textwrap import dedent

from aocd import get_data

DAY = 1
YEAR = 2024
SAMPLE = dedent(
    """\
    125 17
    """
)


def parse(puzzle_input):
    return [int(s) for s in puzzle_input.split(" ")]


def part_1(parsed_input):
    arrangement = parsed_input

    for _ in range(25):
        iteration = []
        for stone in arrangement:
            iteration.extend(transform_stone(stone))
        arrangement = iteration

    return len(arrangement)


def part_2(parsed_input):
    map = defaultdict(int)
    for stone in parsed_input:
        map[stone] += 1

    for _ in range(75):
        stones_to_transform = list(map.items())

        for stone, value in stones_to_transform:
            map[stone] -= value
            if map[stone] == 0:
                del map[stone]

            for res in transform_stone(stone):
                map[res] += value

    return sum(map.values())


@functools.cache
def transform_stone(stone):
    """
    >>> transform_stone(0)
    [1]
    >>> transform_stone(4444)
    [44, 44]
    >>> transform_stone(10)
    [1, 0]
    >>> transform_stone(1)
    [2024]
    >>> transform_stone(999)
    [2021976]
    """
    if stone == 0:
        return [1]

    string = str(stone)
    length = len(string)
    half = length // 2
    if length % 2 == 0:
        return [
            int(string[:half]),
            int(string[half:]),
        ]
    return [stone * 2024]


if __name__ == "__main__":
    data = get_data(day=DAY, year=YEAR).strip()
    parsed = parse(data)
    print(f"Part 1: {part_1(parsed)}")
    print(f"Part 2: {part_2(parsed)}")
