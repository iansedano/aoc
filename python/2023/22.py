from collections import deque

from common import main

DAY = 22
YEAR = 2023
SAMPLE = """\
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""


def parse(puzzle_input):
    return let_bricks_fall(
        [
            tuple(
                tuple(int(p) for p in coord.split(","))  # (x, y, z)
                for coord in line.split("~")
            )
            for line in puzzle_input.splitlines()
        ]
    )


def part1(parsed_input):
    brick_dict = parsed_input

    bricks_can_be_disintegrated = 0
    for idx, brick in brick_dict.items():
        if all(
            any(
                supported_brick_id in other_brick["supporting"]
                for jdx, other_brick in brick_dict.items()
                if jdx != idx
            )
            for supported_brick_id in brick["supporting"]
        ):
            bricks_can_be_disintegrated += 1

    return bricks_can_be_disintegrated


def part2(parsed_input):
    brick_dict = parsed_input

    bricks_falling = 0
    for idx, brick in brick_dict.items():
        disintegrated_bricks = {idx}
        bricks_to_process = deque()
        bricks_to_process.extend(brick["supporting"])
        while bricks_to_process:
            top_brick_id = bricks_to_process.popleft()
            top_brick = brick_dict[top_brick_id]
            if all(
                b_id in disintegrated_bricks for b_id in top_brick["resting_on"]
            ):
                disintegrated_bricks.add(top_brick_id)
                bricks_to_process.extend(top_brick["supporting"])
        bricks_falling += len(disintegrated_bricks) - 1

    return bricks_falling


def let_bricks_fall(bricks):
    stack = []

    bricks = sorted(bricks, key=lambda pair: pair[0][2])
    stack.append(lay_brick_on(bricks[0], ((0, 0, 0), (0, 0, 0))))
    for brick in bricks[1:]:
        possible_bricks = sorted(
            [b for b in stack if brick_can_rest_on_top(brick, b)],
            key=lambda b: b[1][2],
            reverse=True,
        )

        if possible_bricks:
            brick = lay_brick_on(brick, possible_bricks[0])
            stack.append(brick)
        else:
            brick = lay_brick_on(brick, ((0, 0, 0), (0, 0, 0)))
            stack.append(brick)

    numbered_stack = [(i, brick) for i, brick in enumerate(stack)]
    brick_dict = {
        i: {"brick": brick, "resting_on": [], "supporting": []}
        for i, brick in numbered_stack
    }

    for i, brick in numbered_stack:
        for j, brick_over in numbered_stack:
            if is_brick_resting_on(brick_over, brick):
                brick_dict[i]["supporting"].append(j)
                brick_dict[j]["resting_on"].append(i)
                continue

    return brick_dict


def is_brick_resting_on(a, b):
    """Assumes lower end of brick is always first, i.e. ((_, _, 1), (_, _, 2))"""

    (_, _, a_s_z), _ = a
    _, (_, _, b_e_z) = b

    return brick_can_rest_on_top(a, b) and a_s_z - 1 == b_e_z


def lay_brick_on(a, b):
    """Assumes lower end of brick is always first, i.e. ((_, _, 1), (_, _, 2))
    Assumes bricks can overlap at all (x or y of bricks overlap)
    Assumes brick a is over brick b (higher z)
    """
    (a_s_x, a_s_y, a_s_z), (a_e_x, a_e_y, a_e_z) = a
    _, (_, _, b_e_z) = b
    diff = a_s_z - b_e_z - 1

    return (a_s_x, a_s_y, a_s_z - diff), (a_e_x, a_e_y, a_e_z - diff)


def brick_can_rest_on_top(a, b):
    (a_s_x, a_s_y, _), (a_e_x, a_e_y, _) = a
    (b_s_x, b_s_y, _), (b_e_x, b_e_y, _) = b

    a_x = (a_s_x, a_e_x) if a_s_x <= a_e_x else (a_e_x, a_s_x)
    a_y = (a_s_y, a_e_y) if a_s_y <= a_e_y else (a_e_y, a_s_y)

    b_x = (b_s_x, b_e_x) if b_s_x <= b_e_x else (b_e_x, b_s_x)
    b_y = (b_s_y, b_e_y) if b_s_y <= b_e_y else (b_e_y, b_s_y)

    return closed_range_overlap(a_x, b_x) and closed_range_overlap(a_y, b_y)


def closed_range_overlap(a, b):
    return a[0] <= b[1] and b[0] <= a[1]


if __name__ == "__main__":
    main(DAY, YEAR, SAMPLE, parse, part1, part2)
