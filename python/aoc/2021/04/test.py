from operator import itemgetter
from pprint import pp

import bingo
import bingo_input


def test_card_builder():
    test_input = """ 3 55 15 54 81
56 77 20 99 25
90 57 67  0 97
28 45 69 84 14
91 94 39 36 85"""

    assert bingo_input.parse_bingo_card(test_input) == [
        [3, 55, 15, 54, 81],
        [56, 77, 20, 99, 25],
        [90, 57, 67, 0, 97],
        [28, 45, 69, 84, 14],
        [91, 94, 39, 36, 85],
    ]


def test_sample_case():
    test_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

    numbers, bingo_cards = itemgetter("numbers", "bingo_cards")(
        bingo_input.parse_bingo_data(test_input)
    )

    winning_card, winning_number = bingo.get_bingo_winner(numbers, bingo_cards)
    assert bingo.calculate_score(winning_card, winning_number) == 4512

    losing_card, losing_number = bingo.get_bingo_loser(numbers, bingo_cards)

    assert bingo.calculate_score(losing_card, losing_number) == 1924


test_sample_case()
