from vent_input import parse_vent_data

from debug import p
from pprint import pp

Point = tuple[int, int]
Line = tuple[Point, Point]
Grid = list[list[int]]


def filter_diagonal_lines(lines: list[Line]) -> list[Line]:

    return list(
        filter(
            lambda line: True
            if line[0][0] == line[1][0] or line[0][1] == line[1][1]
            else False,
            lines,
        )
    )


def generate_grid(w, h):
    """Generates grid of `0` or width w and height h"""
    return [[0 for _y in range(w)] for _x in range(h)]


def generate_points_along_line(line):
    """Return a list of every point along a line
    Only works for:
    - horizontal lines
    - vertical lines
    - 45 degree lines"""

    output: set[Point] = set()

    point_1: Point = line[0]
    point_2: Point = line[1]

    # runtime check for diagonal lines
    if point_1[0] != point_2[0] and point_1[1] != point_2[1]:
        raise Exception("diagonal line encountered!")

    output.add(point_1)
    output.add(point_2)

    # if vertical
    if point_1[0] == point_2[0]:
        distance = point_2[1] - point_1[1]
        direction = start = 1 if distance >= 0 else -1

        for i in range(start, distance, direction):
            point_to_add = (point_1[0], point_1[1] + i)
            output.add(point_to_add)

    # elif horizontal
    elif point_1[1] == point_2[1]:
        distance = point_2[0] - point_1[0]
        direction = start = 1 if distance >= 0 else -1

        for i in range(start, distance, direction):
            point_to_add = (point_1[0] + i, point_1[1])
            output.add(point_to_add)

    return list(output)


def generate_points_along_line2(line):
    """Return a list of every point along a line
    Only works for:
    - horizontal lines
    - vertical lines
    - 45 degree lines
    """
    output: set[Point] = set()

    point_1: Point = line[0]
    point_2: Point = line[1]

    output.add(point_1)
    output.add(point_2)

    distance = (point_2[0] - point_1[0], point_2[1] - point_1[1])

    x_distance = distance[0]
    y_distance = distance[1]

    # Runtime check for perfect diagonality if not vertical or horizontal
    if x_distance != 0 and y_distance != 0:
        assert abs(x_distance) == abs(y_distance)

    x_direction = x_start = 1 if x_distance >= 0 else -1
    y_direction = y_start = 1 if y_distance >= 0 else -1

    x_gen = (i for i in range(x_start, x_distance, x_direction))
    y_gen = (i for i in range(y_start, y_distance, y_direction))

    current_x = next(x_gen, None)
    current_y = next(y_gen, None)

    # Really only need to check one of these if perfectly diagonal
    while current_x is not None or current_y is not None:
        current_x = 0 if current_x is None else current_x
        current_y = 0 if current_y is None else current_y

        point_to_add = (point_1[0] + current_x, point_1[1] + current_y)
        output.add(point_to_add)
        current_x = next(x_gen, None)
        current_y = next(y_gen, None)

    return list(output)


def get_overlapping_points(lines: list[Line], grid: Grid) -> list[Point]:
    modified_grid = list(grid)

    line: Line
    for line in lines:
        for point in generate_points_along_line2(line):
            modified_grid[point[0]][point[1]] += 1

    overlapping_points = []
    for row in modified_grid:
        for position in row:
            if position > 1:
                overlapping_points.append(position)

    return overlapping_points
