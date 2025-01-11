from dataclasses import dataclass, field

from aocd import get_data


@dataclass
class file:
    name: str
    size: int


@dataclass
class dir:
    name: str
    files: list[file] = field(default_factory=list)
    dirs: list["dir"] = field(default_factory=list)
    size: int = 0


def change_dir(target, cwd):
    if target == "..":
        if len(cwd) == 1:
            return cwd

        cwd.pop(-1)
        return cwd

    if target == "/":
        return cwd[:1]

    if existing_folder := next(
        (folder for folder in cwd[-1].dirs if folder.name == target), False
    ):
        cwd.append(existing_folder)
        return cwd

    cwd.append(dir(target))

    return cwd


def process_ls_line(line, cwd):
    start, name = line.split(" ")

    if start == "dir":
        cwd[-1].dirs.append(dir(name))
        return cwd

    size = int(start)
    cwd[-1].files.append(file(name, int(start)))

    for folder in cwd:
        folder.size += size

    return cwd


def process_chunk(chunk, cwd):
    cwd = change_dir(chunk.pop(0), cwd)

    if len(chunk) == 0:
        return cwd

    chunk.pop(0)  # discarding '$ ls'

    for line in chunk:
        cwd = process_ls_line(line, cwd)

    return cwd


def parse(puzzle_input):
    chunks = [chunk.strip().split("\n") for chunk in puzzle_input.split("$ cd")]
    chunks.pop(0)
    root = dir("/")
    cwd = [root]

    for chunk in chunks:
        cwd = process_chunk(chunk, cwd)

    return root


def recursive_filter(root, key):
    for folder in root.dirs:
        if key(folder):
            yield folder
        yield from recursive_filter(folder, key)


def part1(root):
    return sum(
        folder.size
        for folder in recursive_filter(root, lambda f: f.size <= 100_000)
    )


def part2(root):
    space_left = 70_000_000 - root.size
    ideal_size_to_delete = 30_000_000 - space_left

    return sorted(
        folder.size
        for folder in recursive_filter(
            root, lambda f: f.size >= ideal_size_to_delete
        )
    )[0]


def main():
    puzzle_input = get_data(day=7, year=2022).strip()
    root = parse(puzzle_input)
    solution1 = part1(root)
    solution2 = part2(root)

    return solution1, solution2


if __name__ == "__main__":
    solution1, solution2 = main()
    print(f"{solution1}\n{solution2}")
