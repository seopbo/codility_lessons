def solution(A, B, K):
    if A == B:
        if A % K == 0:
            return 1
        else:
            return 0

    start, start_remainder = divmod(A, K)
    end, end_remainder = divmod(B, K)

    if start_remainder != 0:
        if A >= K:
            A += start_remainder
        else:
            A = K

    if end_remainder != 0:
        B -= end_remainder

    start = A // K
    end = B // K

    return end - start + 1


def test_solution():
    assert solution(6, 11, 2) ==3
