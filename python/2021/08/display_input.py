from pathlib import Path

from debug import p

display_data = list[set[str]]


def get_info_from_file(path=Path(Path(__file__).parent, "input.txt")):
    with open(path, mode="r") as f:
        return f.read()


def parse_display_data(
    raw_string=get_info_from_file(),
):
    """
    Return a list of numbers of horizontal crab positions
    """
    lines = raw_string.strip().split("\n")
    strings = [
        tuple(
            [set(letters) for letters in data.split(" ")] for data in line.split(" | ")
        )
        for line in lines
    ]

    return strings
