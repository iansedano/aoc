import itertools
from collections import deque
from collections.abc import Iterable

import peek
from aoc.tools.grid import get_cardinals, get_edges, print_points
from aoc.tools.vector import add_tuple
from aocd import get_data


def parse(puzzle_input):
    lines = puzzle_input.splitlines()
    shape = (len(lines[0]), len(lines))

    grid = {
        (x, y): char
        for y, line in enumerate(lines)
        for x, char in enumerate(line)
    }

    regions = []

    for point, char in grid.items():
        if any(point in region[1] for region in regions):
            continue

        new_region = (char, {point})
        points_to_examine = deque([point])

        while points_to_examine:
            current = points_to_examine.popleft()
            for cardinal in get_cardinals(current, *shape):
                if grid[cardinal] == char and cardinal not in new_region[1]:
                    new_region[1].add(cardinal)
                    points_to_examine.append(cardinal)

        regions.append(new_region)

    return regions


def part_1(parsed_input):
    return sum(get_region_price(field) for _, field in parsed_input)


def part_2(parsed_input):
    sum = 0
    for char, field in parsed_input:
        print("")
        print(f"====== {char} =======\n")
        result = get_region_price_discounted(field)
        peek(result)
        sum += result
    return sum
    # return sum(get_region_price_discounted(field) for _, field in parsed_input)


def get_region_price(points: Iterable):
    return len(points) * sum(
        cardinal not in points for p in points for cardinal in get_cardinals(p)
    )


def get_region_price_discounted(points: Iterable):
    edges = list(get_edges(points))

    possible_corners_n = ((1, -1), (1, 0), (0, -1), (0, 0))
    possible_straight_n = ((-1, 0), (1, 0))
    possible_corners_w = ((0, 0), (0, 1), (-1, 0), (-1, 1))
    possible_straight_w = ((0, -1), (0, 1))

    queue = set(edges)
    current = queue.pop()
    corners = 0

    while queue:
        possible_corners = (
            possible_corners_n if current[1] == "N" else possible_corners_w
        )
        corner_dir = "W" if current[1] == "N" else "N"

        corner = next(
            (
                pc
                for c in possible_corners
                if (pc := (add_tuple(c, current[0]), corner_dir)) in queue
            ),
            None,
        )
        if corner is not None:
            corners = corners + 1
            current = corner
            queue.remove(corner)
            continue

        possible_straight = (
            possible_straight_n if current[1] == "N" else possible_straight_w
        )
        straight_dir = "N" if current[1] == "N" else "W"

        straight = next(
            (
                ps
                for s in possible_straight
                if (ps := (add_tuple(s, current[0]), straight_dir)) in queue
            ),
            None,
        )

        if straight is not None:
            current = straight
            queue.remove(straight)
            continue

        current = queue.pop()

    return corners


def get_cardinals_d(pos):
    return [
        ((pos[0] + t[0][0], pos[1] + t[0][1]), t[1])
        for t in [((0, -1), "N"), ((1, 0), "E"), ((0, 1), "S"), ((-1, 0), "W")]
    ]


if __name__ == "__main__":
    package_parts = __package__.split(".")
    year, day = int(package_parts[-2].strip("y_")), int(
        package_parts[-1].strip("d_")
    )
    data = get_data(day=day, year=year).strip()
    parsed = parse(data)
    print(f"Part 1: {part_1(parsed)}")
    print(f"Part 2: {part_2(parsed)}")
