from pathlib import Path

from debug import p
from pprint import pp


def get_info_from_file(path=Path(Path(__file__).parent, "input.txt")):
    with open(path, mode="r") as f:
        return f.read()


def parse_risk(raw_string=get_info_from_file()):

    return [[int(n) for n in line.strip()] for line in raw_string.strip().split()]
