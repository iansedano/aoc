import math
import re
from collections import defaultdict
from textwrap import dedent

import peek
from aocd import get_data

DAY = 1
YEAR = 2024
SAMPLE = dedent(
    """\
    p=0,4 v=3,-3
    p=6,3 v=-1,-3
    p=10,3 v=-1,2
    p=2,0 v=2,-1
    p=0,0 v=1,3
    p=3,0 v=-2,-2
    p=7,6 v=-1,-3
    p=3,0 v=-1,-2
    p=9,3 v=2,3
    p=7,3 v=-1,2
    p=2,4 v=2,-3
    p=9,5 v=-3,-3
    """
)


def parse(puzzle_input):
    return [
        tuple(int(d) for d in re.findall(r"-*\d+", line))
        for line in puzzle_input.splitlines()
    ]


def part_1(parsed_input):
    robots = parsed_input
    width, height = 101, 103
    # width, height = 11, 7

    for _ in range(100):
        new_robots = []
        for robot in robots:
            x, y, dx, dy = robot
            new_x, new_y = (x + dx) % (width), (y + dy) % (height)
            new_robots.append((new_x, new_y, dx, dy))
        robots = new_robots

    lower_mid_x = width // 2
    higher_mid_x = math.ceil(width / 2)
    lower_mid_y = height // 2
    higher_mid_y = math.ceil(height / 2)

    quadrants = (
        (range(0, lower_mid_x), range(0, lower_mid_y)),
        (range(higher_mid_x, width), range(0, lower_mid_y)),
        (range(0, lower_mid_x), range(higher_mid_y, height)),
        (range(higher_mid_x, width), range(higher_mid_y, height)),
    )

    totals = [0, 0, 0, 0]

    for robot in robots:
        for i, quadrant in enumerate(quadrants):
            if robot[0] in quadrant[0] and robot[1] in quadrant[1]:
                totals[i] += 1
                break

    return math.prod(t for t in totals if t != 0)


def debug(robots, width, height):
    result = defaultdict(int)

    for robot in robots:
        result[robot[:2]] += 1

    for y in range(height):
        print("")
        for x in range(width):
            if result[(x, y)] > 0:
                print(result[(x, y)], end="")
            else:
                print(".", end="")


def part_2(parsed_input):
    robots = parsed_input
    width, height = 101, 103

    da = 35
    db = 68
    next = 33
    a = True
    a_inc = -2
    b_inc = 2

    for i in range(8000):
        if i == next:
            next = next + da if a else next + db
            da = da + a_inc if a else da
            db = db + b_inc if not a else db
            a = not a

        if i == 1887:
            a = not a
            next = 1987
            da = 3
            db = 98
            a_inc = 2
            b_inc = -2

        new_robots = []
        for robot in robots:
            x, y, dx, dy = robot
            new_x, new_y = (x + dx) % (width), (y + dy) % (height)
            new_robots.append((new_x, new_y, dx, dy))
        robots = new_robots

    return 0


if __name__ == "__main__":
    data = get_data(day=DAY, year=YEAR).strip()
    parsed = parse(data)
    print(f"Part 1: {part_1(parsed)}")
    print(f"Part 2: {part_2(parsed)}")
