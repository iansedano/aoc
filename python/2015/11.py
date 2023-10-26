from common import main
from contextlib import suppress

DAY = 11
YEAR = 2015
SAMPLE = ""


def is_pass_valid(password):
    """
    Must contain increasing straight
    Can't contain i, o, l
    Must contain two different non overlapping pairs

    >>> is_pass_valid("hijklmmn")
    False
    >>> is_pass_valid("abbceffg")
    False
    >>> is_pass_valid("abbcegjk")
    False
    >>> is_pass_valid("abcdffaa")
    True
    >>> is_pass_valid("ghjaabcc")
    True
    """

    if any(char in password for char in ["i", "l", "o"]):
        return False

    return contains_straight(password) and contains_pairs(password)


def contains_straight(password):
    """
    >>> contains_straight("abc")
    True
    >>> contains_straight("efg")
    True
    >>> contains_straight("hij")
    True
    >>> contains_straight("aaaaaabc")
    True
    >>> contains_straight("aaaa")
    False
    """
    for a, b, c in zip(password[:-2], password[1:-1], password[2:]):
        if ord(a) == ord(b) - 1 == ord(c) - 2:
            return True

    return False


def contains_pairs(password):
    """
    >>> contains_pairs("aabb")
    True
    >>> contains_pairs("aajkjdflkbb")
    True
    >>> contains_pairs("safsdaabb")
    True
    >>> contains_pairs("sadfasdaaasdfasbb")
    True
    >>> contains_pairs("asdfbb")
    False
    >>> contains_pairs("asdddfb")
    False
    """
    pass_iter = iter(ord(char) for char in password)
    prev = None
    first_pair_ord = None
    while char := next(pass_iter, False):
        if char == prev:
            if first_pair_ord is None:
                first_pair_ord = char
                prev = None
            elif first_pair_ord == char:
                continue
            else:
                return True
        prev = char
    return False


def increment_password(password):
    """
    >>> increment_password("abc")
    'abd'
    >>> increment_password("abz")
    'aca'
    >>> increment_password("zzz")
    'aaa'
    """
    new_password = [*password[:-1], increment_letter(password[-1])]
    wrap_around = new_password[-1] == "a"
    index = -2
    with suppress(IndexError):
        while wrap_around:
            new_password[index] = increment_letter(new_password[index])
            wrap_around = new_password[index] == "a"
            index -= 1
    return "".join(new_password)


def increment_letter(char):
    """
    >>> increment_letter("a")
    'b'
    >>> increment_letter("b")
    'c'
    >>> increment_letter("z")
    'a'
    """
    return chr(((ord(char) - 96) % 26) + 97)


def parse(puzzle_input):
    return puzzle_input


def part1(input):
    while not is_pass_valid(input):
        input = increment_password(input)
    return input


def part2(input):
    return part1(increment_password(part1(input)))


main(DAY, YEAR, SAMPLE, parse, part1, part2)
