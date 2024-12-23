import itertools
from textwrap import dedent

from aocd import get_data

DAY = 2
YEAR = 2019
SAMPLE = dedent(
    """
    1,9,10,3,2,3,11,0,99,30,40,50
    """.strip()
)

OPCODES = {
    1: "add",
    2: "multiply",
    99: "stop",
}


def parse(puzzle_input):
    return [int(i) for i in puzzle_input.split(",")]


def part_1(parsed_input):
    program = list(parsed_input)
    parsed_input[1] = 12
    parsed_input[2] = 2

    run_program(program)

    return program[0]


def part_2(parsed_input):
    for noun, verb in itertools.product(range(100), range(100)):
        copied_program = list(parsed_input)
        copied_program[1] = noun
        copied_program[2] = verb
        run_program(copied_program)
        if copied_program[0] == 19690720:
            return 100 * noun + verb


def run_program(program):
    instruction_ptr = 0

    while True:
        current_op_code = OPCODES[program[instruction_ptr]]
        first_operand_idx = program[instruction_ptr + 1]
        second_operand_idx = program[instruction_ptr + 2]
        output_idx = program[instruction_ptr + 3]

        if current_op_code == "add":
            program[output_idx] = (
                program[first_operand_idx] + program[second_operand_idx]
            )
        elif current_op_code == "multiply":
            program[output_idx] = (
                program[first_operand_idx] * program[second_operand_idx]
            )
        elif current_op_code == "stop":
            break
        else:
            raise "INVALID OP CODE"
        instruction_ptr += 4
    return program


# 185500 too high

if __name__ == "__main__":
    data = get_data(day=DAY, year=YEAR).strip()
    parsed = parse(data)
    print(f"Part 1: {part_1(parsed)}")
    print(f"Part 2: {part_2(parsed)}")
