from collections import defaultdict
from textwrap import dedent

from aocd import get_data

DAY = 10
YEAR = 2024
SAMPLE = dedent(
    """\
    89010123
    78121874
    87430965
    96549874
    45678903
    32019012
    01329801
    10456732
    """
)


def parse(puzzle_input):
    lines = puzzle_input.splitlines()
    shape = (len(lines), len(lines[0]))
    map = defaultdict(set)

    for y, line in enumerate(puzzle_input.splitlines()):
        for x, char in enumerate(line):
            map[int(char)].add((x, y))

    return map, shape


def part_1(parsed_input):
    map, shape = parsed_input
    trailheads = map[0]
    return sum(len(get_trails(pos, map, shape)) for pos in trailheads)


def part_2(parsed_input):
    map, shape = parsed_input
    trailheads = map[0]
    return sum(get_rating(pos, map, shape) for pos in trailheads)


def get_trails(pos, map, shape, current_height=0, path=None):
    if current_height == 9:
        return {pos}

    if path is None:
        path = set()

    trails = set()
    for cardinal in get_cardinals(pos, shape, path):
        if cardinal in map[current_height + 1]:
            trails = trails.union(
                get_trails(
                    cardinal, map, shape, current_height + 1, path | {pos}
                )
            )

    return trails


def get_rating(pos, map, shape, current_height=0, path=None):
    if current_height == 9:
        return 1

    if path is None:
        path = set()

    trails = 0
    for cardinal in get_cardinals(pos, shape, path):
        if cardinal in map[current_height + 1]:
            trails += get_rating(
                cardinal, map, shape, current_height + 1, path | {pos}
            )

    return trails


def get_cardinals(pos, shape, path):
    transforms = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    out = []

    for t in transforms:
        new_pos = (pos[0] + t[0], pos[1] + t[1])
        if (
            0 <= new_pos[0] < shape[0]
            and 0 <= new_pos[1] < shape[1]
            and new_pos not in path
        ):
            out.append(new_pos)
    return out


if __name__ == "__main__":
    data = get_data(day=DAY, year=YEAR).strip()
    parsed = parse(data)
    print(f"Part 1: {part_1(parsed)}")
    print(f"Part 2: {part_2(parsed)}")
