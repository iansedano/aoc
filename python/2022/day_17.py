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

    sample_puzzle_input = SAMPLE
    data = parse(sample_puzzle_input)
    print()
    solution1 = part1(data)
    print(solution1)
    # assert part1(data) == 3068
    print("SHOULD BE 3068\n")
    # solution2 = part2(data)
    # print(solution2)

    # # raise SystemExit()
    # print("SHOULD BE 1514285714288\n")

    puzzle_input = get_data(day=17, year=2022).strip()
    data = parse(puzzle_input)
    solution1 = part1(data)
    print(solution1)
    print("SHOULD BE 3065\n")
    # solution2 = part2(data)
    # print()
    return solution1, solution2


def parse(puzzle_input: str):
    """Parse input."""
    return list(puzzle_input)


def part1(data):
    """Solve part 1."""

    return sim(
        cave_width=7,
        rocks=itertools.cycle(ROCKS),
        jets=itertools.cycle(data),
        number_of_rocks=2022,
    )


def part2(data):
    """Solve part 2."""
    return sim(
        cave_width=7,
        rocks=itertools.cycle(ROCKS),
        jets=itertools.cycle(data),
        number_of_rocks=1_000_000_000_000,
    )


def instantiate_rock(rock, highest_point=0, left_pad=2, bottom_pad=3):
    """
    Each rock appears so that its left edge is two units away from the left
    wall and its bottom edge is three units above the highest rock in the room
    (or the floor, if there isn't one).
    """
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


class CycleDetector:
    def __init__(self, rock_number, total_rocks):
        self.starting_rock_number = rock_number
        self.total_rocks = total_rocks
        self.log = []
        self.max_height_log = []

    def input(self, rock_number, high_points, current_rock_shape):
        fingerprint = (
            tuple(h - max(high_points) for h in high_points)
            + current_rock_shape
        )
        current_height = min(high_points)

        if fingerprint in self.log:
            return self.calculate_cycle(
                fingerprint, rock_number, current_height
            )

        self.log.append(fingerprint)
        self.max_height_log.append(min(high_points))

        return False

    def calculate_cycle(self, fingerprint, rock_number, current_height):

        cycle_start = self.log.index(fingerprint)
        h_at_start_cycle = self.max_height_log[cycle_start]
        cycle_period = (rock_number - self.starting_rock_number) - cycle_start
        dh = current_height - h_at_start_cycle

        print(f"{dh = } {cycle_period = }")

        rocks_left = self.total_rocks - rock_number
        full_cycles_left = rocks_left // cycle_period
        height_sum = full_cycles_left * dh
        if rocks_left_over := rocks_left % cycle_period:

            left_over_height = (
                self.max_height_log[rocks_left_over + cycle_start]
                - h_at_start_cycle
            )
        else:
            left_over_height = 0

        return -(current_height + height_sum + left_over_height)


def sim(
    cave_width, rocks: itertools.cycle, jets: itertools.cycle, number_of_rocks
):
    cave = set()
    highest_points = (0,) * cave_width

    cycle_detector = CycleDetector(0, number_of_rocks)

    for rock_number in range(number_of_rocks):
        if rock_number % 10_000 == 0:
            print(f"{rock_number = }")

        rock_shape = next(rocks)
        rock = instantiate_rock(rock_shape, min(highest_points))
        rock = push_rock(rock, next(jets) == "<", cave_width, cave)

        at_rest = False
        while not at_rest:
            rock = tuple((x, y + 1) for x, y in rock)
            rock = push_rock(rock, next(jets) == "<", cave_width, cave)

            if any((x, y + 1) in cave or y == 0 for x, y in rock):
                at_rest = True

            if at_rest:
                for point in rock:
                    cave.add(point)

                    new_highest_points = list(highest_points)
                    if point[1] <= new_highest_points[point[0]]:
                        new_highest_points[point[0]] = point[1] - 1
                        highest_points = tuple(new_highest_points)

                if result := cycle_detector.input(
                    rock_number, highest_points, rock_shape
                ):

                    print(f"{result = }")

                    cycle_detector = CycleDetector(rock_number, number_of_rocks)
                    cycle_detector.input(
                        rock_number, highest_points, rock_shape
                    )

                continue

    return -min(highest_points)


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
