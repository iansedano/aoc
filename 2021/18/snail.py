import json
import re

from debug import p
from pprint import pp

import math


class Node:
    def find_leaf(self):
        current = self

        if isinstance(current, P_int):
            current = current.parent

        while not current.is_leaf():
            if isinstance(current.left, S_num):
                current = current.left
            elif isinstance(current.right, S_num):
                current = current.right


class P_int(Node):
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent

    def split(self):
        if self.parent.left is self:
            self.parent.left = S_num(
                [math.floor(self.value / 2), math.ceil(self.value / 2)],
                self.parent,
            )
        elif self.parent.right is self:
            self.parent.right = S_num(
                [math.floor(self.value / 2), math.ceil(self.value / 2)],
                self.parent,
            )

    def add_to_left(self):
        left_neighbor = self.get_neighbor_to_left()
        if left_neighbor is None:
            return
        left_neighbor.value += self.value

    def add_to_right(self):
        right_neighbor = self.get_neighbor_to_right()
        if right_neighbor is None:
            return
        right_neighbor.value += self.value

    def find_parent_with_left(self):
        current = self
        while current.parent.left is current:
            current = current.parent
            if current.parent is None:
                return None

        return current.parent

    def find_parent_with_right(self):
        current = self
        while current.parent.right is current:
            current = current.parent
            if current.parent is None:
                return None

        return current.parent

    def get_neighbor_to_left(self):
        parent_with_left = self.find_parent_with_left()
        if parent_with_left is None:
            return
        if isinstance(parent_with_left.left, P_int):
            return parent_with_left.left
        else:
            return parent_with_left.left.get_right_most_child()

    def get_neighbor_to_right(self):
        parent_with_right = self.find_parent_with_right()
        if parent_with_right is None:
            return
        if isinstance(parent_with_right.right, P_int):
            return parent_with_right.right
        else:
            return parent_with_right.right.get_left_most_child()


class S_num(Node):
    def __init__(self, s_list, parent=None):
        if isinstance(s_list[0], int):
            self.left = P_int(s_list[0], self)
        else:
            self.left = S_num(s_list[0], self)

        if isinstance(s_list[1], int):
            self.right = P_int(s_list[1], self)
        else:
            self.right = S_num(s_list[1], self)
        self.parent = parent

    def is_root(self):
        return True if self.parent == None else False

    def is_leaf(self):
        return isinstance(self.left, P_int) and isinstance(self.right, P_int)

    def __iter__(self):
        return iter([self.left, self.right])

    def __getitem__(self, i):
        if i == 0 or i == "left":
            return self.left
        elif i == 1 or i == "right":
            return self.right
        else:
            raise Exception("invalid index: ", i)

    def toList(self):
        output = []
        if isinstance(self.left, P_int):
            output.append(self.left.value)
        else:
            output.append(self.left.toList())

        if isinstance(self.right, P_int):
            output.append(self.right.value)
        else:
            output.append(self.right.toList())
        return output

    def toJSON(self):
        return json.dumps(self.toList())

    def get_next_exploder_snums(self, level=0, snums_to_explode=None):
        if snums_to_explode is None:
            snums_to_explode = []
        for part in self:
            if not isinstance(part, P_int):
                part.get_next_exploder_snums(level + 1, snums_to_explode)

        if level > 3 and self.is_leaf():
            snums_to_explode.append(self)

        return snums_to_explode

    def explode(self):
        self.left.add_to_left()
        self.right.add_to_right()

        if self.parent.left is self:
            self.parent.left = P_int(0, self.parent)
        elif self.parent.right is self:
            self.parent.right = P_int(0, self.parent)

    def get_left_most_child(self):
        current = self
        while isinstance(current.left, S_num):
            current = current.left

        return current.left

    def get_right_most_child(self):
        current = self
        while isinstance(current.right, S_num):
            current = current.right

        return current.right

    def get_root(self):
        current_node = self
        parent = self.parent

        while parent is not None:
            current_node = parent
            parent = parent.parent

        return current_node

    def split_first_large_num(self):
        root = self.get_root()
        if self is not root:
            raise Exception("split can only be called on root")

        current = self.get_left_most_child()

        while current.value < 10:
            current = current.get_neighbor_to_right()
            if current is None:
                return

        current.split()

    def process(self):
        root = self.get_root()
        if self is not root:
            raise Exception("split can only be called on root")
        processed = False
        prev_state = root.toJSON()

        snums_to_explode = root.get_next_exploder_snums()

        while processed == False:
            while len(snums_to_explode) > 0:
                exploding_snum = snums_to_explode.pop(0)
                exploding_snum.explode()

            snums_to_explode = root.get_next_exploder_snums()

            if len(snums_to_explode) == 0:
                root.split_first_large_num()
                snums_to_explode = root.get_next_exploder_snums()

            raw = root.toJSON()

            if prev_state == raw:
                processed = True
            else:
                prev_state = raw

        return root

    def calculate_magnitude(self):
        if self.get_root() is not self:
            raise Exception("only call this method on root")

        # find leaf


def build_snum(raw_snum):
    l = json.loads(raw_snum)
    return S_num(l)


def process(l):
    root = S_num(json.loads(l))
    return root.process()


def add_snums(snum_a, snum_b):
    new_root = S_num([1, 1], parent=None)
    new_root.left = snum_a
    new_root.right = snum_b
    snum_a.parent = new_root
    snum_b.parent = new_root
    return new_root


def process_lines(lines):
    _lines = lines[1:]
    first_line = json.loads(lines[0])
    snum = S_num(first_line)
    for line in _lines:
        line = json.loads(line)
        snum = add_snums(snum, S_num(line))
        snum.process()
    return snum
