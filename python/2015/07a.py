from common import main
from collections import defaultdict
from pprint import pp

DAY = 7
YEAR = 2015
SAMPLE = """\
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i"""


"""
AND
OR
NOT
LSHIFT
RSHIFT
val
"""


def OP_LSHIFT(x, times):
    """
    >>> OP_LSHIFT(123, 2)
    492
    """
    return (x << times) & 0xFFFF


def OP_RSHIFT(x, times):
    """
    >>> OP_RSHIFT(456, 2)
    114
    """
    return (x >> times) & 0xFFFF


def OP_AND(x, y):
    """
    >>> OP_AND(123, 456)
    72
    """
    return (x & y) & 0xFFFF


def OP_OR(x, y):
    """
    >>> OP_OR(123, 456)
    507
    """
    return (x | y) & 0xFFFF


def OP_NOT(x):
    """
    >>> OP_NOT(123)
    65412
    >>> OP_NOT(456)
    65079
    """
    return (~x) & 0xFFFF


OPS = {
    "LSHIFT": OP_LSHIFT,
    "RSHIFT": OP_RSHIFT,
    "AND": OP_AND,
    "OR": OP_OR,
    "NOT": OP_NOT,
    "SET": lambda val: val,
}


def parse(puzzle_input: str):
    return dict(parse_line(line) for line in puzzle_input.splitlines())


def parse_line(line: str):
    instruction, wire = line.split(" -> ")
    match instruction.split():
        case [left, op, right]:
            return wire, (op, maybe_int(left), maybe_int(right))
        case [op, left]:
            return wire, (op, maybe_int(left))
        case [val]:
            return wire, ("SET", maybe_int(val))
        case _:
            raise ValueError("Invalid line")


def maybe_int(value: str):
    return int(value) if value.isnumeric() else value


def build_system(input: dict):
    system = {}
    for wire, (op, *args) in input.items():
        system[wire] = create_callback(wire, system, op, *args)
    return system


def create_callback(caller, system, op, *args):
    cache = None

    def callback():
        nonlocal cache
        if cache:
            return cache
        if op == "SET" and type(args[0]) is int:
            return args[0]
        resolved_args = [system[arg]() if type(arg) is str else arg for arg in args]
        result = OPS[op](*resolved_args)
        cache = result
        return result

    return callback


def part1(input):
    return build_system(input)["a"]()


def part2(input):
    wire_a = part1(input)
    return build_system(input | {"b": ("SET", wire_a)})["a"]()


main(DAY, YEAR, SAMPLE, parse, part1, part2)
