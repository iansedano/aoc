import input
import bitsys


from debug import p
from pprint import pp


EX_01 = "D2FE28"

"""
110100101111111000101000
VVVTTTAAAAABBBBBCCCCC
The three bits labeled V (110) are the packet version, 6.
The three bits labeled T (100) are the packet type ID, 4, which means the packet is a literal value.
The five bits labeled A (10111) start with a 1 (not the last group, keep reading) and contain the first four bits of the number, 0111.
The five bits labeled B (11110) start with a 1 (not the last group, keep reading) and contain four more bits of the number, 1110.
The five bits labeled C (00101) start with a 0 (last group, end of packet) and contain the last four bits of the number, 0101.
The three unlabeled 0 bits at the end are extra due to the hexadecimal representation and should be ignored.
"""

EX_02 = "38006F45291200"

"""
00111000000000000110111101000101001010010001001000000000
VVVTTTILLLLLLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBBBBBB
The three bits labeled V (001) are the packet version, 1.
The three bits labeled T (110) are the packet type ID, 6, which means the packet is an operator.
The bit labeled I (0) is the length type ID, which indicates that the length is a 15-bit number representing the number of bits in the sub-packets.
The 15 bits labeled L (000000000011011) contain the length of the sub-packets in bits, 27.
The 11 bits labeled A contain the first sub-packet, a literal value representing the number 10.
The 16 bits labeled B contain the second sub-packet, a literal value representing the number 20.
"""

EX_03 = "EE00D40C823060"

"""
11101110000000001101010000001100100000100011000001100000
VVVTTTILLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCC
The three bits labeled V (111) are the packet version, 7.
The three bits labeled T (011) are the packet type ID, 3, which means the packet is an operator.
The bit labeled I (1) is the length type ID, which indicates that the length is a 11-bit number representing the number of sub-packets.
The 11 bits labeled L (00000000011) contain the number of sub-packets, 3.
The 11 bits labeled A contain the first sub-packet, a literal value representing the number 1.
The 11 bits labeled B contain the second sub-packet, a literal value representing the number 2.
The 11 bits labeled C contain the third sub-packet, a literal value representing the number 3.
"""

EX_04 = [
    # operator packet (version 4) which contains an operator packet (version 1)
    # which contains an operator packet (version 5) which contains a
    # literal value (version 6); this packet has a version sum of 16.
    "8A004A801A8002F478",
    # represents an operator packet (version 3) which contains two sub-packets;
    # each sub-packet is an operator packet that contains two literal values.
    # This packet has a version sum of 12.
    "620080001611562C8802118E34",
    # has the same structure as the previous example,
    # but the outermost packet uses a different length type ID.
    # This packet has a version sum of 23.
    "C0015000016115A2E0802F182340",
    # is an operator packet that contains an operator packet that contains an
    # operator packet that contains five literal values;
    # it has a version sum of 31.
    "A0016C880162017C3686B18A3D4780",
]


def test_input():
    bits = input.parse_hexadecimal(EX_01)
    assert bits == "110100101111111000101000"

    bits = input.parse_hexadecimal(EX_02)
    assert bits == "00111000000000000110111101000101001010010001001000000000"

    bits = input.parse_hexadecimal(EX_03)
    assert bits == "11101110000000001101010000001100100000100011000001100000"


test_input()


def test_part_1():
    """what do you get if you add up the version numbers in all packets?"""

    packet_1 = input.parse_hexadecimal(EX_01)
    bitsys.parse(packet_1)

    # packet_2 = input.parse_hexadecimal(EX_02)
    # bitsys.parse(packet_2)

    # packet_3 = input.parse_hexadecimal(EX_03)
    # bitsys.parse(packet_3)


test_part_1()


def test_part2():
    pass


# test_part2()
