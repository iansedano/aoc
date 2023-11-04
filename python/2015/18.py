from itertools import product

from common import main

DAY = 18
YEAR = 2015
SAMPLE = """"""

GRID_SIZE = 100


def parse(puzzle_input):
    # return [
    #     [1 if char == "#" else 0 for char in list(line)]
    #     for line in puzzle_input.splitlines()
    # ]

    lines = puzzle_input.splitlines()
    max_y = len(lines)
    max_x = len(lines[0])

    return (max_x, max_y), {
        (x, y)
        for y, line in enumerate(lines)
        for x, char in enumerate(list(line))
        if char == "#"
    }


def part1(input):
    grid_size, grid = input

    for _ in range(100):
        grid = tick(grid, grid_size)

    return len(grid)


def part2(input):
    grid_size, grid = input

    for _ in range(100):
        for corner in get_corners(grid_size):
            grid.add(corner)
        grid = tick(grid, grid_size)

    for corner in get_corners(grid_size):
        grid.add(corner)

    return len(grid)


def get_corners(max_dim):
    return [
        (0, 0),
        (0, max_dim[1] - 1),
        (max_dim[0] - 1, 0),
        (max_dim[0] - 1, max_dim[1] - 1),
    ]


def tick(grid: set[tuple[int]], max_dim: tuple[int]):
    """
    A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
    A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
    """

    new_grid = set()

    for coord in product(range(max_dim[0]), range(max_dim[1])):
        live_neighbors = len(
            [cell for cell in get_neighbors(coord, max_dim) if cell in grid]
        )

        if coord in grid:
            if live_neighbors in [2, 3]:
                new_grid.add(coord)
        else:
            if live_neighbors == 3:
                new_grid.add(coord)

    return new_grid


def get_neighbors(coord: tuple[int], max_dim: tuple[int]):
    return [
        (new_x, new_y)
        for delta in product([-1, 0, 1], repeat=2)
        if (new_x := coord[0] + delta[0]) < max_dim[0]
        and (new_y := coord[1] + delta[1]) < max_dim[1]
        and (new_x, new_y) != coord
    ]


main(DAY, YEAR, SAMPLE, parse, part1, part2)
