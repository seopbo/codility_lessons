def solution(X, A):
    if X not in A:
        return -1

    second = A.index(X)
    leaves = set(range(1, X))
    before_second = set(A[:second])
    upcoming_second = set(A[second+1:])
    left_leaves = leaves - before_second
    if not left_leaves:
        return second
    else:
        if not left_leaves - upcoming_second:
            return max([A.index(leaf) for leaf in left_leaves])
        else:
            return - 1


def test_solution():
    assert solution(5, [1, 3, 1, 4, 2, 3, 5, 4]) == 6