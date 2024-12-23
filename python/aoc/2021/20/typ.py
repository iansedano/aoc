from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

cardinals = [
    (-1, 1),
    (0, 1),
    (1, 1),
    (-1, 0),
    (0, 0),
    (1, 0),
    (-1, -1),
    (0, -1),
    (1, -1),
]


class Img:
    def __init__(self):
        self._ = {}
        self.fill = "."

    def __getitem__(self, index):

        if index in self._:
            return self._[index]
        else:
            if isinstance(index, Point):
                self._[index] = self.fill
                return self._[index]
            else:
                raise Exception("index must be Point")

    def __setitem__(self, index, value):
        if isinstance(index, Point):
            self._[index] = value
        else:
            raise Exception("index must be Point")

    def __delitem__(self, index):
        if isinstance(index, Point):
            del self._[index]
        else:
            raise Exception("index must be Point")

    def __repr__(self):
        max_y, min_y, max_x, min_x = self.get_max_min_y_x()

        output = []
        for y in range(max_y, min_y, -1):
            for x in range(min_x, max_x):
                output.append(self._[Point(x, y)])
            output.append("\n")

        return "".join(output)

    def get_surrounding(self, p: Point):
        output = []
        for t in cardinals:
            new_point = Point(p.x + t[0], p.y + t[1])
            output.append(self[new_point])

        return output

    def get_max_min_y_x(self):
        max_y = max([point.y for point in self._.keys()])
        min_y = min([point.y for point in self._.keys()]) - 1
        max_x = max([point.x for point in self._.keys()]) + 1
        min_x = min([point.x for point in self._.keys()])

        return max_y, min_y, max_x, min_x

    def get_bin_repr(self, p):
        surrounding_pixels = self.get_surrounding(p)

        bin_string = "".join(["1" if pix == "#" else "0" for pix in surrounding_pixels])

        return int(bin_string, 2)

    def get_keys(self):
        return self._.keys()

    def get_values(self):
        return self._.values()
