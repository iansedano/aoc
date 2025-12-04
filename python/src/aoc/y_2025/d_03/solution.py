def parse(puzzle_input):
    return [
        [int(battery) for battery in bank] for bank in puzzle_input.splitlines()
    ]


def part_1(parsed_input):
    return sum(get_highest_joltage(bank) for bank in parsed_input)


def get_highest_joltage(bank):
    """
    >>> get_highest_joltage([9,8,7,6,5,4,3,2,1,1,1,1,1,1,1])
    98
    >>> get_highest_joltage([8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9])
    89
    >>> get_highest_joltage([2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 7, 8])
    78
    >>> get_highest_joltage([8, 1, 8, 1, 8, 1, 9, 1, 1, 1, 1, 2, 1, 1, 1])
    92
    >>> get_highest_joltage([9, 9])
    99
    >>> get_highest_joltage([9, 8, 9])
    99
    """

    for x in range(9, 0, -1):
        if x not in bank[:-1]:
            continue

        found = None
        highest = -1
        for battery in bank:
            if battery == x and not found:
                found = True
                continue

            if found:
                highest = battery if battery > highest else highest

        return int(f"{x}{highest}")


def part_2(parsed_input):
    return sum(get_highest_joltage_plus(bank) for bank in parsed_input)


def get_highest_joltage_plus(bank):
    """
    >>> get_highest_joltage_plus([9,8,7,6,5,4,3,2,1,1,1,1,1,1,1])
    987654321111
    >>> get_highest_joltage_plus([8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9])
    811111111119
    >>> get_highest_joltage_plus([2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 7, 8])
    434234234278
    >>> get_highest_joltage_plus([8, 1, 8, 1, 8, 1, 9, 1, 1, 1, 1, 2, 1, 1, 1])
    888911112111
    >>> get_highest_joltage_plus([1,2,3,4,5,6,7,8,9,1,1,2,3,4,5,6])
    567891123456
    """
    length = 12
    output = [(-1, -1)] * length
    slots_left = length
    current_slot = 0
    current_idx = 0
    current_battery = bank[current_idx]

    while slots_left:
        if len(bank) - current_idx < slots_left:
            current_idx = output[current_slot][1] + 1
            current_slot += 1
            slots_left -= 1

            try:
                current_battery = bank[current_idx]
            except IndexError:
                break
            continue

        if current_battery > output[current_slot][0]:
            output[current_slot] = (current_battery, current_idx)

        current_idx += 1±±™¡
        if current_idx > len(bank) - 1:
            continue
        current_battery = bank[current_idx]

    return int("".join(str(x[0]) for x in output))


if __name__ == "__main__":
    get_highest_joltage_plus([8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9])
