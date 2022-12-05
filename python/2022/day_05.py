from aocd import get_data


def parse(puzzle_input):
    lines = puzzle_input.split("\n")

    stacks = [list(line[1::4]) for line in lines[:8]]

    piles = [[] for _ in range(9)]
    for line in stacks:
        for i, item in enumerate(line):
            if item.strip():
                piles[i].insert(0, item)

    instructions = [line.split(" ") for line in lines[10:]]
    instructions = [
        tuple(int(line[j]) for j in (1, 3, 5)) for line in instructions
    ]

    return piles, instructions


def part1(data):
    """Solve part 1."""
    piles, instructions = data

    for instruction in instructions:
        times, fromIndex, toIndex = instruction
        fromIndex, toIndex = fromIndex - 1, toIndex - 1

        for _ in range(times):
            piles[toIndex].append(piles[fromIndex].pop())

    return "".join([pile[-1] for pile in piles])


def part2(data):
    """Solve part 2."""
    piles, instructions = data

    for instruction in instructions:
        times, fromIndex, toIndex = instruction
        fromIndex, toIndex = fromIndex - 1, toIndex - 1

        crates_to_move = piles[fromIndex][-times:]
        piles[fromIndex] = piles[fromIndex][:-times]
        piles[toIndex] = piles[toIndex] + crates_to_move

    return "".join([pile[-1] for pile in piles])


def main():
    puzzle_input = get_data(day=5, year=2022).strip()
    data = parse(puzzle_input)
    solution1 = part1(data)
    data = parse(puzzle_input)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    solution1, solution2 = main()

    print(f"{solution1}\n{solution2}")
