import argparse
from pprint import pp
from textwrap import dedent

from aocd import get_data
from time_perf import time_perf


def main(DAY, YEAR, sample, parse, part1, part2):
    def run(input):
        data, parse_time = time_perf(parse, input)
        print(f"Parsed in {parse_time}")
        part_1, time_part_1 = time_perf(part1, data)
        print(f"Part 1: {part_1} in {time_part_1}")
        part_2, time_part_2 = time_perf(part2, data)
        print(f"Part 2: {part_2} in {time_part_2}")

    parser = argparse.ArgumentParser()

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

    args = parser.parse_args()

    if args.pretty_print:
        _print = pp
    else:
        _print = print

    match [args.data, args.action]:
        case ["main", "solve"]:
            run(get_data(day=DAY, year=YEAR).strip())
        case ["main", "parse"]:
            _print(parse(get_data(day=DAY, year=YEAR).strip()))
        case ["main", "input"]:
            _print(get_data(day=DAY, year=YEAR).strip())
        case ["sample", "solve"]:
            run(sample)
        case ["sample", "parse"]:
            _print(parse(sample))
        case ["sample", "input"]:
            _print(sample)
