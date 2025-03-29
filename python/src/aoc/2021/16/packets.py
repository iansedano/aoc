from bitgen import Bit_gen, bin_it_2_int


class Packet:
    def __init__(self, bit_gen, version, type, counter):
        self.bit_gen = bit_gen
        self.version = version
        self.type = type
        self.counter = counter
        self.complete = False


class Literal_Value(Packet):
    def __init__(self, bit_gen: Bit_gen, version, type, counter):
        super().__init__(bit_gen, version, type, counter)
        self.parse_literal_bits()

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

    def calculate_value(self):
        if self.type == 0:
            """sum"""
            for child in self.children:
                if isinstance(child, Operator):
                    child.calculate_value()
            self.value = sum([child.value for child in self.children])
        elif self.type == 1:
            """product"""
            for child in self.children:
                if isinstance(child, Operator):
                    child.calculate_value()
            value = 1
            for child in self.children:
                value *= child.value
            self.value = value
        elif self.type == 2:
            """min"""
            for child in self.children:
                if isinstance(child, Operator):
                    child.calculate_value()
            self.value = min([child.value for child in self.children])
        elif self.type == 3:
            """max"""
            for child in self.children:
                if isinstance(child, Operator):
                    child.calculate_value()
            self.value = max([child.value for child in self.children])
        elif self.type == 5:
            """gt"""
            for child in self.children:
                if isinstance(child, Operator):
                    child.calculate_value()
            if self.children[0].value > self.children[1].value:
                self.value = 1
            else:
                self.value = 0
        elif self.type == 6:
            """lt"""
            for child in self.children:
                if isinstance(child, Operator):
                    child.calculate_value()
            if self.children[0].value < self.children[1].value:
                self.value = 1
            else:
                self.value = 0
        elif self.type == 7:
            """eq"""
            for child in self.children:
                if isinstance(child, Operator):
                    child.calculate_value()
            if self.children[0].value == self.children[1].value:
                self.value = 1
            else:
                self.value = 0


def process_packet(bit_gen):
    if bit_gen.done == True:
        return
    version = bit_gen.get_int(3)
    type = bit_gen.get_int(3)
    if version is None or type is None:
        return None

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
