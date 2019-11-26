def solution(N):
    binary_repr = bin(N)[2:]
    list_of_indices = [idx for idx, value in enumerate(binary_repr) if value == '1']

    if len(list_of_indices) == 1:
        return 0
    else:
        list_of_indices = [0] + list_of_indices
        binary_gap = 0

        for index in range(1, len(list_of_indices)):
            tmp_gap = list_of_indices[index] - list_of_indices[index - 1] - 1
            if  tmp_gap > binary_gap:
                binary_gap = tmp_gap

    return binary_gap


def test_solution():
    assert solution(32) == 0

