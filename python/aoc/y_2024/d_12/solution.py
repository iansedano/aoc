from collections import deque
from collections.abc import Iterable

from aoc.tools.grid import get_cardinals, get_edges
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
    return sum(get_region_price_discounted(field) for _, field in parsed_input)


def get_region_price(points: Iterable):
    return len(points) * sum(
        cardinal not in points for p in points for cardinal in get_cardinals(p)
    )


def get_region_price_discounted(points: Iterable):
    return count_corners(points) * len(points)


def count_corners(points):
    edges = list(get_edges(points))
    queue = set(edges)
    current = next(iter(queue))
    corner_count = 0
    direction = "W" if current[1] == "N" else "N"

    # point, edge, new direction
    possible_corners = {
        "N": (((0, 0), "N", "E"), ((-1, 0), "N", "W")),
        "S": (((0, 1), "N", "E"), ((-1, 1), "N", "W")),
        "E": (((1, 0), "W", "S"), ((1, -1), "W", "N")),
        "W": (((0, 0), "W", "S"), ((0, -1), "W", "N")),
    }

    possible_straight = {
        "N": ((0, -1), "W"),
        "S": ((0, 1), "W"),
        "E": ((1, 0), "N"),
        "W": ((-1, 0), "N"),
    }

    while queue:
        next_possible_corners = possible_corners[direction]

        found_corner = False
        for point, edge, new_direction in next_possible_corners:
            new_edge = (add_tuple(point, current[0]), edge)
            if new_edge in queue:
                corner_count = corner_count + 1
                current = new_edge
                queue.remove(new_edge)
                direction = new_direction
                found_corner = True
                break

        if found_corner:
            continue

        next_straight = possible_straight[direction]
        if (
            ns := (add_tuple(next_straight[0], current[0]), next_straight[1])
        ) in queue:
            current = ns
            queue.remove(ns)
            continue

        queue.discard(current)
        if queue:
            current = next(iter(queue))
            direction = "W" if current[1] == "N" else "N"

    return corner_count


if __name__ == "__main__":
    package_parts = __package__.split(".")
    year, day = int(package_parts[-2].strip("y_")), int(
        package_parts[-1].strip("d_")
    )
    data = get_data(day=day, year=year).strip()
    parsed = parse(data)
    print(f"Part 1: {part_1(parsed)}")
    print(f"Part 2: {part_2(parsed)}")
