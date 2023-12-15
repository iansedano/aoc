from collections import defaultdict

from common import main

DAY = 15
YEAR = 2023
SAMPLE = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""


def parse(puzzle_input):
    return puzzle_input.split(",")


def part1(parsed_input):
    return sum(holiday_hash(s) for s in parsed_input)


def part2(parsed_input):
    boxes = defaultdict(list)
    for step in parsed_input:
        if "=" in step:
            label, focal_length = step.split("=")
            box = holiday_hash(label)
            boxes[box] = op_add(label, int(focal_length), boxes[box])
        elif "-" in step:
            label = step.strip("-")
            box = holiday_hash(label)
            boxes[box] = op_sub(label, boxes[box])

    focusing_power = 0
    for i, box in boxes.items():
        for j, (_, focal_length) in enumerate(box, 1):
            focusing_power += (i + 1) * j * focal_length
    return focusing_power


def op_add(label, focal_length, box):
    out = []
    op_complete = False
    for lb, f in box:
        if lb == label:
            out.append((label, focal_length))
            op_complete = True
        else:
            out.append((lb, f))
    if not op_complete:
        out.append((label, focal_length))
    return out


def op_sub(label, box):
    out = []
    for lb, f in box:
        if lb == label:
            continue
        else:
            out.append((lb, f))
    return out


def holiday_hash(str):
    """"""

    current_value = 0

    for char in str:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256

    return current_value


if __name__ == "__main__":
    main(DAY, YEAR, SAMPLE, parse, part1, part2)
