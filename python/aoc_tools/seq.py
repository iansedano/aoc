import itertools


def find_pattern(seq, start_from=0, pattern_min=2, early_exit=False):
    """
    >>> find_pattern([1,2,1,2,1,2,1,2,1,2])
    2
    >>> find_pattern([1,2,3,1,2,3,1,2,3])
    3
    >>> find_pattern([1,2,3,4,5,1,2,3,4,5,1,2,3,4,5])
    5
    >>> find_pattern([1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4])
    5
    >>> find_pattern([1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1])
    5
    >>> find_pattern([1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,6])
    -1
    """
    seq = tuple(seq[start_from:])
    pattern_length = -1
    max_len = len(seq) // 2
    for window_size in range(max_len, pattern_min - 1, -1):

        left_over = len(seq) % window_size

        chunks = [
            seq[idx : idx + window_size]
            for idx in range(0, len(seq), window_size)
        ]

        if left_over:
            left_over = chunks.pop(-1)

        if all(a == b for a, b in itertools.combinations(chunks, 2)):

            if left_over and left_over != chunks[0][: len(left_over)]:
                break

            pattern_length = window_size

            if early_exit:
                return pattern_length

    return pattern_length
