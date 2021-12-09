import depth_input
import smoke_finder

import math

from debug import p

SAMPLE_01 = """2199943210
3987894921
9856789892
8767896789
9899965678"""


def test_input():
    print(depth_input.parse_depth_data(SAMPLE_01))


def test_sample_part_1():
    heightmap = depth_input.parse_depth_data(SAMPLE_01)

    low_points = smoke_finder.find_low_points(heightmap)
    print(low_points)
    sum = 0
    for low_point in low_points:
        sum += low_point[2] + 1

    print(sum)


def test_part_1():
    heightmap = depth_input.parse_depth_data()

    low_points = smoke_finder.find_low_points(heightmap)
    print(low_points)
    sum = 0
    for low_point in low_points:
        sum += low_point[2] + 1

    print(sum)


def test_sample_part_2():
    heightmap = depth_input.parse_depth_data(SAMPLE_01)

    low_points = smoke_finder.find_low_points(heightmap)

    basins = []
    for low_point in low_points:
        new_basin = smoke_finder.get_basin(heightmap, low_point)
        basins.append(new_basin)

    p(math.prod(sorted([len(b) for b in basins])[-3:]))


def test_part_2():
    heightmap = depth_input.parse_depth_data()

    low_points = smoke_finder.find_low_points(heightmap)

    basins = []
    for low_point in low_points:
        new_basin = smoke_finder.get_basin(heightmap, low_point)
        basins.append(new_basin)

    p(math.prod(sorted([len(b) for b in basins])[-3:]))


test_part_2()
