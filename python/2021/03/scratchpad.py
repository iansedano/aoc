from dataclasses import dataclass

@dataclass
class bitmask:
	mask: int
	type: int


b1    = int("0b1001100010",2)
ones  = int("0b1110111111",2)
zeros = int("0b0000001000",2)
print(b1, ones)

print(bin(b1 & ones), b1&ones)

if b1 == b1&ones:
	print("0 is present")
elif b1 != b1&ones:
	print("0 is not present")


if b1&zeros:
	print("1 is present")
elif not b1&zeros:
	print("1 is not present")

"""
0b1000100010
0b1000100010
"""

m = bitmask(4, 1)
