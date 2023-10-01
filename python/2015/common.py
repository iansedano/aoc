import sys
from textwrap import dedent

from aocd import get_data
from time_perf import time_perf


def main(DAY, YEAR, sample, parse, part1, part2):
    def run(input):
        data, parse_time = time_perf(parse, input)
        part_1, time_part_1 = time_perf(part1, data)
        part_2, time_part_2 = time_perf(part2, data)

        print(
            dedent(
                f"""\
            Parsed in {parse_time}
            Part 1: {part_1} in {time_part_1}
            Part 2: {part_2} in {time_part_2}
        """
            )
        )

    if len(sys.argv) < 2:
        # default, just solve
        run(get_data(day=DAY, year=YEAR).strip())
    elif sys.argv[1] == "sample":
        # solve using the sample data
        run(sample)
    elif sys.argv[1] == "input":
        # just output the input data
        print(get_data(day=DAY, year=YEAR).strip())
    elif sys.argv[1] == "parse":
        # just parse and output the parsed data
        print(parse(get_data(day=DAY, year=YEAR).strip()))
