from pathlib import Path

THIS_DIR = Path(__file__).parent


def build_empty_flag_dict(length):
    flags = {}
    for i in range(length):
        b = "0b" + i * "0" + "1" + (length - 1 - i) * "0"
        flags[int(b, 2)] = [0, 0]
    return flags


def build_flag_dict(bin_nums, length):
    flags = build_empty_flag_dict(length)

    for num in bin_nums:
        for flag in flags.keys():
            if num & flag:
                flags[flag][0] += 1
            else:
                flags[flag][1] += 1

    return flags


def part1(lines):
    bin_nums = [int(f"0b{line.strip()}", 2) for line in lines]
    length = len(lines[0])

    flags = build_flag_dict(bin_nums, length)

    gamma, epsilon = "0b", "0b"

    for flag, counts in flags.items():
        if counts[0] > counts[1]:
            gamma += "1"
            epsilon += "0"
        elif counts[0] < counts[1]:
            gamma += "0"
            epsilon += "1"

    gamma, epsilon = int(gamma, 2), int(epsilon, 2)
    return gamma * epsilon


def padded_bin_num(num, length):
    bnum = bin(num)
    pad = length - len(bnum[2:])
    output = bnum[:2] + pad * "0" + bnum[2:]
    return output


def binary_flip(num, length):
    b_num = padded_bin_num(num, length)
    binary = b_num[2:]
    flipped = "0b" + "".join(["1" if bit == "0" else "0" for bit in binary])
    return int(flipped, 2)


def part2(lines):
    bin_nums = [int(f"0b{line.strip()}", 2) for line in lines]

    length = len(lines[0])
    flags = build_flag_dict(bin_nums, length)

    oxy_nums = []
    co2_nums = []

    position = 0
    for index, items in enumerate(flags.items()):

        flag, count = items
        invert_flag = binary_flip(flag, length)

        if index == 0:

            if count[0] >= count[1]:
                oxy_flag = (flag, 0)
                co2_flag = (invert_flag, 1)

            else:
                oxy_flag = (invert_flag, 1)
                co2_flag = (flag, 0)

            if oxy_flag[1] == 0:
                oxy_nums = list(filter(lambda num: oxy_flag[0] & num, bin_nums))
                co2_nums = list(filter(lambda num: num == co2_flag[0] & num, bin_nums))
            if oxy_flag[1] == 1:
                oxy_nums = list(filter(lambda num: num == oxy_flag[0] & num, bin_nums))
                co2_nums = list(filter(lambda num: co2_flag[0] & num, bin_nums))

        if index > 0:

            if len(oxy_nums) != 1:
                oxy_flags = build_flag_dict(oxy_nums, length)

                oxy_flag, oxy_count = list(oxy_flags.items())[index]

                if oxy_count[0] >= oxy_count[1]:
                    oxy_mask = (oxy_flag, 0)
                else:
                    oxy_mask = (binary_flip(oxy_flag, length), 1)

                if oxy_mask[1] == 0:
                    oxy_nums = list(filter(lambda num: oxy_mask[0] & num, oxy_nums))
                else:
                    oxy_nums = list(
                        filter(lambda num: num == oxy_mask[0] & num, oxy_nums)
                    )

            if len(co2_nums) != 1:
                co2_flags = build_flag_dict(co2_nums, length)

                co2_flag, co2_count = list(co2_flags.items())[index]

                if co2_count[0] >= co2_count[1]:
                    co2_mask = (binary_flip(co2_flag, length), 1)
                else:
                    co2_mask = (co2_flag, 0)

                if co2_mask[1] == 0:
                    co2_nums = list(filter(lambda num: co2_mask[0] & num, co2_nums))
                if co2_mask[1] == 1:
                    co2_nums = list(
                        filter(lambda num: num == co2_mask[0] & num, co2_nums)
                    )

        print(
            "lists",
            [padded_bin_num(num, length) for num in oxy_nums],
            [padded_bin_num(num, length) for num in co2_nums],
        )

    if len(oxy_nums) != 1 or len(co2_nums) != 1:
        print("BAD RESULT")
    oxy_nums = oxy_nums[0]
    co2_nums = co2_nums[0]
    print("oxy and co2", oxy_nums, co2_nums)
    return oxy_nums * co2_nums


def solve():

    with open(Path(THIS_DIR, "03-input.txt"), mode="r") as f:
        text = f.read().strip()
        lines = text.split("\n")
        # print(part1(lines))

        print("PART 2", part2(lines))
