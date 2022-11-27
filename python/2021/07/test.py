import crab_input
import crab_aligner

SAMPLE = "16,1,2,0,4,2,7,1,2,14"
SAMPLE_2 = "0,0,0,0,1,1,1,1,4,4,4,4,5,5,5,5"
SAMPLE_3 = "0,0,0,4,4,4,8,8,8,20"


def test_sample_part_1():
    crab_positions = crab_input.parse_crabs(SAMPLE)
    assert crab_positions == [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

    fuel_spent = crab_aligner.align_crabs(crab_positions)
    assert fuel_spent == 37


def test_custom_sample_part_1():
    crab_positions = crab_input.parse_crabs(SAMPLE_2)
    assert crab_positions == [0, 0, 0, 0, 1, 1, 1, 1, 4, 4, 4, 4, 5, 5, 5, 5]

    fuel_spent = crab_aligner.align_crabs(crab_positions)
    assert fuel_spent == 32


def test_custom_sample2_part_1():
    crab_positions = crab_input.parse_crabs(SAMPLE_3)
    assert crab_positions == [0, 0, 0, 4, 4, 4, 8, 8, 8, 20]

    fuel_spent = crab_aligner.align_crabs(crab_positions)
    assert fuel_spent == 40


def test_calc_fuel():
    assert crab_aligner.calc_fuel_cost(5) == 15
    assert crab_aligner.calc_fuel_cost(11) == 66
    assert crab_aligner.calc_fuel_cost(9) == 45
    assert crab_aligner.calc_fuel_cost(1) == 1


def test_part_1():
    crab_positions = crab_input.parse_crabs()
    fuel_spent = crab_aligner.align_crabs(crab_positions)
    assert fuel_spent == 341534


def test_part_2():
    crab_positions = crab_input.parse_crabs()
    fuel_spent = crab_aligner.align_crabs_new_cost(crab_positions)
    assert fuel_spent == 93397632


# test_calc_fuel()
test_part_2()
