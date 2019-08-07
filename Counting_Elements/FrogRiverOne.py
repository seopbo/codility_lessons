def solution(X, A):
    leaves = set()
    for second in range(0, len(A)):
        leaves.add(A[second])

        if len(leaves) == X:
            return second

    return -1


def test_solution():
    assert solution(5, [1, 3, 1, 4, 2, 3, 5, 4]) == 6
