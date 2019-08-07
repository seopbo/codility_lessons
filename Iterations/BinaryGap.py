def solution(N):
    bit_sequence = format(N, 'b')
    bit_check = []

    for idx, bit in enumerate(bit_sequence):
        if bit == '1':
            bit_check.append(idx)

    binary_gap = []
    for idx in range(1, len(bit_check)):
        binary_gap.append(bit_check[idx] - bit_check[idx - 1] - 1)

    if not any(binary_gap):
        return 0
    else:
        return max(binary_gap)


def test_solution():
    assert solution(32) == 0
    assert solution(1041) == 5
