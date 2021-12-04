

with open("01-input.txt", mode='r') as f:
	prev_number = int(f.readline().strip())

	inc = 0
	dec = 0

	for line in f:
		number = int(line.strip())
		if number == prev_number:
			raise "equal!"
		elif number > prev_number:
			inc += 1
		elif number < prev_number:
			dec += 1

		prev_number = number

print(inc, dec)