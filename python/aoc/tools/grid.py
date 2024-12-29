from collections import defaultdict
from typing import Iterable, Union

from aoc.tools.neighbors import CARDINALS, EAST, NORTH, ORDINALS, SOUTH, WEST
from aoc.tools.vector import Vec2, add_tuple


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


def print_points(
    points: Union[Iterable, tuple],
    *,
    x_range: Union[tuple, int] = None,
    y_range: Union[tuple, int] = None,
    auto_detect=False,
    show_count=False,
):
    if auto_detect and (x_range is not None or y_range is not None):
        raise ValueError(
            "auto_detect and x_range/y_range are mutually exclusive"
        )

    if auto_detect:
        x_range = (min(p[0] for p in points), max(p[0] for p in points) + 1)
        y_range = (min(p[1] for p in points), max(p[1] for p in points) + 1)

    if isinstance(x_range, int):
        x_range = (0, x_range)
    if isinstance(y_range, int):
        y_range = (0, y_range)

    if not isinstance(x_range, tuple) or len(x_range) != 2:
        raise ValueError("Invalid x_range")
    if not isinstance(y_range, tuple) or len(y_range) != 2:
        raise ValueError("Invalid y_range")

    if x_range[0] > x_range[1] or y_range[0] > y_range[1]:
        raise ValueError("Invalid range")

    if isinstance(points, tuple):
        points = [points]

    if not show_count:
        points = set(points)
        for y in range(*y_range):
            for x in range(*x_range):
                if (x, y) in points:
                    print("#", end="")
                else:
                    print(".", end="")
            print("")
    if show_count:
        points = {}
        for p in points:
            points[p] = points.get(p, 0) + 1

        for y in range(*y_range):
            for x in range(*x_range):
                value = points.get((x, y), 0)
                if value > 9:
                    print("+", end="")
                elif value < 0:
                    print("-", end="")
                elif value == 0:
                    print(".", end="")
                else:
                    print(value, end="")
            print("")


def get_cardinals(
    pos, limit_x: Union[int, tuple] = None, limit_y: Union[tuple | int] = None
):
    """limit args can be either a tuple or an int. If an int is passed, it will be converted to a tuple (0, int)
    If None is passed, it will be converted to (-inf, inf)
    limits act like ranges where the first element is inclusive and the second is exclusive
    """
    if limit_x is None:
        limit_x = (float("-inf"), float("inf"))
    if limit_y is None:
        limit_y = (float("-inf"), float("inf"))

    if isinstance(limit_x, int):
        limit_x = (0, limit_x)
    if isinstance(limit_y, int):
        limit_y = (0, limit_y)

    if not isinstance(limit_x, tuple) or len(limit_x) != 2:
        raise ValueError("Invalid limit_x")
    if not isinstance(limit_y, tuple) or len(limit_y) != 2:
        raise ValueError("Invalid limit_y")

    return [
        (pos[0] + t[0], pos[1] + t[1])
        for t in CARDINALS
        if limit_x[0] <= pos[0] + t[0] < limit_x[1]
        and limit_y[0] <= pos[1] + t[1] < limit_y[1]
    ]


def get_edges(points):
    for point in points:
        north = add_tuple(point, NORTH)
        south = add_tuple(point, SOUTH)
        east = add_tuple(point, EAST)
        west = add_tuple(point, WEST)

        if north not in points:
            yield point, "N"
        if south not in points:
            yield south, "N"
        if east not in points:
            yield east, "W"
        if west not in points:
            yield point, "W"


def get_cardinals_with_directions(pos):
    return [((pos[0] + t[0], pos[1] + t[1]), t) for t in CARDINALS]


def get_ordinals(pos):
    return [(pos[0] + t[0], pos[1] + t[1]) for t in ORDINALS]


def get_ordinals_with_directions(pos):
    return [((pos[0] + t[0], pos[1] + t[1]), t) for t in ORDINALS]
