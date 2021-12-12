from __future__ import annotations
from pathlib import Path
from dataclasses import dataclass


from debug import p
from pprint import pp


@dataclass
class Node:
    name: str
    links: list[Node]
    big: bool

    def __init__(self, name, big):
        self.name = name
        self.links = []
        self.big = big

    def __repr__(self):
        return self.name
        # return f"{self.name} {'big' if self.big else 'small'} - {[node.name for node in self.links]}"


def get_info_from_file(path=Path(Path(__file__).parent, "input.txt")):
    with open(path, mode="r") as f:
        return f.read()


def parse_caves(raw_string=get_info_from_file()):

    lines = raw_string.strip().split("\n")

    node_pairs = [line.split("-") for line in lines]

    nodes = {}

    for a, b in node_pairs:

        node_a = Node(a, a.isupper()) if a not in nodes else nodes[a]
        node_b = Node(b, b.isupper()) if b not in nodes else nodes[b]

        node_a.links.append(node_b)
        node_b.links.append(node_a)

        if a not in nodes:
            nodes[a] = node_a

        if b not in nodes:
            nodes[b] = node_b

    return nodes


def get_routes(start_node: Node, target_node: Node):

    current_node: Node = start_node
    stack: list[Node] = [current_node]

    routes: set[str] = set()

    def helper(current_node):

        if current_node is target_node:
            route_code = "".join([node.name for node in stack])
            if route_code not in routes:
                routes.add(route_code)
                stack.pop(-1)
                return

        for node in current_node.links:

            if (not node.big and node in stack) or node.name is start_node:
                continue

            else:
                stack.append(node)
                helper(node)

        if current_node is stack[-1]:
            stack.pop(-1)

    helper(current_node)

    return routes


def get_routes2(start_node: Node, target_node: Node):

    current_node: Node = start_node
    stack: list[Node] = [current_node]
    routes: set[str] = set()

    def helper(current_node, small_cave_visited_twice):

        if current_node is target_node:
            route_code = "".join([node.name for node in stack])
            if route_code not in routes:
                routes.add(route_code)
                stack.pop(-1)
                return

        for node in current_node.links:

            if (
                not node.big and node in stack and small_cave_visited_twice
            ) or node is start_node:
                continue

            elif not node.big and node in stack and not small_cave_visited_twice:
                stack.append(node)
                helper(node, True)
            else:
                stack.append(node)
                helper(node, small_cave_visited_twice)

        if current_node is stack[-1]:
            stack.pop(-1)

    helper(current_node, False)

    return routes
