import functools
import itertools
import math
from dataclasses import dataclass
from operator import add, mul
from pprint import pp
from typing import Callable

from aocd import get_data

SAMPLE = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

import functools
import math


@dataclass
class Monkey:
    items: list[int]
    operation: Callable[[int], int]
    divisible_by_test: int
    if_true: int
    if_false: int
    items_inspected: int = 0


def parse_operation(operation):
    operator = add if operation[2] == "+" else mul

    if operation[4:] == "x":
        return lambda x: operator(x, x)
    else:
        return lambda x: operator(x, int(operation[4:]))


def parse(puzzle_input):
    """Parse input."""
    monkey_data = [
        [line.strip() for line in monkey.strip().split("\n")]
        for monkey in puzzle_input.split("Monkey")
    ][1:]

    monkeys = []

    for monkey in monkey_data:
        # number = int(monkey[0][0])
        items = [
            int(item) for item in monkey[1].split(":")[1].strip().split(",")
        ]
        operation = monkey[2].split("=")[1].strip().replace("old", "x")

        divisible_by = int(monkey[3].split("by")[1].strip())
        if_true = int(monkey[4][-1])
        if_false = int(monkey[5][-1])

        operation = parse_operation(operation)

        monkeys.append(
            Monkey(items, operation, divisible_by, if_true, if_false)
        )

    return monkeys


def part1(data):
    """Solve part 1."""
    ROUNDS = 20
    monkeys = data

    for _, monkey in itertools.product(range(ROUNDS), monkeys):
        for item in monkey.items:
            new_worry_level = monkey.operation(item) // 3
            if new_worry_level % monkey.divisible_by_test == 0:
                monkeys[monkey.if_true].items.append(new_worry_level)
            else:
                monkeys[monkey.if_false].items.append(new_worry_level)
            monkey.items_inspected += 1

        monkey.items = []

    return mul(*sorted([monkey.items_inspected for monkey in monkeys])[-2:])


def part2(data):
    """Solve part 2."""
    ROUNDS = 10000
    monkeys = data
    least_common_multiple = math.lcm(
        *[monkey.divisible_by_test for monkey in monkeys]
    )
    for _, monkey in itertools.product(range(ROUNDS), monkeys):
        for item in monkey.items:
            new_worry_level = monkey.operation(item) % least_common_multiple

            if new_worry_level % monkey.divisible_by_test == 0:
                monkeys[monkey.if_true].items.append(new_worry_level)
            else:
                monkeys[monkey.if_false].items.append(new_worry_level)

            monkey.items_inspected += 1

        monkey.items = []

    # print(
    #     "\n".join(
    #         [
    #             f"{i} {monkey.items_inspected}"
    #             for i, monkey in enumerate(monkeys)
    #         ]
    #     )
    # )

    return mul(*sorted([monkey.items_inspected for monkey in monkeys])[-2:])


def main():
    puzzle_input = get_data(day=11, year=2022).strip()
    # puzzle_input = SAMPLE
    data = parse(puzzle_input)
    solution1 = part1(data)
    data = parse(puzzle_input)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    solution1, solution2 = main()
    print(f"{solution1 = }\n{solution2 = }")
