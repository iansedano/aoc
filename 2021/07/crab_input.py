from pathlib import Path

from debug import p


def get_info_from_file(path=Path(Path(__file__).parent, "input.txt")):
    with open(path, mode="r") as f:
        return f.read()


def parse_crabs(raw_string=get_info_from_file()) -> list[int]:
    """
    Return a list of numbers of horizontal crab positions
    """
    return [int(num) for num in raw_string.strip().split(",")]
