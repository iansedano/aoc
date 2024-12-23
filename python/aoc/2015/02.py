import sys
from textwrap import dedent

from aocd import get_data
from time_perf import time_perf

DAY = 2
YEAR = 2015
SAMPLE = """
"""

def parse(puzzle_input):
    return [tuple(int(num) for num in line.split("x")) for line in puzzle_input.split("\n")]


def part1(input):
    return sum(calc_area(l,w,h) for l,w,h in input)

def part2(input):
    return sum(calc_ribbon(l,w,h) for l,w,h in input)
    
def calc_area(l, w, h):
    area = 2*l*w + 2*w*h + 2*h*l
    s1, s2 = sorted([l,w,h])[:2]
    return area + s1 * s2

def calc_ribbon(l, w, h):
    s1, s2 = sorted([l,w,h])[:2]
    perimeter = 2*s1 + 2*s2
    volume = l * w * h
    return perimeter + volume
    

def main(input):
    data, parse_time = time_perf(parse, input)
    part_1, time_part_1 = time_perf(part1, data)
    part_2, time_part_2 = time_perf(part2, data)
    
    print(dedent(f"""\
        Parsed in {parse_time}
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
    elif sys.argv[1] == "parse":
        print(parse(get_data(day=DAY, year=YEAR).strip()))
