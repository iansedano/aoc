import re

from common import main

DAY = 19
YEAR = 2015
SAMPLE = """"""


def parse(puzzle_input):
    replacements, start_molecule = puzzle_input.split("\n\n")

    replacements = [tuple(line.split(" => ")) for line in replacements.splitlines()]
    return replacements, start_molecule


def part1(parsed_input):
    replacements, start_molecule = parsed_input
    return len(get_all_morphs(start_molecule, replacements))


def part2(parsed_input):
    replacements, start_molecule = parsed_input

    replacements = sorted(
        replacements, key=lambda r: len(r[1]) - len(r[0]), reverse=True
    )

    output = start_molecule
    steps = 0

    while output != "e":
        for new, old in replacements:
            output, was_replaced = replace(old, new, output)
            if was_replaced:
                steps += 1
                break
    return steps


def get_all_morphs(molecule: str, replacements: tuple[str]):
    molecules = set()
    for a, b in replacements:
        for match in re.finditer(a, molecule):
            start, end = match.span()
            molecules.add(molecule[:start] + b + molecule[end:])
    return molecules


def replace(old, new, string):
    new_string = re.sub(old, new, string, 1)
    if new_string == string:
        return string, False
    return new_string, True


main(DAY, YEAR, SAMPLE, parse, part1, part2)
