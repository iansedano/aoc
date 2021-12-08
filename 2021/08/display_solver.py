display = set[str]
display_data = list[display]
real_display = list[int]

NUMBERS = {
    (0, 1, 2, 4, 5, 6): 0,
    (2, 5): 1,
    (0, 2, 3, 4, 6): 2,
    (0, 2, 3, 5, 6): 3,
    (1, 2, 3, 5): 4,
    (0, 1, 3, 5, 6): 5,
    (0, 1, 3, 4, 5, 6): 6,
    (0, 2, 5): 7,
    (0, 1, 2, 3, 4, 5, 6): 8,
    (0, 1, 2, 3, 5, 6): 9,
}


def get_symmetric_diff(sets: list[set, set, set]):
    a = sets[0].symmetric_difference(sets[1])
    b = sets[1].symmetric_difference(sets[2])
    c = sets[0].symmetric_difference(sets[2])

    d = set.union(a, b)
    return set.union(d, c)


class Display_solver:
    """
    0:      1:      2:      3:      4:
     aaaa    ....    aaaa    aaaa    ....
    b    c  .    c  .    c  .    c  b    c
    b    c  .    c  .    c  .    c  b    c
     ....    ....    dddd    dddd    dddd
    e    f  .    f  e    .  .    f  .    f
    e    f  .    f  e    .  .    f  .    f
     gggg    ....    gggg    gggg    ....

      5:      6:      7:      8:      9:
     aaaa    aaaa    aaaa    aaaa    aaaa
    b    .  b    .  .    c  b    c  b    c
    b    .  b    .  .    c  b    c  b    c
     dddd    dddd    ....    dddd    dddd
    .    f  e    f  .    f  e    f  .    f
    .    f  e    f  .    f  e    f  .    f
     gggg    gggg    ....    gggg    gggg"""

    def __init__(self, data: tuple[display_data, display_data]):
        #                                   a, b, c, d, e, f, g
        self.real_display: real_display = [0, 0, 0, 0, 0, 0, 0]
        """
         0000
        1    2
        1    2
         3333
        4    5
        4    5
         6666
        """

        self.number_set: list[display]
        self.display: list[display]
        self.number_set, self.display = data

        self.segment_map: dict[int, display | 0] = {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0,
        }

        self.process_number_set()

        self.part_1 = self.get_number_part_1()

    def process_number_set(self):
        self.number_set.sort(key=len)
        self.segment_map[1] = self.number_set[0]
        self.segment_map[7] = self.number_set[1]
        self.segment_map[4] = self.number_set[2]
        self.segment_map[8] = self.number_set[-1]

        # two_three_five = self.number_set[3:6]

        zero_six_nine = self.number_set[6:9]

        self.real_display[0] = self.segment_map[7] - self.segment_map[1]

        temp_segment_2_5 = self.segment_map[1]
        temp_segment_1_3 = self.segment_map[4] - self.segment_map[1]
        temp_segment_4_6 = self.segment_map[8] - (
            set.union(self.segment_map[4], self.segment_map[7])
        )

        zero_six_nine_diff = get_symmetric_diff(zero_six_nine)

        self.real_display[2] = zero_six_nine_diff.intersection(temp_segment_2_5)
        self.real_display[5] = temp_segment_2_5 - self.real_display[2]

        self.real_display[3] = zero_six_nine_diff.intersection(temp_segment_1_3)
        self.real_display[1] = temp_segment_1_3 - self.real_display[3]

        self.real_display[4] = zero_six_nine_diff.intersection(temp_segment_4_6)
        self.real_display[6] = temp_segment_4_6 - self.real_display[4]

        real_display_list = list(map(lambda x: "".join(x), self.real_display))

        self.real_display = {letter: i for i, letter in enumerate(real_display_list)}

    def get_number_part_1(self):

        how_many = [d if d in self.segment_map.values() else None for d in self.display]
        return len(list(filter(None, how_many)))

    def get_display_number(self):
        display_number = []
        for display in self.display:
            display_number.append(self.find_number(display))

        display_number = int("".join([str(i) for i in display_number]))

        return display_number

    def find_number(self, letters):
        encoding = [self.real_display[letter] for letter in letters]
        encoding = tuple(sorted(encoding))
        return NUMBERS[encoding]
