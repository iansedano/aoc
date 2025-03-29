from common import main

DAY = 14
YEAR = 2023
SAMPLE = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""


def parse(puzzle_input):
    lines = puzzle_input.splitlines()
    shape = (len(lines[0]), len(lines))
    balls = set()
    cubes = set()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                cubes.add((x, y))
            if char == "O":
                balls.add((x, y))

    return shape, balls, cubes


def part1(parsed_input):
    shape, balls, cubes = parsed_input
    cols = [tilt_col(col) for col in get_cols(balls, cubes, shape)]
    return get_load_on_north_beams(cols, shape)


def part2(parsed_input):
    shape, balls, cubes = parsed_input

    ball_states = [balls]

    for spin_number in range(1, 300):
        ball_states.append(spin(shape, ball_states[-1], cubes))

        cycle_size = None
        for i, ball_state in enumerate(ball_states[-2::-1], 1):
            if ball_states[-1] == ball_state:
                cycle_size = i
                break
        if cycle_size:
            break

    ball_states = ball_states[1:]
    cycle_start = spin_number - cycle_size

    idx = (((1_000_000_000 - cycle_start) % cycle_size) + cycle_start) - 1

    return get_load_on_north_beams(
        get_cols(ball_states[idx], cubes, shape), shape
    )


def spin(shape, balls, cubes):
    # North
    cols = [tilt_col(col) for col in get_cols(balls, cubes, shape)]
    balls = get_ball_positions(cols, "y")
    # West
    rows = [tilt_col(row) for row in get_rows(balls, cubes, shape)]
    balls = get_ball_positions(rows, "x")
    # South
    cols = [
        tilt_col(col, shape[1], True) for col in get_cols(balls, cubes, shape)
    ]
    balls = get_ball_positions(cols, "y")
    # East
    rows = [
        tilt_col(row, shape[0], True) for row in get_rows(balls, cubes, shape)
    ]
    return get_ball_positions(rows, "x")


def get_ball_positions(arrays, axis):
    balls = set()
    for a, sub_array in enumerate(arrays):
        for item in sub_array:
            if item[0] == "O":
                if axis == "y":
                    balls.add((a, item[1]))
                elif axis == "x":
                    balls.add((item[1], a))
    return balls


def get_cols(balls, cubes, shape):
    cols = []
    for x in range(shape[0]):
        col = []
        for y in range(shape[1]):
            pos = (x, y)
            if pos in balls:
                col.append(("O", y))
            elif pos in cubes:
                col.append(("#", y))
        cols.append(col)
    return cols


def get_rows(balls, cubes, shape):
    rows = []
    for y in range(shape[1]):
        row = []
        for x in range(shape[0]):
            pos = (x, y)
            if pos in balls:
                row.append(("O", x))
            elif pos in cubes:
                row.append(("#", x))
        rows.append(row)
    return rows


def get_load_on_north_beams(cols, shape):
    return sum(
        sum(shape[1] - y for rock, y in col if rock == "O") for col in cols
    )


def tilt_col(col, limit=0, reversed=False):
    tilted_col = []

    stacking_point = limit - 1 if not reversed else limit
    col = sorted(col, key=lambda x: x[1], reverse=reversed)
    for item in col:
        if item[0] == "#":
            tilted_col.append(item)
            stacking_point = item[1]
        if item[0] == "O":
            stacking_point = (
                stacking_point + 1 if not reversed else stacking_point - 1
            )
            tilted_col.append((item[0], stacking_point))

    return tilted_col


def debug(shape, balls, cubes):
    rows = []
    for y in range(shape[1]):
        row = []
        for x in range(shape[0]):
            pos = (x, y)
            if pos in balls:
                row.append("O")
            elif pos in cubes:
                row.append("#")
            else:
                row.append(".")
        rows.append(row)
    return "\n".join(["".join(row) for row in rows])


if __name__ == "__main__":
    main(DAY, YEAR, SAMPLE, parse, part1, part2)
