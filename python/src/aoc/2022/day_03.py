from aocd import get_data


def chunks(iterable, chunk_size):
    return (
        iterable[i : i + chunk_size]
        for i in range(0, len(iterable), chunk_size)
    )


def parse_sacks_into_parts(puzzle_input):
    return [
        [line[: len(line) // 2], line[len(line) // 2 :]]
        for line in puzzle_input.split("\n")
    ]


def parse_sacks_into_groups(puzzle_input):
    return chunks(puzzle_input.split("\n"), 3)


def get_priority(letter):
    return ord(letter) - 96 if ord(letter) >= 97 else ord(letter) - 38


def part1(data):
    return sum(
        get_priority((set(sack[0]) & set(sack[1])).pop()) for sack in data
    )


def part2(data):
    return sum(
        get_priority((set(group[0]) & set(group[1]) & set(group[2])).pop())
        for group in data
    )


def solve(puzzle_input):
    solution1 = part1(parse_sacks_into_parts(puzzle_input))
    solution2 = part2(parse_sacks_into_groups(puzzle_input))

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = get_data(day=3, year=2022).strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
