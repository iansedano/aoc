from aocd import get_data

DAY = 1
YEAR = 2019
SAMPLE = """12
14
1969
100756"""


def parse(puzzle_input):
    return [line.strip() for line in puzzle_input.split("\n")]


def part_1(parsed_input):
    return sum(get_fuel(int(mass)) for mass in parsed_input)


def part_2(parsed_input):
    return sum(get_fuel_plus(int(mass)) for mass in parsed_input)


def get_fuel(mass):
    mass = mass // 3 - 2
    return mass if mass >= 0 else 0


def get_fuel_plus(mass):
    remaining_mass = mass
    total_fuel = 0

    while remaining_mass:
        fuel_mass = get_fuel(remaining_mass)
        total_fuel += fuel_mass
        remaining_mass = fuel_mass

    return total_fuel


if __name__ == "__main__":
    data = get_data(day=DAY, year=YEAR).strip()
    parsed = parse(data)
    print(f"Part 1: {part_1(parsed)}")
    print(f"Part 2: {part_2(parsed)}")
