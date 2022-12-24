import copy
import functools
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
    solution2 = part2(data)
    print(solution2)
    print("SHOULD BE 1514285714288\n")

    puzzle_input = get_data(day=17, year=2022).strip()
    data = parse(puzzle_input)
    solution1 = part1(data)
    print(solution1)
    print("SHOULD BE 3065\n")
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


def find_repeating_pattern(seq, start_from=0, pattern_min=2, early_exit=False):
    """
    >>> find_repeating_pattern([1,2,1,2,1,2,1,2,1,2])
    2
    >>> find_repeating_pattern([1,2,3,1,2,3,1,2,3])
    3
    >>> find_repeating_pattern([1,2,3,4,5,1,2,3,4,5,1,2,3,4,5])
    5
    """
    seq = tuple(seq[start_from:])
    pattern_length = -1
    max_len = len(seq) // 2
    for window_size in range(max_len, pattern_min - 1, -1):

        chunks = [
            seq[idx : idx + window_size]
            for idx in range(0, len(seq), window_size)
            if idx + window_size < len(seq) + 1
        ]

        if all(a == b for a, b in itertools.combinations(chunks, 2)):
            if early_exit:
                return window_size
            pattern_length = window_size

    return pattern_length


class CycleDetector:
    def __init__(self, rock_number, total_rocks):
        self.starting_rock_number = rock_number
        self.total_rocks = total_rocks
        self.h_log = []
        self.dh_log = []
        self.seq_len = -1

    def input(self, rock_number, current_h):
        if self.h_log:
            self.dh_log.append(current_h - self.h_log[-1])

        self.h_log.append(current_h)

        seq_len = find_repeating_pattern(
            self.dh_log, pattern_min=100, early_exit=True
        )

        if seq_len != -1:

            # print(seq_len)
            # print(f"{rock_number - self.starting_rock_number = }")
            h_diff = self.h_log[seq_len] - self.h_log[0]
            # print(f"{h_diff = }")
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

        return -(start_h + height_sum + left_over_height)


def sim(
    cave_width, rocks: itertools.cycle, jets: itertools.cycle, number_of_rocks
):
    cave = set()
    h_map = (0,) * cave_width
    rocks_before_starting_seq = 1000

    for rock_number in range(number_of_rocks):
        if rock_number % 1_000 == 0:
            print(f"{rock_number = }")

        rock_shape = next(rocks)
        rock = instantiate_rock(rock_shape, min(h_map))
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

                    new_highest_points = list(h_map)
                    if point[1] <= new_highest_points[point[0]]:
                        new_highest_points[point[0]] = point[1] - 1
                        h_map = tuple(new_highest_points)

                if rock_number == rocks_before_starting_seq:
                    cycle_detector = CycleDetector(rock_number, number_of_rocks)

                if rock_number >= rocks_before_starting_seq:
                    h = min(h_map)
                    if result := cycle_detector.input(rock_number, h):

                        print(f"{result = }")
                        return result

                        cycle_detector.starting_rock_number
                        cycle_detector.h_log[0]

                        cycle_detector = CycleDetector(
                            rock_number, number_of_rocks
                        )
                        cycle_detector.input(rock_number, h)

                        continue

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
