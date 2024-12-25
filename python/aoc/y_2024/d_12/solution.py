import itertools
from collections import defaultdict, deque
from collections.abc import Iterable
from textwrap import dedent

import peek
from aocd import get_data


def parse(puzzle_input):
    grid = {}
    lines = puzzle_input.splitlines()
    shape = (len(lines[0]), len(lines))
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, char in enumerate(line):
            grid[x, y] = char

    regions = []

    for point, char in grid.items():
        if any(point in region[1] for region in regions):
            continue

        new_region = (char, {point})
        points_to_examine = deque([point])

        while points_to_examine:
            current = points_to_examine.popleft()
            for cardinal in get_cardinals(current, shape):
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
        cardinal not in points
        for p in points
        for cardinal in get_cardinals_s(p)
    )


def build_perimeter(points):
    return {
        (cardinal, dir)
        for p in points
        for cardinal, dir in get_cardinals_d(p)
        if cardinal not in points
    }


def get_region_price_discounted(points: Iterable):
    # peek(points)
    perimeter = build_perimeter(points)
    peek(perimeter)
    print_points({p[0] for p in perimeter}, (-1, 6), (-1, 6))

    corners = 0
    queue = set(perimeter)
    point, dir = queue.pop()

    while queue:
        peek(point, dir)

        possible_corners, straight = None, None

        if dir == "S" or dir == "N":

            possible_corners = [
                ((x + point[0], y + point[1]), dir)
                for x, y, dir in [
                    *itertools.product((1, -1), (1, -1), ("E", "W")),
                    (0, 0, "E"),
                    (0, 0, "W"),
                ]
            ]

            straight = [
                ((x + point[0], y + point[1]), dir)
                for x, y, dir in itertools.product((1, -1), (0,), (dir,))
            ]

        if dir == "W" or dir == "E":

            possible_corners = [
                ((x + point[0], y + point[1]), dir)
                for x, y, dir in [
                    *itertools.product((1, -1), (1, -1), ("N", "S")),
                    (0, 0, "N"),
                    (0, 0, "S"),
                ]
            ]

            straight = [
                ((x + point[0], y + point[1]), dir)
                for x, y, dir in itertools.product((0,), (1, -1), (dir,))
            ]

        # peek(possible_corners, straight)

        found = False

        for pc in possible_corners:

            if pc in queue:
                # print(pc, "in queue")
                corners += 1
                point, dir = pc
                queue.remove(pc)
                found = True
                break

        if found:
            continue

        for s in straight:
            if s in queue:
                # print(s, "in queue")
                point, dir = s
                queue.remove(s)
                found = True
                break

        if found:
            continue

        print("something went wrong")
        raise SystemExit
    peek(corners, len(points))
    corners = 4 if corners == 3 else corners
    return corners * len(points)


def group_contiguous(nums):
    positions = list(sorted(nums))

    idx = 0

    groups = [[positions[idx]]]

    idx = 1
    group_idx = 0

    while True:
        try:
            positions[idx]
        except IndexError:
            break

        if positions[idx - 1] + 1 == positions[idx]:
            groups[group_idx].append(positions[idx])
            idx += 1
        else:
            groups.append([positions[idx]])
            group_idx += 1
            idx += 1

    return groups


def get_cardinals(pos, shape, exclude=None):
    if exclude is None:
        exclude = {}
    transforms = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    out = []

    for t in transforms:
        new_pos = (pos[0] + t[0], pos[1] + t[1])
        if (
            0 <= new_pos[0] < shape[0]
            and 0 <= new_pos[1] < shape[1]
            and new_pos not in exclude
        ):
            out.append(new_pos)
    return out


def get_cardinals_s(pos):
    return [
        (pos[0] + t[0], pos[1] + t[1])
        for t in [(0, -1), (1, 0), (0, 1), (-1, 0)]
    ]


def get_cardinals_d(pos):
    return [
        ((pos[0] + t[0][0], pos[1] + t[0][1]), t[1])
        for t in [((0, -1), "N"), ((1, 0), "E"), ((0, 1), "S"), ((-1, 0), "W")]
    ]


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


if __name__ == "__main__":
    package_parts = __package__.split(".")
    year, day = package_parts[-2].strip("y_"), package_parts[-1].strip("d_")
    data = get_data(day=day, year=year).strip()
    parsed = parse(data)
    print(f"Part 1: {part_1(parsed)}")
    print(f"Part 2: {part_2(parsed)}")
