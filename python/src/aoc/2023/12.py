import re
from functools import cache

from common import main

DAY = 12
YEAR = 2023
SAMPLE = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


def parse(puzzle_input):
    return [
        (
            (split := line.split())[0],  #  springs i.e. "???.###""
            tuple(
                int(i) for i in split[1].split(",")
            ),  #  groups i.e. (1, 1, 3)
        )
        for line in puzzle_input.splitlines()
    ]


def part1(parsed_input):
    return sum(get_combos(springs, groups) for springs, groups in parsed_input)


def part2(parsed_input):
    unfolded = [
        (
            ((springs + "?") * 5)[:-1],
            groups * 5,
        )
        for springs, groups in parsed_input
    ]
    return part1(unfolded)


@cache
def get_combos(springs, groups):
    if not springs and not groups:
        return 1

    if len(springs) < sum(groups) + len(groups) - 1 or not groups:
        return 0

    if springs.startswith(".") or springs.endswith("."):
        return get_combos(springs.strip("."), groups)

    if springs.startswith("?"):
        rest = springs[1:]
        return get_combos("#" + rest, groups) + get_combos(rest, groups)

    if springs.endswith("?"):
        rest = springs[:-1]
        return get_combos(rest + "#", groups) + get_combos(rest, groups)

    g = groups[0]
    if re.match(rf"^#[#?]{{{g-1}}}(?:[?.]|$)", springs):
        rest = springs[g + 1 :]
        return get_combos(rest, groups[1:])

    return 0


if __name__ == "__main__":
    main(DAY, YEAR, SAMPLE, parse, part1, part2)
