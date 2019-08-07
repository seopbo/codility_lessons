def solution(A):
    return sum(range(1, len(A) + 2)) - sum(A)


def test_solution():
    assert solution([2, 3, 1, 5]) == 4
