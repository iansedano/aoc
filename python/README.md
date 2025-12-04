Set the AOC_SESSION env variable for aocd to work

run VS Code from python as root folder
uv sync

uv run src/aoc/scaffold.py 2 --year 2018

uv run aoc 2018 2 --action input
uv run aoc 2018 2 --action parse
uv run aoc 2018 2 --debug
uv run aoc 2018 2 --debug --data example --example 2
