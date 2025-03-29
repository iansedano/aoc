from pprint import pp

from debug import p
from typ import Img, Point


class Enhancer:
    def __init__(self, img: Img, algo):
        self.fill = "."
        self.img = img
        self.count = 0
        self.algo = algo
        self.flipper = False
        if algo[0] == 1 and algo[511] == 0:
            self.flipper = True

    def execute(self):
        max_y, min_y, max_x, min_x = self.img.get_max_min_y_x()

        # Horrific magic numbers:
        max_y, min_y, max_x, min_x = (
            max_y + 2,
            min_y,
            max_x + 1,
            min_x - 1,
        )

        bin_reprs = {}

        for y in range(min_y, max_y):
            for x in range(min_x, max_x):

                num = self.img.get_bin_repr(Point(x, y))
                bin_reprs[Point(x, y)] = "#" if self.algo[num] == 1 else "."

        for point, value in bin_reprs.items():
            self.img[point] = value

        self.clear_border_artifact()

        max_y, min_y, max_x, min_x = self.img.get_max_min_y_x()

        if self.flipper == True:
            self.fill = "#" if self.fill == "." else "."
            self.img.fill = self.fill

        max_y, min_y, max_x, min_x = self.img.get_max_min_y_x()

    def clear_border_artifact(self):
        max_y, min_y, max_x, min_x = self.img.get_max_min_y_x()

        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x):
                if y == min_y + 1 or y == max_y or x == min_x or x == max_x - 1:
                    
                    # This is a hack because by accessing the point, it creates it,
                    # and then deletes it...which is totally pointless but I couldn't
                    # get it to work without it and don't have time to debug now.
                    self.img[Point(x, y)]
                    
                    del self.img[Point(x, y)]

    def count_pixels(self):

        return sum([1 if v == "#" else 0 for v in self.img.get_values()])
