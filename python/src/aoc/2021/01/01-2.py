

with open("01-input.txt", mode='r') as f:
	prev_window = [
		int(f.readline().strip()),
		int(f.readline().strip()),
		int(f.readline().strip())
	]

	inc = 0
	dec = 0

	gen = (line for line in f)

	window = [prev_window[1], prev_window[2]]

	current = next(gen, False)

	while current:

		window.append(int(current.strip()))
		print(prev_window, window)

		sum_prev_window = sum(prev_window)
		sum_window = sum(window)

		if sum_window > sum_prev_window:
			inc += 1

		prev_window.pop(0)
		prev_window.append(window[-1])

		window.pop(0)
		
		current = next(gen, False)
		
		


	print("874 too low 1635 too high", inc, dec)


