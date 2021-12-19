import input
import snail
import ex
import json

from debug import p
from pprint import pp


def test_parse():
    snail_nums = input.parse_snail_nums()

    pp(snail_nums)


# test_parse()


def test_part_1():

    # assert snail.explode_once(json.loads("[[[[[9,8],1],2],3],4]")) == json.loads(
    #     "[[[[0,9],2],3],4]"
    # )

    # assert snail.explode_once(json.loads("[7,[6,[5,[4,[3,2]]]]]")) == json.loads(
    #     "[7,[6,[5,[7,0]]]]"
    # )

    # assert snail.explode_once(json.loads("[[6,[5,[4,[3,2]]]],1]")) == json.loads(
    #     "[[6,[5,[7,0]]],3]"
    # )

    # assert snail.explode_once(
    #     json.loads("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]")
    # ) == json.loads("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]")

    # split_1 = snail.split_large_num([[[[0, 7], 4], [15, [0, 13]]], [1, 1]])
    # split_2 = snail.split_large_num(split_1)

    # assert split_2 == [
    #     [[[0, 7], 4], [[7, 8], [0, [6, 7]]]],
    #     [1, 1],
    # ]

    """"""

    # snum = snail.build_snum("[[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]]")
    # print(snum.toJSON())
    # print([p.value for p in snum.get_list_of_P_ints()])
    # exploders = snum.get_next_exploder_snums()

    # print("EXPLODERS", [e.toList() for e in exploders])

    # for e in exploders:
    #     print("EXPLODING")
    #     e.explode()
    #     print(snum.toJSON())

    # print("SPLITTING")
    # snum.split_first_large_num()

    # exploders = snum.get_next_exploder_snums()
    # print("EXPLODERS", [e.toList() for e in exploders])

    # print(snum.toJSON())

    # snum = snail.process("[[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]]")

    # assert snum.toList() == [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]

    snum = snail.process_lines(
        "[[[[4, 3], 4], 4], [7, [[8, 4], 9]]]\n[1, 1]".split("\n")
    )
    assert snum.toList() == [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]

    processed = snail.process_lines(ex.ex_02[0].split("\n"))
    assert processed.toList() == [[[[1, 1], [2, 2]], [3, 3]], [4, 4]]

    processed = snail.process_lines(ex.ex_03[0].split("\n"))
    assert processed.toList() == json.loads(ex.ex_03[1])

    processed = snail.process_lines(ex.ex_04[0].split("\n"))
    assert processed.toList() == json.loads(ex.ex_04[1])

    processed = snail.process_lines(ex.ex_05[0].strip().split("\n"))
    assert processed.toList() == json.loads(ex.ex_05[1])

    processed = snail.process_lines(ex.ex_homework.strip().split("\n"))
    assert processed.toList() == json.loads(ex.ex_homework_final)
    assert processed.calculate_magnitude() == ex.ex_homework_mag

    processed = snail.process_lines(input.parse_snail_nums())
    assert processed.calculate_magnitude() == 4347


test_part_1()


def test_part_2():
    largest_mag = snail.find_largest_pair(ex.ex_homework.strip().split("\n"))
    print("LARGEST MAG", largest_mag)

    largest_mag = snail.find_largest_pair(input.parse_snail_nums())
    print("LARGEST MAG", largest_mag)


test_part_2()
