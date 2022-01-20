import itertools


positions = itertools.cycle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

for _ in range(20):
    print(next(positions))
