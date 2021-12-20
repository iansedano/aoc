import input
import risk
from collections import Counter

from debug import p
from pprint import pp


EX_01 = """\
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

EX_02 = """\
19999
19111
11191"""

EX_03 = """\
19119999
19199999
19111111
11191991"""


def test_input():
    risk_map = input.parse_risk(EX_01)


test_input()


def test_part_1():
    risk_map = input.parse_risk(EX_01)
    assert risk.find_path(risk_map) == 40

    risk_map = input.parse_risk(EX_02)
    assert risk.find_path(risk_map) == 8

    risk_map = input.parse_risk(EX_03)
    assert risk.find_path(risk_map) == 12

    risk_map = input.parse_risk()
    assert risk.find_path(risk_map) == 435


test_part_1()


def test_part2():
    # risk_map = input.parse_risk(EX_01)
    # real_cave = risk.build_cave(risk_map)

    # risk.find_path(real_cave) == 315

    # risk_map = input.parse_risk(EX_02)
    # print(risk.find_path(risk_map))
    # real_cave = risk.build_cave(risk_map)

    # print(risk.find_path(real_cave))

    risk_map = input.parse_risk(EX_03)
    print(risk.find_path(risk_map))

    # risk_map = input.parse_risk()
    # real_cave = risk.build_cave(risk_map)
    # print("MAIN")
    # print(risk.find_path(real_cave))


# not 2846
test_part2()
