import lanternfish_input

import laternfish_sim

SAMPLE = "3,4,3,1,2"


def test_parse_fish_sample():
    assert lanternfish_input.parse_fish(SAMPLE) == {
        0: 0,
        1: 1,
        2: 1,
        3: 2,
        4: 1,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
    }


def test_fish_sim_sample():
    fish_dict = lanternfish_input.parse_fish(SAMPLE)
    assert sum(laternfish_sim.simulate_fish(fish_dict, 18).values()) == 26
    assert sum(laternfish_sim.simulate_fish(fish_dict, 80).values()) == 5934
    assert sum(laternfish_sim.simulate_fish(fish_dict, 256).values()) == 26984457539


def test_part_1():
    fish_dict = lanternfish_input.parse_fish()
    assert sum(laternfish_sim.simulate_fish(fish_dict, 80).values()) == 349549
    assert sum(laternfish_sim.simulate_fish(fish_dict, 256).values()) == 1589590444365


test_part_1()  # 1544 too low
