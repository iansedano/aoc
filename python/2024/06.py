from textwrap import dedent

from aocd import get_data

DAY = 1
YEAR = 2024
SAMPLE = dedent(
    """\
    ....#.....
    .........#
    ..........
    ..#.......
    .......#..
    ..........
    .#..^.....
    ........#.
    #.........
    ......#...
    """
)


def parse(puzzle_input):
    grid = {}
    lines = puzzle_input.splitlines()
    height, width = len(lines), len(lines[0])
    guard = None

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                grid[(x, y)] = char
            if char == "^":
                guard = (x, y)

    return grid, guard, (width, height)


UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


def part_1(parsed_input):
    grid, guard, dims = parsed_input
    grid: dict
    return len({pos for pos, direction in get_visited(grid, guard, dims, UP)})


def turn_ninety(direction):
    if direction == UP:
        return RIGHT
    if direction == RIGHT:
        return DOWN
    if direction == DOWN:
        return LEFT
    if direction == LEFT:
        return UP


def get_visited(grid: dict, guard: tuple, dims: tuple, direction: tuple):
    visited = [(guard, direction)]

    while True:
        new_position, new_direction = step(guard, direction, grid)

        if not (
            0 <= new_position[0] < dims[0] and 0 <= new_position[1] < dims[1]
        ):
            break

        if direction != new_direction:
            direction = new_direction
            visited.append((guard, direction))
            continue

        if guard != new_position:
            guard = new_position
            visited.append((new_position, direction))

    return visited


def part_2(parsed_input):
    grid, guard, dims = parsed_input
    initial_position, initial_direction = guard, UP
    visited = get_visited(grid, initial_position, dims, initial_direction)
    new_blocks = set()

    for position, direction in visited:

        new_block_position = (
            position[0] + direction[0],
            position[1] + direction[1],
        )

        if not (
            0 <= new_block_position[0] < dims[0]
            and 0 <= new_block_position[1] < dims[1]
        ):
            continue

        grid_with_new_block = {new_block_position: "#"} | grid

        path = set((initial_position, initial_direction))
        position = initial_position
        direction = initial_direction

        while len(path) < 1000000:
            new_position, new_direction = step(
                position, direction, grid_with_new_block
            )

            if (new_position, new_direction) in path:
                new_blocks.add(new_block_position)
                break

            if not (
                0 <= new_position[0] < dims[0]
                and 0 <= new_position[1] < dims[1]
            ):
                break

            if direction != new_direction:
                direction = new_direction
                path.add((position, direction))
                continue

            if position != new_position:
                position = new_position
                path.add((position, direction))

    return len(new_blocks)


def step(guard, direction, grid):
    new_position = (guard[0] + direction[0], guard[1] + direction[1])

    if grid.get(new_position, None) == "#":
        new_direction = turn_ninety(direction)
        return guard, new_direction

    if grid.get(new_position, None) is None:
        return new_position, direction


if __name__ == "__main__":
    data = get_data(day=DAY, year=YEAR).strip()
    parsed = parse(SAMPLE)
    print(f"Part 1: {part_1(parsed)}")
    print(f"Part 2: {part_2(parsed)}")
