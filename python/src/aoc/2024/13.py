from textwrap import dedent

import sympy
from aocd import get_data

DAY = 13
YEAR = 2024
SAMPLE = dedent(
    """\
    Button A: X+94, Y+34
    Button B: X+22, Y+67
    Prize: X=8400, Y=5400

    Button A: X+26, Y+66
    Button B: X+67, Y+21
    Prize: X=12748, Y=12176

    Button A: X+17, Y+86
    Button B: X+84, Y+37
    Prize: X=7870, Y=6450

    Button A: X+69, Y+23
    Button B: X+27, Y+71
    Prize: X=18641, Y=10279
    """.rstrip()
)


def parse(puzzle_input):
    parts = [line.split("\n") for line in puzzle_input.split("\n\n")]

    button_prizes = []

    for part in parts:
        a, b, prize = part
        a = tuple(int(n) for n in a.strip("Button A: X+").split(", Y+"))
        b = tuple(int(n) for n in b.strip("Button A: X+").split(", Y+"))
        prize = tuple(int(n) for n in prize.strip("Prize: X=").split(", Y="))
        button_prizes.append((a, b, prize))

    return button_prizes


def part_1(parsed_input):
    cost = 0
    for a, b, target in parsed_input:
        solution = solve(a, b, target)
        if solution is not None:
            cost += solution[0] * 3 + solution[1]
    return cost


def part_2(parsed_input):
    inc = 10000000000000
    cost = 0
    for a, b, target in parsed_input:
        solution = solve(a, b, (target[0] + inc, target[1] + inc))
        if solution is not None:
            cost += solution[0] * 3 + solution[1]
    return cost


def solve(button_1, button_2, target):
    """
    >>> solve((94,34),(22,67),(8400,5400))
    (80, 40)
    """
    a, b = sympy.symbols("a b")
    sol = sympy.solve(
        [
            a * button_1[0] + b * button_2[0] - target[0],
            a * button_1[1] + b * button_2[1] - target[1],
        ],
        [a, b],
    )

    if sol[a].is_integer and sol[b].is_integer:
        return sol[a], sol[b]
    else:
        return None


if __name__ == "__main__":
    data = get_data(day=DAY, year=YEAR).strip()
    parsed = parse(data)
    print(f"Part 1: {part_1(parsed)}")
    print(f"Part 2: {part_2(parsed)}")
