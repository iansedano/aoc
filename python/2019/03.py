from textwrap import dedent

from aocd import get_data

DAY = 3
YEAR = 2019
SAMPLE = dedent(
    """
    
    """.strip()
)


def parse(puzzle_input):
    return puzzle_input


def part1(parsed_input):
    return


def part2(parsed_input):
    return


if __name__ == "__main__":
    data = get_data(day=DAY, year=YEAR).strip()
    parsed = parse(data)
    print(f"Part 1: {part1(parsed)}")
    print(f"Part 2: {part2(parsed)}")
