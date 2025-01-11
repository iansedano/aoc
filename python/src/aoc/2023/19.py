import math
from operator import gt, lt

from common import main
from parse import compile

DAY = 19
YEAR = 2023
SAMPLE = """\
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""


def parse(puzzle_input):
    workflows, parts = puzzle_input.split("\n\n")
    workflows = dict(parse_workflow(line) for line in workflows.splitlines())
    parts = [parse_parts(line) for line in parts.splitlines()]
    return workflows, parts


WORKFLOW_LINE_PATTERN = compile("{key}{{{rules}}}")
RULE_PATTERN = compile("{attr:w}{op}{amount:d}:{target}")


def parse_workflow(line):
    line_parse_result = WORKFLOW_LINE_PATTERN.parse(line)

    rules = []
    for potential_rule in line_parse_result["rules"].split(","):
        if rule_parse_result := RULE_PATTERN.parse(potential_rule):
            rules.append(
                (
                    rule_parse_result["attr"],
                    rule_parse_result["op"],
                    rule_parse_result["amount"],
                    rule_parse_result["target"],
                )
            )
        else:
            rules.append((None, None, None, potential_rule))

    return (line_parse_result["key"], rules)


def parse_parts(line):
    return dict(
        (
            (a := attr.split("="))[0],
            int(a[1]),
        )
        for attr in line.strip("{}").split(",")
    )


def rule_creator(attr, op, amount):
    if attr is None:
        return lambda part: True
    if op == ">":
        return lambda part: gt(part[attr], amount)
    elif op == "<":
        return lambda part: lt(part[attr], amount)


def part1(parsed_input):
    workflows, parts = parsed_input
    accepted = []
    part_q = list(parts)

    while part_q:
        part = part_q.pop()

        rule_key = "in"
        while rule_key not in ("R", "A"):
            rules = workflows[rule_key]
            any(
                rule_key := target
                for attr, op, limit, target in rules
                if rule_creator(attr, op, limit)(part)
            )

        if rule_key == "A":
            accepted.append(part)

    return sum(sum(part.values()) for part in accepted)


def part2(parsed_input):
    workflows, _ = parsed_input

    valid_parts = {
        "x": (1, 4001),
        "m": (1, 4001),
        "a": (1, 4001),
        "s": (1, 4001),
    }

    return get_valid_combos("in", workflows, valid_parts)


def get_valid_combos(workflow_key, workflows, parts):
    valid_parts = 0
    for attr, op, limit, target in workflows[workflow_key]:
        accepted = True if target == "A" else False
        rejected = True if target == "R" else False

        if attr is None:  # no rule, just direct all remaining
            valid_parts += (
                math.prod(stop - start for start, stop in parts.values())
                if accepted
                else 0
                if rejected
                else get_valid_combos(target, workflows, parts)
            )
            return valid_parts

        p_range = parts[attr]

        if op == ">":
            w_range = (limit, 4001)
        elif op == "<":
            w_range = (1, limit)

        if w_range[0] >= p_range[1] or w_range[1] <= p_range[0]:
            continue

        left = p_range[0], max(w_range[0], p_range[0])
        redirect_range = max(w_range[0], p_range[0]), min(
            p_range[1], w_range[1]
        )
        right = min(p_range[1], w_range[1]), p_range[1]

        if op == ">":
            leftover_range = left[0], left[1] + 1
            redirect_range = redirect_range[0] + 1, redirect_range[1]
        elif op == "<":
            leftover_range = right

        redirect_parts = parts | {attr: redirect_range}
        valid_parts += (
            math.prod(stop - start for start, stop in redirect_parts.values())
            if accepted
            else 0
            if rejected
            else get_valid_combos(target, workflows, redirect_parts)
        )

        parts = parts | {attr: leftover_range}
    return valid_parts


if __name__ == "__main__":
    main(DAY, YEAR, SAMPLE, parse, part1, part2)
