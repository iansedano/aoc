import pathlib

INPUT_FILE = "day_01.txt"


def parse(puzzle_input):
    return [
        sum(int(line) for line in lines.split("\n"))
        for lines in puzzle_input.split("\n\n")
    ]


def part1(data):
    return max(data)


def part2(data):
    return sum(sorted(data)[-3:])


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = pathlib.Path(INPUT_FILE).read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
