import sys
from collections import defaultdict
from textwrap import dedent

from aocd import get_data
from time_perf import time_perf

"""
"""

DAY = 3
YEAR = 2015
SAMPLE = """
"""

def parse(puzzle_input):
    return tuple(puzzle_input)


def part1(input):
    return visit_houses(input)

def part2(input):
    santa_dirs = input[::2]
    robo_dirs = input[1::2]
    
    return (visit_houses(santa_dirs) + visit_houses(robo_dirs))
   

def visit_houses(dirs):
    x, y = 0, 0
    grid = {(x, y)}
    
    for dir in dirs:
        if dir == "<":
            x -= 1
        elif dir == "^":
            y -= 1
        elif dir == ">":
            x += 1
        elif dir == "v":
            y += 1
        
        grid.add((x,y))
    
    return len(grid)

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
