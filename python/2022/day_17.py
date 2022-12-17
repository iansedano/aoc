import copy
import itertools
import time
from pprint import pp

from aocd import get_data
from rich.console import Console
from rich.live import Live

console = Console()

SAMPLE = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

ROCKS = [
    ((0, 0), (1, 0), (2, 0), (3, 0)),
    ((1, 0), (0, -1), (1, -1), (2, -1), (1, -2)),
    ((0, 0), (1, 0), (2, 0), (2, -1), (2, -2)),
    ((0, 0), (0, -1), (0, -2), (0, -3)),
    ((0, 0), (1, 0), (0, -1), (1, -1)),
]


def main():
    puzzle_input = get_data(day=17, year=2022).strip()
    puzzle_input = SAMPLE
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


def parse(puzzle_input: str):
    """Parse input."""
    return list(puzzle_input)


def part1(data):
    """Solve part 1."""

    cave = sim(
        cave_width=7,
        rocks=itertools.cycle(ROCKS),
        jets=itertools.cycle(data),
        number_of_rocks=2022,
    )

    return min(cave)


def part2(data):
    """Solve part 2."""
    cave = sim(
        cave_width=7,
        rocks=itertools.cycle(ROCKS),
        jets=itertools.cycle(data),
        number_of_rocks=1_000_000_000_000,
    )

    return min(cave)


def instantiate_rock(rock, highest_point=0, left_pad=2, bottom_pad=3):
    return tuple(
        (x + left_pad, y - bottom_pad + highest_point) for x, y in rock
    )


def push_rock(rock, left, max_width, cave):

    rock_max_left = min(point[0] for point in rock)
    rock_max_right = max(point[0] for point in rock)

    if left:
        potential_new_position = tuple((x - 1, y) for x, y in rock)
        if (
            any(point in cave for point in potential_new_position)
            or rock_max_left == 0
        ):
            return rock
        else:
            return potential_new_position

    else:
        potential_new_position = tuple((x + 1, y) for x, y in rock)
        if (
            any(point in cave for point in potential_new_position)
            or rock_max_right >= max_width - 1
        ):
            return rock
        else:
            return potential_new_position


def sim(
    cave_width, rocks: itertools.cycle, jets: itertools.cycle, number_of_rocks
):
    """
    Each rock appears so that its left edge is two units away from the left
    wall and its bottom edge is three units above the highest rock in the room
    (or the floor, if there isn't one).
    """

    cave = set()
    highest_points = [0] * cave_width
    highest_point_log = []
    now = time.perf_counter()
    for _ in range(number_of_rocks):
        if _ % 10_000 == 0:
            now_ = time.perf_counter()
            print(_, end="  ")
            print(now_ - now)
            now = now_

        # print("\n\n============NEW ROCK============\n\n")
        rock = instantiate_rock(next(rocks), min(highest_points))
        # viz(cave, rock)
        rock = push_rock(rock, next(jets) == "<", cave_width, cave)
        # viz(cave, rock)
        at_rest = False

        while not at_rest:
            rock = tuple((x, y + 1) for x, y in rock)
            # viz(cave, rock)
            rock = push_rock(rock, next(jets) == "<", cave_width, cave)

            # viz(cave, rock)

            if any((x, y + 1) in cave or y == 0 for x, y in rock):
                at_rest = True

            if at_rest:
                # print("ROCK AT REST")
                # viz(cave, rock)
                for point in rock:
                    cave.add(point)
                for point in rock:
                    if point[1] <= highest_points[point[0]]:
                        highest_points[point[0]] = point[1] - 1

                highest_point_fingerprint = tuple(
                    height - max(highest_points) for height in highest_points
                )

                if highest_point_fingerprint not in highest_point_log:
                    # print(tuple(highest_point_fingerprint))
                    highest_point_log.append(tuple(highest_point_fingerprint))
                else:
                    print("FOUND")
                    print(_)
                    print(min(highest_points))
                    print(highest_point_log.index(highest_point_fingerprint))
                    print(highest_point_fingerprint)
                    highest_point_log = [highest_point_fingerprint]

                continue

    return highest_points


def map_floor(cave, highest_point):

    print(f"{highest_point = }")

    starting_y = min(
        y for y in range(0, highest_point - 1, -1) if (0, y) in cave
    )

    point = (0, starting_y)
    floor = [point]
    while True:
        surrounding_squares = get_squares_around(point)
        for sq in surrounding_squares:
            if sq in cave and sq not in floor:
                floor.append(sq)
                point = sq
                break

        else:
            break

    return floor


def get_squares_around(point):
    # N NE E SE S SW W NW
    return [
        (point[0] - 1, point[1] - 1),  # NW
        (point[0], point[1] - 1),  # N
        (point[0] + 1, point[1] - 1),  # NE
        (point[0] + 1, point[1]),  # E
        (point[0] - 1, point[1]),  # W
        (point[0] - 1, point[1] + 1),  # SW
        (point[0], point[1] + 1),  # S
        (point[0] + 1, point[1] + 1),  # SE
    ]


def viz(cave, rock):

    cave = copy.deepcopy(cave)
    for point in rock:
        cave.add(point)

    min_x = 0
    min_y = min(key[1] for key in cave) - 2
    max_x = max(key[0] for key in cave) + 1
    max_y = 1

    out = []

    for y in range(min_y, max_y):
        for x in range(min_x, max_x):
            if (x, y) in cave:
                out.append("[#5A4D41 on #74663B]#[/]")
            else:
                out.append(".")
        out.append("\n")

    console.print("".join(out))
    return "".join(out)


if __name__ == "__main__":
    solution1, solution2 = main()
    print(f"{solution1 = }\n{solution2 = }")
