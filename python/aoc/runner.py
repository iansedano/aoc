import argparse
from importlib import import_module
from pprint import pp

from aocd import get_data
from aoc.tools.time_perf import time_perf


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
        parsed_data, parse_time = time_perf(solution_module.parse, data)
        _print(f"Parsed in {parse_time}")
        part_1, time_part_1 = time_perf(solution_module.part_1, parsed_data)
        _print(f"Part 1: {part_1} in {time_part_1}")
        part_2, time_part_2 = time_perf(solution_module.part_2, parsed_data)
        _print(f"Part 2: {part_2} in {time_part_2}")

    elif args.action == "parse":
        parsed_data, parse_time = time_perf(solution_module.parse, data)
        _print(parsed_data)
        _print(f"Parsed in {parse_time}")

    elif args.action == "input":
        _print(data)

    elif args.action == "part1":
        parsed_data, parse_time = time_perf(solution_module.parse, data)
        part_1, time_part_1 = time_perf(solution_module.part_1, parsed_data)
        _print(f"Part 1: {part_1} in {time_part_1}")

    elif args.action == "part2":
        parsed_data, parse_time = time_perf(solution_module.parse, data)
        part_2, time_part_2 = time_perf(solution_module.part_2, parsed_data)
        _print(f"Part 2: {part_2} in {time_part_2}")

    elif args.action == "test":
        for data, expected_1, expected_2 in solution_module.examples:
            parsed_data, parse_time = time_perf(solution_module.parse, data)
            part_1, time_part_1 = time_perf(solution_module.part_1, parsed_data)
            part_2, time_part_2 = time_perf(solution_module.part_2, parsed_data)
            assert part_1 == expected_1
            assert part_2 == expected_2
            print(f"Test passed for {parsed_data}")


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

    return parser.parse_args()


if __name__ == "__main__":
    main()
