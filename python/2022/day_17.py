import copy
import functools
import itertools
import time
from pprint import pp

from aoc_tools.seq import find_pattern

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
    print(f"Sample {solution1 = }")
    assert solution1 == 3068
    solution2 = part2(data)
    print(f"Sample {solution2 = }")
    assert solution2 == 1514285714288

    puzzle_input = get_data(day=17, year=2022).strip()
    data = parse(puzzle_input)
    solution1 = part1(data)
    print(solution1)
    solution2 = part2(data)
    print()
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
        self.h_log = []
        self.dh_log = []
        self.seq_len_checked = 0

    def input(self, current_h):
        if self.h_log:
            self.dh_log.append(current_h - self.h_log[-1])
        self.h_log.append(current_h)

        seq_len = find_pattern(
            self.dh_log,
            pattern_min=max(20, len(self.dh_log) // 2),
            early_exit=True,
        )

        if seq_len != -1:
            h_diff = self.h_log[seq_len] - self.h_log[0]
            return self.calculate_cycle(seq_len, h_diff)

        return False

    def calculate_cycle(self, seq_len, h_diff):
        start_h = self.h_log[0]
        rocks_left = self.total_rocks - self.starting_rock_number
        full_cycles_left = rocks_left // seq_len
        height_sum = full_cycles_left * h_diff
        if rocks_left_over := rocks_left % seq_len:

            left_over_height = self.h_log[rocks_left_over] - start_h
        else:
            left_over_height = 0

        return -(start_h + height_sum + left_over_height + 1)


def sim(
    cave_width, rocks: itertools.cycle, jets: itertools.cycle, number_of_rocks
):
    cave = set()
    h_map = (0,) * cave_width
    rocks_before_starting_seq = 2000

    for rock_number in range(number_of_rocks):
        rock_shape = next(rocks)
        rock = instantiate_rock(rock_shape, min(h_map))
        rock = push_rock(rock, next(jets) == "<", cave_width, cave)

        # while not at rest
        while not any((x, y + 1) in cave or y == 0 for x, y in rock):
            rock = tuple((x, y + 1) for x, y in rock)
            rock = push_rock(rock, next(jets) == "<", cave_width, cave)

        for point in rock:
            cave.add(point)
            new_highest_points = list(h_map)
            if point[1] <= new_highest_points[point[0]]:
                new_highest_points[point[0]] = point[1] - 1
                h_map = tuple(new_highest_points)

        if rock_number == rocks_before_starting_seq:
            cycle_detector = CycleDetector(rock_number, number_of_rocks)

        if rock_number >= rocks_before_starting_seq:
            h = min(h_map)
            if result := cycle_detector.input(h):
                return result

    return -min(h_map)


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
