"""
Drawing on solution by @gahjelle
"""

from common import main

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


def resolve(signals: dict, wires: dict):
    new_signals, unresolved = {}, {}
    for wire, (op, *args) in wires.items():
        if all(arg in signals for arg in args if isinstance(arg, str)):
            new_signals[wire] = OPS[op](*(signals.get(arg, arg) for arg in args))
        else:
            unresolved[wire] = (op, *args)

    return signals | new_signals, unresolved


def part1(input):
    signals, wires = {}, input

    while "a" not in signals:
        signals, wires = resolve(signals, wires)

    return signals["a"]


def part2(input):
    signals, wires = {}, input | {"b": ("SET", part1(input))}
    while "a" not in signals:
        signals, wires = resolve(signals, wires)

    return signals["a"]


main(DAY, YEAR, SAMPLE, parse, part1, part2)
