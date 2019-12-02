def solution(A, K):

    if not A: # array is empty
        return A

    if len(A) == K:
        return A
    elif len(A) > K:
        return A[-K:] + A[:-K]
    else:
        mod = K % len(A)
        return A[-mod:] + A[:-mod]


def test_solution():
    assert solution([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]
    assert solution([0, 0, 0], 1) == [0, 0, 0]
    assert solution([1, 2, 3, 4], 4) == [1, 2, 3, 4]
