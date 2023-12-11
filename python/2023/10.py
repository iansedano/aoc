import re
from collections import defaultdict

from common import main

DAY = 10
YEAR = 2023
SAMPLE = """\
.....
.S-7.
.|.|.
.L-J.
....."""


def parse(puzzle_input):
    lines = puzzle_input.splitlines()

    start = tuple()
    grid = defaultdict(lambda: ".")
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "S":
                start = (x, y)
            grid[(x, y)] = char

    return build_loop(start, grid), grid


def part1(parsed_input):
    loop, _ = parsed_input
    return len(loop) / 2


def part2(parsed_input):
    loop, grid = parsed_input
    new_grid = defaultdict(lambda: ".")
    min_x, min_y, max_x, max_y = 0, 0, 0, 0
    for k, v in grid.items():
        if k in loop:
            new_grid[k] = v
            min_x = min(k[0], min_x)
            min_y = min(k[1], min_y)
            max_x = max(k[0], max_x)
            max_y = max(k[1], max_y)

    new_grid[(72, 30)] = "L"  # Replacing "S" manually

    rows = []
    for y in range(min_y, max_y + 1):
        new_row = []
        for x in range(min_x, max_x + 1):
            new_row.append(new_grid[(x, y)])
        rows.append(new_row)

    rows = ["".join(r) for r in rows]

    area = 0
    for r in rows:
        r = re.sub(r"F-*J", "|", r)
        r = re.sub(r"L-*7", "|", r)
        r = re.sub(r"F-*7", "", r)
        r = re.sub(r"L-*J", "", r)

        inside = False
        for char in r:
            if char == "|":
                inside = not inside
                continue
            if char == "." and inside:
                area += 1

    return area


def build_loop(start, grid):
    loop = [start]
    while True:
        cardinals = get_cardinals(*loop[-1])
        for cardinal in cardinals:
            if connected(loop[-1], cardinal, grid) and cardinal not in loop[1:]:
                if cardinal == loop[0]:
                    return loop
                loop.append(cardinal)
                break


def connected(pos_a, pos_b, grid):
    """
    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    . is ground; there is no pipe in this tile.
    S is the starting position
    """

    connect = {"n": "SLJ|", "e": "S-LF", "s": "S|7F", "w": "S-J7"}

    if pos_a == (pos_b[0], pos_b[1] + 1):
        # b north of a
        return grid[pos_b] in connect["s"] and grid[pos_a] in connect["n"]
    if pos_a == (pos_b[0] - 1, pos_b[1]):
        # b east of a
        return grid[pos_b] in connect["w"] and grid[pos_a] in connect["e"]
    if pos_a == (pos_b[0], pos_b[1] - 1):
        # b south of a
        return grid[pos_b] in connect["n"] and grid[pos_a] in connect["s"]
    if pos_a == (pos_b[0] + 1, pos_b[1]):
        # b west of a
        return grid[pos_b] in connect["e"] and grid[pos_a] in connect["w"]


def get_cardinals(x, y):
    return [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]


if __name__ == "__main__":
    main(DAY, YEAR, SAMPLE, parse, part1, part2)
