import json
import re

from debug import p
from pprint import pp

import math


class P_int:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent


class S_num:
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
        self.add_to_next_number(self.left, "left")
        self.add_to_next_number(self.right, "right")

        if self.parent.left is self:
            self.parent.left = P_int(0, self.parent.left)
        elif self.parent.right is self:
            self.parent.right = P_int(0, self.parent.right)

    def get_list_of_P_ints(self):
        output = []
        if isinstance(self.left, P_int):
            output.append(self.left)
        else:
            output.extend(self.left.get_list_of_P_ints())

        if isinstance(self.right, P_int):
            output.append(self.right)
        else:
            output.extend(self.right.get_list_of_P_ints())

        return output

    def get_root(self):
        current_node = self
        parent = self.parent

        while parent is not None:
            current_node = parent
            parent = parent.parent

        return current_node

    def add_to_next_number(self, p_int, direction):
        root = self.get_root()
        p_int_list = root.get_list_of_P_ints()
        i = 0
        for _p in p_int_list:
            if _p is p_int:
                break
            i += 1
        if direction == "left":
            if i > 0:
                p_int_list[i - 1].value += p_int.value
        if direction == "right":
            if i < len(p_int_list) - 1:
                p_int_list[i + 1].value += p_int.value

    def split_first_large_num(self):
        root = self.get_root()
        if self is not root:
            raise Exception("split can only be called on root")
        list_of_P_ints = self.get_list_of_P_ints()

        for p_int in list_of_P_ints:
            if p_int.value > 9:
                if p_int.parent.left is p_int:
                    p_int.parent.left = S_num(
                        [math.floor(p_int.value / 2), math.ceil(p_int.value / 2)],
                        p_int.parent,
                    )
                if p_int.parent.right is p_int:
                    p_int.parent.right = S_num(
                        [math.floor(p_int.value / 2), math.ceil(p_int.value / 2)],
                        p_int.parent,
                    )
                break

    def process(self):
        root = self.get_root()
        if self is not root:
            raise Exception("split can only be called on root")
        processed = False
        prev_state = root.toJSON()

        snums_to_explode = root.get_next_exploder_snums()
        print("EXPLODERS", [e.toList() for e in snums_to_explode])

        while processed == False:
            print("Starting loop")
            while len(snums_to_explode) > 0:
                exploding_snum = snums_to_explode.pop(0)
                print("going to explode: ", exploding_snum.toList())
                print("parent of exploder: ", exploding_snum.parent)
                exploding_snum.explode()
                p(root.toJSON())

            snums_to_explode = root.get_next_exploder_snums()
            print("EXPLODERS", [e.toList() for e in snums_to_explode])

            if len(snums_to_explode) == 0:
                print("TRYING TO SPLIT")
                root.split_first_large_num()
                p(root.toJSON())
                snums_to_explode = root.get_next_exploder_snums()
                print("EXPLODERS", [e.toList() for e in snums_to_explode])

            raw = root.toJSON()

            if prev_state == raw:
                processed = True
            else:
                prev_state = raw

        return root


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
        print("NEW LINE ============")
        line = json.loads(line)
        snum = add_snums(snum, S_num(line))
        snum.process()
    return snum
