from textwrap import dedent

from aocd import get_data

DAY = 1
YEAR = 2024
SAMPLE = dedent(
    """
    
    """.strip()
)


def parse(puzzle_input):
    return puzzle_input


def part_1(parsed_input):
    return


def part_2(parsed_input):
    return


if __name__ == "__main__":
    data = get_data(day=DAY, year=YEAR).strip()
    parsed = parse(data)
    print(f"Part 1: {part_1(parsed)}")
    print(f"Part 2: {part_2(parsed)}")
