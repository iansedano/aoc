from debug import p
from pprint import pp


def print_packets(packets, tab_level=0):

    for packet in packets:
        for _ in range(tab_level):
            print("\t", end="")
        print(packet)
        if hasattr(packet, "children"):
            print_packets(packet.children, tab_level + 1)


def add_version(packets):

    version_sum = 0

    for packet in packets:
        version_sum += packet.version
        if hasattr(packet, "children"):
            version_sum += add_version(packet.children)

    return version_sum


def calculate_value(packet):
    def helper(packet):
        if packet.type == 0:
            """sum"""

        elif packet.type == 1:
            """product"""
        elif packet.type == 2:
            """min"""
        elif packet.type == 3:
            """max"""
        elif packet.type == 5:
            """gt"""
        elif packet.type == 6:
            """lt"""
        elif packet.type == 7:
            """eq"""
