import itertools

from aoc.tools.peek import peek
from aoc.tools.grid import create_grid_dict_from_string
from aoc.tools.vector import Vec2

DIRS = {
    "^": Vec2(0, -1),
    ">": Vec2(1, 0),
    "v": Vec2(0, 1),
    "<": Vec2(-1, 0),
}


def parse(puzzle_input):
    warehouse, steps = puzzle_input.split("\n\n")
    steps = list(itertools.chain.from_iterable(steps.splitlines()))
    return warehouse, steps


def parse_part_1(warehouse_lines):
    grid = create_grid_dict_from_string(warehouse_lines)
    walls, boxes, character = set(), set(), None
    for pos, char in grid.items():
        if char == "#":
            walls.add(pos)
        elif char == "O":
            boxes.add(pos)
        elif char == "@":
            character = pos

    return walls, boxes, character


def parse_part_2(warehouse_lines):
    grid = create_grid_dict_from_string(warehouse_lines, ignore={"."})
    walls, boxes, character = set(), set(), None
    for pos, char in grid.items():
        if char == "#":
            walls.add(pos)
        elif char == "[":
            boxes.add((pos, pos + (1, 0)))
        elif char == "@":
            character = pos

    return walls, boxes, character


def get_boxes_part_1(position, direction, boxes, walls):
    new_position = add_tuple(position, direction)
    if position in boxes:
        return [position, *get_boxes_part_1(new_position, direction, boxes, walls)]
    if position in walls:
        return ["#"]
    return ["."]


def get_boxes_part_2(position, direction, boxes, walls):
    new_position = position + direction
    peek(new_position)
    if direction.y == 0:
        if box := next((box for box in boxes if new_position in box), None):
            peek(box)
            return {
                box,
                *get_boxes_part_2(new_position + direction, direction, boxes, walls),
            }
        return set()
    next_box = next((box for box in boxes if new_position in box), None)
    if next_box:
        return {
            next_box,
            *{
                box
                for pos in next_box
                for box in get_boxes_part_2(pos, direction, boxes, walls)
            },
        }
    return set()


def move_boxes_part_1(
    character,
    direction,
    boxes,
    walls,
):
    next_character_position = add_tuple(character, direction)
    box_row = get_boxes_part_1(next_character_position, direction, boxes, walls)
    peek(box_row)
    if box_row[-1] == "#":
        return character, boxes
    return add_tuple(character, direction), (
        (boxes - set(box_row[:-1])) | {add_tuple(b, direction) for b in box_row[:-1]}
    )


def part_1(parsed_input):
    warehouse_lines, steps = parsed_input
    walls, boxes, character = parse_part_1(warehouse_lines)
    for step in steps:
        peek(step, character)
        debug_a((9, 9), walls, boxes, character)
        character, boxes = move_boxes_part_1(
            character,
            DIRS[step],
            boxes,
            walls,
        )
    return sum(box[0] + box[1] * 100 for box in boxes)


def add_tuple(a, b):
    return a[0] + b[0], a[1] + b[1]


def part_2(parsed_input):
    peek.enabled = True
    warehouse_lines, steps = parsed_input
    warehouse_lines = expand_warehouse(warehouse_lines)
    walls, boxes, character = parse_part_2(warehouse_lines)
    peek(walls, boxes, character)
    debug_b((30, 50), walls, boxes, character)
    for direction in steps:
        dir = DIRS[direction]
        peek(direction)
        boxes_to_move = get_boxes_part_2(character, dir, boxes, walls)
        peek(boxes_to_move)
        if (
            all(p + dir not in walls for box in boxes_to_move for p in box)
            and character + dir not in walls
        ):
            character = character + dir
            boxes = (boxes - boxes_to_move) | {
                (box[0] + dir, box[1] + dir) for box in boxes_to_move
            }
        debug_b((30, 50), walls, boxes, character)
    peek(boxes)
    return sum((box[0][0] + box[0][1] * 100) for box in boxes)


def expand_warehouse(lines):
    return (
        lines.replace("#", "##")
        .replace(".", "..")
        .replace("@", "@.")
        .replace("O", "[]")
    )


def debug_a(shape, walls, boxes, position):
    for y in range(-1, shape[1] + 1, 1):
        for x in range(-1, shape[0] + 1, 1):
            if (x, y) in walls:
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
    for y in range(shape[0]):
        for x in range(shape[1]):
            if (x, y) in walls:
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
