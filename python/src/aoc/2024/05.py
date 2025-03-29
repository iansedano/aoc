from collections import defaultdict
from textwrap import dedent

from aocd import get_data

DAY = 5
YEAR = 2024
SAMPLE = dedent(
    """\
    47|53
    97|13
    97|61
    97|47
    75|29
    61|13
    75|53
    29|13
    97|29
    53|29
    61|53
    97|53
    61|29
    47|13
    75|47
    97|75
    47|61
    75|61
    47|29
    75|13
    53|13

    75,47,61,53,29
    97,61,53,29,13
    75,29,13
    75,97,47,61,53
    61,13,29
    97,13,75,29,47
    """
)


def parse(puzzle_input):
    ordering_rules, updates = puzzle_input.split("\n\n")
    ordering_rules = [
        tuple(int(part) for part in rule.split("|"))
        for rule in ordering_rules.splitlines()
    ]

    letters_before = defaultdict(set)
    for rule in ordering_rules:
        letters_before[rule[1]].add(rule[0])

    updates = [
        [int(u) for u in update.split(",")] for update in updates.splitlines()
    ]

    return letters_before, updates


def part_1(parsed_input):
    letters_before, updates = parsed_input

    sum = 0
    for update in updates:
        if is_update_ordered(update, letters_before):
            sum += find_middle(update)

    return sum


def part_2(parsed_input):
    letters_before, updates = parsed_input

    sum = 0
    for update in updates:
        if not is_update_ordered(update, letters_before):
            sum += find_middle(order_update(update, letters_before))
    return sum


def find_middle(iterable):
    return iterable[len(iterable) // 2]


def is_update_ordered(update, letters_before):
    for i, page_number in enumerate(update):
        if not all(
            pages in letters_before[page_number] for pages in update[:i]
        ):
            return False
    return True


def order_update(update, letters_before):
    ordered_update: list = update[:1]

    for update_page_no in update[1:]:
        inserted = False
        for i, new_page in enumerate(ordered_update):
            if update_page_no in letters_before[new_page]:
                ordered_update.insert(i, update_page_no)
                inserted = True
                break
        if not inserted:
            ordered_update.append(update_page_no)

    return ordered_update


if __name__ == "__main__":
    data = get_data(day=DAY, year=YEAR).strip()
    parsed = parse(data)
    print(f"Part 1: {part_1(parsed)}")
    print(f"Part 2: {part_2(parsed)}")
