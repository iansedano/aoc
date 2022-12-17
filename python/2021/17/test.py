from pprint import pp

import probe
from debug import p
from typ import Point, Report, Target, Vector

sample_01: Target = Target(Point(20, -5), Point(30, -10))


target: Target = Target(Point(265, -58), Point(287, -103))


def test_part_1():
    launch_vec_1 = Vector(7, 2)
    launch_vec_2 = Vector(6, 3)
    launch_vec_3 = Vector(9, 0)
    launch_vec_4 = Vector(8, 0)
    launch_vec_5 = Vector(6, 9)
    # pos_log, report_log = probe.launch(launch_vec_1, sample_01)
    # p(pos_log)
    # pos_log, report_log = probe.launch(launch_vec_2, sample_01)
    # p(pos_log)
    # pos_log, report_log = probe.launch(launch_vec_3, sample_01)
    # p(pos_log)
    # pos_log, report_log = probe.launch(launch_vec_4, sample_01)
    # p(pos_log)
    pos_log, report_log = probe.launch(launch_vec_5, sample_01)
    print("MAX HEIGHT", max([pos.y for pos in pos_log]))
    print(report_log[-1])
    probe.print_traj(pos_log, sample_01)


# test_part_1()


def part_part_1_2():

    x_range = probe.get_min_vx_range(20, 30)
    p(x_range)
    max_height = 0

    for x in x_range:
        for y in range(20):
            launch_vec = Vector(x, y)
            pos_log, report_log = probe.launch(launch_vec, sample_01)
            hits = [report["hit"] for report in report_log]
            hit = any(hits)
            if hit:
                max_h_traj = max([pos.y for pos in pos_log])
                if max_height < max_h_traj:
                    max_height = max_h_traj
                    print("\n====NEW MAX HEIGHT=====")
                    print(f"==== {max_height} =====")
                    print("LAUNCH VEC", launch_vec)
                    probe.print_traj(pos_log, sample_01)

    x_range = probe.get_min_vx_range(265, 287)
    max_height = 0

    for x in x_range:
        for y in range(1000):
            launch_vec = Vector(x, y)
            pos_log, report_log = probe.launch(launch_vec, target)
            hits = [report["hit"] for report in report_log]
            hit = any(hits)
            if hit:
                max_h_traj = max([pos.y for pos in pos_log])
                if max_height < max_h_traj:
                    max_height = max_h_traj
                    print("\n====NEW MAX HEIGHT=====")
                    print(f"==== {max_height} =====")
                    print("LAUNCH VEC", launch_vec)


# part_part_1_2()


def part_part_2():

    x_range = probe.get_min_vx_range(20, 30)
    p(x_range)
    hit_vecs = []

    for x in x_range:
        for y in range(-20, 20):
            launch_vec = Vector(x, y)
            pos_log, report_log = probe.launch(launch_vec, sample_01)
            hits = [report["hit"] for report in report_log]
            hit = any(hits)
            if hit:
                hit_vecs.append(launch_vec)
    print(len(hit_vecs))

    x_range = probe.get_min_vx_range(265, 287)
    p(x_range)
    hit_vecs = []

    for x in x_range:
        for y in range(-200, 120):
            launch_vec = Vector(x, y)
            pos_log, report_log = probe.launch(launch_vec, target)
            hits = [report["hit"] for report in report_log]
            hit = any(hits)
            if hit:
                hit_vecs.append(launch_vec)

    print(len(hit_vecs))


part_part_2()
