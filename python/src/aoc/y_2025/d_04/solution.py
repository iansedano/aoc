from aoc.tools.grid import create_grid_dict_from_string, get_ordinals


def parse(puzzle_input):
    return create_grid_dict_from_string(puzzle_input, ignore=".")


def part_1(parsed_input):
    grid = parsed_input

    accessible_rolls = 0

    for pos in grid.keys():
        ordinals = get_ordinals(pos)
        rolls = sum(1 if grid.get(ord) is not None else 0 for ord in ordinals)
        if rolls < 4:
            accessible_rolls += 1

    return accessible_rolls


def part_2(parsed_input):
    grid = parsed_input

    accessible_rolls = 0

    while True:
        rolls_removed_in_batch = 0
        keys_to_remove = []
        for pos in grid.keys():
            ordinals = get_ordinals(pos)
            rolls = sum(
                1 if grid.get(ord) is not None else 0 for ord in ordinals
            )
            if rolls < 4:
                rolls_removed_in_batch += 1
                keys_to_remove.append(pos)

        if rolls_removed_in_batch == 0:
            break

        accessible_rolls += rolls_removed_in_batch
        for key in keys_to_remove:
            grid.pop(key)

    return accessible_rolls
