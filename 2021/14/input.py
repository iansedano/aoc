from pathlib import Path

from debug import p
from pprint import pp


def get_info_from_file(path=Path(Path(__file__).parent, "input.txt")):
    with open(path, mode="r") as f:
        return f.read()


def parse_template(raw_string=get_info_from_file()):

    chain, rules = raw_string.strip().split("\n\n")

    chain = [base for base in chain.strip()]

    rules = [[r for r in line.split(" -> ")] for line in rules.strip().split("\n")]

    rules = {tuple(pair): value for pair, value in rules}

    return chain, rules
