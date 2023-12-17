import heapq
from collections import defaultdict

from common import main

DAY = 17
YEAR = 2023
SAMPLE = """\
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""


def parse(puzzle_input):
    return {
        (x, y): int(char)
        for y, row in enumerate(puzzle_input.splitlines())
        for x, char in enumerate(row)
    }


def part1(parsed_input):
    grid = parsed_input
    start = (0, 0)
    target = max(grid.keys())

    scores = path_find(start, grid, get_crucible_steps)

    return min(v for (pos, _, _), v in scores.items() if pos == target)


def part2(parsed_input):
    grid = parsed_input
    start = (0, 0)
    target = max(grid.keys())

    scores = path_find(start, grid, get_ultra_crucible_steps)

    return min(v for (pos, _, _), v in scores.items() if pos == target)


def path_find(start, grid, step_finder):
    costs = defaultdict(lambda: float("inf"))

    costs[(start, (0, 0), 0)] = 0  # pos, dir, consecutive : score

    pq = []

    for direction in [(1, 0), (0, 1)]:
        for step in step_finder(
            start, cost=0, direction=direction, consecutive=0, grid=grid
        ):
            heapq.heappush(pq, step)

    while pq:
        cost, pos, direction, consecutive = heapq.heappop(pq)
        if costs[(pos, direction, consecutive)] > cost:
            costs[(pos, direction, consecutive)] = cost

            for next_pos in step_finder(
                pos, cost, direction, consecutive, grid
            ):
                heapq.heappush(pq, next_pos)
    return costs


def get_crucible_steps(pos, cost, direction, consecutive, grid):
    potential = {(1, 0), (0, 1), (-1, 0), (0, -1)} - {inv_v(direction)}

    if consecutive >= 3:
        potential.discard(direction)
        return [
            (cost + grid[p], p, delta, 1)
            for delta in potential
            if (p := add_v(pos, delta)) in grid
        ]

    return [
        (cost + grid[p], p, delta, 1)
        if delta != direction
        else (cost + grid[p], p, delta, 1 + consecutive)
        for delta in potential
        if (p := add_v(pos, delta)) in grid
    ]


def get_ultra_crucible_steps(pos, cost, direction, consecutive, grid):
    if consecutive < 4:
        next_pos = add_v(pos, direction)
        if next_pos in grid:
            return [
                (cost + grid[next_pos], next_pos, direction, 1 + consecutive)
            ]
        else:
            return []

    potential = {(1, 0), (0, 1), (-1, 0), (0, -1)} - {inv_v(direction)}

    if consecutive >= 10:
        potential.discard(direction)
        return [
            (cost + grid[p], p, delta, 1)
            for delta in potential
            if (p := add_v(pos, delta)) in grid
        ]

    return [
        (cost + grid[p], p, delta, 1)
        if delta != direction
        else (cost + grid[p], p, delta, 1 + consecutive)
        for delta in potential
        if (p := add_v(pos, delta)) in grid
    ]


def add_v(a, b):
    return (a[0] + b[0], a[1] + b[1])


def inv_v(a):
    return (-a[0], -a[1])


if __name__ == "__main__":
    main(DAY, YEAR, SAMPLE, parse, part1, part2)
