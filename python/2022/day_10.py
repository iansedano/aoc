from aocd import get_data
from pprint import pp


def parse(puzzle_input):
    """Parse input."""
    out = []
    for line in puzzle_input.splitlines():
        if line == "noop":
            out.append((1, 0))
        else:
            out.append((2, int(line.split()[1])))
    return out


def part1(data):
    """Solve part 1."""
    clock = 0
    x_register = 1
    cycles_to_sample = (20, 60, 100, 140, 180, 220)
    x_register_at_sample_points = []

    for instruction in data:
        cycles, inc = instruction

        for _ in range(cycles):
            clock += 1
            if clock in cycles_to_sample:
                x_register_at_sample_points.append(x_register * clock)

        x_register += inc

    return sum(x_register_at_sample_points)


def part2(data):
    """Solve part 2."""
    clock = 0
    x_register = 1
    row_ends = (40, 80, 120, 160, 200, 240)
    screen = ["."] * 239

    for instruction in data:
        cycles, inc = instruction
        sprite_position = [x_register - 1, x_register, x_register + 1]

        for _ in range(cycles):
            if clock % 40 in sprite_position:
                screen[clock] = "#"
            clock += 1

        x_register += inc

    out = [[]]
    for i, ch in enumerate(screen):
        out[-1].append(ch)
        if i in [val - 1 for val in row_ends]:
            out.append([])
    return "\n".join(["".join(row) for row in out])


def main():
    puzzle_input = get_data(day=10, year=2022).strip()
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    solution1, solution2 = main()
    print(f"{solution1}\n{solution2}")
