import display_input
import display_solver

SAMPLE_01 = """acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"""
SAMPLE_02 = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""


def test_parse():

    data = display_input.parse_display_data(SAMPLE_02)


def test_sample_part_1():
    data = display_input.parse_display_data(SAMPLE_02)

    sum = 0
    for line in data:
        solver = display_solver.Display_solver(line)
        sum += solver.part_1

    assert sum == 26


def test_part_1():
    data = display_input.parse_display_data()

    sum = 0
    for line in data:
        solver = display_solver.Display_solver(line)
        sum += solver.part_1

    assert sum == 381


def test_sample_01():

    data = display_input.parse_display_data(SAMPLE_01)

    solver = display_solver.Display_solver(data[0])

    assert solver.get_display_number() == 5353


def test_sample_02_part_2():
    data = display_input.parse_display_data(SAMPLE_02)
    sum = 0
    for line in data:
        solver = display_solver.Display_solver(line)
        sum += solver.get_display_number()

    assert sum == 61229


def test_part_2():
    data = display_input.parse_display_data()
    sum = 0
    for line in data:
        solver = display_solver.Display_solver(line)
        sum += solver.get_display_number()

    return sum


print(test_part_2())
