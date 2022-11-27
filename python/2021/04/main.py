import bingo_input
import bingo

from operator import itemgetter


numbers, bingo_cards = itemgetter("numbers", "bingo_cards")(
    bingo_input.parse_bingo_data()
)

winning_card, winning_number = bingo.get_bingo_winner(numbers, bingo_cards)

print(bingo.calculate_score(winning_card, winning_number))

losing_card, losing_number = bingo.get_bingo_loser(numbers, bingo_cards)

print(bingo.calculate_score(losing_card, losing_number))
