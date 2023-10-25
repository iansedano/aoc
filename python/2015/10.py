from common import main


DAY = 10
YEAR = 2015
SAMPLE = ""


def parse(puzzle_input):
    return puzzle_input


def look_and_say(input):
    """
    >>> look_and_say("1")
    '11'
    >>> look_and_say("11")
    '21'
    >>> look_and_say("21")
    '1211'
    >>> look_and_say("1211")
    '111221'
    >>> look_and_say("111221")
    '312211'
    """
    input_iter = iter(input.strip())

    output = []
    first_number = next(input_iter, False)
    current_number = first_number
    current_run = 1

    while number := next(input_iter, False):
        if current_number == number:
            current_run += 1
        else:
            output.extend([str(current_run), current_number])
            current_number = number
            current_run = 1
    output.extend([str(current_run), current_number])

    return "".join(output)


def part1(input):
    seq = input

    for _ in range(40):
        seq = look_and_say(seq)
    return len(seq)


def part2(input):
    seq = input

    for _ in range(50):
        seq = look_and_say(seq)
    return len(seq)


main(DAY, YEAR, SAMPLE, parse, part1, part2)
