arr = [
    [1, 1, 1, 1, 1],
    [1, 9, 9, 9, 1],
    [1, 9, 1, 9, 1],
    [1, 9, 9, 9, 1],
    [1, 1, 1, 1, 1],
]


def modarr(arr):
    arr[0] = "MOD"


modarr(arr)

print(arr)
