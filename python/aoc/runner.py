import argparse
import builtins
from contextlib import contextmanager
from importlib import import_module
from pprint import pp

import peek
from aoc.tools.time_perf import time_perf
from aocd import get_data


def main():
    args = get_args()

    day = str(args.day) if args.day > 9 else f"0{args.day}"

    solution_module = import_module(f"aoc.y_{args.year}.d_{day}")

    if args.pretty_print:
        _print = pp
    else:
        _print = print

    data = None
    if args.data == "main":
        data = get_data(day=args.day, year=args.year)
    elif args.data == "example":
        data = solution_module.examples[args.example - 1][0]

    if args.action == "solve":
        parsed_data, parse_time = run(solution_module.parse, data, args.debug)

        _print(f"Parsed in {parse_time}")

        part_1, time_part_1 = run(
            solution_module.part_1, parsed_data, args.debug
        )
        _print(f"Part 1: {part_1} in {time_part_1}")

        part_2, time_part_2 = run(
            solution_module.part_2, parsed_data, args.debug
        )
        _print(f"Part 2: {part_2} in {time_part_2}")

    elif args.action == "parse":
        parsed_data, parse_time = run(solution_module.parse, data, args.debug)
        _print(parsed_data)
        _print(f"Parsed in {parse_time}")

    elif args.action == "input":
        _print(data)

    elif args.action == "part1":
        parsed_data, parse_time = run(solution_module.parse, data, args.debug)
        part_1, time_part_1 = run(
            solution_module.part_1, parsed_data, args.debug
        )
        _print(f"Part 1: {part_1} in {time_part_1}")

    elif args.action == "part2":
        parsed_data, parse_time = run(solution_module.parse, data, args.debug)
        part_2, time_part_2 = run(
            solution_module.part_2, parsed_data, args.debug
        )
        _print(f"Part 2: {part_2} in {time_part_2}")

    elif args.action == "test":
        for i, (data, expected_1, expected_2) in enumerate(
            solution_module.examples, 1
        ):
            print(f"{"=" * 20} Test {i} {"=" * 20}")
            print(data)

            parsed_data, parse_time = run(
                solution_module.parse, data, args.debug
            )
            _print(f"Parsed in {parse_time}")

            part_1, time_part_1 = run(
                solution_module.part_1, parsed_data, args.debug
            )

            if part_1 == expected_1:
                print(f"Part 1: ✅ in {time_part_1}")
            else:
                print("Part 1: ❌ in {time_part_1}")
                print(f"Expected: {expected_1}")
                print(f"Got: {part_1}")
            part_2, time_part_2 = run(
                solution_module.part_2, parsed_data, args.debug
            )
            if part_2 == expected_2:
                print("Part 2: ✅")
            else:
                print("Part 2: ❌")
                print(f"Expected: {expected_2}")
                print(f"Got: {part_2}")


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("year", type=int)
    parser.add_argument("day", type=int)

    parser.add_argument(
        "-a",
        "--action",
        default="solve",
        required=False,
        choices=["solve", "parse", "input", "test", "part1", "part2"],
    )

    parser.add_argument(
        "-d",
        "--data",
        default="main",
        required=False,
        choices=["main", "example"],
    )

    parser.add_argument(
        "-e",
        "--example",
        default=1,
        type=int,
        required=False,
    )

    parser.add_argument(
        "-p",
        "--pretty-print",
        required=False,
        default=False,
        action="store_true",
    )

    parser.add_argument(
        "--debug",
        required=False,
        default=False,
        action="store_true",
    )

    return parser.parse_args()


@contextmanager
def suppress_print():
    original_print = builtins.print
    try:
        builtins.print = lambda *args, **kwargs: None  # Override with no-op
        peek.enabled = False
        yield
    finally:
        builtins.print = original_print  # Restore original print
        peek.enabled = True


def run(func, data, debug=False):
    if not debug:
        with suppress_print():
            return time_perf(func, data)
    else:
        return time_perf(func, data)


if __name__ == "__main__":
    main()
