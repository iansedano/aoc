from debug import p
from pprint import pp


def bin_it_2_int(it):
    return int("".join(it), 2)


class Bit_gen:
    def __init__(self, bit_string):
        if bit_string == None or bit_string == "":
            self.done = True
            return
        self._bit_string = (bit for bit in bit_string)
        self.counter = 0
        self.G = (bit for bit in bit_string)
        self.buffer = []
        self.done = False

    def next(self):
        if len(self.buffer) > 0:
            return self.buffer.pop(0)
        else:
            return next(self.G, None)

    def get_bits(self, num) -> str:
        if self.done == True:
            return None
        self.counter += num
        output = []
        for _ in range(num):
            next_bit = self.next()
            if next_bit is None:
                self.done = True
                return "".join(output)
            output.append(next_bit)
        return "".join(output)

    def peek(self, num):
        if len(self.buffer) > 0:
            raise Exception("Buffer already has elements inside")
        for _ in range(num):
            self.buffer.append(self.get_bits(1))
        if self.done == True:
            self.buffer = []
            return [None]
        return self.buffer

    def get_int(self, num) -> int:
        """takes any given number of bits from a generator to return an int"""
        self.counter += num
        bin_list = self.get_bits(num)
        if self.done:
            return None
        return bin_it_2_int(bin_list)


class Packet:
    def __init__(self, bit_gen, version, type, counter):
        self.bit_gen = bit_gen
        self.version = version
        self.type = type
        self.counter = counter
        self.complete = False

    # def flush(self):
    #     num_to_flush = 4 - (self.counter % 4)
    #     flushed_bits = self.bit_gen.get_bits(num_to_flush)
    #     if "1" in flushed_bits:
    #         raise Exception(
    #             f"1 in flushed bits! Bit_gen_counter {self.bit_gen.counter}. Packet counter {self.counter}"
    #         )


class Literal_Value(Packet):
    def __init__(self, bit_gen: Bit_gen, version, type, counter):
        super().__init__(bit_gen, version, type, counter)
        self.parse_literal_bits()
        # self.flush()

    def parse_literal_bits(self):
        int_sections = []
        last = False
        while last == False:
            continuation_bit = self.bit_gen.get_bits(1)
            if continuation_bit == "0":
                last = True
            int_sections.extend(self.bit_gen.get_bits(4))
            self.counter += 5
        self.value = bin_it_2_int(int_sections)
        self.complete = True


class Operator(Packet):
    def __init__(self, bit_gen: Bit_gen, version, type, counter):
        super().__init__(bit_gen, version, type, counter)
        self.children = []
        self.length_type_id = self.bit_gen.get_bits(1)
        self.counter += 1

        if self.length_type_id == "0":
            self.process_type_0()

        elif self.length_type_id == "1":
            self.process_type_1()

    def process_type_0(self):
        length = self.bit_gen.get_int(15)
        if length is None:
            return
        self.counter += 15 + length
        self.sub_packet_string = self.bit_gen.get_bits(length)
        # self.clear_trailing_zeros()

        if self.sub_packet_string is None:
            self.sub_packet_string = ""

        self.children.extend(parse(self.sub_packet_string))
        self.complete = True

    def process_type_1(self):
        sub_packets_to_get = self.bit_gen.get_int(11)
        if sub_packets_to_get is None:
            return
        self.counter += 11

        for _ in range(sub_packets_to_get):
            self.children.append(process_packet(self.bit_gen))
        self.complete = True

    # def clear_trailing_zeros(self):
    #     print("clearing zeros till reaching bit")
    #     peek = self.bit_gen.peek(1)

    #     while peek[0] != 1 and peek[0] is not None:
    #         self.bit_gen.get_bits(1)
    #         peek = self.bit_gen.peek(1)


def process_packet(bit_gen):

    if bit_gen.done == True:
        return

    version = bit_gen.get_int(3)
    type = bit_gen.get_int(3)

    if version is None or type is None:
        return None

    # if version == 0 and type == 0:
    #     return None

    if type == 4:

        packet = Literal_Value(bit_gen, version, type, 6)

    else:

        packet = Operator(bit_gen, version, type, 6)

    if packet.complete:
        return packet
    else:
        return None


def parse(bit_string: str):

    if sum([int(b) for b in bit_string]) == 0:
        return

    G = Bit_gen(bit_string)

    if G is None:
        return

    packets = []

    while G.done == False:
        new_packet = process_packet(G)
        if new_packet:
            packets.append(new_packet)

    return packets


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
