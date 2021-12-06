from pathlib import Path

from debug import p


def get_info_from_file(path=Path(Path(__file__).parent, "input.txt")):
    with open(path, mode="r") as f:
        return f.read()


def parse_fish(raw_string=get_info_from_file()) -> dict[int, int]:
    """
    Return a dictionary with the fish internal timer as key
    and the frequency of fish with that timer as value
    """
    fish = [int(fish) for fish in raw_string.strip().split(",")]

    output = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    for f in fish:
        output[f] += 1

    return output
