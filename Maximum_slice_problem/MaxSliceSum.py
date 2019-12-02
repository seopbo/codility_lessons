from sys import maxsize


def solution(A):

    max_sum = -maxsize
    max_ending = 0

    for a in A:
        max_ending += a

        if max_ending > max_sum:
            max_sum = max_ending

        if max_ending < 0:
            max_ending = 0

    return max_sum


def test_solution():
    assert solution([3, 2, -6, 4, -0]) == 5
