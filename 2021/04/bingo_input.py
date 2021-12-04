from pathlib import Path
import re
from debug import p


def get_info_from_file(path=Path(Path(__file__).parent, "input.txt")):
    with open(path, mode="r") as f:
        return f.read()


def parse_bingo_data(raw_string=get_info_from_file()):
    data = raw_string.strip().split("\n\n")
    raw_numbers = data[0]
    raw_bingo_cards = data[1:]

    numbers = [int(num) for num in raw_numbers.strip().split(",")]

    bingo_cards = list(map(lambda card: parse_bingo_card(card), raw_bingo_cards))

    return {"numbers": numbers, "bingo_cards": bingo_cards}


def parse_bingo_card(raw_bingo_data):
    lines = raw_bingo_data.strip().split("\n")
    raw_card = [re.split(r"\s+", line.strip()) for line in lines]
    card = list(map(lambda row: list(map(lambda num: int(num.strip()), row)), raw_card))

    return card
