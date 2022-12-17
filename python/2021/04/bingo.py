from dataclasses import dataclass
from pathlib import PurePath

from debug import p


@dataclass
class card_position:
    number: int
    called: bool


class Card:
    def __init__(self, card: list[list[int]]):
        self.card = self.init_card(card)
        self.won = False

    def init_card(self, card: list[list[int]]):
        return list(
            map(lambda row: list(map(lambda num: card_position(num, False), row)), card)
        )

    def hear_number(self, num: int):
        for i, row in enumerate(self.card):
            for j, position in enumerate(row):
                if position.number == num:
                    position.called = True
                    if self.check_bingo(i, j) == True:
                        self.won = True
                        return "BINGO"
                    else:
                        return

    def check_bingo(self, row_index, col_index):

        row = self.card[row_index]
        col = list(map(lambda row: row[col_index], self.card))

        row_called = list(map(lambda card_pos: card_pos.called, row))
        col_called = list(map(lambda card_pos: card_pos.called, col))

        if all(row_called) or all(col_called):
            return True
        else:
            return False

    def get_unmarked_numbers(self):
        output = []

        for row in self.card:
            for position in row:
                if position.called == False:
                    output.append(position.number)

        return output


def convert_2d_list_to_card_list(input):
    return list(map(lambda num_array: Card(num_array), input))


def get_bingo_winner(numbers, bingo_cards: list[list[int]]):

    cards: list[list[Card]] = convert_2d_list_to_card_list(bingo_cards)

    for num in numbers:
        for card in cards:
            if card.hear_number(num) == "BINGO":
                return card, num


def card_filter(card, number):
    if card.hear_number(number) == "BINGO":
        return False
    return True


def get_bingo_loser(numbers, bingo_cards: list[list[int]]):
    cards: list[list[Card]] = convert_2d_list_to_card_list(bingo_cards)
    cards_remaining = list(cards)
    number_gen = (number for number in numbers)
    current_number = next(number_gen, None)

    while current_number is not None:

        if len(cards_remaining) > 1:
            cards_remaining = list(
                filter(lambda card: card_filter(card, current_number), cards_remaining)
            )
        else:
            losing_card = cards_remaining[0]
            if losing_card.hear_number(current_number) == "BINGO":
                return losing_card, current_number

        current_number = next(number_gen, None)

    return None, None


def calculate_score(card: Card, num):
    return sum(card.get_unmarked_numbers()) * num
