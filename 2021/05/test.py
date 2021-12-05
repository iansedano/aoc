from vent_input import parse_vent_data
import vent_mapping

SAMPLE_01 = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


def test_parse():
    assert parse_vent_data(SAMPLE_01) == [
        ((0, 9), (5, 9)),
        ((8, 0), (0, 8)),
        ((9, 4), (3, 4)),
        ((2, 2), (2, 1)),
        ((7, 0), (7, 4)),
        ((6, 4), (2, 0)),
        ((0, 9), (2, 9)),
        ((3, 4), (1, 4)),
        ((0, 0), (8, 8)),
        ((5, 5), (8, 2)),
    ]


def test_sample_part1():

    lines = parse_vent_data(SAMPLE_01)
    h_v_lines = vent_mapping.filter_diagonal_lines(lines)

    assert h_v_lines == [
        ((0, 9), (5, 9)),
        ((9, 4), (3, 4)),
        ((2, 2), (2, 1)),
        ((7, 0), (7, 4)),
        ((0, 9), (2, 9)),
        ((3, 4), (1, 4)),
    ]

    grid = vent_mapping.generate_grid(10, 10)
    points = vent_mapping.get_overlapping_points(h_v_lines, grid)

    assert len(points) == 5


def test_sample_part2():

    lines = parse_vent_data(SAMPLE_01)
    grid = vent_mapping.generate_grid(10, 10)
    points = vent_mapping.get_overlapping_points(lines, grid)

    assert len(points) == 12


def test_grid():
    assert vent_mapping.generate_grid(5, 5) == [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]

    assert vent_mapping.generate_grid(1, 5) == [
        [0],
        [0],
        [0],
        [0],
        [0],
    ]

    assert vent_mapping.generate_grid(3, 14) == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]


def test_main_data_part_1():

    lines = parse_vent_data()
    h_v_lines = vent_mapping.filter_diagonal_lines(lines)
    grid = vent_mapping.generate_grid(1000, 1000)
    points = vent_mapping.get_overlapping_points(h_v_lines, grid)

    assert len(points) == 7438


def test_part_2():

    lines = parse_vent_data()
    grid = vent_mapping.generate_grid(1000, 1000)
    points = vent_mapping.get_overlapping_points(lines, grid)

    assert len(points) == 21406
