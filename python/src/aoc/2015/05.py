from common import main

DAY = 5
YEAR = 2015
SAMPLE = """
ugknbfddgicrmopn
aaa
jchzalrnumimnmhp
haegwjzuvuyypxyu
dvszwmarrgswjxmb
"""

# nice nice rest naughty


"""
A nice string is one with all of the following properties:

- It contains at least three vowels (aeiou only), like aei, xazegov, or
aeiouaeiouaeiou.

- It contains at least one letter that appears twice in a row, like xx, abcdde
  (dd), or aabbccdd (aa, bb, cc, or dd).

- It does not contain the strings ab, cd, pq, or xy, even if they are part of
  one of the other requirements. For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a
double letter (...dd...), and none of the disallowed substrings. aaa is nice
because it has at least three vowels and a double letter, even though the
letters used by different rules overlap. jchzalrnumimnmhp is naughty because it
has no double letter. haegwjzuvuyypxyu is naughty because it contains the string
xy. dvszwmarrgswjxmb is naughty because it contains only one vowel. How many
strings are nice?
"""


def parse(puzzle_input):
    return puzzle_input.split("\n")


def part1(input):
    return sum(isNicePart1(s) for s in input)


def part2(input):
    return sum(isNicePart2(s) for s in input)


def isNicePart1(input):
    hasTwoInRow = False
    current = None
    for letter in input:
        if current == letter:
            hasTwoInRow = True
            break
        current = letter

    if hasTwoInRow == False:
        return False

    if len(list(filter(lambda l: l in "aeiou", input))) < 3:
        return False

    if "xy" in input or "ab" in input or "cd" in input or "pq" in input:
        return False

    return True


def isNicePart2(input):
    pairs = list(zip(input[:-1], input[1:]))
    has_non_overlapping_pair = False
    for i, pair in enumerate(pairs):
        non_overlapping_pairs = [
            pair for j, pair in enumerate(pairs) if j < i - 1 or j > i + 1
        ]
        if pair in non_overlapping_pairs:
            has_non_overlapping_pair = True
            break

    if not has_non_overlapping_pair:
        return False

    for tri in zip(input[:-2], input[1:-1], input[2:]):
        if tri[0] == tri[2]:
            return True

    return False


main(DAY, YEAR, SAMPLE, parse, part1, part2)
