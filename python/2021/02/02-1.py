horizontal = 0
depth = 0
aim = 0

with open("02-input.txt", mode='r') as f:

	array = [line for line in f.readlines()]

	# instruction = next(gen, False)

	for line in array:
		direction, value = line.split(" ")

		if direction == "forward":
			horizontal += int(value)
			depth += int(value) * aim
		elif direction == "down":
			aim += int(value)
		elif direction == "up":
			aim -= int(value)

		# instruction = next(gen, False)

	print(horizontal * depth)
