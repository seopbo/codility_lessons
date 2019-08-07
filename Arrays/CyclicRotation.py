def solution(A, K):
    rotated = A.copy()
    if not rotated:
        return rotated

    while K > 0:
        rotated.insert(0, rotated.pop())
        K -= 1
    return rotated


def test_solution():
    assert solution([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]
    assert solution([0, 0, 0], 1) == [0, 0, 0]
    assert solution([1, 2, 3, 4], 4) == [1, 2, 3, 4]