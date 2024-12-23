from pprint import pp

import dot_fold
import input
from debug import p

EX_01 = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""


def test_input():
    dots, folds = input.parse_dots()


test_input()


def test_part_1():
    dots, folds = input.parse_dots(EX_01)
    dots = dot_fold.fold(dots, folds[0])
    assert len(dots) == 17

    dots, folds = input.parse_dots()
    dots = dot_fold.fold(dots, folds[0])
    assert len(dots) == 814


test_part_1()


def test_part_2():

    dots, folds = input.parse_dots()

    for fold in folds:
        dots = dot_fold.fold(dots, fold)

    dot_fold.print_dots(dots)


test_part_2()
