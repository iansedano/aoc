from collections import namedtuple
from heapq import heappop, heappush

import peek  # noqa

from aoc.tools.grid import create_grid_bi_dict_from_string, print_points
from aoc.tools.neighbors import CARDINALS, EAST, NORTH, SOUTH, WEST  # noqa


def parse(puzzle_input):
    grid, mapping = create_grid_bi_dict_from_string(puzzle_input, ignore=".")
    start, end = mapping["S"].pop(), mapping["E"].pop()
    return mapping["#"], start, end


# class Node:
#     def __init__(self, position, heading, score):
#         self.position = position
#         self.heading = heading
#         self.score = score
#
#     @property
#     def state(self):
#         return (self.position, self.heading)
#
#     def __repr__(self):
#         return f"Node(position={self.position}, heading={self.heading}, score={self.score})"


Node = namedtuple("Node", ["score", "position", "heading"])
NodePlus = namedtuple("NodePlus", ["score", "position", "heading", "path"])


class Queue:
    def __init__(self):
        self._items = []
        self.visited = set()

    def enqueue(self, *nodes):
        for n in nodes:
            if n in self.visited:
                continue
            self.visited.add((n.position, n.heading))
            heappush(self._items, n)

    def dequeue(self):
        return heappop(self._items)


class QueuePlus:
    def __init__(self):
        self._items = []
        # self.visited = set()

    def enqueue(self, *nodes):
        for n in nodes:
            heappush(self._items, n)

    def dequeue(self):
        return heappop(self._items)


def build_get_next_possible(visited, walls):
    def get_next_possible(node: Node):
        other_headings = CARDINALS - {node.heading}

        turns = (
            Node(node.score + 1000, node.position, hd)
            for hd in other_headings
            if (node.position, hd) not in visited and node.position not in walls
        )

        if (step := (node.position + node.heading, node.heading)) in visited or (
            step[0] in walls
        ):
            return turns

        return (Node(node.score + 1, *step), *turns)

    return get_next_possible


def part_1(parsed_input):
    walls, start, end = parsed_input
    node = Node(0, start, EAST)
    queue = Queue()

    print_points(walls, auto_detect=True)
    get_next_possible_states = build_get_next_possible(queue.visited, walls)

    queue.enqueue(node)
    node = queue.dequeue()
    while node.position != end:
        next_states = get_next_possible_states(node)
        queue.enqueue(*next_states)
        node = queue.dequeue()

    return node.score


def part_2(parsed_input):
    walls, start, end = parsed_input
    node = NodePlus(0, start, EAST, set())
    queue = QueuePlus()

    print_points(walls, auto_detect=True)

    def get_next_possible_states(node):
        other_headings = CARDINALS - {node.heading}

        turns = (
            NodePlus(
                node.score + 1000,
                node.position,
                hd,
                node.path,
            )
            for hd in other_headings
            if (node.position) not in node.path
        )

        if (step := node.position) in node.path or (step in walls):
            return turns

        return (
            NodePlus(node.score + 1, step, node.heading, node.path | {node.position}),
            *turns,
        )

    queue.enqueue(node)
    paths = []
    optimal_path_len = float("inf")
    dbg_count = 0
    while queue._items:
        # breakpoint()
        dbg_count += 1
        # if dbg_count > 100:
        #     break
        node = queue.dequeue()
        print(node)
        print_points([n for n in node.path], x_range=(0, 15), y_range=(0, 15))
        print()
        if node.score > optimal_path_len:
            continue
        if node.position == end:
            if len(node.path) <= optimal_path_len:
                paths.append(node)
                optimal_path_len = len(node.path)
            continue
        # peek(node)
        next_states = get_next_possible_states(node)
        queue.enqueue(*next_states)

    return len(paths)
