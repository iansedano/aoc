from pprint import pp

from debug import p
from typ import Point, Report, Target, Vector


def compare_pos_with_target(pos: Point, target: Target) -> Report:
    report = {
        "x_left": target.top_left.x - pos.x,
        "x_right": target.bottom_right.x - pos.x,
        "y_top": target.top_left.y - pos.y,
        "y_bottom": target.bottom_right.y - pos.y,
    }

    if report["x_right"] < 0 or report["y_bottom"] > 0:
        report["missed"] = True
    else:
        report["missed"] = False

    if (
        report["x_right"] >= 0
        and report["y_bottom"] <= 0
        and report["x_left"] <= 0
        and report["y_top"] >= 0
    ):
        report["hit"] = True
    else:
        report["hit"] = False

    return report


def tick(p: Point, v: Vector) -> tuple[Point, Vector]:
    new_p = Point(p.x + v.x, p.y + v.y)
    new_v = Vector(v.x - 1 if v.x > 0 else 0, v.y - 1)

    return (new_p, new_v)


def launch(vec: Vector, target: Target) -> tuple[list[Point], list[Report]]:
    position: Point = Point(0, 0)

    report = compare_pos_with_target(position, target)

    pos_log = [position]
    report_log = [report]

    while report["hit"] == False and report["missed"] == False:
        position, vec = tick(position, vec)
        pos_log.append(position)
        report = compare_pos_with_target(position, target)
        report_log.append(report)

    return pos_log, report_log


def print_traj(pos_log, target):
    padding = 50
    min_max_x = (0, max([pos.x for pos in pos_log]) + padding)
    min_max_y = (
        min([pos.y for pos in pos_log]) - padding,
        max([pos.y for pos in pos_log]) + padding,
    )

    grid = {x: {y: "." for y in range(*min_max_y)} for x in range(*min_max_x)}

    for pos in pos_log:
        grid[pos.x][pos.y] = "#"

    for pos in target:
        grid[pos.x][pos.y] = "X"

    for x, y in grid.items():
        for point in y.values():
            print(point, end="")
        print("\n", end="")


def get_min_vx_range(left_x, right_x):
    min_vel = get_min_vx(left_x)
    distance = triangular_num(min_vel)
    max_vel = min_vel
    while distance < right_x:
        max_vel += 1
        distance = triangular_num(max_vel)

    return range(min_vel, right_x + 1)


def get_min_vx(left_x):
    vel = 0
    distance = 0
    while distance < left_x:
        vel += 1
        distance = triangular_num(vel)
    return vel


def triangular_num(num):
    return (num * (num + 1)) / 2
