from collections import defaultdict
from itertools import product
from textwrap import dedent

from aocd import get_data

DAY = 4
YEAR = 2024
SAMPLE = dedent(
    """\
    MMMSXXMASM
    MSAMXMSMSA
    AMXSXMAAMM
    MSAMASMSMX
    XMASAMXAMM
    XXAMMXXAMA
    SMSMSASXSS
    SAXAMASAAA
    MAMMMXMMMM
    MXMXAXMASX
    """
)


def parse(puzzle_input):
    lines = puzzle_input.splitlines()
    height = len(lines)
    width = len(lines[0])

    grid = defaultdict(str)
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, char in enumerate(line):
            grid[(x, y)] = char

    return (width, height), grid


def part_1(parsed_input):
    (width, height), grid = parsed_input
    valid = ["XMAS", "SAMX"]

    horizontal = [(0, 0), (1, 0), (2, 0), (3, 0)]
    diagonal_r = [(0, 0), (1, 1), (2, 2), (3, 3)]
    vertical = [(0, 0), (0, 1), (0, 2), (0, 3)]
    diagonal_l = [(0, 0), (-1, 1), (-2, 2), (-3, 3)]

    dirs = [horizontal, diagonal_r, vertical, diagonal_l]

    return sum(
        sum(
            [
                "".join([grid[(pos[0] + x, pos[1] + y)] for pos in dir])
                in valid
                for dir in dirs
            ]
        )
        for y, x in product(range(height), range(width))
    )

    # count = 0

    # for y, x in product(range(height), range(width)):
    #     possibles = [
    #         "".join([grid[(pos[0] + x, pos[1] + y)] for pos in dir])
    #         for dir in dirs
    #     ]
    #     for possible in possibles:
    #         if possible in valid:
    #             count += 1

    # return count


def part_2(parsed_input):
    (width, height), grid = parsed_input
    valid = ["MAS", "SAM"]

    ex_left = [(0, 0), (1, 1), (2, 2)]
    ex_right = [(2, 0), (1, 1), (0, 2)]

    count = 0

    for y, x in product(range(height), range(width)):

        left = "".join([grid[(pos[0] + x, pos[1] + y)] for pos in ex_left])
        right = "".join([grid[(pos[0] + x, pos[1] + y)] for pos in ex_right])

        if left in valid and right in valid:
            count += 1

    return count


if __name__ == "__main__":
    data = get_data(day=DAY, year=YEAR).strip()
    parsed = parse(SAMPLE)
    print(f"Part 1: {part_1(parsed)}")
    print(f"Part 2: {part_2(parsed)}")
