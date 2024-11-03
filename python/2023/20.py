import math
from collections import deque

from common import main

DAY = 20
YEAR = 2023

SAMPLE = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""
SAMPLE_2 = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""


def parse(puzzle_input):
    modules = dict(parse_line(line) for line in puzzle_input.splitlines())

    output = None
    for sender, module in modules.items():
        for val in module["outputs"]:
            try:
                if modules[val]["type"] == "&":
                    modules[val]["inputs"].append((sender, "lo"))
            except KeyError:
                output = val
    return modules, output


def parse_line(line):
    module, outputs = line.split(" -> ")
    outputs = outputs.split(", ")
    if module.startswith("%"):
        return (
            module.strip("%"),
            {"type": "%", "outputs": outputs, "state": "off"},
        )
    elif module.startswith("&"):
        return (
            module.strip("&"),
            {"type": "&", "outputs": outputs, "inputs": []},
        )
    elif module.startswith("broadcaster"):
        return (
            module,
            {"type": "broadcaster", "outputs": outputs},
        )


def part1(parsed_input):
    modules, output = parsed_input

    # Simulate pulses keeping track of pulses sent
    pulses_sent = {"hi": 0, "lo": 0}
    pulses = deque()
    for _ in range(1000):
        pulses.append(("lo", "broadcaster", "button"))
        while pulses:
            pulse, module_key, sender = pulses.popleft()
            pulses_sent[pulse] += 1
            if module_key != output:
                new_pulses, updated_module = process_pulse(
                    pulse, module_key, modules[module_key], sender
                )
                modules[module_key] = updated_module
                pulses.extend(new_pulses)

    return pulses_sent["lo"] * pulses_sent["hi"]


def part2(parsed_input):
    modules, output = parsed_input

    # Work out where to calculate cycles from
    # Find "&" module connected to output and then use inputs to that "&" module
    modules_into_output = [
        (mod_key, module)
        for mod_key, module in modules.items()
        if output in module["outputs"]
    ]
    assert len(modules_into_output) == 1
    module_into_output = modules_into_output[0]
    assert module_into_output[1]["type"] == "&"
    cycles = {key: [] for key, _ in module_into_output[1]["inputs"]}

    # Simulate pulses keeping track of cycles
    pulses = deque()
    for i in range(10_000):  # 8k works but using 10k for redundancy
        pulses.append(("lo", "broadcaster", "button"))
        while pulses:
            pulse, module_key, sender = pulses.popleft()
            if sender in cycles and pulse == "hi":
                cycles[sender].append(i)

            if module_key != output:
                new_pulses, updated_module = process_pulse(
                    pulse, module_key, modules[module_key], sender
                )
                modules[module_key] = updated_module
                pulses.extend(new_pulses)

    return math.lcm(
        *(
            next(b - a for a, b in zip(cycle[:-1], cycle[1:]))
            for cycle in cycles.values()
        )
    )


def process_pulse(pulse, module_key, module, sender):
    outputs = module["outputs"]

    match module["type"]:
        case "broadcaster":
            return_pulses = [(pulse, o, module_key) for o in outputs]
            return_module = module

        case "%":
            if pulse == "lo":
                if module["state"] == "off":
                    return_pulses = [("hi", o, module_key) for o in outputs]
                    return_module = module | {"state": "on"}
                elif module["state"] == "on":
                    return_pulses = [("lo", o, module_key) for o in outputs]
                    return_module = module | {"state": "off"}
            else:
                return_pulses = []
                return_module = module

        case "&":
            updated_inputs = [
                (key, prev_pulse) if key != sender else (key, pulse)
                for key, prev_pulse in module["inputs"]
            ]
            if all(prev_pulse == "hi" for _, prev_pulse in updated_inputs):
                return_pulses = [("lo", o, module_key) for o in outputs]
            else:
                return_pulses = [("hi", o, module_key) for o in outputs]

            return_module = module | {"inputs": updated_inputs}

    return return_pulses, return_module


if __name__ == "__main__":
    main(DAY, YEAR, SAMPLE, parse, part1, part2)
