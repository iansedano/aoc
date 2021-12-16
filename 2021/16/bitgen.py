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
