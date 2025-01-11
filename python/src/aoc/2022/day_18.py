import functools
import sys

from aoc_tools.vector import Vec3 as v
from aocd import get_data

DAY = 18
SAMPLE = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5"""


def parse(puzzle_input: str):
    """Parse input."""
    return {
        v(*(int(n) for n in line.split(",")))
        for line in puzzle_input.splitlines()
    }


def part1(data):
    """Solve part 1."""

    free = 0
    for point in data:
        adjacents = get_adjacent_coords(point)
        free += sum(a not in data for a in adjacents)

    return free


def part2(data):
    """Solve part 2."""
    minims = v(*[min(item[dim] - 1 for item in data) for dim in [0, 1, 2]])
    maxims = v(*[max(item[dim] + 1 for item in data) for dim in [0, 1, 2]])

    if minims in data:
        print("item in corner")
        return

    visited = set()
    get_empties = functools.partial(
        get_adjacent_coords, min=minims, max=maxims, visited=visited
    )

    next_points_to_check = tuple(get_empties(minims))

    showing_faces = 0

    while next_points_to_check:
        new_next_points = []

        for point in next_points_to_check:
            if point not in data and point not in visited:
                visited.add(point)
                new_next_points.extend(get_empties(point))
            elif point in data:
                showing_faces += 1

        next_points_to_check = tuple(new_next_points)

    return showing_faces


def get_adjacent_coords(p: v, min=None, max=None, visited=None):
    adjacents = [
        v(p.x - 1, p.y, p.z),
        v(p.x + 1, p.y, p.z),
        v(p.x, p.y - 1, p.z),
        v(p.x, p.y + 1, p.z),
        v(p.x, p.y, p.z - 1),
        v(p.x, p.y, p.z + 1),
    ]
    if min:
        adjacents = filter(
            lambda p: p.x >= min.x and p.y >= min.y and p.z >= min.z, adjacents
        )
    if max:
        adjacents = filter(
            lambda p: p.x <= max.x and p.y <= max.y and p.z <= max.z, adjacents
        )
    if visited:
        adjacents = filter(lambda p: p not in visited, adjacents)

    return adjacents


def main(main=True):
    if main:
        print("MAIN")
        data = parse(get_data(day=DAY, year=2022).strip())
    else:
        print("SAMPLE")
        data = parse(SAMPLE.strip())

    solution1 = part1(data)
    solution2 = part2(data)

    print(f"\t{solution1 = }\n\t{solution2 = }")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        main(False)
        main(True)
    elif sys.argv[1] == "sample":
        main(False)
    elif sys.argv[1] == "main":
        main(True)
