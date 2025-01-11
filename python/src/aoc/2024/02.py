from textwrap import dedent

from aocd import get_data

DAY = 2
YEAR = 2024
SAMPLE = dedent(
    """\
    7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9
    """
)


def parse(puzzle_input: str):
    return [
        [int(item) for item in line.split()]
        for line in puzzle_input.splitlines()
    ]


def part_1(parsed_input):
    return sum(is_safe(line) for line in parsed_input)


def part_2(parsed_input):
    return sum(is_safe_with_dampener(line) for line in parsed_input)


def is_safe(levels):
    diffs = [j - i for i, j in zip(levels[:-1], levels[1:])]
    if not all(diff > 0 for diff in diffs) and not all(
        diff < 0 for diff in diffs
    ):
        return False
    if any(diff == 0 for diff in diffs):
        return False
    if any(abs(diff) > 3 for diff in diffs):
        return False
    return True


def is_safe_with_dampener(levels):
    if is_safe(levels):
        return True

    for i in range(len(levels)):
        dampened_levels = [level for j, level in enumerate(levels) if i != j]
        if is_safe(dampened_levels):
            return True

    return False


if __name__ == "__main__":
    data = get_data(day=DAY, year=YEAR).strip()
    parsed = parse(SAMPLE)
    print(f"Part 1: {part_1(parsed)}")
    print(f"Part 2: {part_2(parsed)}")
