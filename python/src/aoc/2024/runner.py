import argparse
from importlib import import_module
from pprint import pp

from aocd import get_data
from time_perf import time_perf


def main():
    args = get_args()

    module = import_module(str(args.day) if args.day > 9 else f"0{args.day}")

    if args.pretty_print:
        _print = pp
    else:
        _print = print

    def run(input):
        data, parse_time = time_perf(module.parse, input)
        print(f"Parsed in {parse_time}")
        part_1, time_part_1 = time_perf(module.part_1, data)
        print(f"Part 1: {part_1} in {time_part_1}")
        part_2, time_part_2 = time_perf(module.part_2, data)
        print(f"Part 2: {part_2} in {time_part_2}")

    match [args.data, args.action]:
        case ["main", "solve"]:
            run(get_data(day=args.day, year=args.year).strip())
        case ["main", "parse"]:
            _print(module.parse(get_data(day=args.day, year=args.year).strip()))
        case ["main", "input"]:
            _print(get_data(day=args.day, year=args.year).strip())
        case ["sample", "solve"]:
            run(module.SAMPLE)
        case ["sample", "parse"]:
            _print(module.parse(module.SAMPLE))
        case ["sample", "input"]:
            _print(module.SAMPLE)


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("year", type=int)
    parser.add_argument("day", type=int)

    parser.add_argument(
        "-d",
        "--data",
        default="main",
        required=False,
        choices=["main", "sample"],
    )
    parser.add_argument(
        "-a",
        "--action",
        default="solve",
        required=False,
        choices=["solve", "parse", "input"],
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
