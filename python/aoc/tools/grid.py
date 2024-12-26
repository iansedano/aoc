from collections import defaultdict

from aoc.tools.vector import Vec2
from aoc.tools.neighbors import CARDINALS, ORDINALS


class Grid2D:

    @classmethod
    def from_string(cls, input, ignore=None):
        ignore = set() if ignore is None else ignore
        cls.grid = {}
        for y, line in enumerate(input.splitlines()):
            for x, char in enumerate(line):
                if char not in ignore:
                    cls.grid[Vec2(x, y)] = char


def create_grid_dict_from_string(
    input, ignore=None, use_tuples=False, collect_chars=False
):
    ignore = set() if ignore is None else ignore
    grid = {}

    if collect_chars:
        chars = defaultdict(set)

    for y, line in enumerate(input.splitlines()):
        for x, char in enumerate(line):
            if char not in ignore:
                if use_tuples:
                    grid[(x, y)] = char
                    if collect_chars:
                        chars[char].add((x, y))
                else:
                    grid[Vec2(x, y)] = char
                    if collect_chars:
                        chars[char].add(Vec2(x, y))

    return grid if not collect_chars else grid, chars


def print_points(points, x_range, y_range):
    if not isinstance(points, set):
        points = set(points)
    for y in range(*y_range):
        for x in range(*x_range):
            if (x, y) in points:
                print("#", end="")
            else:
                print(".", end="")
        print("")


def get_cardinals(pos):
    return [(pos[0] + t[0], pos[1] + t[1]) for t in CARDINALS]


def get_cardinals_with_directions(pos):
    return [((pos[0] + t[0], pos[1] + t[1]), t) for t in CARDINALS]


def get_ordinals(pos):
    return [(pos[0] + t[0], pos[1] + t[1]) for t in ORDINALS]


def get_ordinals_with_directions(pos):
    return [((pos[0] + t[0], pos[1] + t[1]), t) for t in ORDINALS]
