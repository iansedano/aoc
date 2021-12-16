from debug import p
from pprint import pp


def bin_it_2_int(it):
    return int("".join(it), 2)


class Bit_gen:
    def __init__(self, bit_string):
        self._bit_string = (bit for bit in bit_string)
        self.counter = 0
        self.G = (bit for bit in bit_string)
        self.buffer = []

    def next(self):
        if len(self.buffer) > 0:
            return self.buffer.pop(0)
        else:
            return next(self.G, None)

    def peek(self, num):
        if len(self.buffer) > 0:
            raise Exception("Buffer already has elements inside")
        for _ in range(num):
            self.buffer.append(next(self.G, None))
        return self.buffer

    def get_bits(self, num) -> str:
        self.counter += num
        output = []
        for _ in range(num):
            output.append(self.next())
        return "".join(output)

    def get_int(self, num) -> int:
        """takes any given number of bits from a generator to return an int"""
        self.counter += num
        bin_list = self.get_bits(num)
        return bin_it_2_int(bin_list)


class Packet:
    def __init__(self, bit_gen, version, type, counter):
        self.bit_gen = bit_gen
        self.version = version
        self.type = type
        self.counter = counter

    def flush(self):
        num_to_flush = 4 - (self.counter % 4)
        flushed_bits = self.bit_gen.get_bits(num_to_flush)
        if "1" in flushed_bits:
            raise Exception(
                f"1 in flushed bits! Bit_gen_counter {self.bit_gen.counter}. Packet counter {self.counter}"
            )


class Literal_Value(Packet):
    def __init__(self, bit_gen: Bit_gen, version, type, counter):
        super().__init__(bit_gen, version, type, counter)
        self.value = self.parse_literal_bits()
        self.flush()

    def parse_literal_bits(self):
        int_sections = []
        last = False
        while last == False:
            continuation_bit = self.bit_gen.get_bits(1)
            if continuation_bit == "0":
                last = True
            int_sections.extend(self.bit_gen.get_bits(4))
            self.counter += 5
        self.literal_bits = bin_it_2_int(int_sections)
        return self.literal_bits


class Operator(Packet):
    def __init__(self, bit_gen: Bit_gen, version, type, counter):
        super().__init__(bit_gen, version, type, counter)
        self.length_type_id = self.bit_gen.get_bits(1)
        self.counter += 1
        p(self.length_type_id)

        if self.length_type_id == "0":
            length = self.bit_gen.get_int(15)
            self.counter += 15 + length
            p(length)
            self.sub_packet_string = self.bit_gen.get_bits(length)
            p(self.sub_packet_string)
            self.clear_trailing_zeros()

        elif self.length_type_id == "1":
            sub_packets_to_get = self.bit_gen.get_int(11)
            self.counter += 11
            self.sub_packet_list = []
            for _ in range(sub_packets_to_get):
                packet = self.bit_gen.get_bits(11)
                self.counter += 11
                self.sub_packet_list.append(packet)
            self.clear_trailing_zeros()

    def clear_trailing_zeros(self):
        while self.bit_gen.peek(1) != 1:
            self.bit_gen.get_bits(1)
        return


def process_packet(bit_gen):

    version = bit_gen.get_int(3)
    type = bit_gen.get_int(3)
    print(f"Packet version {version}, type {type}")

    if type == 4:
        P = Literal_Value(bit_gen, version, type, 6)
        p(P.value)

    else:
        P = Operator(bit_gen, version, type, 6)

    return P


def parse(bit_string: str):
    G = Bit_gen(bit_string)

    while True:
        try:
            process_packet(G)
        except TypeError:
            print("NO MORE BITS")
            break
