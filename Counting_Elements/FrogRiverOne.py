def solution(X, A):
    leaves = set(range(1, X+1))

    for second, leaf in enumerate(A):
        if leaf in leaves:
            leaves.remove(leaf)

        if not leaves:
            return second

    return -1


def test_solution():
    assert solution(5, [1, 3, 1, 4, 2, 3, 5, 4]) == 6


