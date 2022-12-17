from pathlib import Path
from pprint import pp

import snail
from debug import p


def get_info_from_file(path=Path(Path(__file__).parent, "input.txt")):
    with open(path, mode="r") as f:
        return f.read()


def parse_snail_nums(raw_string=get_info_from_file()):
    lines = raw_string.strip().split("\n")

    return lines
