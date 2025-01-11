import re
from textwrap import dedent

from aocd import get_data

DAY = 3
YEAR = 2024
SAMPLE = dedent(
    """\
    xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
    """
)


def parse(puzzle_input):
    return puzzle_input


def part_1(parsed_input):
    res = re.findall(r"mul\((\d{1,4}),(\d{1,4})\)", parsed_input)
    return sum(int(i) * int(j) for i, j in res)


def part_2(parsed_input):
    res = re.findall(
        r"mul\((\d{1,4}),(\d{1,4})\)|(do)\(\)|(don't)\(\)", parsed_input
    )

    enabled = True
    sum = 0
    for inst in res:
        left, right, do, dont = inst

        if left and right and enabled:
            sum += int(left) * int(right)
            continue

        if do:
            enabled = True
            continue

        if dont:
            enabled = False
            continue

    return sum


if __name__ == "__main__":
    data = get_data(day=DAY, year=YEAR).strip()
    parsed = parse(data)
    print(f"Part 1: {part_1(parsed)}")
    print(f"Part 2: {part_2(parsed)}")
