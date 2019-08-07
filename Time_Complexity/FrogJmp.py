def solution(X, Y, D):
    quotient, remainder = divmod(Y - X, D)
    if remainder == 0:
        return quotient
    else:
        return quotient + 1


def test_solution():
    assert solution(10, 85, 30) == 3
    assert solution(10, 40, 30) == 1
