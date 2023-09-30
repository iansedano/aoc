import sys
from textwrap import dedent

from aocd import get_data
from time_perf import time_perf

"""
"""

DAY = 1
YEAR = 2015
SAMPLE = """
"""

def parse(puzzle_input):
    return puzzle_input


def part1(input):
    """
    """

def part2(input):
    """
    """


def main(input):
    data = parse(input)
    part_1, time_part_1 = time_perf(part1, data)
    part_2, time_part_2 = time_perf(part2, data)
    
    print(dedent(f"""\
        Part 1: {part_1} in {time_part_1}
        Part 2: {part_2} in {time_part_2}
    """))
    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        main(get_data(day=DAY, year=YEAR).strip())
    elif sys.argv[1] == "sample":
        main(SAMPLE)
    elif sys.argv[1] == "input":
        print(get_data(day=DAY, year=YEAR).strip())
