"""
Based on @gahjelle
"""

import itertools

import sympy
from common import main

DAY = 24
YEAR = 2023
SAMPLE = """\
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""


def parse(puzzle_input):
    return [parse_stone(line) for line in puzzle_input.splitlines()]


def parse_stone(line):
    return tuple(
        tuple(int(c) for c in part.split(", ")) for part in line.split(" @ ")
    )


def part1(parsed_input):
    # sample_min, sample_max = 7, 27
    # ranges = ((sample_min, sample_min), (sample_max, sample_max))
    real_min, real_max = 200000000000000, 400000000000000
    ranges = ((real_min, real_min), (real_max, real_max))

    return sum(
        in_range(ranges, intersect)
        for a, b in itertools.combinations(parsed_input, r=2)
        if a != b and (intersect := get_xy_intersect(a, b)) is not None
    )


def part2(parsed_input):
    """Based on @gahjelle"""
    x, y, z, dx, dy, dz, t1, t2, t3 = sympy.symbols(
        "x, y, z, dx, dy, dz, t1, t2, t3"
    )
    (x1, y1, z1), (dx1, dy1, dz1) = parsed_input[0]
    (x2, y2, z2), (dx2, dy2, dz2) = parsed_input[1]
    (x3, y3, z3), (dx3, dy3, dz3) = parsed_input[2]

    equations = [
        t1 * (dx1 - dx) - x + x1,
        t1 * (dy1 - dy) - y + y1,
        t1 * (dz1 - dz) - z + z1,
        t2 * (dx2 - dx) - x + x2,
        t2 * (dy2 - dy) - y + y2,
        t2 * (dz2 - dz) - z + z2,
        t3 * (dx3 - dx) - x + x3,
        t3 * (dy3 - dy) - y + y3,
        t3 * (dz3 - dz) - z + z3,
    ]

    X, Y, Z, *_ = sympy.solve(equations, [x, y, z, dx, dy, dz, t1, t2, t3])[0]
    return X + Y + Z


def in_range(range, pos):
    return all(min <= val <= max for val, min, max in zip(pos, *range))


def get_xy_intersect(a, b):
    (ax, ay, _), (avx, avy, _) = a
    (bx, by, _), (bvx, bvy, _) = b

    am = avy / avx
    bm = bvy / bvx

    if am == bm:
        return None

    ab = ay - am * ax
    bb = by - bm * bx

    x = (bb - ab) / (am - bm)
    y = am * x + ab

    a_time = (x - ax) / avx
    b_time = (x - bx) / bvx

    if a_time > 0 and b_time > 0:
        return (x, y)
    else:
        return None


if __name__ == "__main__":
    main(DAY, YEAR, SAMPLE, parse, part1, part2)
