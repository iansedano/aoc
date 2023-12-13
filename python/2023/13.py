from common import main

DAY = 13
YEAR = 2023
SAMPLE = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""


def parse(puzzle_input):
    grid_rows = [grid.splitlines() for grid in puzzle_input.split("\n\n")]
    grid_cols = [transpose(row) for row in grid_rows]
    return list(zip(grid_rows, grid_cols))


def part1(parsed_input):
    return sum(reflection_score(rows, cols) for rows, cols in parsed_input)


def part2(parsed_input):
    return sum(
        reflection_score(rows, cols, smudge_factor=1)
        for rows, cols in parsed_input
    )


def reflection_score(rows, cols, smudge_factor=0):
    row_reflection = find_reflection(rows, smudge_factor)

    return (
        row_reflection * 100
        if row_reflection is not None
        else find_reflection(cols, smudge_factor)
    )


def find_reflection(rows, smudge_factor=0):
    for i in range(len(rows) - 1):
        reflection_point = (i, i + 1)
        left = rows[reflection_point[0] :: -1]
        right = rows[reflection_point[1] :]

        if sum(str_diff(a, b) for a, b in zip(left, right)) == smudge_factor:
            return len(left)
    return None


def str_diff(str_a, str_b):
    return sum(char_a != char_b for char_a, char_b in zip(str_a, str_b))


def transpose(array):
    return ["".join(x) for x in zip(*array)]


if __name__ == "__main__":
    main(DAY, YEAR, SAMPLE, parse, part1, part2)
