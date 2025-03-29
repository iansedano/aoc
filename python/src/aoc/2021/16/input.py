from pathlib import Path
from pprint import pp

from debug import p


def get_info_from_file(path=Path(Path(__file__).parent, "input.txt")):
    with open(path, mode="r") as f:
        return f.read()


HEX = {
    "0" : "0000",
    "1" : "0001",
    "2" : "0010",
    "3" : "0011",
    "4" : "0100",
    "5" : "0101",
    "6" : "0110",
    "7" : "0111",
    "8" : "1000",
    "9" : "1001",
    "A" : "1010",
    "B" : "1011",
    "C" : "1100",
    "D" : "1101",
    "E" : "1110",
    "F" : "1111"
}

def parse_hexadecimal(raw_string=get_info_from_file()):
    return "".join([HEX[char] for char in raw_string.strip()])
