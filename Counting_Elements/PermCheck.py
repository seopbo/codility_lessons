def solution(A):
    if max(A) != len(A) or len(set(A)) != len(A):
        return 0
    return 1


def test_solution():
    assert solution([4, 1, 3, 2]) == 1
    assert solution([4, 1, 3]) == 0
