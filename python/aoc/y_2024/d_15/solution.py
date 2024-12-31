import itertools
from collections import defaultdict
from textwrap import dedent

import peek
from aocd import get_data


DIRS = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0),
}


def parse(puzzle_input):
    warehouse, steps = puzzle_input.split("\n\n")
    warehouse_lines = warehouse.splitlines()[1:-1]
    steps = list(itertools.chain.from_iterable(steps.splitlines()))

    return (
        warehouse_lines,
        steps,
    )


def part_1(parsed_input):
    warehouse_lines, steps = parsed_input

    grid = {}
    position = None
    shape = (len(warehouse_lines), len(warehouse_lines[0][1:-1]))
    walls = set()
    boxes = set()

    for y, row in list(enumerate(warehouse_lines)):
        for x, cell in list(enumerate(row[1:-1])):
            if cell == "@":
                position = (x, y)
                continue
            if cell != ".":
                grid[(x, y)] = cell
                if cell == "#":
                    walls.add((x, y))
                elif cell == "O":
                    boxes.add((x, y))

    character = position

    for step in steps:
        peek.enabled = False
        peek("===NEW STEP===")

        peek(character, step)
        direction = DIRS[step]
        next_character_pos = add_tuple(character, direction)
        stack = []
        next_stack_pos = next_character_pos
        while True:
            if (
                next_stack_pos in walls
                or not (0 <= next_stack_pos[0] < shape[0])
                or not (0 <= next_stack_pos[1] < shape[1])
            ):
                stack.append(("#", next_stack_pos))
                break

            if next_stack_pos not in boxes:
                stack.append((".", next_stack_pos))
                break
            else:
                stack.append(("O", next_stack_pos))

            next_stack_pos = add_tuple(next_stack_pos, direction)
        peek(stack)

        # debug(shape, walls, boxes, character)

        if stack[-1][0] == ".":
            character = next_character_pos
            new_box_positions = set()

            for char, box_pos in stack[:-1]:
                if char != "O":
                    raise SystemExit("Something went wrong")
                new_box_positions.add(add_tuple(box_pos, direction))

            boxes = (boxes - {b[1] for b in stack}) | new_box_positions

    return sum(box[0] + 1 + (box[1] + 1) * 100 for box in boxes)


def add_tuple(a, b):
    return a[0] + b[0], a[1] + b[1]


def part_2(parsed_input):
    peek.enabled = True
    warehouse_lines, steps = parsed_input

    warehouse_lines = [
        line[1:-1]
        .replace("#", "##")
        .replace(".", "..")
        .replace("@", "@.")
        .replace("O", "[]")
        for line in warehouse_lines
    ]

    position = None
    shape = (len(warehouse_lines[0]), len(warehouse_lines))

    walls = set()
    boxes = set()

    for y, row in list(enumerate(warehouse_lines)):
        for x, cell in list(enumerate(row)):
            if cell == "@":
                position = (x, y)
                continue
            if cell != ".":
                if cell == "#":
                    walls.add((x, y))
                elif cell == "[":
                    boxes.add(((x, y), (x + 1, y)))

    character = position

    for step in steps:

        peek.enabled = True
        peek("===NEW STEP===")
        debug_b(shape, walls, boxes, character)
        peek(character, step)

        direction = DIRS[step]
        next_character_pos = add_tuple(character, direction)
        stack = []
        leading_edge = (next_character_pos,)

        peek(leading_edge)

        while True:
            if (
                any(pos in walls for pos in leading_edge)
                or not any(0 <= pos[0] < shape[0] for pos in leading_edge)
                or not any(0 <= pos[1] < shape[1] for pos in leading_edge)
            ):
                stack.append(("#", leading_edge))
                break

            boxes_hit = set()

            for box in boxes:
                if any(pos in box for pos in leading_edge):
                    boxes_hit.add(box)

            peek(boxes_hit)

            if any(
                pos not in itertools.chain.from_iterable(boxes)
                for pos in leading_edge
            ):
                stack.append((".", leading_edge))
                break
            else:
                stack.append(("O", leading_edge))
            peek(stack)

            # next_stack_pos = add_tuple(next_stack_pos, direction)

        if stack[-1][0] == ".":
            character = next_character_pos
            new_box_positions = set()

            for char, box_pos in stack[:-1]:
                if char != "O":
                    raise SystemExit("Something went wrong")
                new_box_positions.add(add_tuple(box_pos, direction))

            boxes = (boxes - {b[1] for b in stack}) | new_box_positions

    return sum(box[0] + 1 + (box[1] + 1) * 100 for box in boxes)


def debug_a(shape, walls, boxes, position):
    for y in range(-1, shape[1] + 1, 1):
        for x in range(-1, shape[0] + 1, 1):
            if x in [-1, shape[0]] or y in [-1, shape[1]]:
                print("#", end="")
            elif (x, y) in walls:
                print("#", end="")
            elif (x, y) in boxes:
                print("O", end="")
            elif (x, y) == position:
                print("@", end="")
            else:
                print(".", end="")
        print("")
    print("")


def debug_b(shape, walls, boxes, position):
    for y in range(-1, shape[1] + 1):
        for x in range(-1, shape[0] + 1):
            if x in [-1, shape[0]] or y in [-1, shape[1]]:
                print("#", end="")
            elif (x, y) in walls:
                print("#", end="")
            elif ((x, y), (x + 1, y)) in boxes:
                print("[", end="")
            elif ((x - 1, y), (x, y)) in boxes:
                print("]", end="")
            elif (x, y) == position:
                print("@", end="")
            else:
                print(".", end="")
        print("")
    print("")


if __name__ == "__main__":
    data = get_data(day=DAY, year=YEAR).strip()
    parsed = parse(SAMPLE)
    print(f"Part 1: {part_1(parsed)}")
    print(f"Part 2: {part_2(parsed)}")
