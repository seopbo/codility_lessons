def solution(X, Y, D):
    quoient, remainder = divmod(Y-X, D)

    if remainder > 0:
        return quoient + 1
    else:
        return quoient


def test_solution():
    assert solution(10, 85, 30) == 3
    assert solution(10, 40, 30) == 1
